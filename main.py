"""
NumberCals FastAPI application.

Routing conventions (house style):
  * plain `def` routes (not async) unless I/O-bound
  * templates.TemplateResponse(request, "x.html", _ctx(...)) — request positional
  * route handlers named page_<thing>
  * ALL dedicated routes are declared BEFORE the generic catchall
"""
from __future__ import annotations

import pathlib

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from core import branding, registry
from core import faqs
from core import related

ROOT = pathlib.Path(__file__).parent
templates = Jinja2Templates(directory=str(ROOT / "templates"))

app = FastAPI(title="NumberCals")
app.mount("/static", StaticFiles(directory=str(ROOT / "static")), name="static")

# Scan the folder tree once at boot. This is the only discovery step.
registry.load_all(ROOT)


def _nav_tree() -> list[dict]:
    """Section -> topics -> sub-clusters -> calculators, for the sidebar.

    Built from the registry so it stays plug-and-play: a new calculator folder
    shows up automatically with no edits. Shape per section:
        {id, name, glyph, count,
         topics: [{topic, order,
                   subs: [{name, calcs: [{name, url, formula}, ...]}, ...]}, ...]}
    """
    tree = []
    for s in registry.sections_sorted():
        topics = registry.topics_in_section(s["id"])
        topics_out = [
            {"topic": t["topic"], "order": t["order"],
             "subs": [
                 {"name": sub["name"],
                  "calcs": [{"name": c.name, "url": c.manifest["url"],
                             "formula": c.formula} for c in sub["calcs"]]}
                 for sub in t["subs"]
             ]}
            for t in topics
        ]
        count = sum(len(sub["calcs"])
                    for t in topics_out for sub in t["subs"])
        tree.append({
            "id": s["id"], "name": s["name"], "glyph": s.get("glyph", "•"),
            "count": count, "topics": topics_out,
        })
    return tree


def _ctx(**extra) -> dict:
    """Every route merges branding + nav sections into its context."""
    ctx = branding.context()
    ctx["nav_sections"] = registry.sections_sorted()
    ctx["nav_tree"] = _nav_tree()
    ctx["calc_count"] = registry.calc_count()
    ctx.update(extra)
    return ctx


# ---------------------------------------------------------------------------
# Pages — dedicated routes FIRST.
# ---------------------------------------------------------------------------
@app.get("/", response_class=HTMLResponse)
def page_home(request: Request):
    return templates.TemplateResponse(
        request, "home.html",
        _ctx(sections=registry.sections_sorted()),
    )


@app.get("/about", response_class=HTMLResponse)
def page_about(request: Request):
    return templates.TemplateResponse(
        request, "about.html",
        _ctx(),  # calc_count already in _ctx -> About number is automatic
    )


@app.get("/contact", response_class=HTMLResponse)
def page_contact(request: Request):
    return templates.TemplateResponse(request, "contact.html", _ctx())


@app.get("/privacy", response_class=HTMLResponse)
def page_privacy(request: Request):
    return templates.TemplateResponse(request, "privacy.html", _ctx())


@app.get("/terms", response_class=HTMLResponse)
def page_terms(request: Request):
    return templates.TemplateResponse(request, "terms.html", _ctx())


@app.get("/scholars", response_class=HTMLResponse)
def page_scholars(request: Request):
    # "Minds behind Maths" — full A–Z directory of all published scholars,
    # whether or not a calculator references them yet.
    groups: dict[str, list[dict]] = {}
    for s in registry.all_scholars():
        letter = s.name[0].upper()
        groups.setdefault(letter, []).append(s.manifest)
    return templates.TemplateResponse(request, "scholars.html",
                                      _ctx(letters=dict(sorted(groups.items()))))


@app.get("/scholar/{slug}", response_class=HTMLResponse)
def page_scholar(request: Request, slug: str):
    scholar = registry.resolve_scholar(slug)
    if scholar is None:
        raise HTTPException(404, "No such scholar")
    linked = [c.manifest for c in registry.calcs_for_scholar(slug)]
    return templates.TemplateResponse(
        request, "scholar.html",
        _ctx(scholar=scholar.manifest, linked=linked,
             page_title=f"{scholar.name} · {branding.SITE_NAME}",
             page_description=scholar.blurb[:150]),
    )


@app.get("/search", response_class=HTMLResponse)
def page_search(request: Request, q: str = ""):
    results = registry.search(q)
    return templates.TemplateResponse(
        request, "search.html",
        _ctx(query=q, results=[c.manifest for c in results]),
    )


@app.get("/section/{section_id}", response_class=HTMLResponse)
def page_section(request: Request, section_id: str):
    if section_id not in {s["id"] for s in registry.sections_sorted()}:
        raise HTTPException(404, "No such section")
    meta = registry.SECTIONS[section_id]
    topics = registry.topics_in_section(section_id)
    topics_ctx = [
        {"topic": t["topic"], "order": t["order"],
         "subs": [{"name": sub["name"],
                   "calcs": [c.manifest for c in sub["calcs"]]}
                  for sub in t["subs"]]}
        for t in topics
    ]
    return templates.TemplateResponse(
        request, "section.html",
        _ctx(section=meta, topics=topics_ctx),
    )


@app.get("/calc/{slug}", response_class=HTMLResponse)
def page_calc(request: Request, slug: str):
    calc = registry.resolve(slug)
    if calc is None:
        raise HTTPException(404, "No such calculator")
    viz = calc.viz_template or "viz/_generic.html"
    sch = registry.resolve_scholar(calc.scholar) if calc.scholar else None
    return templates.TemplateResponse(
        request, "calc.html",
        _ctx(calc=calc.manifest, viz_template=viz,
             scholar=sch.manifest if sch else None,
             faqs=faqs.faqs_for(calc.slug),
             related=related.related_calcs(calc.slug),
             page_title=f"{calc.name} · {branding.SITE_NAME}",
             page_description=calc.summary or branding.TAGLINE),
    )


# ---------------------------------------------------------------------------
# JSON / SEO endpoints.
# ---------------------------------------------------------------------------
@app.get("/api/catalog")
def api_catalog():
    return JSONResponse([c.manifest for c in registry.REGISTRY.values()])


@app.post("/api/compute/{slug}")
def api_compute(slug: str, inputs: dict):
    calc = registry.resolve(slug)
    if calc is None:
        raise HTTPException(404, "No such calculator")
    try:
        return JSONResponse(calc.compute(**inputs))
    except TypeError as e:
        raise HTTPException(422, f"Bad inputs: {e}")


@app.get("/healthz")
def healthz():
    return {"ok": True, "calculators": registry.calc_count()}


@app.get("/robots.txt", response_class=PlainTextResponse)
def robots():
    return "User-agent: *\nDisallow: /api/\nDisallow: /healthz\nSitemap: /sitemap.xml\n"


@app.get("/sitemap.xml")
def sitemap(request: Request):
    import datetime
    base = str(request.base_url).rstrip("/")
    today = datetime.date.today().isoformat()
    urls = ["/", "/about", "/contact", "/scholars", "/privacy", "/terms"]
    urls += [f"/section/{s['id']}" for s in registry.sections_sorted()]
    urls += [c.manifest["url"] for c in registry.REGISTRY.values()]
    body = "".join(
        f"<url><loc>{base}{u}</loc>"
        f"<lastmod>{today}</lastmod>"
        f"<changefreq>weekly</changefreq></url>"
        for u in urls
    )
    xml = ('<?xml version="1.0" encoding="UTF-8"?>'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
           f"{body}</urlset>")
    return PlainTextResponse(xml, media_type="application/xml")
