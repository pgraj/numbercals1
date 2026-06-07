"""Newton's Second Law: F = m a. Solve for force, mass or acceleration."""
from __future__ import annotations
from core.registry import register

_DISCLAIMER = ("These values are estimates and may contain computation, formula, "
    "or system errors. They are provided for general reference only — always verify "
    "results independently before relying on them for academic or professional "
    "decisions.")

_LAW_STATEMENT = ("The net force on a body equals its mass times its acceleration, F = m a. "
    "A bigger force gives a bigger acceleration, and the same force gives a heavier body a "
    "smaller acceleration.")
_LAW_SOURCE_NAME = "Wikipedia \u2014 Newton's laws of motion"
_LAW_SOURCE_URL = "https://en.wikipedia.org/wiki/Newton%27s_laws_of_motion"

def _f(x):
    if x is None: return ""
    if abs(x - round(x)) < 1e-9: return str(int(round(x)))
    return ("%.4f" % x).rstrip("0").rstrip(".")

_EXPLANATION = [
    {"heading": "What the second law says",
     "body": "Push something and it speeds up \u2014 that change in motion is called "
             "acceleration. The second law tells you exactly how much: the net force "
             "equals the mass times the acceleration, written F = m a."},
    {"heading": "Heavier means harder to move",
     "body": "For the same push, a heavier object accelerates less. Push an empty shopping "
             "trolley and it shoots forward; push a full one with the same effort and it "
             "barely budges. More mass, less acceleration."},
    {"heading": "Rearranging to find any piece",
     "body": "Because F = m a links three things, knowing any two gives the third. Force = "
             "mass \u00d7 acceleration, mass = force \u00f7 acceleration, and acceleration = "
             "force \u00f7 mass."},
]

@register(
    slug="newtons-second-law",
    name="Newton's Second Law (F = ma)",
    section="physics",
    topic="Mechanics & Forces",
    sub="Newton's Laws",
    order=1,
    summary="Use Newton's second law F = ma to solve for force, mass or acceleration.",
    formula="F = m a",
    tags=["newton", "second law", "force", "mass", "acceleration", "mechanics"],
    viz_template="viz/newtons-second-law.html",
    scholar="isaac-newton",
    related=["newtons-first-law", "newtons-third-law", "acceleration", "work-done"],
)
def compute(solve_for="force", mass=2.0, acceleration=5.0, force=None, **_ignored):
    try:
        sf = str(solve_for or "force").strip().lower()
    except Exception:
        sf = "force"

    def num(v):
        if v is None or v == "":
            return None
        return float(v)

    try:
        m = num(mass)
        a = num(acceleration)
        F = num(force)
    except (TypeError, ValueError):
        return {"error": "Please enter numbers only.", "steps": [], "disclaimer": _DISCLAIMER}

    out_mass = m
    out_acc = a
    out_force = F
    steps = []
    result = ""

    if sf == "force":
        if m is None or a is None:
            return {"error": "Enter mass and acceleration to find force.",
                    "steps": [], "disclaimer": _DISCLAIMER}
        out_force = m * a
        steps = [
            {"label": "Second law", "math": r"\(F = m a\)",
             "note": "Net force equals mass times acceleration."},
            {"label": "Substitute",
             "math": r"\(F = (" + _f(m) + r")(" + _f(a) + r")\)",
             "note": "Mass in kg, acceleration in m/s\u00b2."},
            {"label": "Result", "math": r"\(F = " + _f(out_force) + r"\ \text{N}\)",
             "note": "Force in newtons."},
        ]
        result = "Force = " + _f(out_force) + " N"

    elif sf == "mass":
        if F is None or a is None:
            return {"error": "Enter force and acceleration to find mass.",
                    "steps": [], "disclaimer": _DISCLAIMER}
        if a == 0:
            return {"error": "Acceleration cannot be zero when solving for mass.",
                    "steps": [], "disclaimer": _DISCLAIMER}
        out_mass = F / a
        steps = [
            {"label": "Rearrange", "math": r"\(m = \dfrac{F}{a}\)",
             "note": "Solve F = ma for mass."},
            {"label": "Substitute",
             "math": r"\(m = \dfrac{" + _f(F) + r"}{" + _f(a) + r"}\)",
             "note": "Force in newtons, acceleration in m/s\u00b2."},
            {"label": "Result", "math": r"\(m = " + _f(out_mass) + r"\ \text{kg}\)",
             "note": "Mass in kilograms."},
        ]
        result = "Mass = " + _f(out_mass) + " kg"

    elif sf == "acceleration":
        if F is None or m is None:
            return {"error": "Enter force and mass to find acceleration.",
                    "steps": [], "disclaimer": _DISCLAIMER}
        if m == 0:
            return {"error": "Mass cannot be zero when solving for acceleration.",
                    "steps": [], "disclaimer": _DISCLAIMER}
        out_acc = F / m
        steps = [
            {"label": "Rearrange", "math": r"\(a = \dfrac{F}{m}\)",
             "note": "Solve F = ma for acceleration."},
            {"label": "Substitute",
             "math": r"\(a = \dfrac{" + _f(F) + r"}{" + _f(m) + r"}\)",
             "note": "Force in newtons, mass in kg."},
            {"label": "Result", "math": r"\(a = " + _f(out_acc) + r"\ \text{m/s}^2\)",
             "note": "Acceleration in metres per second-squared."},
        ]
        result = "Acceleration = " + _f(out_acc) + " m/s\u00b2"

    else:
        return {"error": "Choose what to solve for: force, mass or acceleration.",
                "steps": [], "disclaimer": _DISCLAIMER}

    return {
        "result": result,
        "solve_for": sf,
        "mass": out_mass,
        "acceleration": out_acc,
        "force": out_force,
        "steps": steps,
        "explanation": _EXPLANATION,
        "law_statement": _LAW_STATEMENT,
        "law_source_name": _LAW_SOURCE_NAME,
        "law_source_url": _LAW_SOURCE_URL,
        "disclaimer": _DISCLAIMER,
    }

from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
