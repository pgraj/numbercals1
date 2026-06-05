"""Nusselt Number Calculator — dimensionless number engine.

Collapses several physical inputs into a single unitless ratio (Nu) and
classifies the resulting regime. This is not a unit-pair converter.
"""
from core.registry import register

_DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or "
    "system errors. They are provided for general reference only — always "
    "verify results independently before relying on them for engineering, "
    "commercial, or professional decisions."
)

# (label, lower_bound_or_None, upper_bound_or_None)
_REGIMES = [
    ("Conduction-like (Nu\u22481)", None, 2.0),
    ("Moderate convection", 2.0, 100.0),
    ("Strong convection", 100.0, None),
]


def _classify(x):
    for label, lo, hi in _REGIMES:
        lo_ok = (lo is None) or (x >= lo)
        hi_ok = (hi is None) or (x < hi)
        if lo_ok and hi_ok:
            return label
    return _REGIMES[-1][0]


_EXPLANATION = [
    {"heading": "What Nusselt number compares",
     "body": "Nu is the ratio of convective heat transfer (heat carried by moving fluid) to conductive heat transfer (heat seeping through still fluid) at a surface. It is dimensionless. Nu ≈ 1 means the fluid is barely moving and conduction dominates; large Nu means convection is doing most of the work."},
    {"heading": "The formula",
     "body": "Nu = hL ÷ k, where h is the convective heat-transfer coefficient, L the characteristic length and k the fluid's thermal conductivity. A bigger Nu means a given surface sheds heat much faster — exactly what you want in a radiator and want to avoid in insulation."},
    {"heading": "Reading the dial",
     "body": "The thermographic gauge runs cool-to-hot as Nu rises, so you can see whether your situation is conduction-like or strongly convective. Engineers use correlations (Nu as a function of Reynolds and Prandtl numbers) to size heat exchangers."},
]


@register(
    slug="nusselt-number",
    name="Nusselt Number Calculator",
    section="conversions",
    sub="3 · Dimensionless Number Engines",
    summary="Compute the Nusselt number from convective coefficient, characteristic length and fluid thermal conductivity — the convective-to-conductive heat transfer ratio.",
    formula="Nu = h·L ÷ k",
    tags=['nusselt', 'number', 'dimensionless', 'fluid', 'aerospace'],
    viz_template="viz/nusselt-number.html",
)
def compute(h=None, L=None, k=None, **_ignored):
    vals = {}
    if h is None:
        return {"error": "Missing input: Convective coeff h (W/m²·K)", "steps": []}
    try:
        h = float(h)
    except (TypeError, ValueError):
        return {"error": "Convective coeff h (W/m²·K) must be a number.", "steps": []}
    vals["h"] = h
    if L is None:
        return {"error": "Missing input: Characteristic length L (m)", "steps": []}
    try:
        L = float(L)
    except (TypeError, ValueError):
        return {"error": "Characteristic length L (m) must be a number.", "steps": []}
    vals["L"] = L
    if k is None:
        return {"error": "Missing input: Fluid conductivity k (W/m·K)", "steps": []}
    try:
        k = float(k)
    except (TypeError, ValueError):
        return {"error": "Fluid conductivity k (W/m·K) must be a number.", "steps": []}
    vals["k"] = k
    if k == 0:
        return {"error": "Invalid input: division by zero. Check denominators.", "steps": []}
    nu = (h*L)/k
    regime = _classify(nu)
    steps = [
        {"label": "Substitute", "math": f"Nu = (h·L) ÷ k = ({h:g}·{L:g}) ÷ {k:g}"},
        {"label": "Result", "math": f"Nu = {nu:g} ({regime})"},
    ]
    return {
        "result": nu,
        "value": nu,
        "symbol": "Nu",
        "regime": regime,
        "regimes": [{"label": l, "lo": lo, "hi": hi} for (l, lo, hi) in _REGIMES],
        "steps": steps,
        "explanation": _EXPLANATION,
        "disclaimer": _DISCLAIMER,
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
