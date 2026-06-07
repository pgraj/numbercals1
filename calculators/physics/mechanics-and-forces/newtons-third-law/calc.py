"""Newton's Third Law: action and reaction are equal and opposite, on two different bodies.
Pick a scenario and an action force; see the equal-and-opposite reaction."""
from __future__ import annotations
from core.registry import register

_DISCLAIMER = ("These values are estimates and may contain computation, formula, "
    "or system errors. They are provided for general reference only — always verify "
    "results independently before relying on them for academic or professional "
    "decisions.")

_LAW_STATEMENT = ("When one body exerts a force on a second body, the second exerts a force "
    "of the same size in the opposite direction on the first. The two forces act on different "
    "bodies, so they never cancel each other.")
_LAW_SOURCE_NAME = "Wikipedia \u2014 Newton's laws of motion"
_LAW_SOURCE_URL = "https://en.wikipedia.org/wiki/Newton%27s_laws_of_motion"

def _f(x):
    if x is None: return ""
    if abs(x - round(x)) < 1e-9: return str(int(round(x)))
    return ("%.4f" % x).rstrip("0").rstrip(".")

# Scenario -> (body A, action by A on B, body B, reaction by B on A)
_SCENARIOS = {
    "swimmer": ("swimmer", "pushes the water backward", "water", "pushes the swimmer forward"),
    "rocket":  ("rocket", "pushes the gas downward", "gas", "pushes the rocket upward"),
    "walking": ("foot", "pushes the ground backward", "ground", "pushes the foot forward"),
    "gun":     ("gun", "pushes the bullet forward", "bullet", "pushes the gun back (recoil)"),
    "book":    ("book", "presses down on the table", "table", "presses up on the book"),
}

_EXPLANATION = [
    {"heading": "What the third law says",
     "body": "Forces always come in pairs. Whenever you push on something, it pushes back "
             "on you just as hard, in the opposite direction. There is no such thing as a "
             "one-sided push."},
    {"heading": "The pair acts on two different things",
     "body": "This is the key point students often miss. The two forces do NOT act on the "
             "same object, so they do not cancel out. You push the wall (force on the "
             "wall); the wall pushes you (force on you). Different bodies."},
    {"heading": "Why it makes things move",
     "body": "A swimmer pushes water backward, so the water pushes the swimmer forward. A "
             "rocket throws gas down, so the gas pushes the rocket up. The reaction force "
             "is what actually propels you."},
]

@register(
    slug="newtons-third-law",
    name="Newton's Third Law (Action\u2013Reaction)",
    section="physics",
    topic="Mechanics & Forces",
    sub="Newton's Laws",
    order=2,
    summary="See Newton's third law: every action force has an equal and opposite reaction on a different body.",
    formula="F(A on B) = \u2212 F(B on A)",
    tags=["newton", "third law", "action", "reaction", "force", "pairs", "mechanics"],
    viz_template="viz/newtons-third-law.html",
    scholar="isaac-newton",
    related=["newtons-first-law", "newtons-second-law"],
)
def compute(scenario="swimmer", action_force=20.0, **_ignored):
    sc = str(scenario or "swimmer").strip().lower()
    if sc not in _SCENARIOS:
        sc = "swimmer"

    def num(v):
        if v is None or v == "":
            return None
        return float(v)

    try:
        F = num(action_force)
    except (TypeError, ValueError):
        return {"error": "Please enter a number for the action force.",
                "steps": [], "disclaimer": _DISCLAIMER}
    if F is None:
        F = 20.0
    if F < 0:
        return {"error": "Enter the force size as a positive number.",
                "steps": [], "disclaimer": _DISCLAIMER}

    bodyA, actAB, bodyB, reactBA = _SCENARIOS[sc]
    reaction = F  # equal in size

    steps = [
        {"label": "The rule", "math": r"\(\vec{F}_{A\to B} = -\,\vec{F}_{B\to A}\)",
         "note": "Action and reaction are equal in size and opposite in direction."},
        {"label": "Action", "math": r"\(F_{\text{action}} = " + _f(F) + r"\ \text{N}\)",
         "note": "The " + bodyA + " " + actAB + " with " + _f(F) + " N."},
        {"label": "Reaction", "math": r"\(F_{\text{reaction}} = " + _f(reaction) + r"\ \text{N}\)",
         "note": "So the " + bodyB + " " + reactBA + " with the same " + _f(reaction) + " N."},
    ]

    result = ("Action: the " + bodyA + " " + actAB + " with " + _f(F) + " N. "
              "Reaction: the " + bodyB + " " + reactBA + " with an equal " + _f(reaction) + " N.")

    return {
        "result": result,
        "scenario": sc,
        "body_a": bodyA,
        "body_b": bodyB,
        "action_force": F,
        "reaction_force": reaction,
        "action_desc": actAB,
        "reaction_desc": reactBA,
        "steps": steps,
        "explanation": _EXPLANATION,
        "law_statement": _LAW_STATEMENT,
        "law_source_name": _LAW_SOURCE_NAME,
        "law_source_url": _LAW_SOURCE_URL,
        "disclaimer": _DISCLAIMER,
    }

from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
