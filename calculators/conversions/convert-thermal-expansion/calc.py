"""Thermal Expansion Coefficient Converter — hub-and-spoke unit converter.

Architecture: every value is converted to the SI base unit (per kelvin)
first, then from the base to the target. No peer-to-peer conversions.
"""
from core.registry import register

# label -> multiplier that takes 1 <unit> to the base (per kelvin)
TO_BASE = {
    "1/K": 1.0,
    "1/\u00b0F": 1.8
}

_DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or "
    "system errors. They are provided for general reference only — always "
    "verify results independently before relying on them for engineering, "
    "commercial, or professional decisions."
)

_BENCHMARKS = [
    {"label": "Steel ~1.2e-5 /K", "base": 1.2e-05},
    {"label": "Aluminium ~2.3e-5 /K", "base": 2.3e-05},
    {"label": "Invar ~1.2e-6 /K", "base": 1.2e-06}
]


_EXPLANATION = [
    {"heading": "Why materials grow when heated",
     "body": "Heat makes atoms vibrate more and sit slightly farther apart, so most materials expand when warmed. The linear coefficient of thermal expansion (α) says how much: the fractional change in length per degree of temperature rise. Its SI unit is 'per kelvin' (1/K)."},
    {"heading": "How to read the number",
     "body": "Steel's α ≈ 1.2 × 10⁻⁵ /K means a 1 m steel bar grows 0.000012 m (12 micrometres) for every 1 K rise. Over a 50 m bridge and a 40 K summer-to-winter swing, that is 50 × 1.2e-5 × 40 = 0.024 m = 24 mm — real movement, which is why bridges have expansion joints."},
    {"heading": "The °F conversion (a factor, not an offset)",
     "body": "Converting α between '/K' and '/°F' is just a scale factor, because we are dealing with a temperature DIFFERENCE, not a temperature. A change of 1 K equals a change of 1.8 °F, so α in 1/°F = α in 1/K ÷ 1.8. (No 32° offset here — that offset only applies to actual temperatures, not to temperature differences.) Example: 1.2e-5 /K ÷ 1.8 ≈ 6.67e-6 /°F."},
]


@register(
    slug="convert-thermal-expansion",
    name="Thermal Expansion Coefficient Converter",
    section="conversions",
    sub="3 · Thermal, Materials & Everyday",
    summary="Convert linear thermal expansion coefficient between 1/K and 1/°F.",
    formula="result = value × (from→1/K) ÷ (to→1/K); 1/°F = 1.8 × 1/K",
    tags=['thermal', 'expansion', 'converter', 'conversion'],
    viz_template="viz/convert-thermal-expansion.html",
)
def compute(value=None, from_unit=None, to_unit=None, **_ignored):
    """Convert `value` from `from_unit` to `to_unit` via the per kelvin."""
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
        {"label": "To base unit (per kelvin)",
          "math": f"{v:g} {fu} × {TO_BASE[fu]:g} = {base:g} per kelvin"},
        {"label": "Base to target",
          "math": f"{base:g} ÷ {TO_BASE[tu]:g} = {result:g} {tu}"},
    ]
    return {
        "result": result,
        "result_unit": tu,
        "base_value": base,
        "base_unit": "per kelvin",
        "benchmarks": _BENCHMARKS,
        "steps": steps,
        "explanation": _EXPLANATION,
        "disclaimer": _DISCLAIMER,
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
