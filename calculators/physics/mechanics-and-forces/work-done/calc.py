"""Work Done: W = F d cos(theta). Angle calc — theta in the chosen unit, defaults to 0."""
from __future__ import annotations
import math
from core.registry import register

_DISCLAIMER = ("These values are estimates and may contain computation, formula, "
    "or system errors. They are provided for general reference only — always verify "
    "results independently before relying on them for academic or professional "
    "decisions.")

def _f(x):
    if x is None: return ""
    if abs(x - round(x)) < 1e-9: return str(int(round(x)))
    return ("%.4f" % x).rstrip("0").rstrip(".")

_LAW_STATEMENT = ("The work done by a constant force is the energy transferred when the force "
    "moves a body through a distance. It equals the force times the distance times the cosine "
    "of the angle between them, W = F d cos\u03b8.")
_LAW_SOURCE_NAME = "Wikipedia \u2014 Work (physics)"
_LAW_SOURCE_URL = "https://en.wikipedia.org/wiki/Work_(physics)"

_EXPLANATION = [
    {"heading": "What work means in physics",
     "body": "Work is done when a force moves its point of application through a "
             "distance. It measures the energy transferred by that force, and it is "
             "measured in joules, the same unit as energy."},
    {"heading": "Why the angle appears",
     "body": "Only the part of the force along the direction of movement does work. The "
             "factor cos\u03b8, where \u03b8 is the angle between the force and the "
             "displacement, picks out that part. A force at right angles to the motion "
             "does no work at all, because cos\u03b8 is zero."},
    {"heading": "Sign of the work",
     "body": "If the force has a component along the motion the work is positive; if it "
             "opposes the motion, as friction does, cos\u03b8 is negative and the work is "
             "negative, meaning energy is taken away."},
]

@register(
    slug="work-done",
    name="Work Done",
    section="physics",
    topic="Mechanics & Forces",
    sub="Work & Power",
    order=3,
    summary="Calculate the work done by a force over a distance, allowing for the angle between the force and the movement.",
    formula="W = F d cos\u03b8",
    tags=["work", "work done", "force", "distance", "joules", "mechanics", "energy"],
    viz_template="viz/work-done.html",
    related=["mechanical-power", "kinetic-energy", "potential-energy"],
)
def compute(force=10.0, distance=5.0, angle=0.0, angle_unit="deg", **_ignored):
    unit = str(angle_unit or "deg").strip().lower()
    if unit not in ("deg", "rad"):
        unit = "deg"

    def num(v):
        if v is None or v == "":
            return None
        return float(v)

    try:
        F = num(force)
        d = num(distance)
        a = num(angle)
    except (TypeError, ValueError):
        return {"error": "Please enter numbers only.", "steps": [], "disclaimer": _DISCLAIMER}

    if F is None or d is None:
        return {"error": "Enter a force and a distance.", "steps": [], "disclaimer": _DISCLAIMER}
    if a is None:
        a = 0.0

    # read angle in chosen unit, convert to degrees internally
    if unit == "deg":
        angle_deg = a
    else:
        angle_deg = math.degrees(a)

    angle_rad = math.radians(angle_deg)
    cos_t = math.cos(angle_rad)
    work = F * d * cos_t

    # display angle in chosen unit
    if unit == "deg":
        ang_disp = _f(angle_deg) + r"^\circ"
    else:
        ang_disp = _f(a) + r"\ \text{rad}"

    steps = [
        {"label": "Formula", "math": r"\(W = F\,d\,\cos\theta\)",
         "note": "Work is force times distance times the cosine of the angle between them."},
        {"label": "Substitute",
         "math": r"\(W = (" + _f(F) + r")(" + _f(d) + r")\cos(" + ang_disp + r")\)",
         "note": "Force in newtons, distance in metres."},
        {"label": "Cosine factor",
         "math": r"\(\cos(" + ang_disp + r") = " + _f(cos_t) + r"\)",
         "note": "The fraction of the force that acts along the movement."},
        {"label": "Result", "math": r"\(W = " + _f(work) + r"\ \text{J}\)",
         "note": "Work in joules."},
    ]

    result = "Work done = " + _f(work) + " J"

    return {
        "result": result,
        "force": F,
        "distance": d,
        "angle_deg": angle_deg,
        "cos_theta": cos_t,
        "work": work,
        "steps": steps,
        "explanation": _EXPLANATION,
        "law_statement": _LAW_STATEMENT,
        "law_source_name": _LAW_SOURCE_NAME,
        "law_source_url": _LAW_SOURCE_URL,
        "disclaimer": _DISCLAIMER,
        "angle_unit": unit,
    }

from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
