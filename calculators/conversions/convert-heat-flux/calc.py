"""Heat Flux Converter — hub-and-spoke unit converter.

Architecture: every value is converted to the SI base unit (watt per square metre)
first, then from the base to the target. No peer-to-peer conversions.
"""
from core.registry import register

# label -> multiplier that takes 1 <unit> to the base (watt per square metre)
TO_BASE = {
    "W/m\u00b2": 1.0,
    "BTU/(hr\u00b7ft\u00b2)": 3.154590745
}

_DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or "
    "system errors. They are provided for general reference only — always "
    "verify results independently before relying on them for engineering, "
    "commercial, or professional decisions."
)

_BENCHMARKS = [
    {"label": "Sunlight ~1000 W/m\u00b2", "base": 1000.0},
    {"label": "Skin comfort ~50 W/m\u00b2", "base": 50.0},
    {"label": "Re-entry ~1e6 W/m\u00b2", "base": 1000000.0}
]


_EXPLANATION = [
    {"heading": "Heat flux = heat per area per time",
     "body": "Heat flux is the rate of heat flow through a unit area: watts per square metre, W/m². It answers 'how intensely is heat crossing this surface?' rather than 'how much total heat'."},
    {"heading": "A feel for the numbers",
     "body": "Comfortable skin loses ~50 W/m². Bright sunlight delivers ~1000 W/m² (the basis of solar-panel ratings). A spacecraft heat shield during re-entry can face over 1,000,000 W/m² — which is why ablative shields exist."},
    {"heading": "The imperial unit",
     "body": "US practice uses BTU/(hr·ft²); 1 of those = 3.1546 W/m². So 1000 W/m² of sunshine is about 1000 ÷ 3.1546 ≈ 317 BTU/(hr·ft²)."},
]


@register(
    slug="convert-heat-flux",
    name="Heat Flux Converter",
    section="conversions",
    sub="3 · Thermal, Materials & Everyday",
    summary="Convert heat flux density between W/m² and BTU/(hr·ft²) via the SI base.",
    formula="result = value × (from→W/m²) ÷ (to→W/m²)",
    tags=['heat', 'flux', 'converter', 'conversion'],
    viz_template="viz/convert-heat-flux.html",
)
def compute(value=None, from_unit=None, to_unit=None, **_ignored):
    """Convert `value` from `from_unit` to `to_unit` via the watt per square metre."""
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
        {"label": "To base unit (watt per square metre)",
          "math": f"{v:g} {fu} × {TO_BASE[fu]:g} = {base:g} watt per square metre"},
        {"label": "Base to target",
          "math": f"{base:g} ÷ {TO_BASE[tu]:g} = {result:g} {tu}"},
    ]
    return {
        "result": result,
        "result_unit": tu,
        "base_value": base,
        "base_unit": "watt per square metre",
        "benchmarks": _BENCHMARKS,
        "steps": steps,
        "explanation": _EXPLANATION,
        "disclaimer": _DISCLAIMER,
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
