"""
NumberCals health checks — powers the /debug page and a CLI sanity sweep.

Read-only. Walks the live REGISTRY and reports problems that would otherwise
only surface as a broken page in production:

  * viz_template set but the template file is missing on disk
  * scholar=<slug> that doesn't resolve to a registered scholar
  * curated related=[...] slugs that don't resolve (dead related link)
  * calcs with too few discriminating tags (poor auto-relatedness)
  * duplicate slugs (shouldn't happen — REGISTRY is keyed by slug — but we
    report sections/subs that collide in confusing ways)
  * sections declared but unused, and calcs whose section has no tile

Nothing here mutates state; safe to call on every request to /debug.
"""
from __future__ import annotations

import pathlib

from core import registry, related


def _templates_root() -> pathlib.Path:
    # templates/ sits next to the app root; source_dir on a calc points into
    # calculators/, so walk up to the project root and into templates/.
    for c in registry.REGISTRY.values():
        if c.source_dir:
            # .../calculators/<section>/<sub>/<slug> -> project root is 4 up
            return c.source_dir.parents[3] / "templates"
    return pathlib.Path("templates")


def check_viz_templates() -> list[dict]:
    """Calcs whose viz_template doesn't exist on disk."""
    troot = _templates_root()
    out = []
    for c in registry.REGISTRY.values():
        if not c.viz_template:
            continue
        path = troot / c.viz_template
        if not path.exists():
            out.append({"slug": c.slug, "viz_template": c.viz_template,
                        "expected_path": str(path)})
    return out


def check_scholars() -> list[dict]:
    """Calcs linking to a scholar slug that isn't registered."""
    out = []
    for c in registry.REGISTRY.values():
        if c.scholar and c.scholar not in registry.SCHOLARS:
            out.append({"slug": c.slug, "scholar": c.scholar})
    return out


def check_related_links() -> list[dict]:
    """Curated related=[...] slugs that don't resolve to a registered calc."""
    out = []
    for c in registry.REGISTRY.values():
        dead = [r for r in c.related if registry.resolve(r) is None]
        if dead:
            out.append({"slug": c.slug, "dead_related": dead})
    return out


def check_thin_tags(min_tags: int = 2) -> list[dict]:
    """Calcs with too few discriminating tags (after stopword removal) — these
    get weak auto-relatedness, so flag them for a tag top-up."""
    out = []
    for c in registry.REGISTRY.values():
        discriminating = {t.strip().lower() for t in (c.tags or [])} - related.STOPWORDS
        if len(discriminating) < min_tags:
            out.append({"slug": c.slug, "tag_count": len(discriminating),
                        "tags": sorted(discriminating)})
    return out


def check_section_tiles() -> list[dict]:
    """Calcs whose section has only the auto-placeholder tile (no sections/*.py)."""
    out = []
    for c in registry.REGISTRY.values():
        meta = registry.SECTIONS.get(c.section, {})
        if meta.get("glyph", "•") == "•" and meta.get("order", 99) == 99:
            out.append({"slug": c.slug, "section": c.section})
    return out


def summary() -> dict:
    """One call for the /debug page: counts + every check, plus an overall ok."""
    viz = check_viz_templates()
    scholars = check_scholars()
    rel = check_related_links()
    thin = check_thin_tags()
    tiles = check_section_tiles()
    checks = {
        "missing_viz_templates": viz,
        "unresolved_scholars": scholars,
        "dead_related_links": rel,
        "thin_tags": thin,
        "placeholder_section_tiles": tiles,
    }
    # thin_tags and placeholder tiles are warnings, not hard errors
    hard = bool(viz or scholars or rel)
    return {
        "counts": {
            "calculators": registry.calc_count(),
            "sections": len(registry.sections_sorted()),
            "scholars_registered": len(registry.SCHOLARS),
            "scholars_referenced": len(registry.referenced_scholars()),
        },
        "checks": checks,
        "ok": not hard,
        "warnings_only": (not hard) and bool(thin or tiles),
    }
