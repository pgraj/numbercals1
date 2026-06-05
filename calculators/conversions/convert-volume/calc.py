"""Volume Converter — hub-and-spoke unit converter.

Architecture: every value is converted to the SI base unit (cubic metre)
first, then from the base to the target. No peer-to-peer conversions.
"""
from core.registry import register

# label -> multiplier that takes 1 <unit> to the base (cubic metre)
TO_BASE = {
    "L": 0.001,
    "mL": 1e-06,
    "US gal": 0.003785411784,
    "US qt": 0.000946352946,
    "US pt": 0.000473176473,
    "US cup": 0.0002365882365,
    "fl oz": 2.95735295625e-05,
    "tbsp": 1.47867647813e-05,
    "tsp": 4.92892159375e-06,
    "in\u00b3": 1.6387064e-05,
    "ft\u00b3": 0.028316846592
}

_DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or "
    "system errors. They are provided for general reference only — always "
    "verify results independently before relying on them for engineering, "
    "commercial, or professional decisions."
)

_BENCHMARKS = [
    {"label": "Soda can 0.355 L", "base": 0.000355},
    {"label": "Bathtub ~150 L", "base": 0.15},
    {"label": "Olympic pool 2500 m\u00b3", "base": 2500.0}
]


_EXPLANATION = [
    {"heading": "Volume is length cubed",
     "body": "The SI unit is the cubic metre (m³) — a cube one metre on each side. A litre is exactly 1/1000 of a cubic metre (a 10 cm cube), which is why 1 mL = 1 cm³."},
    {"heading": "US cooking units are small fractions",
     "body": "US customary cooking measures all derive from the gallon: 1 US gallon = 3.785411784 L, and a quart is ¼ gallon, a pint ⅛, a cup 1/16, a fluid ounce 1/128. The factors look fiddly because each step halves or quarters the one above."},
    {"heading": "Watch US vs Imperial",
     "body": "A US gallon (3.785 L) is smaller than an Imperial gallon (4.546 L). This converter uses US customary units; a UK recipe's 'pint' is larger than a US pint."},
]


@register(
    slug="convert-volume",
    name="Volume Converter",
    section="conversions",
    sub="3 · Thermal, Materials & Everyday",
    summary="Convert volume between litres, US customary cooking units and cubic measures via the cubic metre.",
    formula="result = value × (from→m³) ÷ (to→m³)",
    tags=['volume', 'converter', 'conversion'],
    viz_template="viz/convert-volume.html",
)
def compute(value=None, from_unit=None, to_unit=None, **_ignored):
    """Convert `value` from `from_unit` to `to_unit` via the cubic metre."""
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
        {"label": "To base unit (cubic metre)",
          "math": f"{v:g} {fu} × {TO_BASE[fu]:g} = {base:g} cubic metre"},
        {"label": "Base to target",
          "math": f"{base:g} ÷ {TO_BASE[tu]:g} = {result:g} {tu}"},
    ]
    return {
        "result": result,
        "result_unit": tu,
        "base_value": base,
        "base_unit": "cubic metre",
        "benchmarks": _BENCHMARKS,
        "steps": steps,
        "explanation": _EXPLANATION,
        "disclaimer": _DISCLAIMER,
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
