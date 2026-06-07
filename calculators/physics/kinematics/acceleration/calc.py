"""Acceleration: a = (v - u) / t. Solve for acceleration, final velocity, initial
velocity or time."""
from __future__ import annotations
from core.registry import register

_DISCLAIMER = ("These values are estimates and may contain computation, formula, "
    "or system errors. They are provided for general reference only \u2014 always verify "
    "results independently before relying on them for academic or professional "
    "decisions.")

_LAW_STATEMENT = ("Acceleration is how quickly velocity changes: a = (v \u2212 u) / t, the "
    "change in velocity divided by the time taken. Speeding up gives positive "
    "acceleration; slowing down gives negative (deceleration).")
_LAW_SOURCE_NAME = "Wikipedia \u2014 Acceleration"
_LAW_SOURCE_URL = "https://en.wikipedia.org/wiki/Acceleration"

def _f(x):
    if x is None: return ""
    if abs(x - round(x)) < 1e-9: return str(int(round(x)))
    return ("%.4f" % x).rstrip("0").rstrip(".")

_EXPLANATION = [
    {"heading": "What acceleration means",
     "body": "Acceleration measures how fast your speed is changing each second. A car that "
             "goes from 0 to 20 m/s in 4 seconds gains 5 m/s every second \u2014 an "
             "acceleration of 5 m/s\u00b2."},
    {"heading": "u, v and t",
     "body": "Here u is the starting velocity, v is the final velocity, and t is the time. "
             "The change in velocity is v \u2212 u, and dividing by the time gives the "
             "acceleration. If v is less than u the answer is negative \u2014 that is "
             "slowing down."},
    {"heading": "Units",
     "body": "Velocity is in metres per second (m/s) and time in seconds, so acceleration "
             "is in metres per second squared (m/s\u00b2). Gravity near Earth is about "
             "9.81 m/s\u00b2."},
]

@register(
    slug="acceleration",
    name="Acceleration",
    section="physics",
    topic="Kinematics",
    sub="Acceleration",
    order=3,
    summary="Find acceleration from the change in velocity over time, or solve for final/initial velocity or time, using a = (v - u)/t.",
    formula="a = (v \u2212 u) / t",
    tags=["acceleration", "velocity", "deceleration", "kinematics", "motion", "suvat"],
    viz_template="viz/acceleration.html",
    related=["speed", "distance", "time-kinematic"],
)
def compute(solve_for="acceleration", initial_velocity=0.0, final_velocity=20.0,
            time=4.0, acceleration=None, **_ignored):
    try:
        sf = str(solve_for or "acceleration").strip().lower()
    except Exception:
        sf = "acceleration"
    def num(v):
        if v is None or v == "": return None
        return float(v)
    try:
        u = num(initial_velocity); v = num(final_velocity); t = num(time); a = num(acceleration)
    except (TypeError, ValueError):
        return {"error": "Please enter numbers only.", "steps": [], "disclaimer": _DISCLAIMER}

    out_u, out_v, out_t, out_a = u, v, t, a
    steps = []; result = ""

    if sf == "acceleration":
        if u is None or v is None or t is None:
            return {"error": "Enter initial velocity, final velocity and time to find acceleration.", "steps": [], "disclaimer": _DISCLAIMER}
        if t == 0:
            return {"error": "Time cannot be zero when solving for acceleration.", "steps": [], "disclaimer": _DISCLAIMER}
        out_a = (v - u) / t
        steps = [
            {"label": "Formula", "math": r"\(a = \dfrac{v - u}{t}\)", "note": "Acceleration = change in velocity over time."},
            {"label": "Substitute", "math": r"\(a = \dfrac{" + _f(v) + r" - " + _f(u) + r"}{" + _f(t) + r"}\)", "note": "Velocities in m/s, time in seconds."},
            {"label": "Result", "math": r"\(a = " + _f(out_a) + r"\ \text{m/s}^2\)", "note": "Acceleration in m/s squared."},
        ]
        result = "Acceleration = " + _f(out_a) + " m/s\u00b2"
    elif sf == "final_velocity" or sf == "final":
        if u is None or a is None or t is None:
            return {"error": "Enter initial velocity, acceleration and time to find final velocity.", "steps": [], "disclaimer": _DISCLAIMER}
        out_v = u + a * t
        steps = [
            {"label": "Rearrange", "math": r"\(v = u + a t\)", "note": "Solve a = (v-u)/t for final velocity."},
            {"label": "Substitute", "math": r"\(v = " + _f(u) + r" + (" + _f(a) + r")(" + _f(t) + r")\)", "note": "Initial velocity in m/s, acceleration in m/s squared."},
            {"label": "Result", "math": r"\(v = " + _f(out_v) + r"\ \text{m/s}\)", "note": "Final velocity in m/s."},
        ]
        result = "Final velocity = " + _f(out_v) + " m/s"
    elif sf == "initial_velocity" or sf == "initial":
        if v is None or a is None or t is None:
            return {"error": "Enter final velocity, acceleration and time to find initial velocity.", "steps": [], "disclaimer": _DISCLAIMER}
        out_u = v - a * t
        steps = [
            {"label": "Rearrange", "math": r"\(u = v - a t\)", "note": "Solve a = (v-u)/t for initial velocity."},
            {"label": "Substitute", "math": r"\(u = " + _f(v) + r" - (" + _f(a) + r")(" + _f(t) + r")\)", "note": "Final velocity in m/s, acceleration in m/s squared."},
            {"label": "Result", "math": r"\(u = " + _f(out_u) + r"\ \text{m/s}\)", "note": "Initial velocity in m/s."},
        ]
        result = "Initial velocity = " + _f(out_u) + " m/s"
    elif sf == "time":
        if u is None or v is None or a is None:
            return {"error": "Enter initial velocity, final velocity and acceleration to find time.", "steps": [], "disclaimer": _DISCLAIMER}
        if a == 0:
            return {"error": "Acceleration cannot be zero when solving for time.", "steps": [], "disclaimer": _DISCLAIMER}
        out_t = (v - u) / a
        steps = [
            {"label": "Rearrange", "math": r"\(t = \dfrac{v - u}{a}\)", "note": "Solve a = (v-u)/t for time."},
            {"label": "Substitute", "math": r"\(t = \dfrac{" + _f(v) + r" - " + _f(u) + r"}{" + _f(a) + r"}\)", "note": "Velocities in m/s, acceleration in m/s squared."},
            {"label": "Result", "math": r"\(t = " + _f(out_t) + r"\ \text{s}\)", "note": "Time in seconds."},
        ]
        result = "Time = " + _f(out_t) + " s"
    else:
        return {"error": "Choose what to solve for: acceleration, final velocity, initial velocity or time.", "steps": [], "disclaimer": _DISCLAIMER}

    return {
        "result": result, "solve_for": sf,
        "initial_velocity": out_u, "final_velocity": out_v, "time": out_t, "acceleration": out_a,
        "steps": steps, "explanation": _EXPLANATION,
        "law_statement": _LAW_STATEMENT,
        "law_source_name": _LAW_SOURCE_NAME, "law_source_url": _LAW_SOURCE_URL,
        "disclaimer": _DISCLAIMER,
    }

from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
