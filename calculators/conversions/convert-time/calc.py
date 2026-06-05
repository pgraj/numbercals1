"""Time Converter — hub-and-spoke unit converter.

Architecture: every value is converted to the SI base unit (second)
first, then from the base to the target. No peer-to-peer conversions.
"""
from core.registry import register

# label -> multiplier that takes 1 <unit> to the base (second)
TO_BASE = {
    "ns": 1e-09,
    "\u03bcs": 1e-06,
    "ms": 0.001,
    "s": 1.0,
    "min": 60.0,
    "hr": 3600.0,
    "day": 86400.0,
    "week": 604800.0,
    "month": 2592000.0,
    "year": 31557600.0,
    "decade": 315576000.0,
    "century": 3155760000.0,
    "millennium": 31557600000.0
}

_DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or "
    "system errors. They are provided for general reference only — always "
    "verify results independently before relying on them for engineering, "
    "commercial, or professional decisions."
)

_BENCHMARKS = [
    {"label": "Heartbeat ~0.85 s", "base": 0.85},
    {"label": "Day 86400 s", "base": 86400.0},
    {"label": "Year ~31.56 Ms", "base": 31557600.0}
]


_EXPLANATION = [
    {"heading": "The second is the anchor",
     "body": "The SI second is defined by the vibration of a caesium-133 atom (9,192,631,770 cycles). Everything larger is built from it: a minute is 60 s, an hour 3600 s, a day 86,400 s."},
    {"heading": "Why months and years are approximate",
     "body": "Calendar months vary (28–31 days), so this tool uses a fixed 30-day month for arithmetic. The year here is the Julian year of 365.25 days (= 31,557,600 s), the convention used in astronomy, which is why a 'year' here is slightly longer than a common 365-day year."},
    {"heading": "Reading very small units",
     "body": "Going the other way, 1 second = 1000 milliseconds = 1,000,000 microseconds = 1,000,000,000 nanoseconds. Computer clocks and physics experiments live down here."},
]


@register(
    slug="convert-time",
    name="Time Converter",
    section="conversions",
    sub="2 · Advanced Converters",
    summary="Convert time between nanoseconds and millennia via the second. Month = 30 days, year = 365.25 days (Julian).",
    formula="result = value × (from→s) ÷ (to→s)",
    tags=['time', 'converter', 'conversion'],
    viz_template="viz/convert-time.html",
)
def compute(value=None, from_unit=None, to_unit=None, **_ignored):
    """Convert `value` from `from_unit` to `to_unit` via the second."""
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
        {"label": "To base unit (second)",
          "math": f"{v:g} {fu} × {TO_BASE[fu]:g} = {base:g} second"},
        {"label": "Base to target",
          "math": f"{base:g} ÷ {TO_BASE[tu]:g} = {result:g} {tu}"},
    ]
    return {
        "result": result,
        "result_unit": tu,
        "base_value": base,
        "base_unit": "second",
        "benchmarks": _BENCHMARKS,
        "steps": steps,
        "explanation": _EXPLANATION,
        "disclaimer": _DISCLAIMER,
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
