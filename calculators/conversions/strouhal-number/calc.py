"""Strouhal Number Calculator — dimensionless number engine.

Collapses several physical inputs into a single unitless ratio (St) and
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
    ("Low (quasi-steady)", None, 0.1),
    ("Typical wake (0.1\u20130.3)", 0.1, 0.3),
    ("High-frequency oscillation", 0.3, None),
]


def _classify(x):
    for label, lo, hi in _REGIMES:
        lo_ok = (lo is None) or (x >= lo)
        hi_ok = (hi is None) or (x < hi)
        if lo_ok and hi_ok:
            return label
    return _REGIMES[-1][0]


_EXPLANATION = [
    {"heading": "What Strouhal number describes",
     "body": "St links the frequency of repeating flow patterns (like the vortices that peel off behind a cylinder) to the flow speed and the body size. It is dimensionless and captures the 'rhythm' of unsteady flow."},
    {"heading": "The formula",
     "body": "St = fL ÷ v, where f is the shedding frequency, L the body's characteristic size and v the flow speed. For a huge range of conditions St sits around 0.2 — nature's preferred wake rhythm — which is why so many objects in wind 'sing' at predictable pitches."},
    {"heading": "Why it matters (and reading the slider)",
     "body": "When the shedding frequency matches a structure's natural frequency, you get resonant vibration — the mechanism that destroyed the Tacoma Narrows bridge and that engineers design chimneys and cables to avoid. The slider highlights the risky St band so you can see whether your configuration sits in it."},
]


@register(
    slug="strouhal-number",
    name="Strouhal Number Calculator",
    section="conversions",
    sub="3 · Dimensionless Number Engines",
    summary="Compute the Strouhal number from vortex shedding frequency, characteristic length and flow velocity for oscillating-flow and wake analysis.",
    formula="St = f·L ÷ v",
    tags=['strouhal', 'number', 'dimensionless', 'fluid', 'aerospace'],
    viz_template="viz/strouhal-number.html",
)
def compute(f=None, L=None, v=None, **_ignored):
    vals = {}
    if f is None:
        return {"error": "Missing input: Shedding frequency f (Hz)", "steps": []}
    try:
        f = float(f)
    except (TypeError, ValueError):
        return {"error": "Shedding frequency f (Hz) must be a number.", "steps": []}
    vals["f"] = f
    if L is None:
        return {"error": "Missing input: Characteristic length L (m)", "steps": []}
    try:
        L = float(L)
    except (TypeError, ValueError):
        return {"error": "Characteristic length L (m) must be a number.", "steps": []}
    vals["L"] = L
    if v is None:
        return {"error": "Missing input: Flow velocity v (m/s)", "steps": []}
    try:
        v = float(v)
    except (TypeError, ValueError):
        return {"error": "Flow velocity v (m/s) must be a number.", "steps": []}
    vals["v"] = v
    if v == 0:
        return {"error": "Invalid input: division by zero. Check denominators.", "steps": []}
    st = (f*L)/v
    regime = _classify(st)
    steps = [
        {"label": "Substitute", "math": f"St = (f·L) ÷ v = ({f:g}·{L:g}) ÷ {v:g}"},
        {"label": "Result", "math": f"St = {st:g} ({regime})"},
    ]
    return {
        "result": st,
        "value": st,
        "symbol": "St",
        "regime": regime,
        "regimes": [{"label": l, "lo": lo, "hi": hi} for (l, lo, hi) in _REGIMES],
        "steps": steps,
        "explanation": _EXPLANATION,
        "disclaimer": _DISCLAIMER,
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
