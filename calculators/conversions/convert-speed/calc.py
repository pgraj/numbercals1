"""Speed Converter — hub-and-spoke unit converter.

Architecture: every value is converted to the SI base unit (metre per second)
first, then from the base to the target. No peer-to-peer conversions.
"""
from core.registry import register

# label -> multiplier that takes 1 <unit> to the base (metre per second)
TO_BASE = {
    "m/s": 1.0,
    "km/h": 0.277777777778,
    "mph": 0.44704,
    "knots": 0.514444444444,
    "ft/s": 0.3048
}

_DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or "
    "system errors. They are provided for general reference only — always "
    "verify results independently before relying on them for engineering, "
    "commercial, or professional decisions."
)

_BENCHMARKS = [
    {"label": "Walking ~1.4 m/s", "base": 1.4},
    {"label": "Highway ~28 m/s", "base": 27.78},
    {"label": "Sound ~343 m/s", "base": 343.0}
]


_EXPLANATION = [
    {"heading": "Speed is distance over time",
     "body": "The SI unit is metres per second (m/s). Every other speed unit is just a different distance-and-time pairing converted back to m/s. 1 km/h = 1000 m ÷ 3600 s = 0.2778 m/s."},
    {"heading": "The units and where they live",
     "body": "km/h and mph are road speeds; knots (nautical miles per hour, 1 knot = 0.5144 m/s) are used in aviation and at sea; ft/s appears in US physics and ballistics. The speed of sound at sea level is about 343 m/s ≈ 1235 km/h ≈ 767 mph — the line between subsonic and supersonic."},
    {"heading": "Reading the bar",
     "body": "Your converted speed sits beside benchmarks — a brisk walk (~1.4 m/s), highway driving (~28 m/s), the speed of sound (~343 m/s) — so the number is grounded in things you can picture."},
]


@register(
    slug="convert-speed",
    name="Speed Converter",
    section="conversions",
    sub="1 · Basic Converters",
    summary="Convert speed between m/s, km/h, mph, knots and ft/s via metres per second.",
    formula="result = value × (from→m/s) ÷ (to→m/s)",
    tags=['speed', 'converter', 'conversion'],
    viz_template="viz/convert-speed.html",
)
def compute(value=None, from_unit=None, to_unit=None, **_ignored):
    """Convert `value` from `from_unit` to `to_unit` via the metre per second."""
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
        {"label": "To base unit (metre per second)",
          "math": f"{v:g} {fu} × {TO_BASE[fu]:g} = {base:g} metre per second"},
        {"label": "Base to target",
          "math": f"{base:g} ÷ {TO_BASE[tu]:g} = {result:g} {tu}"},
    ]
    return {
        "result": result,
        "result_unit": tu,
        "base_value": base,
        "base_unit": "metre per second",
        "benchmarks": _BENCHMARKS,
        "steps": steps,
        "explanation": _EXPLANATION,
        "disclaimer": _DISCLAIMER,
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
