"""Chemical Specific Energy Converter — hub-and-spoke unit converter.

Architecture: every value is converted to the SI base unit (megajoule per kilogram)
first, then from the base to the target. No peer-to-peer conversions.
"""
from core.registry import register

# label -> multiplier that takes 1 <unit> to the base (megajoule per kilogram)
TO_BASE = {
    "MJ/kg": 1.0,
    "BTU/lb": 0.002326,
    "kWh/kg": 3.6,
    "cal/g": 0.004184
}

_DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or "
    "system errors. They are provided for general reference only — always "
    "verify results independently before relying on them for engineering, "
    "commercial, or professional decisions."
)

_BENCHMARKS = [
    {"label": "Wood ~16 MJ/kg", "base": 16.0},
    {"label": "Petrol ~46 MJ/kg", "base": 46.0},
    {"label": "Hydrogen ~142 MJ/kg", "base": 142.0}
]


_EXPLANATION = [
    {"heading": "Specific energy = energy per kilogram",
     "body": "This compares fuels by how much energy each kilogram stores (gravimetric energy density). The SI-friendly unit here is MJ/kg. It tells you how much 'punch' a fuel packs for its mass — critical for vehicles and rockets where weight matters."},
    {"heading": "The units you will meet",
     "body": "BTU/lb appears in US engineering; kWh/kg in battery and electric contexts; cal/g in chemistry and nutrition. 1 MJ/kg ≈ 430 BTU/lb ≈ 0.278 kWh/kg ≈ 239 cal/g."},
    {"heading": "Why hydrogen looks amazing but isn't simple",
     "body": "Hydrogen stores ~142 MJ/kg — three times petrol's ~46 MJ/kg by mass. But hydrogen is incredibly light, so per litre it stores far less energy unless compressed or liquefied. Specific energy (per kg) and energy density (per litre) tell different halves of the story."},
]


@register(
    slug="convert-fuel-energy",
    name="Chemical Specific Energy Converter",
    section="conversions",
    sub="2 · Mechanics & Fluids",
    summary="Convert specific (gravimetric) energy of fuels between MJ/kg, BTU/lb, kWh/kg and cal/g.",
    formula="result = value × (from→MJ/kg) ÷ (to→MJ/kg)",
    tags=['fuel', 'energy', 'converter', 'conversion'],
    viz_template="viz/convert-fuel-energy.html",
)
def compute(value=None, from_unit=None, to_unit=None, **_ignored):
    """Convert `value` from `from_unit` to `to_unit` via the megajoule per kilogram."""
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
        {"label": "To base unit (megajoule per kilogram)",
          "math": f"{v:g} {fu} × {TO_BASE[fu]:g} = {base:g} megajoule per kilogram"},
        {"label": "Base to target",
          "math": f"{base:g} ÷ {TO_BASE[tu]:g} = {result:g} {tu}"},
    ]
    return {
        "result": result,
        "result_unit": tu,
        "base_value": base,
        "base_unit": "megajoule per kilogram",
        "benchmarks": _BENCHMARKS,
        "steps": steps,
        "explanation": _EXPLANATION,
        "disclaimer": _DISCLAIMER,
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
