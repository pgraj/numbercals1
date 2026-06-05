"""y = sin x — Trigonometric Functions & Graphs cluster (Stage 2).

Evaluate sin at an angle and report the graph's key features. Accepts
`angle_unit` ("deg"|"rad"): x is READ and DISPLAYED in the chosen unit, the steps
match, and the viz relabels the x-axis in π-fractions when radians is selected.
The signature visual links the unit-circle point to the sine wave beside it.
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
        "period, and range in degrees or radians, with a linked animation where a "
        "point moving around the unit circle traces the sine wave out in real time "
        "so you can see exactly why the curve has its shape."
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
def compute(angle_deg=None, angle_unit="deg"):
    try:
        unit = "rad" if str(angle_unit) == "rad" else "deg"
        if angle_deg is None or angle_deg == "":
            return _err("Enter an angle in %s." % ("radians" if unit == "rad" else "degrees"))
        x_in = float(angle_deg)
        x = x_in if unit == "deg" else math.degrees(x_in)
        y = math.sin(math.radians(x))
        xd = _ang(x, unit)
        steps = [
            {"label": "Read the input angle",
             "math": r"\(x = %s\)" % xd,
             "note": "The horizontal axis of the graph is the angle."},
            {"label": "Evaluate the sine",
             "math": r"\(y = \sin %s = %s\)" % (xd, _fmt(y)),
             "note": "This y-value is the height of the unit-circle point at that angle."},
            {"label": "Where it sits on the curve",
             "math": r"\((%s,\ %s)\)" % (xd, _fmt(y)),
             "note": "sin repeats every 360° (2π rad), so this point recurs each full turn."},
        ]
        return {
            "result": _fmt(y), "x": x, "y": round(y, 6),
            "angle_unit": unit, "amplitude": 1, "period_deg": 360,
            "steps": steps,
            "explanation": [
                {"heading": "Why it waves",
                 "body": "As a point travels around the unit circle, its height "
                         "(the sine) rises to 1 at 90°, falls back through 0 at "
                         "180°, down to −1 at 270°, and back to 0 at 360°. Plotting "
                         "that height against the angle traces the sine wave."},
                {"heading": "Degrees or radians",
                 "body": "The curve is the same either way; only the x-axis labels "
                         "change. In radians the axis is marked in multiples of π — "
                         "0, π/2, π, 3π/2, 2π — which is how the function appears in "
                         "calculus."},
                {"heading": "Amplitude, period, range",
                 "body": "The basic sine curve has amplitude 1 (it reaches ±1), a "
                         "period of 360° or 2π radians, and a range from −1 to 1. It "
                         "crosses zero at 0°, 180°, 360°, and so on."},
            ],
            "disclaimer": DISCLAIMER,
        }
    except (TypeError, ValueError):
        return _err("Please enter a valid number.")


def _ang(deg, unit):
    if unit == "rad":
        return _fmt(math.radians(deg)) + r"\,\text{rad}"
    return _fmt(deg) + r"^\circ"


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
