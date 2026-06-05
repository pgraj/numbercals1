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


# --- scholars A–Z directory + citations (added when scholar set landed) ----
def test_all_twelve_scholars_in_directory(client, reg):
    names = {s.name for s in reg.all_scholars()}
    assert len(names) >= 12
    assert "Aryabhata" in names and "Manjul Bhargava" in names


def test_scholars_page_is_alphabetical_az(client):
    page = client.get("/scholars").text
    # A–Z index and at least the A and B letter groups present
    assert 'class="az-index"' in page
    assert 'id="sec-A"' in page and 'id="sec-B"' in page


def test_scholar_profiles_have_citations(client, reg):
    for s in reg.all_scholars():
        assert s.source_url, f"{s.name} missing citation URL"
        page = client.get(f"/scholar/{s.slug}").text
        assert s.source_url in page


def test_unreferenced_scholar_still_listed_but_no_calcs(client):
    # Bhargava has no calculator yet: listed in directory, profile shows the
    # "will appear here" note rather than a formula list.
    page = client.get("/scholar/bhargava").text
    assert "Manjul Bhargava" in page
    assert "will appear here" in page


# --- Delivery 1: legal pages, configurable email, search, footer ----------
def test_privacy_and_terms_pages_render(client):
    assert client.get("/privacy").status_code == 200
    assert client.get("/terms").status_code == 200
    assert "Privacy Policy" in client.get("/privacy").text
    assert "Terms of Use" in client.get("/terms").text


def test_legal_pages_in_sitemap(client):
    sm = client.get("/sitemap.xml").text
    assert "/privacy" in sm and "/terms" in sm


def test_contact_email_is_configurable_and_correct(client):
    from core import branding
    assert branding.CONTACT_EMAIL == "hello@numbercals.com"
    assert "hello@numbercals.com" in client.get("/contact").text
    # the old address must not appear anywhere
    assert "govind.labs" not in client.get("/contact").text


def test_footer_has_privacy_terms_links(client):
    home = client.get("/").text
    assert 'href="/privacy"' in home and 'href="/terms"' in home


def test_search_returns_results(client):
    page = client.get("/search?q=compound").text
    assert "compound-interest" in page


def test_search_no_match_is_graceful(client):
    page = client.get("/search?q=zzzznomatch").text
    assert "No matches" in page


def test_scholars_filter_chips_present(client):
    page = client.get("/scholars").text
    assert 'class="az-chip' in page and 'data-letter="ALL"' in page


# --- Delivery 2: left-panel nav + theme switcher --------------------------
def test_sidebar_lists_all_sections(client, reg):
    home = client.get("/").text
    assert 'class="sidebar"' in home
    for s in reg.sections_sorted():
        assert f'/section/{s["id"]}' in home


def test_top_bar_trimmed_no_section_links(client):
    # Sections moved to the sidebar; the old .site-nav top list is gone.
    home = client.get("/").text
    assert 'class="site-nav"' not in home
    assert 'class="brand"' in home  # brand stays


def test_theme_switcher_present(client):
    home = client.get("/").text
    assert 'class="theme-switch"' in home
    for t in ("light", "sepia", "dark"):
        assert f'data-theme-set="{t}"' in home


def test_theme_css_defines_three_themes():
    css = (ROOT / "static" / "app.css").read_text()
    assert '[data-theme="light"]' in css
    assert '[data-theme="dark"]' in css
    assert '[data-theme="sepia"]' in css


def test_theme_and_skin_assets_served(client):
    assert client.get("/static/theme.js").status_code == 200
    assert "refresh" in client.get("/static/skin.js").text  # NCSkin.refresh exists


# --- version badge no longer overlaps (moved into header flow) -------------
def test_version_badge_not_fixed_position():
    css = (ROOT / "static" / "app.css").read_text()
    # the .version-badge rule must not use position:fixed anymore
    import re
    block = re.search(r"\.version-badge\{[^}]*\}", css).group(0)
    assert "position:fixed" not in block


def test_version_badge_in_header(client):
    home = client.get("/").text
    # badge sits inside the header, after search; not a floating div at body top
    assert 'class="version-badge"' in home
