"""Pressure: P = F / A. Solve for pressure, force or area."""
from __future__ import annotations
from core.registry import register

_DISCLAIMER = ("These values are estimates and may contain computation, formula, "
    "or system errors. They are provided for general reference only — always verify "
    "results independently before relying on them for academic or professional "
    "decisions.")

_LAW_STATEMENT = ("Pressure is how much force is pushing on each unit of area. It equals the "
    "force divided by the area it acts on, P = F / A. The same force on a smaller area gives "
    "a higher pressure.")
_LAW_SOURCE_NAME = "Wikipedia \u2014 Pressure"
_LAW_SOURCE_URL = "https://en.wikipedia.org/wiki/Pressure"

def _f(x):
    if x is None: return ""
    if abs(x - round(x)) < 1e-9: return str(int(round(x)))
    return ("%.4f" % x).rstrip("0").rstrip(".")

_EXPLANATION = [
    {"heading": "What pressure means",
     "body": "Pressure is about how concentrated a push is. Press a drawing pin: the same "
             "push from your thumb is spread over your wide thumb but squeezed onto the "
             "tiny sharp point, so the point has huge pressure and digs in."},
    {"heading": "Same force, different area",
     "body": "A sharp knife cuts better than a blunt one because its thin edge puts the "
             "force on a tiny area, giving high pressure. Snowshoes do the opposite \u2014 "
             "they spread your weight over a big area, lowering the pressure so you do not "
             "sink."},
    {"heading": "Units",
     "body": "With force in newtons and area in square metres, pressure comes out in "
             "pascals (Pa). One pascal is one newton per square metre."},
]

@register(
    slug="pressure",
    name="Pressure",
    section="physics",
    topic="Fluids & Matter",
    sub="Density & Pressure",
    order=1,
    summary="Find pressure from force and area, or solve for force or area, using P = F / A.",
    formula="P = F / A",
    tags=["pressure", "force", "area", "pascal", "matter", "fluids"],
    viz_template="viz/pressure.html",
    related=["density", "archimedes-principle", "boyles-law"],
)
def compute(solve_for="pressure", force=20.0, area=0.5, pressure=None, **_ignored):
    try:
        sf = str(solve_for or "pressure").strip().lower()
    except Exception:
        sf = "pressure"

    def num(v):
        if v is None or v == "":
            return None
        return float(v)

    try:
        F = num(force)
        A = num(area)
        P = num(pressure)
    except (TypeError, ValueError):
        return {"error": "Please enter numbers only.", "steps": [], "disclaimer": _DISCLAIMER}

    out_force = F
    out_area = A
    out_pressure = P
    steps = []
    result = ""

    if sf == "pressure":
        if F is None or A is None:
            return {"error": "Enter force and area to find pressure.",
                    "steps": [], "disclaimer": _DISCLAIMER}
        if A == 0:
            return {"error": "Area cannot be zero when solving for pressure.",
                    "steps": [], "disclaimer": _DISCLAIMER}
        out_pressure = F / A
        steps = [
            {"label": "Formula", "math": r"\(P = \dfrac{F}{A}\)",
             "note": "Pressure equals force divided by area."},
            {"label": "Substitute",
             "math": r"\(P = \dfrac{" + _f(F) + r"}{" + _f(A) + r"}\)",
             "note": "Force in newtons, area in m\u00b2."},
            {"label": "Result", "math": r"\(P = " + _f(out_pressure) + r"\ \text{Pa}\)",
             "note": "Pressure in pascals."},
        ]
        result = "Pressure = " + _f(out_pressure) + " Pa"

    elif sf == "force":
        if P is None or A is None:
            return {"error": "Enter pressure and area to find force.",
                    "steps": [], "disclaimer": _DISCLAIMER}
        out_force = P * A
        steps = [
            {"label": "Rearrange", "math": r"\(F = P A\)",
             "note": "Solve P = F/A for force."},
            {"label": "Substitute",
             "math": r"\(F = (" + _f(P) + r")(" + _f(A) + r")\)",
             "note": "Pressure in pascals, area in m\u00b2."},
            {"label": "Result", "math": r"\(F = " + _f(out_force) + r"\ \text{N}\)",
             "note": "Force in newtons."},
        ]
        result = "Force = " + _f(out_force) + " N"

    elif sf == "area":
        if P is None or F is None:
            return {"error": "Enter pressure and force to find area.",
                    "steps": [], "disclaimer": _DISCLAIMER}
        if P == 0:
            return {"error": "Pressure cannot be zero when solving for area.",
                    "steps": [], "disclaimer": _DISCLAIMER}
        out_area = F / P
        steps = [
            {"label": "Rearrange", "math": r"\(A = \dfrac{F}{P}\)",
             "note": "Solve P = F/A for area."},
            {"label": "Substitute",
             "math": r"\(A = \dfrac{" + _f(F) + r"}{" + _f(P) + r"}\)",
             "note": "Force in newtons, pressure in pascals."},
            {"label": "Result", "math": r"\(A = " + _f(out_area) + r"\ \text{m}^2\)",
             "note": "Area in square metres."},
        ]
        result = "Area = " + _f(out_area) + " m\u00b2"

    else:
        return {"error": "Choose what to solve for: pressure, force or area.",
                "steps": [], "disclaimer": _DISCLAIMER}

    return {
        "result": result,
        "solve_for": sf,
        "force": out_force,
        "area": out_area,
        "pressure": out_pressure,
        "steps": steps,
        "explanation": _EXPLANATION,
        "law_statement": _LAW_STATEMENT,
        "law_source_name": _LAW_SOURCE_NAME,
        "law_source_url": _LAW_SOURCE_URL,
        "disclaimer": _DISCLAIMER,
    }

from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
