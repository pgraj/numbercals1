"""Viscosity Converter — hub-and-spoke unit converter.

Architecture: every value is converted to the SI base unit (pascal-second)
first, then from the base to the target. No peer-to-peer conversions.
"""
from core.registry import register

# label -> multiplier that takes 1 <unit> to the base (pascal-second)
TO_BASE = {
    "Pa\u00b7s": 1.0,
    "Poise": 0.1,
    "cP": 0.001,
    "m\u00b2/s": 1.0,
    "St": 0.0001,
    "cSt": 1e-06
}

_DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or "
    "system errors. They are provided for general reference only — always "
    "verify results independently before relying on them for engineering, "
    "commercial, or professional decisions."
)

_BENCHMARKS = [
    {"label": "Water ~0.001 Pa\u00b7s", "base": 0.001},
    {"label": "Olive oil ~0.08 Pa\u00b7s", "base": 0.08},
    {"label": "Honey ~10 Pa\u00b7s", "base": 10.0}
]


_EXPLANATION = [
    {"heading": "What viscosity measures",
     "body": "Viscosity is a fluid's resistance to flow — its 'thickness'. Water is thin (low viscosity); honey is thick (high viscosity). The SI unit of DYNAMIC viscosity is the pascal-second (Pa·s)."},
    {"heading": "Dynamic vs kinematic — keep them apart",
     "body": "Dynamic viscosity (μ) is the raw resistance, in Pa·s or poise (1 P = 0.1 Pa·s; 1 centipoise cP = 0.001 Pa·s, and water is conveniently ~1 cP). KINEMATIC viscosity (ν) is dynamic viscosity divided by density, in m²/s or stokes (1 St = 1e-4 m²/s; 1 cSt = 1e-6 m²/s). They describe different things, so this tool only converts within one family at a time — never mix Pa·s with m²/s."},
    {"heading": "Why it matters",
     "body": "Engine oils are graded by viscosity (the '5W-30' on the bottle). Too thin and it won't protect; too thick and it wastes energy. Kinematic viscosity drives how fluids behave in pipes and is a key input to the Reynolds number."},
]


@register(
    slug="convert-viscosity",
    name="Viscosity Converter",
    section="conversions",
    sub="2 · Advanced Converters",
    summary="Convert dynamic viscosity (Pa·s, poise, cP) and kinematic viscosity (m²/s, stokes, cSt). Pick one family.",
    formula="result = value × (from→Pa·s) ÷ (to→Pa·s); kinematic via m²/s",
    tags=['viscosity', 'converter', 'conversion'],
    viz_template="viz/convert-viscosity.html",
)
def compute(value=None, from_unit=None, to_unit=None, **_ignored):
    """Convert `value` from `from_unit` to `to_unit` via the pascal-second."""
    if value is None or from_unit is None or to_unit is None:
        return {"error": "Provide a value, a source unit, and a target unit.", "steps": []}
    try:
        v = float(value)
    except (TypeError, ValueError):
        return {"error": "Value must be a number.", "steps": []}
    fu, tu = str(from_unit), str(to_unit)
    if fu not in TO_BASE:
        return {"error": "Unknown source unit: " + fu, "steps": []}
    if tu not in TO_BASE:
        return {"error": "Unknown target unit: " + tu, "steps": []}

    base = v * TO_BASE[fu]
    result = base / TO_BASE[tu]

    steps = [
        {"label": "To base unit (pascal-second)",
          "math": f"{v:g} {fu} × {TO_BASE[fu]:g} = {base:g} pascal-second"},
        {"label": "Base to target",
          "math": f"{base:g} ÷ {TO_BASE[tu]:g} = {result:g} {tu}"},
    ]
    return {
        "result": result,
        "result_unit": tu,
        "base_value": base,
        "base_unit": "pascal-second",
        "benchmarks": _BENCHMARKS,
        "steps": steps,
        "explanation": _EXPLANATION,
        "disclaimer": _DISCLAIMER,
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
