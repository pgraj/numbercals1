"""Newton's Laws of Motion: a 3-mode selector. 1st (inertia) and 3rd (action-reaction)
are conceptual; 2nd law solves F = m a for force, mass or acceleration."""
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

_EXPLANATION = [
    {"heading": "The three laws together",
     "body": "Newton's three laws describe how forces change motion. The first explains "
             "what happens with no net force, the second says exactly how a net force "
             "changes motion, and the third describes how forces always come in pairs."},
    {"heading": "The second law is the workhorse",
     "body": "F = ma is the law you calculate with. The net force on a body equals its "
             "mass times its acceleration, so a given force produces less acceleration on "
             "a heavier body. Rearranging it lets you find any one of force, mass or "
             "acceleration from the other two."},
    {"heading": "First and third laws in words",
     "body": "First law (inertia): a body stays at rest, or moves at constant velocity, "
             "unless a net force acts on it. Third law: for every action there is an "
             "equal and opposite reaction \u2014 forces always act in pairs on two "
             "different bodies."},
]

@register(
    slug="newtons-laws",
    name="Newton's Laws of Motion",
    section="physics",
    topic="Mechanics & Forces",
    sub="Newton's Laws",
    order=0,
    summary="Explore Newton's three laws of motion and solve F = ma for force, mass or acceleration.",
    formula="F = m a  (2nd law)",
    tags=["newton", "laws of motion", "force", "mass", "acceleration", "inertia", "mechanics"],
    viz_template="viz/newtons-laws.html",
    scholar="isaac-newton",
    related=["work-done", "mechanical-power", "kinetic-energy"],
)
def compute(law="second", solve_for="force", mass=2.0, acceleration=5.0, force=None, **_ignored):
    try:
        which = str(law or "second").strip().lower()
    except Exception:
        which = "second"

    if which in ("first", "1", "1st", "inertia"):
        steps = [
            {"label": "First law (inertia)",
             "math": r"\(\sum F = 0 \;\Rightarrow\; v = \text{constant}\)",
             "note": "With no net force, velocity does not change."},
            {"label": "In words", "math": r"\(\text{rest stays at rest; motion stays uniform}\)",
             "note": "A body keeps its state of motion unless a net force acts."},
        ]
        return {
            "result": "First law: with zero net force a body stays at rest or keeps moving "
                       "at constant velocity (inertia).",
            "law": "first",
            "steps": steps,
            "explanation": _EXPLANATION,
            "disclaimer": _DISCLAIMER,
        }

    if which in ("third", "3", "3rd", "action", "reaction", "action-reaction"):
        steps = [
            {"label": "Third law (action\u2013reaction)",
             "math": r"\(\vec{F}_{AB} = -\,\vec{F}_{BA}\)",
             "note": "The force A exerts on B is equal and opposite to the force B exerts on A."},
            {"label": "In words", "math": r"\(\text{equal in size, opposite in direction}\)",
             "note": "The paired forces act on two different bodies, so they do not cancel."},
        ]
        return {
            "result": "Third law: every action has an equal and opposite reaction; forces "
                       "act in pairs on two different bodies.",
            "law": "third",
            "steps": steps,
            "explanation": _EXPLANATION,
            "disclaimer": _DISCLAIMER,
        }

    # default: second law, solve F = m a
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
        "law": "second",
        "solve_for": sf,
        "mass": out_mass,
        "acceleration": out_acc,
        "force": out_force,
        "steps": steps,
        "explanation": _EXPLANATION,
        "disclaimer": _DISCLAIMER,
    }

from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
