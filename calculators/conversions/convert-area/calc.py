"""Area Converter — hub-and-spoke unit converter.

Architecture: every value is converted to the SI base unit (square metre)
first, then from the base to the target. No peer-to-peer conversions.
"""
from core.registry import register

# label -> multiplier that takes 1 <unit> to the base (square metre)
TO_BASE = {
    "mm\u00b2": 1e-06,
    "cm\u00b2": 0.0001,
    "m\u00b2": 1.0,
    "km\u00b2": 1000000.0,
    "in\u00b2": 0.00064516,
    "ft\u00b2": 0.09290304,
    "acre": 4046.8564224,
    "hectare": 10000.0
}

_DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or "
    "system errors. They are provided for general reference only — always "
    "verify results independently before relying on them for engineering, "
    "commercial, or professional decisions."
)

_BENCHMARKS = [
    {"label": "A4 sheet ~0.062 m\u00b2", "base": 0.062},
    {"label": "Tennis court ~261 m\u00b2", "base": 260.87},
    {"label": "Football pitch ~7140 m\u00b2", "base": 7140.0}
]


_EXPLANATION = [
    {"heading": "Area is length squared",
     "body": "The SI unit is the square metre (m²) — a square one metre on a side. Because it is length squared, the conversion factors are the LENGTH factor squared: 1 m = 100 cm, so 1 m² = 100² = 10,000 cm². This catches people out: doubling a room's linear size quadruples its area."},
    {"heading": "Land units",
     "body": "A hectare is 10,000 m² (a 100 m square) — used worldwide for land. An acre is 4046.86 m², an older unit (originally the area a team of oxen could plough in a day). 1 hectare ≈ 2.47 acres."},
    {"heading": "Reading the bar",
     "body": "The bar places your converted area next to familiar benchmarks — a sheet of paper, a tennis court, a football pitch — so an abstract figure like '260 m²' gains real-world scale."},
]


@register(
    slug="convert-area",
    name="Area Converter",
    section="conversions",
    sub="1 · Basic Converters",
    summary="Convert area between metric and imperial units, including acres and hectares, via the square metre.",
    formula="result = value × (from→m²) ÷ (to→m²)",
    tags=['area', 'converter', 'conversion'],
    viz_template="viz/convert-area.html",
)
def compute(value=None, from_unit=None, to_unit=None, **_ignored):
    """Convert `value` from `from_unit` to `to_unit` via the square metre."""
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
        {"label": "To base unit (square metre)",
          "math": f"{v:g} {fu} × {TO_BASE[fu]:g} = {base:g} square metre"},
        {"label": "Base to target",
          "math": f"{base:g} ÷ {TO_BASE[tu]:g} = {result:g} {tu}"},
    ]
    return {
        "result": result,
        "result_unit": tu,
        "base_value": base,
        "base_unit": "square metre",
        "benchmarks": _BENCHMARKS,
        "steps": steps,
        "explanation": _EXPLANATION,
        "disclaimer": _DISCLAIMER,
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
