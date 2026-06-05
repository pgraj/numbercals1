# NumberCals — plug-and-play framework (skeleton)

**Tagline:** From Aryabhata to Algorithms — Calculators for the Curious.

## Run
    pip install -r requirements.txt
    python -m uvicorn main:app --reload    (or: run.bat)
    # open http://localhost:8000

## Test
    pytest -q

## The plug-and-play contract
- **Add a calculator** → drop `calculators/<section>/<sub>/<slug>/calc.py`
  with an `@register(...)` decorator. Restart. It appears everywhere.
- **Remove** → delete the folder. **Quarantine** → rename `calc.py` → `_calc.py`.
- You never edit `core/registry.py`, nav, or any list. Home grid, section
  pages, search, sitemap, and the About count all rebuild from disk.

## Optional: control a section's look
Add `sections/<id>.py` with `register_section(id=..., name=..., glyph=...,
hue=..., order=..., blurb=...)`.

## Custom graph for one calculator
Pass `viz_template="viz/<name>.html"` in `@register`; otherwise the generic
input-and-plot panel is used. See `templates/viz/projectile.html`.

## Layout
    main.py                 FastAPI app (routes, SEO, compute API)
    core/registry.py        write-once registry + folder scan
    core/branding.py        versions + global disclaimer
    sections/*.py           optional section display declarations
    calculators/**/calc.py  one folder per calculator
    templates/              base + pages + viz/ partials
    static/                 app.css, calc.js, viz-generic.js
    tests/                  framework + plug-and-play tests

## Scholars ("Minds behind Maths")
- Add a profile: `scholars/<slug>.py` with `register_scholar(slug=..., name=...,
  era=..., field_of=..., blurb=...)`.
- Link a formula to it: add `scholar="<slug>"` to that calculator's `@register`.
- A scholar only appears on /scholars once at least one calculator links to
  them. Their profile page auto-lists every formula that references them.

## Ads (site-wide)
- The ad slot is included in `base.html`, so it appears on every page.
- It renders nothing until you set `ADSENSE_CLIENT` (and `AD_SLOT`) in
  `core/branding.py`. No broken empty box before approval.
