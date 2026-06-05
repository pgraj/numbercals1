"""Length Converter — hub-and-spoke unit converter.

Architecture: every value is converted to the SI base unit (metre)
first, then from the base to the target. No peer-to-peer conversions.
"""
from core.registry import register

# label -> multiplier that takes 1 <unit> to the base (metre)
TO_BASE = {
    "nm": 1e-09,
    "\u03bcm": 1e-06,
    "mm": 0.001,
    "cm": 0.01,
    "m": 1.0,
    "km": 1000.0,
    "in": 0.0254,
    "ft": 0.3048,
    "yd": 0.9144,
    "mile": 1609.344,
    "nmi": 1852.0,
    "AU": 149597870700.0,
    "light-year": 9460730472580800.0
}

_DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or "
    "system errors. They are provided for general reference only — always "
    "verify results independently before relying on them for engineering, "
    "commercial, or professional decisions."
)

_BENCHMARKS = [
    {"label": "Human height ~1.7 m", "base": 1.7},
    {"label": "Football pitch ~105 m", "base": 105.0},
    {"label": "Marathon 42.195 km", "base": 42195.0}
]


_EXPLANATION = [
    {"heading": "What is the metre, really?",
     "body": "The metre is the SI base unit of length. Since 1983 it has been defined as the distance light travels in a vacuum in 1/299,792,458 of a second — a definition tied to a fundamental constant rather than a physical bar, so it never drifts. Every other length unit is just a fixed multiple of the metre."},
    {"heading": "How the conversion works (hub-and-spoke)",
     "body": "Rather than memorising every pair (cm→inch, mile→km, …), we convert your value to metres first, then from metres to your target. One number in, one number out, via a common hub. That is why 1 inch = 0.0254 m exactly and 1 foot = 0.3048 m exactly — those are defined values, not measurements."},
    {"heading": "Why some factors look 'ugly'",
     "body": "Metric steps are powers of ten (1 km = 1000 m), so they look clean. Imperial units came from older human-scale references (a foot, a yard) and were later pinned to the metre, giving exact but non-round factors like 1 mile = 1609.344 m."},
]


@register(
    slug="convert-length",
    name="Scale Converter",
    section="conversions",
    sub="1 · Basic Converters",
    summary="Convert length between metric, imperial and astronomical units — nanometres to light-years — via the metre.",
    formula="result = value × (from→metre) ÷ (to→metre)",
    tags=['length', 'converter', 'conversion'],
    viz_template="viz/convert-length.html",
)
def compute(value=None, from_unit=None, to_unit=None, **_ignored):
    """Convert `value` from `from_unit` to `to_unit` via the metre."""
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
        {"label": "To base unit (metre)",
          "math": f"{v:g} {fu} × {TO_BASE[fu]:g} = {base:g} metre"},
        {"label": "Base to target",
          "math": f"{base:g} ÷ {TO_BASE[tu]:g} = {result:g} {tu}"},
    ]
    return {
        "result": result,
        "result_unit": tu,
        "base_value": base,
        "base_unit": "metre",
        "benchmarks": _BENCHMARKS,
        "steps": steps,
        "explanation": _EXPLANATION,
        "disclaimer": _DISCLAIMER,
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
