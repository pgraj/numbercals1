"""Mass-Energy Equivalence: E = mc^2. Solve for energy or mass."""
from __future__ import annotations
import math
from core.registry import register

_C = 299792458.0          # speed of light in vacuum, m/s (exact)
_C2 = _C * _C             # c squared
_J_PER_KWH = 3.6e6        # joules in one kilowatt-hour
_J_PER_KT_TNT = 4.184e12  # joules in one kilotonne of TNT

_DISCLAIMER = ("These values are estimates and may contain computation, formula, "
    "or system errors. They are provided for general reference only \u2014 always verify "
    "results independently before relying on them for academic or professional "
    "decisions.")

def _f(x):
    if x is None: return ""
    if abs(x - round(x)) < 1e-9: return str(int(round(x)))
    return ("%.4f" % x).rstrip("0").rstrip(".")

def _sci(x):
    """Format large/small numbers in tidy scientific notation for display."""
    if x is None or x == 0:
        return "0"
    if 1e-3 <= abs(x) < 1e7:
        return _f(x)
    exp = int(math.floor(math.log10(abs(x))))
    mant = x / (10 ** exp)
    mant_s = ("%.3f" % mant).rstrip("0").rstrip(".")
    return mant_s + r" \times 10^{" + str(exp) + "}"

def _sci_plain(x):
    """Scientific notation as plain text (for result strings, not LaTeX)."""
    if x is None or x == 0:
        return "0"
    if 1e-3 <= abs(x) < 1e7:
        return _f(x)
    exp = int(math.floor(math.log10(abs(x))))
    mant = x / (10 ** exp)
    mant_s = ("%.3f" % mant).rstrip("0").rstrip(".")
    return mant_s + " x 10^" + str(exp)

def _energy_comparison(joules):
    """Plain-language sense of scale for an energy in joules."""
    if joules is None or joules <= 0:
        return ""
    kwh = joules / _J_PER_KWH
    kt = joules / _J_PER_KT_TNT
    def _sig3(x):
        # 3 significant figures, scientific if very large/small
        if x == 0: return "0"
        if 1e-3 <= abs(x) < 1e6:
            r = float("%.3g" % x)
            return _f(r)
        return _sci_plain(float("%.3g" % x))
    parts = []
    # kWh comparison (household electricity)
    if kwh >= 1:
        parts.append("about " + _sig3(kwh) + " kilowatt-hours of electricity")
    # TNT comparison
    if kt >= 1:
        parts.append("roughly " + _sig3(kt) + " kilotonnes of TNT")
    elif kt * 1000 >= 0.001:
        tonnes = joules / (_J_PER_KT_TNT / 1000.0)
        parts.append("roughly " + _sig3(tonnes) + " tonnes of TNT")
    if not parts:
        return ""
    return " \u2014 equivalent to " + ", or ".join(parts) + "."

_LAW_STATEMENT = ("Mass-energy equivalence states that the energy of a body at rest equals "
    "its mass times the speed of light squared, E = m c\u00b2. A tiny amount of mass holds an "
    "enormous amount of energy, because c\u00b2 is a very large number.")
_LAW_SOURCE_NAME = "Wikipedia \u2014 Mass\u2013energy equivalence"
_LAW_SOURCE_URL = "https://en.wikipedia.org/wiki/Mass%E2%80%93energy_equivalence"

_EXPLANATION = [
    {"heading": "What the equation means",
     "body": "Einstein's E = mc\u00b2 says mass and energy are two forms of the same thing. "
             "Any mass at rest is, in effect, frozen energy. Convert even a little mass "
             "completely and you release a colossal amount of energy."},
    {"heading": "Why the energy is so huge",
     "body": "The speed of light c is about 300 million metres per second, and the formula "
             "uses c squared \u2014 roughly 9 followed by sixteen zeros. Multiplying mass by "
             "that vast number is why one gram of matter holds energy comparable to a large "
             "explosion."},
    {"heading": "Where it actually happens",
     "body": "Full mass-to-energy conversion is rare. The Sun turns about four million "
             "tonnes of mass into sunlight every second; nuclear reactors and bombs convert "
             "a small fraction of their fuel's mass; and PET scanners detect energy from "
             "electrons meeting their antimatter twins."},
]

@register(
    slug="mass-energy-equivalence",
    name="E = mc\u00b2 (Mass\u2013Energy Equivalence)",
    section="physics",
    topic="Modern Physics",
    sub="Relativity",
    order=1,
    summary="Convert rest mass into its equivalent energy with Einstein's E = mc\u00b2, or solve for the mass from a given energy.",
    formula="E = m c\u00b2",
    tags=["mass energy equivalence", "E=mc2", "einstein", "relativity",
          "rest energy", "nuclear", "joules", "modern physics"],
    viz_template="viz/mass-energy-equivalence.html",
    related=["kinetic-energy", "potential-energy", "work-done"],
    scholar="albert-einstein",
)
def compute(solve_for="energy", mass=0.001, energy=None, **_ignored):
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
        e = num(energy)
    except (TypeError, ValueError):
        return {"error": "Please enter numbers only.", "steps": [], "disclaimer": _DISCLAIMER}

    steps = []
    result = ""
    out_mass = m
    out_energy = e
    comparison = ""

    if sf == "energy":
        if m is None:
            return {"error": "Enter a mass to find its equivalent energy.",
                    "steps": [], "disclaimer": _DISCLAIMER}
        if m < 0:
            return {"error": "Mass cannot be negative.", "steps": [], "disclaimer": _DISCLAIMER}
        out_energy = m * _C2
        comparison = _energy_comparison(out_energy)
        steps = [
            {"label": "Formula", "math": r"\(E = m c^2\)",
             "note": "Rest energy from mass."},
            {"label": "Speed of light",
             "math": r"\(c = 299792458\ \text{m/s},\quad c^2 = " + _sci(_C2) + r"\ \text{m}^2/\text{s}^2\)",
             "note": "c squared is an enormous number, which is why the energy is so large."},
            {"label": "Substitute",
             "math": r"\(E = (" + _f(m) + r")\,(" + _sci(_C2) + r")\)",
             "note": "Insert the mass in kilograms."},
            {"label": "Result", "math": r"\(E = " + _sci(out_energy) + r"\ \text{J}\)",
             "note": "Energy in joules."},
        ]
        result = "Energy = " + _sci_plain(out_energy) + " J" + comparison

    elif sf == "mass":
        if e is None:
            return {"error": "Enter an energy to find the equivalent mass.",
                    "steps": [], "disclaimer": _DISCLAIMER}
        if e < 0:
            return {"error": "Energy cannot be negative.", "steps": [], "disclaimer": _DISCLAIMER}
        out_mass = e / _C2
        steps = [
            {"label": "Rearrange", "math": r"\(m = \dfrac{E}{c^2}\)",
             "note": "Solve E = mc\u00b2 for mass."},
            {"label": "Speed of light",
             "math": r"\(c^2 = " + _sci(_C2) + r"\ \text{m}^2/\text{s}^2\)",
             "note": "The same large constant divides the energy."},
            {"label": "Substitute",
             "math": r"\(m = \dfrac{" + _sci(e) + r"}{" + _sci(_C2) + r"}\)",
             "note": "Insert the energy in joules."},
            {"label": "Result", "math": r"\(m = " + _sci(out_mass) + r"\ \text{kg}\)",
             "note": "Mass in kilograms \u2014 note how little mass a large energy needs."},
        ]
        result = "Mass = " + _sci_plain(out_mass) + " kg"

    else:
        return {"error": "Choose what to solve for: energy or mass.",
                "steps": [], "disclaimer": _DISCLAIMER}

    return {
        "result": result,
        "solve_for": sf,
        "mass": out_mass,
        "energy": out_energy,
        "comparison": comparison,
        "steps": steps,
        "explanation": _EXPLANATION,
        "law_statement": _LAW_STATEMENT,
        "law_source_name": _LAW_SOURCE_NAME,
        "law_source_url": _LAW_SOURCE_URL,
        "disclaimer": _DISCLAIMER,
    }

from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
