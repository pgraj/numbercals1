"""Reynolds Number Calculator — dimensionless number engine.

Collapses several physical inputs into a single unitless ratio (Re) and
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
    ("Laminar", None, 2300),
    ("Transition", 2300, 4000),
    ("Turbulent", 4000, None),
]


def _classify(x):
    for label, lo, hi in _REGIMES:
        lo_ok = (lo is None) or (x >= lo)
        hi_ok = (hi is None) or (x < hi)
        if lo_ok and hi_ok:
            return label
    return _REGIMES[-1][0]


_EXPLANATION = [
    {"heading": "What the Reynolds number actually compares",
     "body": "Re is the ratio of inertial forces (the fluid's tendency to keep moving and form eddies) to viscous forces (the fluid's internal 'stickiness' that smooths flow out). It is dimensionless — a pure number — so the same value means the same flow behaviour whether you're studying a blood vessel or an aircraft wing."},
    {"heading": "The formula, term by term",
     "body": "Re = ρvL ÷ μ. ρ is density and v is velocity (together, the inertia — heavy fast fluid resists being calmed). L is a characteristic length (pipe diameter, wing chord). μ is dynamic viscosity (the stickiness fighting eddies). Big ρ, v or L push toward turbulence; big μ pulls back toward smooth flow."},
    {"heading": "Reading the regime plane",
     "body": "Below Re ≈ 2,300 flow is laminar — smooth, orderly layers. Above ≈ 4,000 it is turbulent — chaotic and mixing. Between is an unstable transition band. The plot marks your computed Re against these zones so you can see not just the number but which regime you're in and how close you are to flipping into the next one."},
    {"heading": "Worked example",
     "body": "Air (ρ = 1.225, μ = 1.81e-5) over a 2 m wing at 50 m/s: Re = (1.225 × 50 × 2) ÷ 1.81e-5 ≈ 6.8 million — deep in turbulent territory, as expected for an aircraft."},
]


@register(
    slug="reynolds-number",
    name="Reynolds Number Calculator",
    section="conversions",
    sub="3 · Dimensionless Number Engines",
    summary="Compute the Reynolds number from density, velocity, length and dynamic viscosity to classify a flow as laminar, transitional or turbulent.",
    formula="Re = ρ·v·L ÷ μ",
    tags=['reynolds', 'number', 'dimensionless', 'fluid', 'aerospace'],
    viz_template="viz/reynolds-number.html",
)
def compute(rho=None, v=None, L=None, mu=None, **_ignored):
    vals = {}
    if rho is None:
        return {"error": "Missing input: Density ρ (kg/m³)", "steps": []}
    try:
        rho = float(rho)
    except (TypeError, ValueError):
        return {"error": "Density ρ (kg/m³) must be a number.", "steps": []}
    vals["rho"] = rho
    if v is None:
        return {"error": "Missing input: Velocity v (m/s)", "steps": []}
    try:
        v = float(v)
    except (TypeError, ValueError):
        return {"error": "Velocity v (m/s) must be a number.", "steps": []}
    vals["v"] = v
    if L is None:
        return {"error": "Missing input: Chord length L (m)", "steps": []}
    try:
        L = float(L)
    except (TypeError, ValueError):
        return {"error": "Chord length L (m) must be a number.", "steps": []}
    vals["L"] = L
    if mu is None:
        return {"error": "Missing input: Dynamic viscosity μ (Pa·s)", "steps": []}
    try:
        mu = float(mu)
    except (TypeError, ValueError):
        return {"error": "Dynamic viscosity μ (Pa·s) must be a number.", "steps": []}
    vals["mu"] = mu
    if mu == 0:
        return {"error": "Invalid input: division by zero. Check denominators.", "steps": []}
    re = (rho*v*L)/mu
    regime = _classify(re)
    steps = [
        {"label": "Substitute", "math": f"Re = (ρ·v·L) ÷ μ = ({rho:g}·{v:g}·{L:g}) ÷ {mu:g}"},
        {"label": "Result", "math": f"Re = {re:g} ({regime})"},
    ]
    return {
        "result": re,
        "value": re,
        "symbol": "Re",
        "regime": regime,
        "regimes": [{"label": l, "lo": lo, "hi": hi} for (l, lo, hi) in _REGIMES],
        "steps": steps,
        "explanation": _EXPLANATION,
        "disclaimer": _DISCLAIMER,
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
