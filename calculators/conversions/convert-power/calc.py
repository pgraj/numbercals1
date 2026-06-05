"""Power Converter — hub-and-spoke unit converter.

Architecture: every value is converted to the SI base unit (watt)
first, then from the base to the target. No peer-to-peer conversions.
"""
from core.registry import register

# label -> multiplier that takes 1 <unit> to the base (watt)
TO_BASE = {
    "W": 1.0,
    "kW": 1000.0,
    "MW": 1000000.0,
    "mech hp": 745.69987158227,
    "metric hp": 735.49875
}

_DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or "
    "system errors. They are provided for general reference only — always "
    "verify results independently before relying on them for engineering, "
    "commercial, or professional decisions."
)

_BENCHMARKS = [
    {"label": "LED bulb ~10 W", "base": 10.0},
    {"label": "Car engine ~110 kW", "base": 110000.0},
    {"label": "Wind turbine ~3 MW", "base": 3000000.0}
]


_EXPLANATION = [
    {"heading": "Power is energy per second",
     "body": "Power is the rate of using energy: 1 watt = 1 joule per second. A device's power tells you how fast it consumes energy; multiply by time to get total energy used."},
    {"heading": "Horsepower, two flavours",
     "body": "James Watt defined horsepower to sell steam engines against draft horses. Mechanical (imperial) horsepower = 745.7 W; metric horsepower (used on European car specs, 'PS' or 'CV') = 735.5 W. They differ by ~1.4%, so a 100 hp engine and a 100 PS engine are not identical."},
    {"heading": "Worked example",
     "body": "A 150 mechanical-hp engine = 150 × 745.7 = 111,855 W ≈ 112 kW. Seeing it in kW makes it directly comparable to an electric motor rated in kilowatts."},
]


@register(
    slug="convert-power",
    name="Power Converter",
    section="conversions",
    sub="1 · Basic Converters",
    summary="Convert power between watts, kW, MW, mechanical and metric horsepower via the watt.",
    formula="result = value × (from→W) ÷ (to→W)",
    tags=['power', 'converter', 'conversion'],
    viz_template="viz/convert-power.html",
)
def compute(value=None, from_unit=None, to_unit=None, **_ignored):
    """Convert `value` from `from_unit` to `to_unit` via the watt."""
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
        {"label": "To base unit (watt)",
          "math": f"{v:g} {fu} × {TO_BASE[fu]:g} = {base:g} watt"},
        {"label": "Base to target",
          "math": f"{base:g} ÷ {TO_BASE[tu]:g} = {result:g} {tu}"},
    ]
    return {
        "result": result,
        "result_unit": tu,
        "base_value": base,
        "base_unit": "watt",
        "benchmarks": _BENCHMARKS,
        "steps": steps,
        "explanation": _EXPLANATION,
        "disclaimer": _DISCLAIMER,
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
