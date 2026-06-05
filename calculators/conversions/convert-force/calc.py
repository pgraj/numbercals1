"""Force & Thrust Converter — hub-and-spoke unit converter.

Architecture: every value is converted to the SI base unit (newton)
first, then from the base to the target. No peer-to-peer conversions.
"""
from core.registry import register

# label -> multiplier that takes 1 <unit> to the base (newton)
TO_BASE = {
    "N": 1.0,
    "kN": 1000.0,
    "lbf": 4.4482216152605,
    "kgf": 9.80665
}

_DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or "
    "system errors. They are provided for general reference only — always "
    "verify results independently before relying on them for engineering, "
    "commercial, or professional decisions."
)

_BENCHMARKS = [
    {"label": "Apple weight ~1 N", "base": 1.0},
    {"label": "Person weight ~700 N", "base": 700.0},
    {"label": "Jet engine ~100 kN", "base": 100000.0}
]


_EXPLANATION = [
    {"heading": "Force, and why the newton",
     "body": "A force is a push or pull. The SI unit, the newton (N), is the force that accelerates 1 kg at 1 m/s²: 1 N = 1 kg·m/s². Holding a small apple against gravity takes about 1 N — a handy mental benchmark."},
    {"heading": "Weight is a force",
     "body": "Kilogram-force (kgf) and pound-force (lbf) are 'gravity' units: 1 kgf is the weight of 1 kg on Earth = 1 × 9.80665 = 9.80665 N. 1 lbf = 4.4482 N. They feel intuitive because they map onto how heavy something feels, but the newton is the proper physics unit."},
    {"heading": "Thrust is just force with a direction",
     "body": "A rocket or jet engine's thrust is a force, quoted in newtons or kilonewtons (1 kN = 1000 N). A small jet engine might produce ~100 kN. To compare engines fairly you also look at specific impulse (a separate converter), which measures how efficiently that thrust is produced."},
]


@register(
    slug="convert-force",
    name="Force & Thrust Converter",
    section="conversions",
    sub="1 · Basic Converters",
    summary="Convert force and thrust between newtons, kilonewtons, pound-force and kilogram-force via the newton.",
    formula="result = value × (from→N) ÷ (to→N)",
    tags=['force', 'converter', 'conversion'],
    viz_template="viz/convert-force.html",
)
def compute(value=None, from_unit=None, to_unit=None, **_ignored):
    """Convert `value` from `from_unit` to `to_unit` via the newton."""
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
        {"label": "To base unit (newton)",
          "math": f"{v:g} {fu} × {TO_BASE[fu]:g} = {base:g} newton"},
        {"label": "Base to target",
          "math": f"{base:g} ÷ {TO_BASE[tu]:g} = {result:g} {tu}"},
    ]
    return {
        "result": result,
        "result_unit": tu,
        "base_value": base,
        "base_unit": "newton",
        "benchmarks": _BENCHMARKS,
        "steps": steps,
        "explanation": _EXPLANATION,
        "disclaimer": _DISCLAIMER,
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
