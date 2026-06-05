"""Specific Impulse Converter — hub-and-spoke unit converter.

Architecture: every value is converted to the SI base unit (newton-second per kilogram)
first, then from the base to the target. No peer-to-peer conversions.
"""
from core.registry import register

# label -> multiplier that takes 1 <unit> to the base (newton-second per kilogram)
TO_BASE = {
    "N\u00b7s/kg": 1.0,
    "m/s": 1.0,
    "s": 9.80665
}

_DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or "
    "system errors. They are provided for general reference only — always "
    "verify results independently before relying on them for engineering, "
    "commercial, or professional decisions."
)

_BENCHMARKS = [
    {"label": "Solid booster ~250 s", "base": 2451.7},
    {"label": "Kerolox ~300 s", "base": 2942.0},
    {"label": "Hydrolox ~450 s", "base": 4413.0}
]


_EXPLANATION = [
    {"heading": "What specific impulse means",
     "body": "Specific impulse (Isp) measures rocket-engine efficiency: how much thrust you get per unit of propellant used per second. Higher Isp means you go further on the same fuel. It is the rocket equivalent of 'miles per gallon'."},
    {"heading": "Seconds vs m/s — the same thing twice",
     "body": "Confusingly, Isp is quoted two ways. As an effective exhaust velocity it is in m/s (or N·s/kg, which is identical). As 'seconds' it is that velocity divided by g₀ = 9.80665 m/s². So to convert Isp in seconds to m/s, multiply by 9.80665; to go back, divide. The 'seconds' figure is popular because it comes out the same in metric or imperial units."},
    {"heading": "Worked example",
     "body": "A kerosene/oxygen engine with Isp ≈ 300 s has an exhaust velocity of 300 × 9.80665 ≈ 2942 m/s. A hydrogen/oxygen engine (~450 s) reaches ~4413 m/s — far more efficient, which is why upper stages often use hydrogen."},
]


@register(
    slug="convert-specific-impulse",
    name="Specific Impulse Converter",
    section="conversions",
    sub="2 · Mechanics & Fluids",
    summary="Convert rocket specific impulse between seconds and effective exhaust velocity (N·s/kg = m/s) using g₀.",
    formula="Isp(m/s) = Isp(s) × g₀; g₀ = 9.80665 m/s². Base = N·s/kg = m/s.",
    tags=['specific', 'impulse', 'converter', 'conversion'],
    viz_template="viz/convert-specific-impulse.html",
)
def compute(value=None, from_unit=None, to_unit=None, **_ignored):
    """Convert `value` from `from_unit` to `to_unit` via the newton-second per kilogram."""
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
        {"label": "To base unit (newton-second per kilogram)",
          "math": f"{v:g} {fu} × {TO_BASE[fu]:g} = {base:g} newton-second per kilogram"},
        {"label": "Base to target",
          "math": f"{base:g} ÷ {TO_BASE[tu]:g} = {result:g} {tu}"},
    ]
    return {
        "result": result,
        "result_unit": tu,
        "base_value": base,
        "base_unit": "newton-second per kilogram",
        "benchmarks": _BENCHMARKS,
        "steps": steps,
        "explanation": _EXPLANATION,
        "disclaimer": _DISCLAIMER,
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
