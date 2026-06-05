"""Mach Number Calculator — dimensionless number engine.

Collapses several physical inputs into a single unitless ratio (M) and
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
    ("Subsonic", None, 0.8),
    ("Transonic", 0.8, 1.2),
    ("Supersonic", 1.2, 5.0),
    ("Hypersonic", 5.0, None),
]


def _classify(x):
    for label, lo, hi in _REGIMES:
        lo_ok = (lo is None) or (x >= lo)
        hi_ok = (hi is None) or (x < hi)
        if lo_ok and hi_ok:
            return label
    return _REGIMES[-1][0]


_EXPLANATION = [
    {"heading": "What Mach number means",
     "body": "Mach number (M) is an object's speed divided by the local speed of sound. It is dimensionless. M tells you whether air can 'get out of the way' smoothly (low M) or piles up into shock waves (M near and above 1), which is why it, not raw speed, governs high-speed flight."},
    {"heading": "Why the speed of sound varies",
     "body": "Sound speed isn't fixed — it depends on temperature: a = √(γRT), where γ is the gas's specific-heat ratio (1.4 for air), R the gas constant and T the absolute temperature. Colder air = slower sound = a given speed is a HIGHER Mach number. That is why aircraft hit Mach 1 at a lower true speed high up where the air is cold."},
    {"heading": "Reading the dial",
     "body": "The gauge bands the flight regimes: subsonic (M < 0.8), transonic (0.8–1.2, where shocks first form and drag spikes), supersonic (1.2–5) and hypersonic (M ≥ 5). The needle shows where your speed-and-temperature combination lands."},
]


@register(
    slug="mach-number",
    name="Mach Number Calculator",
    section="conversions",
    sub="3 · Dimensionless Number Engines",
    summary="Compute the Mach number from speed, air temperature and gas properties to classify flight as subsonic, transonic, supersonic or hypersonic.",
    formula="M = v ÷ √(γ·R·T)",
    tags=['mach', 'number', 'dimensionless', 'fluid', 'aerospace'],
    viz_template="viz/mach-number.html",
)
def compute(v=None, T=None, gamma=None, R=None, **_ignored):
    vals = {}
    if v is None:
        return {"error": "Missing input: Speed v (m/s)", "steps": []}
    try:
        v = float(v)
    except (TypeError, ValueError):
        return {"error": "Speed v (m/s) must be a number.", "steps": []}
    vals["v"] = v
    if T is None:
        return {"error": "Missing input: Air temperature T (K)", "steps": []}
    try:
        T = float(T)
    except (TypeError, ValueError):
        return {"error": "Air temperature T (K) must be a number.", "steps": []}
    vals["T"] = T
    if gamma is None:
        return {"error": "Missing input: Specific heat ratio γ", "steps": []}
    try:
        gamma = float(gamma)
    except (TypeError, ValueError):
        return {"error": "Specific heat ratio γ must be a number.", "steps": []}
    vals["gamma"] = gamma
    if R is None:
        return {"error": "Missing input: Gas constant R (J/kg·K)", "steps": []}
    try:
        R = float(R)
    except (TypeError, ValueError):
        return {"error": "Gas constant R (J/kg·K) must be a number.", "steps": []}
    vals["R"] = R
    if gamma*R*T <= 0:
        return {"error": "Invalid input: division by zero. Check denominators.", "steps": []}
    m = v/((gamma*R*T)**0.5)
    regime = _classify(m)
    steps = [
        {"label": "Substitute", "math": f"a = √(γ·R·T) = √({gamma:g}·{R:g}·{T:g}); M = v ÷ a = {v:g} ÷ a"},
        {"label": "Result", "math": f"M = {m:g} ({regime})"},
    ]
    return {
        "result": m,
        "value": m,
        "symbol": "M",
        "regime": regime,
        "regimes": [{"label": l, "lo": lo, "hi": hi} for (l, lo, hi) in _REGIMES],
        "steps": steps,
        "explanation": _EXPLANATION,
        "disclaimer": _DISCLAIMER,
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
