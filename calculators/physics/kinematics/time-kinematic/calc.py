"""Time (from speed and distance): t = d / v. Solve for time, distance or speed."""
from __future__ import annotations
from core.registry import register

_DISCLAIMER = ("These values are estimates and may contain computation, formula, "
    "or system errors. They are provided for general reference only \u2014 always verify "
    "results independently before relying on them for academic or professional "
    "decisions.")

_LAW_STATEMENT = ("Time taken is distance divided by speed: t = d / v. The farther you go or "
    "the slower you travel, the longer it takes.")
_LAW_SOURCE_NAME = "Wikipedia \u2014 Time"
_LAW_SOURCE_URL = "https://en.wikipedia.org/wiki/Time"

def _f(x):
    if x is None: return ""
    if abs(x - round(x)) < 1e-9: return str(int(round(x)))
    return ("%.4f" % x).rstrip("0").rstrip(".")

_EXPLANATION = [
    {"heading": "What this finds",
     "body": "If you know how far you need to go and how fast you are going, this tells you "
             "how long it takes. 100 metres at 20 m/s takes 100 \u00f7 20 = 5 seconds."},
    {"heading": "Same triangle again",
     "body": "It is the speed-distance-time relationship rearranged for time: t = d/v. The "
             "Speed and Distance calculators handle the other two corners of the triangle."},
    {"heading": "Units",
     "body": "Distance in metres and speed in m/s give time in seconds. Kilometres with "
             "km/h give hours. Keep both inputs in matching units."},
]

@register(
    slug="time-kinematic",
    name="Time (from Speed & Distance)",
    section="physics",
    topic="Kinematics",
    sub="Speed, Distance & Time",
    order=2,
    summary="Find the time taken from distance and speed, or solve for distance or speed, using t = d / v.",
    formula="t = d / v",
    tags=["time", "speed", "distance", "kinematics", "motion"],
    viz_template="viz/time-kinematic.html",
    related=["speed", "distance", "acceleration"],
)
def compute(solve_for="time", distance=100.0, speed=20.0, time=None, **_ignored):
    try:
        sf = str(solve_for or "time").strip().lower()
    except Exception:
        sf = "time"
    def num(v):
        if v is None or v == "": return None
        return float(v)
    try:
        d = num(distance); v = num(speed); t = num(time)
    except (TypeError, ValueError):
        return {"error": "Please enter numbers only.", "steps": [], "disclaimer": _DISCLAIMER}

    out_d, out_v, out_t = d, v, t
    steps = []; result = ""

    if sf == "time":
        if d is None or v is None:
            return {"error": "Enter distance and speed to find time.", "steps": [], "disclaimer": _DISCLAIMER}
        if v == 0:
            return {"error": "Speed cannot be zero when solving for time.", "steps": [], "disclaimer": _DISCLAIMER}
        out_t = d / v
        steps = [
            {"label": "Formula", "math": r"\(t = \dfrac{d}{v}\)", "note": "Time = distance divided by speed."},
            {"label": "Substitute", "math": r"\(t = \dfrac{" + _f(d) + r"}{" + _f(v) + r"}\)", "note": "Distance in metres, speed in m/s."},
            {"label": "Result", "math": r"\(t = " + _f(out_t) + r"\ \text{s}\)", "note": "Time in seconds."},
        ]
        result = "Time = " + _f(out_t) + " s"
    elif sf == "distance":
        if v is None or t is None:
            return {"error": "Enter speed and time to find distance.", "steps": [], "disclaimer": _DISCLAIMER}
        out_d = v * t
        steps = [
            {"label": "Rearrange", "math": r"\(d = v t\)", "note": "Solve t = d/v for distance."},
            {"label": "Substitute", "math": r"\(d = (" + _f(v) + r")(" + _f(t) + r")\)", "note": "Speed in m/s, time in seconds."},
            {"label": "Result", "math": r"\(d = " + _f(out_d) + r"\ \text{m}\)", "note": "Distance in metres."},
        ]
        result = "Distance = " + _f(out_d) + " m"
    elif sf == "speed":
        if d is None or t is None:
            return {"error": "Enter distance and time to find speed.", "steps": [], "disclaimer": _DISCLAIMER}
        if t == 0:
            return {"error": "Time cannot be zero when solving for speed.", "steps": [], "disclaimer": _DISCLAIMER}
        out_v = d / t
        steps = [
            {"label": "Rearrange", "math": r"\(v = \dfrac{d}{t}\)", "note": "Solve t = d/v for speed."},
            {"label": "Substitute", "math": r"\(v = \dfrac{" + _f(d) + r"}{" + _f(t) + r"}\)", "note": "Distance in metres, time in seconds."},
            {"label": "Result", "math": r"\(v = " + _f(out_v) + r"\ \text{m/s}\)", "note": "Speed in metres per second."},
        ]
        result = "Speed = " + _f(out_v) + " m/s"
    else:
        return {"error": "Choose what to solve for: time, distance or speed.", "steps": [], "disclaimer": _DISCLAIMER}

    return {
        "result": result, "solve_for": sf,
        "distance": out_d, "speed": out_v, "time": out_t,
        "steps": steps, "explanation": _EXPLANATION,
        "law_statement": _LAW_STATEMENT,
        "law_source_name": _LAW_SOURCE_NAME, "law_source_url": _LAW_SOURCE_URL,
        "disclaimer": _DISCLAIMER,
    }

from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
