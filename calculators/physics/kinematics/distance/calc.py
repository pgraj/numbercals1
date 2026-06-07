"""Distance: d = v * t. Solve for distance, speed or time."""
from __future__ import annotations
from core.registry import register

_DISCLAIMER = ("These values are estimates and may contain computation, formula, "
    "or system errors. They are provided for general reference only \u2014 always verify "
    "results independently before relying on them for academic or professional "
    "decisions.")

_LAW_STATEMENT = ("Distance is speed multiplied by time: d = v \u00d7 t. Travel at a steady "
    "speed for longer and you cover more ground.")
_LAW_SOURCE_NAME = "Wikipedia \u2014 Distance"
_LAW_SOURCE_URL = "https://en.wikipedia.org/wiki/Distance"

def _f(x):
    if x is None: return ""
    if abs(x - round(x)) < 1e-9: return str(int(round(x)))
    return ("%.4f" % x).rstrip("0").rstrip(".")

_EXPLANATION = [
    {"heading": "What this finds",
     "body": "If you know how fast you are going and for how long, you can work out how far "
             "you travel. A car at 20 m/s for 5 seconds covers 20 \u00d7 5 = 100 metres."},
    {"heading": "Same triangle, different corner",
     "body": "This is the same speed-distance-time relationship as the Speed calculator, "
             "just rearranged: d = v\u00d7t. Use whichever calculator matches what you are "
             "asked to find."},
    {"heading": "Units",
     "body": "Speed in m/s and time in seconds give distance in metres. km/h with hours "
             "give kilometres. Keep the units consistent on both inputs."},
]

@register(
    slug="distance",
    name="Distance",
    section="physics",
    topic="Kinematics",
    sub="Speed, Distance & Time",
    order=1,
    summary="Find distance from speed and time, or solve for speed or time, using d = v t.",
    formula="d = v t",
    tags=["distance", "speed", "time", "kinematics", "motion"],
    viz_template="viz/distance.html",
    related=["speed", "time-kinematic", "acceleration"],
)
def compute(solve_for="distance", speed=20.0, time=5.0, distance=None, **_ignored):
    try:
        sf = str(solve_for or "distance").strip().lower()
    except Exception:
        sf = "distance"
    def num(v):
        if v is None or v == "": return None
        return float(v)
    try:
        v = num(speed); t = num(time); d = num(distance)
    except (TypeError, ValueError):
        return {"error": "Please enter numbers only.", "steps": [], "disclaimer": _DISCLAIMER}

    out_d, out_v, out_t = d, v, t
    steps = []; result = ""

    if sf == "distance":
        if v is None or t is None:
            return {"error": "Enter speed and time to find distance.", "steps": [], "disclaimer": _DISCLAIMER}
        out_d = v * t
        steps = [
            {"label": "Formula", "math": r"\(d = v t\)", "note": "Distance = speed times time."},
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
            {"label": "Rearrange", "math": r"\(v = \dfrac{d}{t}\)", "note": "Solve d = vt for speed."},
            {"label": "Substitute", "math": r"\(v = \dfrac{" + _f(d) + r"}{" + _f(t) + r"}\)", "note": "Distance in metres, time in seconds."},
            {"label": "Result", "math": r"\(v = " + _f(out_v) + r"\ \text{m/s}\)", "note": "Speed in metres per second."},
        ]
        result = "Speed = " + _f(out_v) + " m/s"
    elif sf == "time":
        if d is None or v is None:
            return {"error": "Enter distance and speed to find time.", "steps": [], "disclaimer": _DISCLAIMER}
        if v == 0:
            return {"error": "Speed cannot be zero when solving for time.", "steps": [], "disclaimer": _DISCLAIMER}
        out_t = d / v
        steps = [
            {"label": "Rearrange", "math": r"\(t = \dfrac{d}{v}\)", "note": "Solve d = vt for time."},
            {"label": "Substitute", "math": r"\(t = \dfrac{" + _f(d) + r"}{" + _f(v) + r"}\)", "note": "Distance in metres, speed in m/s."},
            {"label": "Result", "math": r"\(t = " + _f(out_t) + r"\ \text{s}\)", "note": "Time in seconds."},
        ]
        result = "Time = " + _f(out_t) + " s"
    else:
        return {"error": "Choose what to solve for: distance, speed or time.", "steps": [], "disclaimer": _DISCLAIMER}

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
