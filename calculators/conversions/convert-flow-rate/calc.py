"""Flow Rate Converter — hub-and-spoke unit converter.

Architecture: every value is converted to the SI base unit (cubic metre per second)
first, then from the base to the target. No peer-to-peer conversions.
"""
from core.registry import register

# label -> multiplier that takes 1 <unit> to the base (cubic metre per second)
TO_BASE = {
    "m\u00b3/s": 1.0,
    "CFM": 0.000471947443,
    "L/min": 1.66666666667e-05,
    "L/s": 0.001
}

_DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or "
    "system errors. They are provided for general reference only — always "
    "verify results independently before relying on them for engineering, "
    "commercial, or professional decisions."
)

_BENCHMARKS = [
    {"label": "Tap ~0.0002 m\u00b3/s", "base": 0.0002},
    {"label": "Shower ~0.00015 m\u00b3/s", "base": 0.00015},
    {"label": "Fire hose ~0.06 m\u00b3/s", "base": 0.06}
]


_EXPLANATION = [
    {"heading": "Two kinds of 'flow'",
     "body": "Flow rate is how much fluid passes a point per second. VOLUMETRIC flow (m³/s, L/min, CFM) measures volume per time; MASS flow (kg/s) measures mass per time. They are linked by density (mass flow = volume flow × density), but they are not interchangeable units — this converter handles volumetric flow."},
    {"heading": "The everyday units",
     "body": "CFM (cubic feet per minute) is the standard for air — fans, ventilation, compressors. L/min and L/s are used for water, pumps and taps. 1 CFM ≈ 0.000472 m³/s ≈ 28.3 L/min."},
    {"heading": "Worked example",
     "body": "A shower at 9 L/min = 9 ÷ 60 = 0.15 L/s = 0.00015 m³/s. Over a 10-minute shower that is 90 litres — a tangible way to see water use."},
]


@register(
    slug="convert-flow-rate",
    name="Flow Rate Converter",
    section="conversions",
    sub="2 · Mechanics & Fluids",
    summary="Convert volumetric flow rate between m³/s, CFM, L/min and L/s via cubic metres per second.",
    formula="result = value × (from→m³/s) ÷ (to→m³/s)",
    tags=['flow', 'rate', 'converter', 'conversion'],
    viz_template="viz/convert-flow-rate.html",
)
def compute(value=None, from_unit=None, to_unit=None, **_ignored):
    """Convert `value` from `from_unit` to `to_unit` via the cubic metre per second."""
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
        {"label": "To base unit (cubic metre per second)",
          "math": f"{v:g} {fu} × {TO_BASE[fu]:g} = {base:g} cubic metre per second"},
        {"label": "Base to target",
          "math": f"{base:g} ÷ {TO_BASE[tu]:g} = {result:g} {tu}"},
    ]
    return {
        "result": result,
        "result_unit": tu,
        "base_value": base,
        "base_unit": "cubic metre per second",
        "benchmarks": _BENCHMARKS,
        "steps": steps,
        "explanation": _EXPLANATION,
        "disclaimer": _DISCLAIMER,
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
