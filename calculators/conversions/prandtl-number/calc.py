"""Prandtl Number Calculator — dimensionless number engine.

Collapses several physical inputs into a single unitless ratio (Pr) and
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
    ("Thermal-dominated (Pr<1)", None, 1.0),
    ("Balanced (Pr\u22481)", 1.0, 1.0001),
    ("Momentum-dominated (Pr>1)", 1.0001, None),
]


def _classify(x):
    for label, lo, hi in _REGIMES:
        lo_ok = (lo is None) or (x >= lo)
        hi_ok = (hi is None) or (x < hi)
        if lo_ok and hi_ok:
            return label
    return _REGIMES[-1][0]


_EXPLANATION = [
    {"heading": "What Prandtl number compares",
     "body": "Pr is the ratio of how fast momentum diffuses through a fluid to how fast heat diffuses through it. It is dimensionless and depends only on the fluid itself (not on the flow), so it is a property you can look up for air, water or oil."},
    {"heading": "The formula and what it implies",
     "body": "Pr = Cpμ ÷ k. If Pr < 1 (like air, ≈ 0.7) heat spreads faster than momentum, so the thermal boundary layer is thicker than the velocity one. If Pr > 1 (like oils) momentum wins and the velocity layer is thicker. This controls how heat transfer and drag relate in a flow."},
    {"heading": "Reading the plane",
     "body": "The plot places your Pr relative to the Pr = 1 dividing line, showing at a glance whether your fluid is thermal-dominated or momentum-dominated — the first thing an engineer checks when designing a heat exchanger."},
]


@register(
    slug="prandtl-number",
    name="Prandtl Number Calculator",
    section="conversions",
    sub="4 · Dimensionless Number Engines",
    summary="Compute the Prandtl number from specific heat, dynamic viscosity and thermal conductivity to compare momentum and thermal diffusion.",
    formula="Pr = Cp·μ ÷ k",
    tags=['prandtl', 'number', 'dimensionless', 'fluid', 'aerospace'],
    viz_template="viz/prandtl-number.html",
)
def compute(Cp=None, mu=None, k=None, **_ignored):
    vals = {}
    if Cp is None:
        return {"error": "Missing input: Specific heat Cp (J/kg·K)", "steps": []}
    try:
        Cp = float(Cp)
    except (TypeError, ValueError):
        return {"error": "Specific heat Cp (J/kg·K) must be a number.", "steps": []}
    vals["Cp"] = Cp
    if mu is None:
        return {"error": "Missing input: Dynamic viscosity μ (Pa·s)", "steps": []}
    try:
        mu = float(mu)
    except (TypeError, ValueError):
        return {"error": "Dynamic viscosity μ (Pa·s) must be a number.", "steps": []}
    vals["mu"] = mu
    if k is None:
        return {"error": "Missing input: Thermal conductivity k (W/m·K)", "steps": []}
    try:
        k = float(k)
    except (TypeError, ValueError):
        return {"error": "Thermal conductivity k (W/m·K) must be a number.", "steps": []}
    vals["k"] = k
    if k == 0:
        return {"error": "Invalid input: division by zero. Check denominators.", "steps": []}
    pr = (Cp*mu)/k
    regime = _classify(pr)
    steps = [
        {"label": "Substitute", "math": f"Pr = (Cp·μ) ÷ k = ({Cp:g}·{mu:g}) ÷ {k:g}"},
        {"label": "Result", "math": f"Pr = {pr:g} ({regime})"},
    ]
    return {
        "result": pr,
        "value": pr,
        "symbol": "Pr",
        "regime": regime,
        "regimes": [{"label": l, "lo": lo, "hi": hi} for (l, lo, hi) in _REGIMES],
        "steps": steps,
        "explanation": _EXPLANATION,
        "disclaimer": _DISCLAIMER,
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
