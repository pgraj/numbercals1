"""Newton's First Law (inertia): a body keeps its motion unless a net force acts.
Interactive scenario: choose rest or moving, toggle the net force, see what happens."""
from __future__ import annotations
from core.registry import register

_DISCLAIMER = ("These values are estimates and may contain computation, formula, "
    "or system errors. They are provided for general reference only — always verify "
    "results independently before relying on them for academic or professional "
    "decisions.")

_LAW_STATEMENT = ("A body remains at rest, or moving at a constant speed in a straight line, "
    "unless it is acted upon by a net external force. This tendency to keep its state of "
    "motion is called inertia.")
_LAW_SOURCE_NAME = "Wikipedia \u2014 Newton's laws of motion"
_LAW_SOURCE_URL = "https://en.wikipedia.org/wiki/Newton%27s_laws_of_motion"

_EXPLANATION = [
    {"heading": "What the first law says",
     "body": "Things do not change how they are moving on their own. Something sitting "
             "still stays still. Something moving keeps moving the same way \u2014 unless a "
             "push or pull (a force) comes along to change it."},
    {"heading": "This 'laziness' is called inertia",
     "body": "Inertia is just the name for an object's resistance to changing its motion. "
             "Heavier objects have more inertia, which is why a loaded trolley is harder to "
             "start moving \u2014 and harder to stop \u2014 than an empty one."},
    {"heading": "Why we do not always see it",
     "body": "On Earth, moving things usually slow down and stop. That is not the object "
             "changing its mind \u2014 it is hidden forces like friction and air resistance "
             "pushing against it. Remove those (like in space) and motion really does carry "
             "on forever."},
]

@register(
    slug="newtons-first-law",
    name="Newton's First Law (Inertia)",
    section="physics",
    topic="Mechanics & Forces",
    sub="Newton's Laws",
    order=0,
    summary="See Newton's first law in action: a body keeps still or keeps moving unless a net force acts on it.",
    formula="\u2211F = 0 \u21d2 velocity stays constant",
    tags=["newton", "first law", "inertia", "force", "motion", "rest", "mechanics"],
    viz_template="viz/newtons-first-law.html",
    scholar="isaac-newton",
    related=["newtons-second-law", "newtons-third-law", "acceleration"],
)
def compute(initial_state="moving", net_force="off", **_ignored):
    state = str(initial_state or "moving").strip().lower()
    if state not in ("rest", "moving"):
        state = "moving"
    force = str(net_force or "off").strip().lower()
    force_on = force in ("on", "yes", "true", "1")

    if state == "rest":
        if force_on:
            outcome = "A net force acts, so the body starts to move \u2014 it accelerates from rest."
            verdict = "Motion changes: starts moving"
        else:
            outcome = "No net force, so the body stays exactly where it is, at rest."
            verdict = "Motion unchanged: stays at rest"
    else:  # moving
        if force_on:
            outcome = "A net force acts, so the body's motion changes \u2014 it speeds up, slows down, or turns."
            verdict = "Motion changes: speeds up, slows, or turns"
        else:
            outcome = "No net force, so the body keeps moving at the same speed in a straight line."
            verdict = "Motion unchanged: constant velocity"

    steps = [
        {"label": "The rule", "math": r"\(\sum F = 0 \;\Rightarrow\; v = \text{constant}\)",
         "note": "With zero net force, velocity (speed and direction) does not change."},
        {"label": "With a force", "math": r"\(\sum F \neq 0 \;\Rightarrow\; \text{motion changes}\)",
         "note": "A net force is the only thing that can change how a body moves."},
        {"label": "This case", "math": r"\(\text{" + verdict + r"}\)",
         "note": outcome},
    ]

    return {
        "result": verdict + ". " + outcome,
        "initial_state": state,
        "force_on": force_on,
        "verdict": verdict,
        "steps": steps,
        "explanation": _EXPLANATION,
        "law_statement": _LAW_STATEMENT,
        "law_source_name": _LAW_SOURCE_NAME,
        "law_source_url": _LAW_SOURCE_URL,
        "disclaimer": _DISCLAIMER,
    }

from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
