"""Stress & Modulus Converter — hub-and-spoke unit converter.

Architecture: every value is converted to the SI base unit (pascal)
first, then from the base to the target. No peer-to-peer conversions.
"""
from core.registry import register

# label -> multiplier that takes 1 <unit> to the base (pascal)
TO_BASE = {
    "Pa": 1.0,
    "MPa": 1000000.0,
    "GPa": 1000000000.0,
    "PSI": 6894.757293168,
    "ksi": 6894757.293168
}

_DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or "
    "system errors. They are provided for general reference only — always "
    "verify results independently before relying on them for engineering, "
    "commercial, or professional decisions."
)

_EXPLANATION = [
    {"heading": "Stress is pressure inside a material",
     "body": "When you load a structure, the internal force spread over the cross-sectional area is the stress, measured in pascals (Pa) — the same unit as pressure. Because materials carry huge forces over small areas, stresses run into megapascals (MPa = 10⁶ Pa) and gigapascals (GPa = 10⁹ Pa)."},
    {"heading": "Stress vs modulus",
     "body": "Two related quantities share these units. Stress is the load a material currently feels; the elastic modulus (stiffness) is how much stress it takes to stretch the material by a given fraction. Steel's yield stress is about 250 MPa (the point at which it permanently deforms), while its modulus is about 200 GPa (its stiffness) — roughly a thousand times larger, because modulus describes resistance to any stretching at all."},
    {"heading": "Everyday reference points",
     "body": "For a sense of scale: concrete in compression handles around 30 MPa, structural steel yields near 250 MPa, and steel's stiffness (modulus) sits around 200 GPa. Comparing your converted value against these benchmarks makes the raw number meaningful rather than abstract."},
    {"heading": "The imperial units",
     "body": "US engineering uses PSI and ksi (kilo-PSI, 1000 PSI). 1 MPa = 145 PSI = 0.145 ksi. So 250 MPa ≈ 36,260 PSI ≈ 36.3 ksi. The step-by-step working below shows exactly how your value passes through the pascal to reach the target unit."},
]


@register(
    slug="convert-stress",
    name="Stress & Modulus Converter",
    section="conversions",
    sub="2 · Mechanics & Fluids",
    summary="Convert mechanical stress and elastic modulus between Pa, MPa, GPa, PSI and ksi via the pascal.",
    formula="result = value × (from→Pa) ÷ (to→Pa)",
    tags=['stress', 'modulus', 'pascal', 'converter', 'conversion'],
    viz_template="viz/convert-stress.html",
)
def compute(value=None, from_unit=None, to_unit=None, **_ignored):
    """Convert `value` from `from_unit` to `to_unit` via the pascal."""
    if value is None or from_unit is None or to_unit is None:
        return {"error": "Provide a value, a source unit, and a target unit.", "steps": [], "disclaimer": _DISCLAIMER}
    try:
        v = float(value)
    except (TypeError, ValueError):
        return {"error": "Value must be a number.", "steps": [], "disclaimer": _DISCLAIMER}
    fu, tu = str(from_unit), str(to_unit)
    if fu not in TO_BASE:
        return {"error": "Unknown source unit: " + fu, "steps": [], "disclaimer": _DISCLAIMER}
    if tu not in TO_BASE:
        return {"error": "Unknown target unit: " + tu, "steps": [], "disclaimer": _DISCLAIMER}

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
        "steps": steps,
        "explanation": _EXPLANATION,
        "disclaimer": _DISCLAIMER,
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
