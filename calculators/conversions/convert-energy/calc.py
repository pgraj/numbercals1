"""Energy Converter — hub-and-spoke unit converter.

Architecture: every value is converted to the SI base unit (joule)
first, then from the base to the target. No peer-to-peer conversions.
"""
from core.registry import register

# label -> multiplier that takes 1 <unit> to the base (joule)
TO_BASE = {
    "J": 1.0,
    "cal": 4.184,
    "kcal": 4184.0,
    "Wh": 3600.0,
    "kWh": 3600000.0,
    "BTU": 1055.05585262,
    "eV": 1.602176634e-19,
    "MJ": 1000000.0
}

_DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or "
    "system errors. They are provided for general reference only — always "
    "verify results independently before relying on them for engineering, "
    "commercial, or professional decisions."
)

_BENCHMARKS = [
    {"label": "AA battery ~10 kJ", "base": 10000.0},
    {"label": "Apple ~520 kJ", "base": 520000.0},
    {"label": "Home/day ~108 MJ", "base": 108000000.0}
]


_EXPLANATION = [
    {"heading": "One unit, many disguises",
     "body": "Energy always measures the same physical thing — the capacity to do work or produce heat — but different fields invented their own units. The SI unit is the joule (J): the energy to push with 1 newton over 1 metre."},
    {"heading": "The everyday units",
     "body": "A calorie (4.184 J) heats 1 g of water by 1 °C; the 'Calorie' on food labels is actually a kilocalorie (4184 J). A watt-hour (3600 J) is one watt sustained for an hour, and a kilowatt-hour (3.6 MJ) is the unit on your electricity bill. A BTU (1055 J) is the heating/cooling unit on air-conditioners."},
    {"heading": "Worked example",
     "body": "1 kWh = 1 × 3,600,000 J = 3.6 MJ. So a 2000 W heater run for one hour uses 2 kWh = 7.2 MJ — roughly the chemical energy in a small chocolate bar's worth of food, which is why energy comparisons across domains are so revealing."},
]


@register(
    slug="convert-energy",
    name="Energy Converter",
    section="conversions",
    sub="1 · Basic Converters",
    summary="Convert energy between joules, calories, watt-hours, BTU and electronvolts via the joule.",
    formula="result = value × (from→J) ÷ (to→J)",
    tags=['energy', 'converter', 'conversion'],
    viz_template="viz/convert-energy.html",
)
def compute(value=None, from_unit=None, to_unit=None, **_ignored):
    """Convert `value` from `from_unit` to `to_unit` via the joule."""
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
        {"label": "To base unit (joule)",
          "math": f"{v:g} {fu} × {TO_BASE[fu]:g} = {base:g} joule"},
        {"label": "Base to target",
          "math": f"{base:g} ÷ {TO_BASE[tu]:g} = {result:g} {tu}"},
    ]
    return {
        "result": result,
        "result_unit": tu,
        "base_value": base,
        "base_unit": "joule",
        "benchmarks": _BENCHMARKS,
        "steps": steps,
        "explanation": _EXPLANATION,
        "disclaimer": _DISCLAIMER,
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
