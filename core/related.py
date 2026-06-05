"""
NumberCals relatedness — zero-touch "Related calculators" links.

WRITE ONCE, like registry.py. You never edit this file or any per-calc data to
get related links: relatedness is computed at request time from the `tags`,
`topic`, `sub`, and `section` that every calculator already declares in its
@register(...). Drop in a new calculator with sensible tags and it joins the
graph automatically — nothing to wire, no links file to maintain.

How the score works (higher = more related), for two calcs A and B:
    + shared tags         each shared tag is worth the most (the main signal)
    + same topic          a solid bonus (e.g. both "Trigonometry")
    + same sub-cluster    a further bonus (e.g. both "Right-Angle Trigonometry")
    + same section         a small bonus
Calcs in unrelated areas with no shared tags score 0 and never appear.

This is intentionally simple and explainable — see `related_debug()` for the
per-candidate breakdown used by the debug page, so a surprising link is always
traceable to the tags that caused it.
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from core import registry

if TYPE_CHECKING:
    from core.registry import Calc

# Scoring weights. Tuned so a single shared tag outranks "same section alone",
# and same-topic outranks a lone shared tag only when combined with section.
W_SHARED_TAG = 3
W_SAME_TOPIC = 4
W_SAME_SUB = 2
W_SAME_SECTION = 1

# Generic tags that appear on almost everything carry no discriminating signal,
# so they're ignored when matching (they'd relate everything to everything).
# Extend freely; this is the one knob worth curating.
STOPWORDS = {
    "trigonometry", "mathematics", "maths", "calculator", "worked example",
    "real life trigonometry", "geometry",
}


def _norm_tags(calc: "Calc") -> set[str]:
    return {t.strip().lower() for t in (calc.tags or []) if t.strip()} - STOPWORDS


def _score(a: "Calc", b: "Calc", a_tags: set[str]) -> tuple[int, list[str]]:
    """Return (score, shared_tags) for candidate b relative to anchor a."""
    shared = a_tags & _norm_tags(b)
    score = len(shared) * W_SHARED_TAG
    if a.topic and a.topic == b.topic:
        score += W_SAME_TOPIC
    if a.sub and a.sub == b.sub:
        score += W_SAME_SUB
    if a.section == b.section:
        score += W_SAME_SECTION
    return score, sorted(shared)


def related_calcs(slug: str, limit: int = 6) -> list[dict]:
    """Top related calculators for `slug`, as template-ready dicts.

    Curated `related` slugs (declared in the calc's @register) come first, in
    declared order, resolved against the live registry (unknown/unregistered
    slugs are skipped — no dead links). The remaining slots are filled by the
    auto-computed tag/topic ranking, excluding anything already shown and the
    anchor itself. Deterministic: auto ties break by name.

    Returns [{slug, name, url, section, score, curated}, ...], highest priority
    first, excluding the anchor and anything that scores 0 (unless curated).
    """
    anchor = registry.resolve(slug)
    if anchor is None:
        return []
    a_tags = _norm_tags(anchor)

    out: list[dict] = []
    seen: set[str] = {slug}

    # 1. curated first (directional, editorial) — resolved & de-duped
    for cslug in anchor.related:
        if cslug in seen:
            continue
        cand = registry.resolve(cslug)
        if cand is None:
            continue  # not registered yet -> skip, never a dead link
        out.append({
            "slug": cand.slug, "name": cand.name, "url": f"/calc/{cand.slug}",
            "section": cand.section, "score": None, "curated": True,
        })
        seen.add(cslug)

    # 2. auto-fill the rest by tag/topic score
    scored = []
    for cand in registry.REGISTRY.values():
        if cand.slug in seen:
            continue
        score, shared = _score(anchor, cand, a_tags)
        if score <= 0:
            continue
        scored.append((score, cand))
    scored.sort(key=lambda t: (-t[0], t[1].name.lower()))
    for score, cand in scored:
        if len(out) >= limit:
            break
        out.append({
            "slug": cand.slug, "name": cand.name, "url": f"/calc/{cand.slug}",
            "section": cand.section, "score": score, "curated": False,
        })

    return out[:limit]


def related_debug(slug: str, limit: int = 12) -> dict:
    """Explainable breakdown for the debug page: every scoring candidate with
    the shared tags and component scores, so a surprising link is traceable."""
    anchor = registry.resolve(slug)
    if anchor is None:
        return {"slug": slug, "found": False, "candidates": []}
    a_tags = _norm_tags(anchor)
    rows = []
    for cand in registry.REGISTRY.values():
        if cand.slug == slug:
            continue
        score, shared = _score(anchor, cand, a_tags)
        if score <= 0:
            continue
        rows.append({
            "slug": cand.slug, "name": cand.name, "score": score,
            "shared_tags": shared,
            "same_topic": bool(anchor.topic and anchor.topic == cand.topic),
            "same_sub": bool(anchor.sub and anchor.sub == cand.sub),
            "same_section": anchor.section == cand.section,
        })
    rows.sort(key=lambda r: (-r["score"], r["name"].lower()))
    return {
        "slug": slug, "found": True, "anchor_name": anchor.name,
        "anchor_tags": sorted(a_tags), "candidates": rows[:limit],
    }
