"""Angular Velocity Converter — hub-and-spoke unit converter.

Architecture: every value is converted to the SI base unit (radian per second)
first, then from the base to the target. No peer-to-peer conversions.
"""
from core.registry import register

# label -> multiplier that takes 1 <unit> to the base (radian per second)
TO_BASE = {
    "rad/s": 1.0,
    "RPM": 0.10471975512,
    "deg/s": 0.0174532925199
}

_DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or "
    "system errors. They are provided for general reference only — always "
    "verify results independently before relying on them for engineering, "
    "commercial, or professional decisions."
)

_BENCHMARKS = [
    {"label": "Clock second hand ~0.105 rad/s", "base": 0.10471975512},
    {"label": "Vinyl 33\u2153 RPM ~3.49 rad/s", "base": 3.4906585},
    {"label": "Drill ~314 rad/s", "base": 314.159}
]


_EXPLANATION = [
    {"heading": "How fast something spins",
     "body": "Angular velocity measures rotation rate. The SI unit, radians per second (rad/s), counts how many radians of angle are swept each second. One full turn is 2π ≈ 6.283 radians, so one revolution per second = 2π rad/s."},
    {"heading": "RPM is the everyday unit",
     "body": "Revolutions per minute (RPM) is what tachometers and drills quote. To convert: 1 RPM = 2π/60 ≈ 0.10472 rad/s. Degrees per second (deg/s) appears in robotics and cameras: 1 deg/s = π/180 ≈ 0.01745 rad/s."},
    {"heading": "Worked example",
     "body": "A drill at 3000 RPM = 3000 × 0.10472 ≈ 314.2 rad/s. Radians per second is the form physics needs, because it plugs straight into v = ω·r to get the speed at the rim."},
]


@register(
    slug="convert-angular-velocity",
    name="Angular Velocity Converter",
    section="conversions",
    sub="2 · Mechanics & Fluids",
    summary="Convert angular velocity between rad/s, RPM and deg/s via radians per second.",
    formula="result = value × (from→rad/s) ÷ (to→rad/s)",
    tags=['angular', 'velocity', 'converter', 'conversion'],
    viz_template="viz/convert-angular-velocity.html",
)
def compute(value=None, from_unit=None, to_unit=None, **_ignored):
    """Convert `value` from `from_unit` to `to_unit` via the radian per second."""
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
        {"label": "To base unit (radian per second)",
          "math": f"{v:g} {fu} × {TO_BASE[fu]:g} = {base:g} radian per second"},
        {"label": "Base to target",
          "math": f"{base:g} ÷ {TO_BASE[tu]:g} = {result:g} {tu}"},
    ]
    return {
        "result": result,
        "result_unit": tu,
        "base_value": base,
        "base_unit": "radian per second",
        "benchmarks": _BENCHMARKS,
        "steps": steps,
        "explanation": _EXPLANATION,
        "disclaimer": _DISCLAIMER,
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
