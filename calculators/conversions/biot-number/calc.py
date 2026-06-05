"""Biot Number Calculator — dimensionless number engine.

Collapses several physical inputs into a single unitless ratio (Bi) and
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
    ("Lumped OK (Bi<0.1)", None, 0.1),
    ("Intermediate", 0.1, 1.0),
    ("Internal gradients dominate (Bi>1)", 1.0, None),
]


def _classify(x):
    for label, lo, hi in _REGIMES:
        lo_ok = (lo is None) or (x >= lo)
        hi_ok = (hi is None) or (x < hi)
        if lo_ok and hi_ok:
            return label
    return _REGIMES[-1][0]


_EXPLANATION = [
    {"heading": "What the Biot number tells you",
     "body": "Bi compares two resistances to heat flow: the resistance at a body's SURFACE (getting heat into or out of the surrounding fluid) versus the resistance INSIDE the body (conducting heat through the solid). It answers: when this object heats or cools, does its inside keep up with its surface, or lag behind?"},
    {"heading": "The formula, and what the three inputs do",
     "body": "Bi = hL ÷ kₛ. h is the surface heat-transfer coefficient (how fast the surface exchanges heat with the fluid), L the characteristic size, and kₛ the SOLID's thermal conductivity. Raising h or L increases surface exchange relative to internal conduction (Bi up); a more conductive solid (higher kₛ) evens the inside out faster (Bi down). The result you read off is the single ratio Bi — the donut shows how the total thermal resistance splits between surface and core."},
    {"heading": "The decision it drives",
     "body": "If Bi < 0.1, internal conduction is so fast the whole object is essentially one uniform temperature — you can use the simple 'lumped capacitance' cooling model. If Bi > 1, the inside lags badly and you must treat the temperature as varying through the body (think a thick roast: surface hot, centre still cold). That threshold is the practical takeaway."},
    {"heading": "Worked example",
     "body": "A metal part with h = 50, L = 0.05 m, kₛ = 50: Bi = (50 × 0.05) ÷ 50 = 0.05. Below 0.1, so it heats almost uniformly — the lumped model is valid."},
]


@register(
    slug="biot-number",
    name="Biot Number Calculator",
    section="conversions",
    sub="3 · Dimensionless Number Engines",
    summary="Compute the Biot number from heat transfer coefficient, characteristic length and solid thermal conductivity — surface dissipation vs internal conduction.",
    formula="Bi = h·L ÷ kₛ",
    tags=['biot', 'number', 'dimensionless', 'fluid', 'aerospace'],
    viz_template="viz/biot-number.html",
)
def compute(h=None, L=None, ks=None, **_ignored):
    vals = {}
    if h is None:
        return {"error": "Missing input: Heat transfer coeff h (W/m²·K)", "steps": []}
    try:
        h = float(h)
    except (TypeError, ValueError):
        return {"error": "Heat transfer coeff h (W/m²·K) must be a number.", "steps": []}
    vals["h"] = h
    if L is None:
        return {"error": "Missing input: Characteristic length L (m)", "steps": []}
    try:
        L = float(L)
    except (TypeError, ValueError):
        return {"error": "Characteristic length L (m) must be a number.", "steps": []}
    vals["L"] = L
    if ks is None:
        return {"error": "Missing input: Solid conductivity kₛ (W/m·K)", "steps": []}
    try:
        ks = float(ks)
    except (TypeError, ValueError):
        return {"error": "Solid conductivity kₛ (W/m·K) must be a number.", "steps": []}
    vals["ks"] = ks
    if ks == 0:
        return {"error": "Invalid input: division by zero. Check denominators.", "steps": []}
    bi = (h*L)/ks
    regime = _classify(bi)
    steps = [
        {"label": "Substitute", "math": f"Bi = (h·L) ÷ kₛ = ({h:g}·{L:g}) ÷ {ks:g}"},
        {"label": "Result", "math": f"Bi = {bi:g} ({regime})"},
    ]
    return {
        "result": bi,
        "value": bi,
        "symbol": "Bi",
        "regime": regime,
        "regimes": [{"label": l, "lo": lo, "hi": hi} for (l, lo, hi) in _REGIMES],
        "steps": steps,
        "explanation": _EXPLANATION,
        "disclaimer": _DISCLAIMER,
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
