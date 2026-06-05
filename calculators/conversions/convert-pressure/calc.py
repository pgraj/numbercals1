"""Pressure Converter — hub-and-spoke unit converter.

Architecture: every value is converted to the SI base unit (pascal)
first, then from the base to the target. No peer-to-peer conversions.
"""
from core.registry import register

# label -> multiplier that takes 1 <unit> to the base (pascal)
TO_BASE = {
    "Pa": 1.0,
    "bar": 100000.0,
    "mbar": 100.0,
    "PSI": 6894.757293168,
    "atm": 101325.0,
    "mmHg": 133.322387415,
    "Torr": 133.322368421,
    "inH\u2082O": 249.0889
}

_DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or "
    "system errors. They are provided for general reference only — always "
    "verify results independently before relying on them for engineering, "
    "commercial, or professional decisions."
)

_BENCHMARKS = [
    {"label": "Tyre ~220 kPa", "base": 220000.0},
    {"label": "Sea level 101.325 kPa", "base": 101325.0},
    {"label": "Vacuum ~0 Pa", "base": 1.0}
]


_EXPLANATION = [
    {"heading": "What is a pascal?",
     "body": "Pressure is force spread over an area. The SI unit, the pascal (Pa), is exactly one newton of force pressed onto one square metre: 1 Pa = 1 N/m². That is a tiny pressure — about the weight of a sheet of paper resting on a tabletop — which is why everyday pressures run into thousands or hundreds of thousands of pascals."},
    {"heading": "Where does 101,325 come from? (the 1 atm blind spot)",
     "body": "One standard atmosphere (1 atm) is DEFINED as exactly 101,325 Pa. It is not a random number — it is the average air pressure at sea level, set as a reference standard. You can sanity-check it physically: the atmosphere is roughly a 10.3 m column of water (or 760 mm of mercury) pressing down. Pressure from a fluid column is P = ρ·g·h. For mercury, ρ = 13,595 kg/m³, g = 9.80665 m/s², h = 0.76 m, giving 13,595 × 9.80665 × 0.76 ≈ 101,325 Pa. That is why a barometer reads '760 mmHg' at sea level — it is the same pressure, just measured as a height of mercury."},
    {"heading": "The practical units",
     "body": "1 bar = 100,000 Pa (close to 1 atm, used in weather and engineering). 1 PSI = 6894.76 Pa (pounds per square inch, used for tyres in the US). Your car tyre at ~32 PSI ≈ 220,000 Pa ≈ 2.2 bar ≈ 2.2 times atmospheric pressure."},
    {"heading": "Worked example",
     "body": "Convert 1 atm to PSI: 1 atm = 101,325 Pa, then 101,325 ÷ 6894.76 ≈ 14.696 PSI. So normal sea-level pressure is about 14.7 PSI — the number every diver and mechanic carries in their head."},
]


@register(
    slug="convert-pressure",
    name="Pressure Converter",
    section="conversions",
    sub="2 · Advanced Converters",
    summary="Convert pressure between Pa, bar, PSI, atm, mmHg/Torr and inH₂O via the pascal.",
    formula="result = value × (from→Pa) ÷ (to→Pa)",
    tags=['pressure', 'converter', 'conversion'],
    viz_template="viz/convert-pressure.html",
)
def compute(value=None, from_unit=None, to_unit=None, **_ignored):
    """Convert `value` from `from_unit` to `to_unit` via the pascal."""
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
        {"label": "To base unit (pascal)",
          "math": f"{v:g} {fu} × {TO_BASE[fu]:g} = {base:g} pascal"},
        {"label": "Base to target",
          "math": f"{base:g} ÷ {TO_BASE[tu]:g} = {result:g} {tu}"},
    ]
    return {
        "result": result,
        "result_unit": tu,
        "base_value": base,
        "base_unit": "pascal",
        "benchmarks": _BENCHMARKS,
        "steps": steps,
        "explanation": _EXPLANATION,
        "disclaimer": _DISCLAIMER,
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
