"""Kinetic Energy: KE = 1/2 m v^2. Solve for energy, mass or speed."""
from __future__ import annotations
import math
from core.registry import register

_DISCLAIMER = ("These values are estimates and may contain computation, formula, "
    "or system errors. They are provided for general reference only — always verify "
    "results independently before relying on them for academic or professional "
    "decisions.")

def _f(x):
    if x is None: return ""
    if abs(x - round(x)) < 1e-9: return str(int(round(x)))
    return ("%.4f" % x).rstrip("0").rstrip(".")

_LAW_STATEMENT = ("Kinetic energy is the energy a body has because of its motion. For a body "
    "of mass m moving at speed v, it equals one half of the mass times the speed squared, "
    "KE = \u00bd m v\u00b2.")
_LAW_SOURCE_NAME = "Wikipedia \u2014 Kinetic energy"
_LAW_SOURCE_URL = "https://en.wikipedia.org/wiki/Kinetic_energy"

_EXPLANATION = [
    {"heading": "What kinetic energy is",
     "body": "Kinetic energy is the energy a body has because it is moving. A heavier "
             "body, or a faster one, carries more kinetic energy, and bringing it to "
             "rest releases that energy."},
    {"heading": "Why speed matters most",
     "body": "Energy grows with the square of the speed, so doubling the speed gives "
             "four times the kinetic energy. This is why stopping distances and impact "
             "energies rise so steeply as speed increases."},
    {"heading": "Units",
     "body": "With mass in kilograms and speed in metres per second, the energy comes "
             "out in joules (J). One joule is one kilogram metre-squared per "
             "second-squared."},
]

@register(
    slug="kinetic-energy",
    name="Kinetic Energy",
    section="physics",
    topic="Mechanics & Forces",
    sub="Energy",
    order=1,
    summary="Work out the kinetic energy of a moving body from its mass and speed, or solve for mass or speed.",
    formula="KE = \u00bd m v\u00b2",
    tags=["kinetic energy", "energy", "motion", "joules", "mechanics", "speed", "mass"],
    viz_template="viz/kinetic-energy.html",
    related=["potential-energy", "work-done", "mechanical-power", "speed"],
)
def compute(solve_for="energy", mass=2.0, speed=10.0, energy=None, **_ignored):
    # coerce
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
        v = num(speed)
        e = num(energy)
    except (TypeError, ValueError):
        return {"error": "Please enter numbers only.", "steps": [], "disclaimer": _DISCLAIMER}

    steps = []
    result = ""
    out_mass = m
    out_speed = v
    out_energy = e

    if sf == "energy":
        if m is None or v is None:
            return {"error": "Enter mass and speed to find kinetic energy.",
                    "steps": [], "disclaimer": _DISCLAIMER}
        if m < 0:
            return {"error": "Mass cannot be negative.", "steps": [], "disclaimer": _DISCLAIMER}
        out_energy = 0.5 * m * v * v
        steps = [
            {"label": "Formula", "math": r"\(KE = \tfrac{1}{2} m v^2\)",
             "note": "Kinetic energy from mass and speed."},
            {"label": "Substitute",
             "math": r"\(KE = \tfrac{1}{2}\,(" + _f(m) + r")\,(" + _f(v) + r")^2\)",
             "note": "Insert the mass in kg and speed in m/s."},
            {"label": "Result", "math": r"\(KE = " + _f(out_energy) + r"\ \text{J}\)",
             "note": "Energy in joules."},
        ]
        result = "Kinetic energy = " + _f(out_energy) + " J"

    elif sf == "mass":
        if e is None or v is None:
            return {"error": "Enter energy and speed to find mass.",
                    "steps": [], "disclaimer": _DISCLAIMER}
        if v == 0:
            return {"error": "Speed cannot be zero when solving for mass.",
                    "steps": [], "disclaimer": _DISCLAIMER}
        if e < 0:
            return {"error": "Energy cannot be negative.", "steps": [], "disclaimer": _DISCLAIMER}
        out_mass = (2.0 * e) / (v * v)
        steps = [
            {"label": "Rearrange", "math": r"\(m = \dfrac{2\,KE}{v^2}\)",
             "note": "Solve the kinetic energy formula for mass."},
            {"label": "Substitute",
             "math": r"\(m = \dfrac{2\,(" + _f(e) + r")}{(" + _f(v) + r")^2}\)",
             "note": "Insert the energy in J and speed in m/s."},
            {"label": "Result", "math": r"\(m = " + _f(out_mass) + r"\ \text{kg}\)",
             "note": "Mass in kilograms."},
        ]
        result = "Mass = " + _f(out_mass) + " kg"

    elif sf == "speed":
        if e is None or m is None:
            return {"error": "Enter energy and mass to find speed.",
                    "steps": [], "disclaimer": _DISCLAIMER}
        if m <= 0:
            return {"error": "Mass must be greater than zero when solving for speed.",
                    "steps": [], "disclaimer": _DISCLAIMER}
        if e < 0:
            return {"error": "Energy cannot be negative.", "steps": [], "disclaimer": _DISCLAIMER}
        out_speed = math.sqrt((2.0 * e) / m)
        steps = [
            {"label": "Rearrange", "math": r"\(v = \sqrt{\dfrac{2\,KE}{m}}\)",
             "note": "Solve the kinetic energy formula for speed."},
            {"label": "Substitute",
             "math": r"\(v = \sqrt{\dfrac{2\,(" + _f(e) + r")}{" + _f(m) + r"}}\)",
             "note": "Insert the energy in J and mass in kg."},
            {"label": "Result", "math": r"\(v = " + _f(out_speed) + r"\ \text{m/s}\)",
             "note": "Speed in metres per second."},
        ]
        result = "Speed = " + _f(out_speed) + " m/s"

    else:
        return {"error": "Choose what to solve for: energy, mass or speed.",
                "steps": [], "disclaimer": _DISCLAIMER}

    return {
        "result": result,
        "solve_for": sf,
        "mass": out_mass,
        "speed": out_speed,
        "energy": out_energy,
        "steps": steps,
        "explanation": _EXPLANATION,
        "law_statement": _LAW_STATEMENT,
        "law_source_name": _LAW_SOURCE_NAME,
        "law_source_url": _LAW_SOURCE_URL,
        "disclaimer": _DISCLAIMER,
    }

from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
