"""
NumberCals registry — the single source of truth.

WRITE ONCE. You should never need to edit this file to add or remove a
calculator. The plug-and-play contract is:

    To ADD a calculator    -> drop a folder calculators/<section>/<sub>/<slug>/calc.py
                              with an @register(...) decorator on its compute fn.
    To REMOVE a calculator -> delete that folder (or rename calc.py -> _calc.py
                              to quarantine without deleting).

On the next server start, load_all() walks the tree, every @register runs,
and the home page / section pages / search index / About count all rebuild
themselves from whatever happens to be on disk. No nav file, no ALL_MODULES
list, no manual imports.
"""
from __future__ import annotations

import importlib.util
import pathlib
from dataclasses import dataclass, field
from typing import Any, Callable

# ---------------------------------------------------------------------------
# In-memory state, populated by load_all() at boot.
# ---------------------------------------------------------------------------
REGISTRY: dict[str, "Calc"] = {}      # slug -> Calc
SECTIONS: dict[str, dict] = {}        # section id -> display meta
SCHOLARS: dict[str, "Scholar"] = {}   # scholar slug -> Scholar


@dataclass
class Scholar:
    """One scholar profile for the 'Minds behind Maths' page."""
    slug: str
    name: str
    era: str = ""
    field_of: str = ""        # e.g. "Mathematics, astronomy"
    blurb: str = ""
    source_name: str = ""     # citation label, e.g. "MacTutor (St Andrews)"
    source_url: str = ""      # citation link
    published: bool = True

    @property
    def manifest(self) -> dict:
        return {
            "slug": self.slug, "name": self.name, "era": self.era,
            "field_of": self.field_of, "blurb": self.blurb,
            "source_name": self.source_name, "source_url": self.source_url,
            "url": f"/scholar/{self.slug}",
        }


@dataclass
class Calc:
    """One calculator. Built from an @register-decorated compute function."""
    fn: Callable[..., dict]
    slug: str
    name: str
    section: str
    sub: str
    topic: str = ""          # outer grouping inside a section (e.g. "Trigonometry")
    order: int = 0           # topic sort key (lower first; ties -> alphabetical)
    summary: str = ""
    formula: str = ""
    tags: list[str] = field(default_factory=list)
    viz_template: str | None = None   # e.g. "viz/projectile.html"; None -> generic
    scholar: str | None = None        # slug linking to a registered Scholar
    related: list[str] = field(default_factory=list)  # curated related calc slugs
    source_dir: pathlib.Path | None = None

    def compute(self, **kwargs: Any) -> dict:
        return self.fn(**kwargs)

    @property
    def manifest(self) -> dict:
        """JSON-serialisable view, consumed by /api/catalog and templates."""
        return {
            "slug": self.slug,
            "name": self.name,
            "section": self.section,
            "sub": self.sub,
            "topic": self.topic,
            "order": self.order,
            "summary": self.summary,
            "formula": self.formula,
            "tags": self.tags,
            "has_custom_viz": self.viz_template is not None,
            "scholar": self.scholar,
            "url": f"/calc/{self.slug}",
        }


# ---------------------------------------------------------------------------
# Decorators used by leaf calc.py files and optional sections/*.py files.
# ---------------------------------------------------------------------------
def register(
    *,
    slug: str,
    name: str,
    section: str,
    sub: str,
    topic: str = "",
    order: int = 0,
    summary: str = "",
    formula: str = "",
    tags: list[str] | None = None,
    viz_template: str | None = None,
    scholar: str | None = None,
    related: list[str] | None = None,
):
    """Decorator placed on each calculator's compute function.

    `related` is an OPTIONAL curated list of calculator slugs this page should
    link to (used for directional links like a worked example -> the exact
    calculators it demonstrates). Leave it unset for ordinary calculators: the
    "Related calculators" rail is computed automatically from tags/topic by
    core.related, so you never need to wire links by hand. Curated `related`
    entries are merged ahead of the auto-computed ones and resolved against the
    live registry, so a slug that isn't (yet) registered is simply skipped.
    """
    def deco(fn: Callable[..., dict]) -> Callable[..., dict]:
        # A new section value auto-creates a placeholder section so the home
        # grid never has a dangling reference. sections/*.py can override look.
        SECTIONS.setdefault(
            section,
            {"id": section, "name": section.replace("-", " ").title(),
             "glyph": "•", "hue": 220, "blurb": "", "order": 99},
        )
        REGISTRY[slug] = Calc(
            fn=fn, slug=slug, name=name, section=section, sub=sub,
            topic=topic, order=order,
            summary=summary, formula=formula, tags=tags or [],
            viz_template=viz_template, scholar=scholar,
            related=related or [],
        )
        return fn
    return deco


def register_scholar(
    *,
    slug: str,
    name: str,
    era: str = "",
    field_of: str = "",
    blurb: str = "",
    source_name: str = "",
    source_url: str = "",
    published: bool = True,
):
    """Declared in scholars/<slug>.py. A calc links to one via scholar=<slug>."""
    SCHOLARS[slug] = Scholar(
        slug=slug, name=name, era=era, field_of=field_of,
        blurb=blurb, source_name=source_name, source_url=source_url,
        published=published,
    )


def register_section(
    *,
    id: str,
    name: str,
    glyph: str = "•",
    hue: int = 220,
    blurb: str = "",
    order: int = 50,
):
    """Optional. Declared in sections/<id>.py to control tile look & order."""
    SECTIONS[id] = {**SECTIONS.get(id, {}),
                    "id": id, "name": name, "glyph": glyph,
                    "hue": hue, "blurb": blurb, "order": order}


# ---------------------------------------------------------------------------
# Boot-time folder scan.
# ---------------------------------------------------------------------------
def _import(path: pathlib.Path) -> None:
    spec = importlib.util.spec_from_file_location(
        f"_nc_{path.parent.name}_{path.stem}", path
    )
    mod = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(mod)


def load_all(root: str | pathlib.Path = ".") -> None:
    """Walk sections/, scholars/, then calculators/, importing each module once."""
    REGISTRY.clear()
    SECTIONS.clear()
    SCHOLARS.clear()
    root = pathlib.Path(root)

    # 1. Optional section declarations run first so look & order are known.
    sections_dir = root / "sections"
    if sections_dir.exists():
        for path in sorted(sections_dir.glob("*.py")):
            if path.stem.startswith("_"):
                continue
            _import(path)

    # 2. Scholar profiles. A calc's scholar=<slug> resolves against these.
    scholars_dir = root / "scholars"
    if scholars_dir.exists():
        for path in sorted(scholars_dir.glob("*.py")):
            if path.stem.startswith("_"):
                continue
            _import(path)

    # 3. Every calculator. Underscore-prefixed files are quarantined (skipped).
    calc_dir = root / "calculators"
    if calc_dir.exists():
        for path in sorted(calc_dir.rglob("calc.py")):
            if path.name.startswith("_"):
                continue
            calc = _register_with_source(path)


def _register_with_source(path: pathlib.Path) -> None:
    """Import a calc.py and tag the resulting Calc with its source folder."""
    before = set(REGISTRY.keys())
    _import(path)
    for slug in set(REGISTRY.keys()) - before:
        REGISTRY[slug].source_dir = path.parent


# ---------------------------------------------------------------------------
# Read helpers used by routes & templates. (resolve, group, count)
# ---------------------------------------------------------------------------
def calc_count() -> int:
    """Live total — drives the About page number automatically."""
    return len(REGISTRY)


def sections_sorted() -> list[dict]:
    used = {c.section for c in REGISTRY.values()}
    return sorted(
        (s for sid, s in SECTIONS.items() if sid in used),
        key=lambda s: (s.get("order", 99), s["name"]),
    )


def calcs_in_section(section_id: str) -> dict[str, list[Calc]]:
    """Return {sub_section_name: [Calc, ...]} for one section."""
    grouped: dict[str, list[Calc]] = {}
    for c in REGISTRY.values():
        if c.section == section_id:
            grouped.setdefault(c.sub, []).append(c)
    for sub in grouped.values():
        sub.sort(key=lambda c: c.name)
    return dict(sorted(grouped.items()))


def topics_in_section(section_id: str) -> list[dict]:
    """Two-level grouping for the section: Topic -> Sub(cluster) -> [Calc].

    Returns an ORDERED list (not a dict) so topic sequence is controlled by the
    `order` field, not alphabetics:
        [{"topic": str, "order": int,
          "subs": [{"name": sub, "calcs": [Calc, ...]}, ...]}, ...]

    Topics sort by (min order among their calcs, topic name). Subs within a
    topic sort alphabetically (use a numbered prefix on `sub` if you need a
    specific cluster order, exactly as before). Calcs sort by name.

    Calculators with an empty topic are grouped under a single "" topic placed
    last, so un-migrated calculators still appear rather than vanishing.
    """
    # topic -> {"order": int, "subs": {sub: [Calc]}}
    topics: dict[str, dict] = {}
    for c in REGISTRY.values():
        if c.section != section_id:
            continue
        t = topics.setdefault(c.topic, {"order": c.order, "subs": {}})
        # a topic's effective order is the smallest order seen among its calcs
        t["order"] = min(t["order"], c.order) if t["subs"] else c.order
        t["subs"].setdefault(c.sub, []).append(c)

    out = []
    for topic_name, data in topics.items():
        subs = [{"name": sub, "calcs": sorted(cs, key=lambda c: c.name)}
                for sub, cs in sorted(data["subs"].items())]
        out.append({"topic": topic_name, "order": data["order"], "subs": subs})

    # empty-topic bucket sorts last; otherwise by (order, topic name)
    out.sort(key=lambda t: (t["topic"] == "", t["order"], t["topic"].lower()))
    return out


def resolve(slug: str) -> Calc | None:
    return REGISTRY.get(slug)


def search(query: str) -> list[Calc]:
    q = query.lower().strip()
    if not q:
        return []
    hits = []
    for c in REGISTRY.values():
        hay = " ".join([c.name, c.summary, c.section, c.sub, *c.tags]).lower()
        if q in hay:
            hits.append(c)
    return sorted(hits, key=lambda c: c.name)


# --- Scholars -------------------------------------------------------------
def resolve_scholar(slug: str) -> "Scholar | None":
    s = SCHOLARS.get(slug)
    return s if (s and s.published) else None


def calcs_for_scholar(slug: str) -> list[Calc]:
    """Every calculator that links to this scholar via scholar=<slug>."""
    return sorted((c for c in REGISTRY.values() if c.scholar == slug),
                  key=lambda c: c.name)


def referenced_scholars() -> list["Scholar"]:
    """Scholars surfaced on the 'Minds behind Maths' page — only those that
    at least one registered calculator references. This is the 'developed as
    and when we add formulas' behaviour: a scholar with no linked formula
    stays hidden until a calculator points to them."""
    used = {c.scholar for c in REGISTRY.values() if c.scholar}
    return sorted(
        (s for slug, s in SCHOLARS.items() if slug in used and s.published),
        key=lambda s: s.name,
    )


def all_scholars() -> list["Scholar"]:
    """Every published scholar, alphabetical by name — for the A–Z directory.
    Unlike referenced_scholars(), this lists scholars even if no calculator
    links to them yet (so the 'Minds behind Maths' directory can be complete
    while their formulas are still being added)."""
    return sorted((s for s in SCHOLARS.values() if s.published),
                  key=lambda s: s.name)
