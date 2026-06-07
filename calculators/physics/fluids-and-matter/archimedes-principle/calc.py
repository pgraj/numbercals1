"""Archimedes' Principle: buoyant force F_b = rho_fluid * V_displaced * g.
Solve for buoyant force, fluid density or displaced volume."""
from __future__ import annotations
from core.registry import register

_DISCLAIMER = ("These values are estimates and may contain computation, formula, "
    "or system errors. They are provided for general reference only — always verify "
    "results independently before relying on them for academic or professional "
    "decisions.")

_LAW_STATEMENT = ("Any object placed in a fluid is pushed up by a force equal to the weight "
    "of the fluid it pushes out of the way. That upward buoyant force is F_b = \u03c1 V g, "
    "the fluid's density times the displaced volume times gravity.")
_LAW_SOURCE_NAME = "Wikipedia \u2014 Archimedes' principle"
_LAW_SOURCE_URL = "https://en.wikipedia.org/wiki/Archimedes%27_principle"

_G = 9.81  # m/s^2

def _f(x):
    if x is None: return ""
    if abs(x - round(x)) < 1e-9: return str(int(round(x)))
    return ("%.4f" % x).rstrip("0").rstrip(".")

_EXPLANATION = [
    {"heading": "What the principle says",
     "body": "When you lower something into water, it shoves some water aside. The water "
             "pushes back up on the object with a force equal to the weight of the water "
             "that got pushed out of the way. That upward push is called buoyancy."},
    {"heading": "Why ships float",
     "body": "A heavy steel ship floats because its shape pushes aside a huge amount of "
             "water. As long as the weight of water pushed aside is as big as the ship's "
             "weight, the upward push holds it up. Squash the same steel into a ball and "
             "it sinks \u2014 it no longer pushes enough water aside."},
    {"heading": "Units",
     "body": "With fluid density in kg/m\u00b3, displaced volume in m\u00b3 and g = 9.81 "
             "m/s\u00b2, the buoyant force comes out in newtons (N). Water's density is "
             "about 1000 kg/m\u00b3."},
]

@register(
    slug="archimedes-principle",
    name="Archimedes' Principle",
    section="physics",
    topic="Fluids & Matter",
    sub="Buoyancy",
    order=3,
    summary="Find the buoyant force on a submerged object, or solve for fluid density or displaced volume.",
    formula="F_b = \u03c1 V g",
    tags=["archimedes", "buoyancy", "buoyant force", "float", "displaced", "fluids", "matter"],
    viz_template="viz/archimedes-principle.html",
    scholar="archimedes",
    related=["density", "pressure", "boyles-law"],
)
def compute(solve_for="force", fluid_density=1000.0, volume=0.001, force=None, g=_G, **_ignored):
    try:
        sf = str(solve_for or "force").strip().lower()
    except Exception:
        sf = "force"

    def num(v):
        if v is None or v == "":
            return None
        return float(v)

    try:
        rho = num(fluid_density)
        V = num(volume)
        Fb = num(force)
        gg = num(g)
    except (TypeError, ValueError):
        return {"error": "Please enter numbers only.", "steps": [], "disclaimer": _DISCLAIMER}

    if gg is None or gg <= 0:
        gg = _G

    out_density = rho
    out_volume = V
    out_force = Fb
    steps = []
    result = ""

    if sf == "force":
        if rho is None or V is None:
            return {"error": "Enter fluid density and displaced volume to find the buoyant force.",
                    "steps": [], "disclaimer": _DISCLAIMER}
        if rho < 0 or V < 0:
            return {"error": "Density and volume must be positive.", "steps": [], "disclaimer": _DISCLAIMER}
        out_force = rho * V * gg
        steps = [
            {"label": "Formula", "math": r"\(F_b = \rho\,V\,g\)",
             "note": "Buoyant force = fluid density times displaced volume times gravity."},
            {"label": "Substitute",
             "math": r"\(F_b = (" + _f(rho) + r")(" + _f(V) + r")(" + _f(gg) + r")\)",
             "note": "Density in kg/m\u00b3, volume in m\u00b3, g in m/s\u00b2."},
            {"label": "Result", "math": r"\(F_b = " + _f(out_force) + r"\ \text{N}\)",
             "note": "Buoyant force in newtons."},
        ]
        result = "Buoyant force = " + _f(out_force) + " N"

    elif sf == "fluid_density" or sf == "density":
        if Fb is None or V is None:
            return {"error": "Enter buoyant force and displaced volume to find the fluid density.",
                    "steps": [], "disclaimer": _DISCLAIMER}
        if V == 0:
            return {"error": "Displaced volume cannot be zero when solving for density.",
                    "steps": [], "disclaimer": _DISCLAIMER}
        out_density = Fb / (V * gg)
        steps = [
            {"label": "Rearrange", "math": r"\(\rho = \dfrac{F_b}{V g}\)",
             "note": "Solve the buoyancy formula for fluid density."},
            {"label": "Substitute",
             "math": r"\(\rho = \dfrac{" + _f(Fb) + r"}{(" + _f(V) + r")(" + _f(gg) + r")}\)",
             "note": "Force in N, volume in m\u00b3, g in m/s\u00b2."},
            {"label": "Result", "math": r"\(\rho = " + _f(out_density) + r"\ \text{kg/m}^3\)",
             "note": "Fluid density in kilograms per cubic metre."},
        ]
        result = "Fluid density = " + _f(out_density) + " kg/m\u00b3"

    elif sf == "volume":
        if Fb is None or rho is None:
            return {"error": "Enter buoyant force and fluid density to find the displaced volume.",
                    "steps": [], "disclaimer": _DISCLAIMER}
        if rho == 0:
            return {"error": "Fluid density cannot be zero when solving for volume.",
                    "steps": [], "disclaimer": _DISCLAIMER}
        out_volume = Fb / (rho * gg)
        steps = [
            {"label": "Rearrange", "math": r"\(V = \dfrac{F_b}{\rho g}\)",
             "note": "Solve the buoyancy formula for displaced volume."},
            {"label": "Substitute",
             "math": r"\(V = \dfrac{" + _f(Fb) + r"}{(" + _f(rho) + r")(" + _f(gg) + r")}\)",
             "note": "Force in N, density in kg/m\u00b3, g in m/s\u00b2."},
            {"label": "Result", "math": r"\(V = " + _f(out_volume) + r"\ \text{m}^3\)",
             "note": "Displaced volume in cubic metres."},
        ]
        result = "Displaced volume = " + _f(out_volume) + " m\u00b3"

    else:
        return {"error": "Choose what to solve for: force, fluid density or volume.",
                "steps": [], "disclaimer": _DISCLAIMER}

    return {
        "result": result,
        "solve_for": sf,
        "fluid_density": out_density,
        "volume": out_volume,
        "force": out_force,
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
