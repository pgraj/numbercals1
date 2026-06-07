"""Density: rho = m / V. Solve for density, mass or volume. Includes a material
picker (auto-fills a typical density) plus weight and a NIOSH lift check."""
from __future__ import annotations
from core.registry import register

_DISCLAIMER = ("These values are estimates and may contain computation, formula, "
    "or system errors. They are provided for general reference only \u2014 always verify "
    "results independently before relying on them for academic or professional "
    "decisions.")

_LAW_STATEMENT = ("Density is how much mass is packed into a given volume. It equals the mass "
    "divided by the volume, \u03c1 = m / V. A dense material has a lot of mass squeezed into "
    "a small space.")
_LAW_SOURCE_NAME = "Wikipedia \u2014 Density"
_LAW_SOURCE_URL = "https://en.wikipedia.org/wiki/Density"

_G = 9.81  # m/s^2

# Typical densities (kg/m^3), rounded textbook values.
# Source: standard materials density tables (e.g. engineeringtoolbox.com,
# amesweb.info). Values are indicative room-temperature figures.
_MATERIALS = {
    "cotton":    80,
    "wood":      650,
    "water":     1000,
    "aluminium": 2705,
    "iron":      7860,
    "gold":      19320,
}
_MATERIAL_LABEL = {
    "cotton": "Cotton", "wood": "Wood (oak)", "water": "Water",
    "aluminium": "Aluminium", "iron": "Iron", "gold": "Gold",
}

# NIOSH load constant: 23 kg is safe to lift for most people under ideal conditions.
# Source: NIOSH lifting equation (CCOHS / OSHA).
_NIOSH_KG = 23.0
_NIOSH_NOTE = ("NIOSH (the US National Institute for Occupational Safety and Health) sets "
    "about 23 kg as a load safe for most people to lift under ideal conditions.")
_NIOSH_SOURCE_NAME = "CCOHS \u2014 NIOSH lifting equation"
_NIOSH_SOURCE_URL = "https://www.ccohs.ca/oshanswers/ergonomics/niosh/assessing.html"

def _f(x):
    if x is None: return ""
    if abs(x - round(x)) < 1e-9: return str(int(round(x)))
    return ("%.4f" % x).rstrip("0").rstrip(".")

_EXPLANATION = [
    {"heading": "What density means",
     "body": "Density tells you how heavy something is for its size. A box of cotton and "
             "the same-size box of iron are very different weights \u2014 the iron is far "
             "denser, because much more mass is packed into the same space."},
    {"heading": "Same volume, very different mass",
     "body": "Fill one cup with water and one with gold: same volume, but the gold cup is "
             "about 19 times heavier. That is why the material matters so much \u2014 each "
             "material has its own density, so the same size gives a very different mass."},
    {"heading": "When it gets too heavy to lift",
     "body": "Mass is what you actually have to lift. A small block of iron or gold can "
             "already be too heavy to lift safely, while a big bundle of cotton is light. "
             "This calculator shows the weight and whether it is within a safe lifting "
             "load."},
]

@register(
    slug="density",
    name="Density",
    section="physics",
    topic="Fluids & Matter",
    sub="Density & Pressure",
    order=0,
    summary="Find density from mass and volume (or solve for mass or volume), pick a material, and see the weight and whether it is safe to lift.",
    formula="\u03c1 = m / V",
    tags=["density", "mass", "volume", "matter", "fluids", "float", "sink", "material"],
    viz_template="viz/density.html",
    related=["pressure", "archimedes-principle", "boyles-law"],
)
def compute(solve_for="density", mass=2.0, volume=0.001, density=None,
            material="custom", **_ignored):
    try:
        sf = str(solve_for or "density").strip().lower()
    except Exception:
        sf = "density"

    mat = str(material or "custom").strip().lower()

    def num(v):
        if v is None or v == "":
            return None
        return float(v)

    try:
        m = num(mass)
        V = num(volume)
        rho = num(density)
    except (TypeError, ValueError):
        return {"error": "Please enter numbers only.", "steps": [], "disclaimer": _DISCLAIMER}

    # If a known material is chosen, it supplies the density (overrides typed density).
    material_density = _MATERIALS.get(mat)
    if material_density is not None and sf != "density":
        rho = float(material_density)

    out_mass = m
    out_volume = V
    out_density = rho
    steps = []
    result = ""

    if sf == "density":
        if m is None or V is None:
            return {"error": "Enter mass and volume to find density.",
                    "steps": [], "disclaimer": _DISCLAIMER}
        if V == 0:
            return {"error": "Volume cannot be zero when solving for density.",
                    "steps": [], "disclaimer": _DISCLAIMER}
        out_density = m / V
        steps = [
            {"label": "Formula", "math": r"\(\rho = \dfrac{m}{V}\)",
             "note": "Density equals mass divided by volume."},
            {"label": "Substitute",
             "math": r"\(\rho = \dfrac{" + _f(m) + r"}{" + _f(V) + r"}\)",
             "note": "Mass in kg, volume in m\u00b3."},
            {"label": "Result", "math": r"\(\rho = " + _f(out_density) + r"\ \text{kg/m}^3\)",
             "note": "Density in kilograms per cubic metre."},
        ]
        result = "Density = " + _f(out_density) + " kg/m\u00b3"

    elif sf == "mass":
        if rho is None or V is None:
            return {"error": "Enter density (or pick a material) and volume to find mass.",
                    "steps": [], "disclaimer": _DISCLAIMER}
        out_mass = rho * V
        steps = [
            {"label": "Rearrange", "math": r"\(m = \rho V\)",
             "note": "Solve density = m/V for mass."},
            {"label": "Substitute",
             "math": r"\(m = (" + _f(rho) + r")(" + _f(V) + r")\)",
             "note": "Density in kg/m\u00b3, volume in m\u00b3."},
            {"label": "Result", "math": r"\(m = " + _f(out_mass) + r"\ \text{kg}\)",
             "note": "Mass in kilograms."},
        ]
        result = "Mass = " + _f(out_mass) + " kg"

    elif sf == "volume":
        if rho is None or m is None:
            return {"error": "Enter density (or pick a material) and mass to find volume.",
                    "steps": [], "disclaimer": _DISCLAIMER}
        if rho == 0:
            return {"error": "Density cannot be zero when solving for volume.",
                    "steps": [], "disclaimer": _DISCLAIMER}
        out_volume = m / rho
        steps = [
            {"label": "Rearrange", "math": r"\(V = \dfrac{m}{\rho}\)",
             "note": "Solve density = m/V for volume."},
            {"label": "Substitute",
             "math": r"\(V = \dfrac{" + _f(m) + r"}{" + _f(rho) + r"}\)",
             "note": "Mass in kg, density in kg/m\u00b3."},
            {"label": "Result", "math": r"\(V = " + _f(out_volume) + r"\ \text{m}^3\)",
             "note": "Volume in cubic metres."},
        ]
        result = "Volume = " + _f(out_volume) + " m\u00b3"

    else:
        return {"error": "Choose what to solve for: density, mass or volume.",
                "steps": [], "disclaimer": _DISCLAIMER}

    # Weight + lift check (uses whatever mass we now have)
    lift_mass = out_mass
    weight_n = None
    can_lift = None
    lift_note = ""
    if lift_mass is not None:
        weight_n = lift_mass * _G
        can_lift = lift_mass <= _NIOSH_KG
        if can_lift:
            lift_note = ("Weight \u2248 " + _f(weight_n) + " N (" + _f(lift_mass) +
                         " kg). Within the ~23 kg safe single-person lift.")
        else:
            lift_note = ("Weight \u2248 " + _f(weight_n) + " N (" + _f(lift_mass) +
                         " kg). Above the ~23 kg safe single-person lift \u2014 too heavy "
                         "to lift safely alone.")

    return {
        "result": result,
        "solve_for": sf,
        "material": mat,
        "material_label": _MATERIAL_LABEL.get(mat, "Custom"),
        "mass": out_mass,
        "volume": out_volume,
        "density": out_density,
        "weight_n": weight_n,
        "can_lift": can_lift,
        "lift_limit_kg": _NIOSH_KG,
        "lift_note": lift_note,
        "lift_source_name": _NIOSH_SOURCE_NAME,
        "lift_source_url": _NIOSH_SOURCE_URL,
        "steps": steps,
        "explanation": _EXPLANATION,
        "law_statement": _LAW_STATEMENT,
        "law_source_name": _LAW_SOURCE_NAME,
        "law_source_url": _LAW_SOURCE_URL,
        "disclaimer": _DISCLAIMER,
    }

from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
