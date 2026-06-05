"""Mass Converter — hub-and-spoke unit converter.

Architecture: every value is converted to the SI base unit (kilogram)
first, then from the base to the target. No peer-to-peer conversions.
"""
from core.registry import register

# label -> multiplier that takes 1 <unit> to the base (kilogram)
TO_BASE = {
    "\u03bcg": 1e-09,
    "mg": 1e-06,
    "g": 0.001,
    "kg": 1.0,
    "t (metric)": 1000.0,
    "oz": 0.028349523125,
    "lb": 0.45359237,
    "stone": 6.35029318,
    "short ton": 907.18474,
    "long ton": 1016.0469088,
    "troy oz": 0.0311034768,
    "troy lb": 0.3732417216
}

_DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or "
    "system errors. They are provided for general reference only — always "
    "verify results independently before relying on them for engineering, "
    "commercial, or professional decisions."
)

_BENCHMARKS = [
    {"label": "Apple ~0.15 kg", "base": 0.15},
    {"label": "Person ~70 kg", "base": 70.0},
    {"label": "Small car ~1200 kg", "base": 1200.0}
]


_EXPLANATION = [
    {"heading": "Mass vs weight",
     "body": "This converts mass (how much matter is in something), whose SI unit is the kilogram. Weight is a force (mass × gravity) measured in newtons — a 70 kg person has the same mass on the Moon but about one-sixth the weight. Bathroom scales show mass by assuming Earth gravity."},
    {"heading": "The kilogram and its relatives",
     "body": "Since 2019 the kilogram is defined via the Planck constant. Everyday units hang off it by fixed factors: 1 pound = 0.45359237 kg exactly, 1 ounce = 1/16 lb, 1 stone = 14 lb. Troy units (used for precious metals) are different: 1 troy ounce ≈ 31.103 g, heavier than the everyday ounce."},
    {"heading": "Tons are a trap",
     "body": "Three different 'tons' exist: the metric tonne (1000 kg), the US short ton (907.18 kg) and the UK long ton (1016.05 kg). Always check which one a figure means — the gap is over 10%."},
]


@register(
    slug="convert-mass",
    name="Mass Converter",
    section="conversions",
    sub="1 · Basic Converters",
    summary="Convert mass between metric, avoirdupois and troy units, including metric and imperial tons, via the kilogram.",
    formula="result = value × (from→kg) ÷ (to→kg)",
    tags=['mass', 'converter', 'conversion'],
    viz_template="viz/convert-mass.html",
)
def compute(value=None, from_unit=None, to_unit=None, **_ignored):
    """Convert `value` from `from_unit` to `to_unit` via the kilogram."""
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
        {"label": "To base unit (kilogram)",
          "math": f"{v:g} {fu} × {TO_BASE[fu]:g} = {base:g} kilogram"},
        {"label": "Base to target",
          "math": f"{base:g} ÷ {TO_BASE[tu]:g} = {result:g} {tu}"},
    ]
    return {
        "result": result,
        "result_unit": tu,
        "base_value": base,
        "base_unit": "kilogram",
        "benchmarks": _BENCHMARKS,
        "steps": steps,
        "explanation": _EXPLANATION,
        "disclaimer": _DISCLAIMER,
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
