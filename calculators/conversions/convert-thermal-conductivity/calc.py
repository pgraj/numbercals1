"""Thermal Conductivity Converter — hub-and-spoke unit converter.

Architecture: every value is converted to the SI base unit (watt per metre-kelvin)
first, then from the base to the target. No peer-to-peer conversions.
"""
from core.registry import register

# label -> multiplier that takes 1 <unit> to the base (watt per metre-kelvin)
TO_BASE = {
    "W/(m\u00b7K)": 1.0,
    "BTU/(hr\u00b7ft\u00b7\u00b0F)": 1.730734666
}

_DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or "
    "system errors. They are provided for general reference only — always "
    "verify results independently before relying on them for engineering, "
    "commercial, or professional decisions."
)

_BENCHMARKS = [
    {"label": "Air ~0.026", "base": 0.026},
    {"label": "Water ~0.6", "base": 0.6},
    {"label": "Copper ~400", "base": 400.0}
]


_EXPLANATION = [
    {"heading": "What thermal conductivity tells you",
     "body": "Thermal conductivity (k) measures how readily a material carries heat. High-k materials (metals) move heat fast; low-k materials (air, foam, wood) resist it and make good insulators. The SI unit is the watt per metre-kelvin, W/(m·K): how many watts flow through a 1 m thick, 1 m² slab for each 1 K of temperature difference across it."},
    {"heading": "A feel for the numbers",
     "body": "Still air ≈ 0.026, water ≈ 0.6, glass ≈ 1, steel ≈ 50, aluminium ≈ 240, copper ≈ 400 W/(m·K). Copper conducts heat about 15,000× better than air — which is exactly why saucepans are copper-bottomed and insulation traps air."},
    {"heading": "The imperial unit",
     "body": "US engineering often uses BTU/(hr·ft·°F). The conversion is 1 BTU/(hr·ft·°F) = 1.7307 W/(m·K). So a material listed as 231 in W/(m·K) is about 400 ÷ 1.7307 ≈ 231 BTU/(hr·ft·°F) — the same physical conductivity, different bookkeeping."},
]


@register(
    slug="convert-thermal-conductivity",
    name="Thermal Conductivity Converter",
    section="conversions",
    sub="3 · Thermal, Materials & Everyday",
    summary="Convert thermal conductivity between W/(m·K) and BTU/(hr·ft·°F) via the SI base.",
    formula="result = value × (from→W/(m·K)) ÷ (to→W/(m·K))",
    tags=['thermal', 'conductivity', 'converter', 'conversion'],
    viz_template="viz/convert-thermal-conductivity.html",
)
def compute(value=None, from_unit=None, to_unit=None, **_ignored):
    """Convert `value` from `from_unit` to `to_unit` via the watt per metre-kelvin."""
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
        {"label": "To base unit (watt per metre-kelvin)",
          "math": f"{v:g} {fu} × {TO_BASE[fu]:g} = {base:g} watt per metre-kelvin"},
        {"label": "Base to target",
          "math": f"{base:g} ÷ {TO_BASE[tu]:g} = {result:g} {tu}"},
    ]
    return {
        "result": result,
        "result_unit": tu,
        "base_value": base,
        "base_unit": "watt per metre-kelvin",
        "benchmarks": _BENCHMARKS,
        "steps": steps,
        "explanation": _EXPLANATION,
        "disclaimer": _DISCLAIMER,
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
