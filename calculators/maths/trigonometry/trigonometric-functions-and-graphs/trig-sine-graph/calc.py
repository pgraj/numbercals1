"""y = sin x — Trigonometric Functions & Graphs cluster (Stage 2).

Evaluate sin at an angle and report the graph's key features (amplitude 1,
period 360°/2π, range [-1, 1], roots, max/min). The signature visual links the
unit-circle point to the sine wave tracing out beside it.
"""
import math

from core.registry import register

DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or system "
    "errors. They are provided for general reference only — always verify results "
    "independently before relying on them for academic or professional decisions."
)


@register(
    slug="trig-sine-graph",
    name="y = sin x",
    section="maths",
    sub="Trigonometric Functions & Graphs",
    topic="Trigonometry",
    order=0,
    summary=(
        "Plot and evaluate the sine function y = sin x, seeing its amplitude, "
        "period, and range, with a linked animation where a point moving around "
        "the unit circle traces the sine wave out in real time so you can see "
        "exactly why the curve has its shape."
    ),
    formula="y = sin x  (amplitude 1, period 360° = 2π)",
    tags=[
        "sine graph", "y = sin x", "sine curve", "amplitude", "period",
        "periodic function", "trigonometry", "CBSE Class 11", "A-Level",
        "GCSE Higher", "Common Core HSF-TF", "Singapore A-Math",
        "France Premiere", "Germany Klasse 10", "ACARA Year 11", "UAE Grade 11",
    ],
    viz_template="viz/trig-sine-graph.html",
)
def compute(angle_deg=None):
    try:
        if angle_deg is None or angle_deg == "":
            return _err("Enter an angle in degrees.")
        x = float(angle_deg)
        y = math.sin(math.radians(x))

        steps = [
            {"label": "Read the input angle",
             "math": r"\(x = %s^\circ\)" % _fmt(x),
             "note": "The horizontal axis of the graph is the angle."},
            {"label": "Evaluate the sine",
             "math": r"\(y = \sin %s^\circ = %s\)" % (_fmt(x), _fmt(y)),
             "note": "This y-value is the height of the unit-circle point at that angle."},
            {"label": "Where it sits on the curve",
             "math": r"\((%s^\circ,\ %s)\)" % (_fmt(x), _fmt(y)),
             "note": "sin repeats every 360°, so this point recurs each full turn."},
        ]
        return {
            "result": _fmt(y),
            "x": x,
            "y": round(y, 6),
            "amplitude": 1,
            "period_deg": 360,
            "steps": steps,
            "explanation": [
                {"heading": "Why it waves",
                 "body": "As a point travels around the unit circle, its height "
                         "(the sine) rises to 1 at 90°, falls back through 0 at "
                         "180°, down to −1 at 270°, and back to 0 at 360°. Plotting "
                         "that height against the angle traces the sine wave."},
                {"heading": "Amplitude, period, range",
                 "body": "The basic sine curve has amplitude 1 (it reaches ±1), a "
                         "period of 360° or 2π radians (it repeats every full turn), "
                         "and a range from −1 to 1. It crosses zero at 0°, 180°, "
                         "360°, and so on."},
            ],
            "disclaimer": DISCLAIMER,
        }
    except (TypeError, ValueError):
        return _err("Please enter a valid number of degrees.")


def _err(msg):
    return {"error": msg, "steps": [], "disclaimer": DISCLAIMER}


def _fmt(x):
    if x is None:
        return ""
    if abs(x - round(x)) < 1e-9:
        return str(int(round(x)))
    return ("%.4f" % x).rstrip("0").rstrip(".")


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
