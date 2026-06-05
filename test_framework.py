"""
NumberCals — FRAMEWORK guarantees (WRITE-ONCE).

These test the plug-and-play rules themselves, not any individual calculator:
skin consistency, auto-linking, live counts, SEO, site-wide ads, scholar
surfacing, plug-and-play add/remove. They rarely change when you add a
calculator, so you keep this file on disk and never re-upload it.

Run from project root:  pytest -q
"""
import importlib
import pathlib
import re
import shutil
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))


# --- discovery & auto-linking ---------------------------------------------
def test_sections_auto_grouped(reg):
    ids = {s["id"] for s in reg.sections_sorted()}
    assert {"physics", "maths", "accounting"} <= ids


def test_about_count_is_live(client, reg):
    n = reg.calc_count()
    about = client.get("/about").text
    assert f">{n}</strong>" in about


def test_home_and_section_pages_render(client):
    assert client.get("/").status_code == 200
    assert client.get("/section/physics").status_code == 200
    assert client.get("/calc/does-not-exist").status_code == 404


def test_search_indexes_calcs(client):
    assert client.get("/search?q=interest").status_code == 200


# --- skin consistency (blocks an inconsistent build) ----------------------
def test_no_hardcoded_colours_in_viz_templates():
    viz_dir = ROOT / "templates" / "viz"
    hexpat = re.compile(r"#[0-9a-fA-F]{3,6}\b")
    rgbpat = re.compile(r"\brgba?\([0-9]")
    offenders = [t.name for t in viz_dir.glob("*.html")
                 if hexpat.search(t.read_text()) or rgbpat.search(t.read_text())]
    assert not offenders, f"Viz templates hardcode colours: {offenders}"


def test_calc_pages_extend_base_skin():
    assert 'extends "base.html"' in (ROOT / "templates" / "calc.html").read_text()


# --- SEO (monetisation depends on these) ----------------------------------
def test_calc_page_seo_meta(client):
    p = client.get("/calc/projectile").text
    assert 'rel="canonical"' in p
    assert 'property="og:title"' in p
    assert "application/ld+json" in p


def test_sitemap_and_robots(client):
    assert "Disallow: /api/" in client.get("/robots.txt").text
    sm = client.get("/sitemap.xml").text
    assert "<lastmod>" in sm and "/calc/projectile" in sm


# --- ads site-wide --------------------------------------------------------
def test_ad_slot_is_sitewide_and_safe_when_empty(client):
    base = (ROOT / "templates" / "base.html").read_text()
    assert "_ad_slot.html" in base
    for url in ["/", "/about", "/scholars", "/section/maths"]:
        assert "adsbygoogle" not in client.get(url).text  # nothing leaks unconfigured


# --- scholars surface only when referenced --------------------------------
def test_scholars_surface_only_when_referenced(reg):
    surfaced = {s.slug for s in reg.referenced_scholars()}
    used = {c.scholar for c in reg.REGISTRY.values() if c.scholar}
    assert surfaced == {u for u in used if u in reg.SCHOLARS}


# --- plug-and-play add / remove / quarantine ------------------------------
def test_plug_and_play_add_then_remove(client):
    import main
    new_dir = ROOT / "calculators" / "maths" / "geometry" / "circle-area"
    new_dir.mkdir(parents=True, exist_ok=True)
    (new_dir / "calc.py").write_text(
        "from math import pi\n"
        "from core.registry import register\n"
        "@register(slug='circle-area', name='Circle area', section='maths',\n"
        "          sub='Geometry', formula='A = pi r^2', summary='Area of a circle.')\n"
        "def compute(r: float):\n"
        "    return {'area': pi*float(r)**2}\n"
    )
    try:
        importlib.reload(main)
        from core import registry
        assert "circle-area" in registry.REGISTRY
    finally:
        shutil.rmtree(new_dir.parent)
        importlib.reload(main)
        from core import registry
        assert "circle-area" not in registry.REGISTRY


def test_quarantine_underscore_skips(client):
    import main
    src = ROOT / "calculators" / "accounting" / "finance" / "compound-interest" / "calc.py"
    quarantined = src.with_name("_calc.py")
    src.rename(quarantined)
    try:
        importlib.reload(main)
        from core import registry
        assert "compound-interest" not in registry.REGISTRY
    finally:
        quarantined.rename(src)
        importlib.reload(main)
