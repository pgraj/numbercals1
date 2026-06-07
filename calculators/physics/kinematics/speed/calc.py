"""Speed: v = d / t. Solve for speed, distance or time."""
from __future__ import annotations
from core.registry import register

_DISCLAIMER = ("These values are estimates and may contain computation, formula, "
    "or system errors. They are provided for general reference only \u2014 always verify "
    "results independently before relying on them for academic or professional "
    "decisions.")

_LAW_STATEMENT = ("Speed is how much distance you cover in a given time: v = d / t. Cover "
    "more distance in the same time and your speed is higher.")
_LAW_SOURCE_NAME = "Wikipedia \u2014 Speed"
_LAW_SOURCE_URL = "https://en.wikipedia.org/wiki/Speed"

def _f(x):
    if x is None: return ""
    if abs(x - round(x)) < 1e-9: return str(int(round(x)))
    return ("%.4f" % x).rstrip("0").rstrip(".")

_EXPLANATION = [
    {"heading": "What speed means",
     "body": "Speed tells you how quickly something moves \u2014 how much distance it covers "
             "each second (or hour). A car at 60 km/h covers 60 kilometres every hour."},
    {"heading": "The triangle trick",
     "body": "Speed, distance and time form a simple triangle: v = d/t, d = v\u00d7t, and "
             "t = d/v. Cover the one you want and the other two show how to find it."},
    {"heading": "Units",
     "body": "If distance is in metres and time in seconds, speed is in metres per second "
             "(m/s). Kilometres and hours give km/h. Keep the units consistent."},
]

@register(
    slug="speed",
    name="Speed",
    section="physics",
    topic="Kinematics",
    sub="Speed, Distance & Time",
    order=0,
    summary="Find speed from distance and time, or solve for distance or time, using v = d / t.",
    formula="v = d / t",
    tags=["speed", "velocity", "distance", "time", "kinematics", "motion"],
    viz_template="viz/speed.html",
    related=["distance", "time-kinematic", "acceleration"],
)
def compute(solve_for="speed", distance=100.0, time=10.0, speed=None, **_ignored):
    try:
        sf = str(solve_for or "speed").strip().lower()
    except Exception:
        sf = "speed"
    def num(v):
        if v is None or v == "": return None
        return float(v)
    try:
        d = num(distance); t = num(time); v = num(speed)
    except (TypeError, ValueError):
        return {"error": "Please enter numbers only.", "steps": [], "disclaimer": _DISCLAIMER}

    out_d, out_t, out_v = d, t, v
    steps = []; result = ""

    if sf == "speed":
        if d is None or t is None:
            return {"error": "Enter distance and time to find speed.", "steps": [], "disclaimer": _DISCLAIMER}
        if t == 0:
            return {"error": "Time cannot be zero when solving for speed.", "steps": [], "disclaimer": _DISCLAIMER}
        out_v = d / t
        steps = [
            {"label": "Formula", "math": r"\(v = \dfrac{d}{t}\)", "note": "Speed = distance divided by time."},
            {"label": "Substitute", "math": r"\(v = \dfrac{" + _f(d) + r"}{" + _f(t) + r"}\)", "note": "Distance in metres, time in seconds."},
            {"label": "Result", "math": r"\(v = " + _f(out_v) + r"\ \text{m/s}\)", "note": "Speed in metres per second."},
        ]
        result = "Speed = " + _f(out_v) + " m/s"
    elif sf == "distance":
        if v is None or t is None:
            return {"error": "Enter speed and time to find distance.", "steps": [], "disclaimer": _DISCLAIMER}
        out_d = v * t
        steps = [
            {"label": "Rearrange", "math": r"\(d = v t\)", "note": "Solve v = d/t for distance."},
            {"label": "Substitute", "math": r"\(d = (" + _f(v) + r")(" + _f(t) + r")\)", "note": "Speed in m/s, time in seconds."},
            {"label": "Result", "math": r"\(d = " + _f(out_d) + r"\ \text{m}\)", "note": "Distance in metres."},
        ]
        result = "Distance = " + _f(out_d) + " m"
    elif sf == "time":
        if v is None or d is None:
            return {"error": "Enter speed and distance to find time.", "steps": [], "disclaimer": _DISCLAIMER}
        if v == 0:
            return {"error": "Speed cannot be zero when solving for time.", "steps": [], "disclaimer": _DISCLAIMER}
        out_t = d / v
        steps = [
            {"label": "Rearrange", "math": r"\(t = \dfrac{d}{v}\)", "note": "Solve v = d/t for time."},
            {"label": "Substitute", "math": r"\(t = \dfrac{" + _f(d) + r"}{" + _f(v) + r"}\)", "note": "Distance in metres, speed in m/s."},
            {"label": "Result", "math": r"\(t = " + _f(out_t) + r"\ \text{s}\)", "note": "Time in seconds."},
        ]
        result = "Time = " + _f(out_t) + " s"
    else:
        return {"error": "Choose what to solve for: speed, distance or time.", "steps": [], "disclaimer": _DISCLAIMER}

    return {
        "result": result, "solve_for": sf,
        "distance": out_d, "time": out_t, "speed": out_v,
        "steps": steps, "explanation": _EXPLANATION,
        "law_statement": _LAW_STATEMENT,
        "law_source_name": _LAW_SOURCE_NAME, "law_source_url": _LAW_SOURCE_URL,
        "disclaimer": _DISCLAIMER,
    }

from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
