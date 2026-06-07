"""Potential Energy: PE = m g h (gravitational). Solve for energy, mass or height."""
from __future__ import annotations
from core.registry import register

_DISCLAIMER = ("These values are estimates and may contain computation, formula, "
    "or system errors. They are provided for general reference only — always verify "
    "results independently before relying on them for academic or professional "
    "decisions.")

_G = 9.81  # m/s^2, standard gravitational acceleration at Earth's surface

def _f(x):
    if x is None: return ""
    if abs(x - round(x)) < 1e-9: return str(int(round(x)))
    return ("%.4f" % x).rstrip("0").rstrip(".")

_LAW_STATEMENT = ("Gravitational potential energy is the energy a body stores because of its "
    "height in a gravitational field. For a body of mass m at height h, it equals the mass "
    "times the gravitational field strength g times the height, PE = m g h.")
_LAW_SOURCE_NAME = "Wikipedia \u2014 Potential energy"
_LAW_SOURCE_URL = "https://en.wikipedia.org/wiki/Potential_energy"

_EXPLANATION = [
    {"heading": "What gravitational potential energy is",
     "body": "Potential energy is the energy a body stores because of its height in a "
             "gravitational field. Lift something up and you store energy in it; let it "
             "fall and that energy is released, turning into kinetic energy."},
    {"heading": "The role of g",
     "body": "The strength of gravity at the Earth's surface is taken as g = 9.81 metres "
             "per second-squared. Height is measured from whatever reference level you "
             "choose, usually the ground or a tabletop."},
    {"heading": "Units",
     "body": "With mass in kilograms, g in metres per second-squared and height in "
             "metres, the energy comes out in joules (J)."},
]

@register(
    slug="potential-energy",
    name="Potential Energy",
    section="physics",
    topic="Mechanics & Forces",
    sub="Energy",
    order=2,
    summary="Find the gravitational potential energy of a raised body from its mass and height, or solve for mass or height.",
    formula="PE = m g h",
    tags=["potential energy", "gravitational", "energy", "joules", "height", "mechanics", "mass"],
    viz_template="viz/potential-energy.html",
    related=["kinetic-energy", "work-done", "mechanical-power"],
)
def compute(solve_for="energy", mass=2.0, height=5.0, energy=None, g=_G, **_ignored):
    try:
        sf = str(solve_for or "energy").strip().lower()
    except Exception:
        sf = "energy"

    def num(v):
        if v is None or v == "":
            return None
        return float(v)

    try:
        m = num(mass)
        h = num(height)
        e = num(energy)
        gg = num(g)
    except (TypeError, ValueError):
        return {"error": "Please enter numbers only.", "steps": [], "disclaimer": _DISCLAIMER}

    if gg is None or gg <= 0:
        gg = _G

    out_mass = m
    out_height = h
    out_energy = e
    steps = []
    result = ""

    if sf == "energy":
        if m is None or h is None:
            return {"error": "Enter mass and height to find potential energy.",
                    "steps": [], "disclaimer": _DISCLAIMER}
        if m < 0:
            return {"error": "Mass cannot be negative.", "steps": [], "disclaimer": _DISCLAIMER}
        out_energy = m * gg * h
        steps = [
            {"label": "Formula", "math": r"\(PE = m g h\)",
             "note": "Gravitational potential energy."},
            {"label": "Substitute",
             "math": r"\(PE = (" + _f(m) + r")(" + _f(gg) + r")(" + _f(h) + r")\)",
             "note": "Mass in kg, g in m/s\u00b2, height in m."},
            {"label": "Result", "math": r"\(PE = " + _f(out_energy) + r"\ \text{J}\)",
             "note": "Energy in joules."},
        ]
        result = "Potential energy = " + _f(out_energy) + " J"

    elif sf == "mass":
        if e is None or h is None:
            return {"error": "Enter energy and height to find mass.",
                    "steps": [], "disclaimer": _DISCLAIMER}
        if h == 0:
            return {"error": "Height cannot be zero when solving for mass.",
                    "steps": [], "disclaimer": _DISCLAIMER}
        out_mass = e / (gg * h)
        steps = [
            {"label": "Rearrange", "math": r"\(m = \dfrac{PE}{g h}\)",
             "note": "Solve PE = mgh for mass."},
            {"label": "Substitute",
             "math": r"\(m = \dfrac{" + _f(e) + r"}{(" + _f(gg) + r")(" + _f(h) + r")}\)",
             "note": "Energy in J, g in m/s\u00b2, height in m."},
            {"label": "Result", "math": r"\(m = " + _f(out_mass) + r"\ \text{kg}\)",
             "note": "Mass in kilograms."},
        ]
        result = "Mass = " + _f(out_mass) + " kg"

    elif sf == "height":
        if e is None or m is None:
            return {"error": "Enter energy and mass to find height.",
                    "steps": [], "disclaimer": _DISCLAIMER}
        if m <= 0:
            return {"error": "Mass must be greater than zero when solving for height.",
                    "steps": [], "disclaimer": _DISCLAIMER}
        out_height = e / (m * gg)
        steps = [
            {"label": "Rearrange", "math": r"\(h = \dfrac{PE}{m g}\)",
             "note": "Solve PE = mgh for height."},
            {"label": "Substitute",
             "math": r"\(h = \dfrac{" + _f(e) + r"}{(" + _f(m) + r")(" + _f(gg) + r")}\)",
             "note": "Energy in J, mass in kg, g in m/s\u00b2."},
            {"label": "Result", "math": r"\(h = " + _f(out_height) + r"\ \text{m}\)",
             "note": "Height in metres."},
        ]
        result = "Height = " + _f(out_height) + " m"

    else:
        return {"error": "Choose what to solve for: energy, mass or height.",
                "steps": [], "disclaimer": _DISCLAIMER}

    return {
        "result": result,
        "solve_for": sf,
        "mass": out_mass,
        "height": out_height,
        "energy": out_energy,
        "g": gg,
        "steps": steps,
        "explanation": _EXPLANATION,
        "law_statement": _LAW_STATEMENT,
        "law_source_name": _LAW_SOURCE_NAME,
        "law_source_url": _LAW_SOURCE_URL,
        "disclaimer": _DISCLAIMER,
    }

from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
