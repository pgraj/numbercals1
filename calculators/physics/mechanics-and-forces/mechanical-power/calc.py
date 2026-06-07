"""Mechanical Power: P = W / t. Solve for power, work or time."""
from __future__ import annotations
from core.registry import register

_DISCLAIMER = ("These values are estimates and may contain computation, formula, "
    "or system errors. They are provided for general reference only — always verify "
    "results independently before relying on them for academic or professional "
    "decisions.")

def _f(x):
    if x is None: return ""
    if abs(x - round(x)) < 1e-9: return str(int(round(x)))
    return ("%.4f" % x).rstrip("0").rstrip(".")

_LAW_STATEMENT = ("Power is the rate at which work is done, or energy is transferred. "
    "Mechanical power equals the work done divided by the time taken, P = W / t (equivalently "
    "P = F v, force times velocity).")
_LAW_SOURCE_NAME = "Wikipedia \u2014 Power (physics)"
_LAW_SOURCE_URL = "https://en.wikipedia.org/wiki/Power_(physics)"

_EXPLANATION = [
    {"heading": "What power measures",
     "body": "Power is the rate at which work is done, or energy is transferred. Two "
             "engines might do the same amount of work, but the more powerful one does "
             "it in less time."},
    {"heading": "Mechanical, not electrical",
     "body": "This calculator uses the mechanical form P = W / t. It can also be written "
             "as P = F v, force times velocity, for a steady push at constant speed. "
             "Electrical power, P = VI, is handled by a separate calculator."},
    {"heading": "Units",
     "body": "With work in joules and time in seconds, power comes out in watts (W). One "
             "watt is one joule per second; 1000 watts make a kilowatt."},
]

@register(
    slug="mechanical-power",
    name="Mechanical Power",
    section="physics",
    topic="Mechanics & Forces",
    sub="Work & Power",
    order=4,
    summary="Find mechanical power as the rate of doing work from work and time, or solve for work or time.",
    formula="P = W / t",
    tags=["power", "mechanical power", "work", "watts", "rate", "mechanics", "energy"],
    viz_template="viz/mechanical-power.html",
    related=["work-done", "kinetic-energy", "potential-energy"],
)
def compute(solve_for="power", work=500.0, time=10.0, power=None, **_ignored):
    try:
        sf = str(solve_for or "power").strip().lower()
    except Exception:
        sf = "power"

    def num(v):
        if v is None or v == "":
            return None
        return float(v)

    try:
        w = num(work)
        t = num(time)
        p = num(power)
    except (TypeError, ValueError):
        return {"error": "Please enter numbers only.", "steps": [], "disclaimer": _DISCLAIMER}

    out_work = w
    out_time = t
    out_power = p
    steps = []
    result = ""

    if sf == "power":
        if w is None or t is None:
            return {"error": "Enter work and time to find power.",
                    "steps": [], "disclaimer": _DISCLAIMER}
        if t == 0:
            return {"error": "Time cannot be zero when solving for power.",
                    "steps": [], "disclaimer": _DISCLAIMER}
        out_power = w / t
        steps = [
            {"label": "Formula", "math": r"\(P = \dfrac{W}{t}\)",
             "note": "Power is work divided by the time taken."},
            {"label": "Substitute",
             "math": r"\(P = \dfrac{" + _f(w) + r"}{" + _f(t) + r"}\)",
             "note": "Work in joules, time in seconds."},
            {"label": "Result", "math": r"\(P = " + _f(out_power) + r"\ \text{W}\)",
             "note": "Power in watts."},
        ]
        result = "Power = " + _f(out_power) + " W"

    elif sf == "work":
        if p is None or t is None:
            return {"error": "Enter power and time to find work.",
                    "steps": [], "disclaimer": _DISCLAIMER}
        out_work = p * t
        steps = [
            {"label": "Rearrange", "math": r"\(W = P\,t\)",
             "note": "Solve P = W/t for work."},
            {"label": "Substitute",
             "math": r"\(W = (" + _f(p) + r")(" + _f(t) + r")\)",
             "note": "Power in watts, time in seconds."},
            {"label": "Result", "math": r"\(W = " + _f(out_work) + r"\ \text{J}\)",
             "note": "Work in joules."},
        ]
        result = "Work = " + _f(out_work) + " J"

    elif sf == "time":
        if p is None or w is None:
            return {"error": "Enter power and work to find time.",
                    "steps": [], "disclaimer": _DISCLAIMER}
        if p == 0:
            return {"error": "Power cannot be zero when solving for time.",
                    "steps": [], "disclaimer": _DISCLAIMER}
        out_time = w / p
        steps = [
            {"label": "Rearrange", "math": r"\(t = \dfrac{W}{P}\)",
             "note": "Solve P = W/t for time."},
            {"label": "Substitute",
             "math": r"\(t = \dfrac{" + _f(w) + r"}{" + _f(p) + r"}\)",
             "note": "Work in joules, power in watts."},
            {"label": "Result", "math": r"\(t = " + _f(out_time) + r"\ \text{s}\)",
             "note": "Time in seconds."},
        ]
        result = "Time = " + _f(out_time) + " s"

    else:
        return {"error": "Choose what to solve for: power, work or time.",
                "steps": [], "disclaimer": _DISCLAIMER}

    return {
        "result": result,
        "solve_for": sf,
        "work": out_work,
        "time": out_time,
        "power": out_power,
        "steps": steps,
        "explanation": _EXPLANATION,
        "law_statement": _LAW_STATEMENT,
        "law_source_name": _LAW_SOURCE_NAME,
        "law_source_url": _LAW_SOURCE_URL,
        "disclaimer": _DISCLAIMER,
    }

from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
