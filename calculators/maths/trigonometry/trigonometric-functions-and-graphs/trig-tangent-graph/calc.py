"""y = tan x — Trigonometric Functions & Graphs cluster (Stage 2).

Accepts `angle_unit` ("deg"|"rad"): x is READ and DISPLAYED in the chosen unit,
the steps match, and the viz relabels the x-axis in π-fractions when radians is
selected. Tangent is undefined where cos x = 0 (90° + 180°k, i.e. π/2 + πk).
"""
import math

from core.registry import register

DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or system "
    "errors. They are provided for general reference only — always verify results "
    "independently before relying on them for academic or professional decisions."
)


@register(
    slug="trig-tangent-graph",
    name="y = tan x",
    section="maths",
    sub="Trigonometric Functions & Graphs",
    topic="Trigonometry",
    order=0,
    summary=(
        "Plot and evaluate the tangent function y = tan x, with its vertical "
        "asymptotes at 90°, 270° and every 180° thereafter, a period of just "
        "180°, and an unbounded range, in degrees or radians, shown on a graph "
        "where the curve diverges towards each asymptote."
    ),
    formula="y = tan x = sin x / cos x  (period 180°, asymptotes where cos x = 0)",
    tags=[
        "tangent graph", "y = tan x", "asymptote", "period 180", "discontinuous",
        "trigonometry", "CBSE Class 11", "A-Level", "Common Core HSF-TF",
        "Singapore A-Math", "France Premiere", "Germany Klasse 10",
        "ACARA Year 11", "UAE Grade 11",
    ],
    viz_template="viz/trig-tangent-graph.html",
)
def compute(angle_deg=None, angle_unit="deg"):
    try:
        unit = "rad" if str(angle_unit) == "rad" else "deg"
        if angle_deg is None or angle_deg == "":
            return _err("Enter an angle in %s." % ("radians" if unit == "rad" else "degrees"))
        x_in = float(angle_deg)
        x = x_in if unit == "deg" else math.degrees(x_in)
        xd = _ang(x, unit)
        # undefined where cos x = 0, i.e. x = 90 + 180k
        if abs((x - 90) % 180) < 1e-9:
            return {
                "result": "undefined", "x": x, "y": None, "undefined": True,
                "angle_unit": unit, "period_deg": 180,
                "steps": [
                    {"label": "Check the cosine",
                     "math": r"\(\cos %s = 0\)" % xd,
                     "note": "Tangent is sin x / cos x, so it is undefined when cos x is zero."},
                    {"label": "This is an asymptote",
                     "math": r"\(\tan %s \to \pm\infty\)" % xd,
                     "note": "The graph has a vertical asymptote here; there is no value."},
                ],
                "explanation": _expl(), "disclaimer": DISCLAIMER,
            }
        y = math.tan(math.radians(x))
        steps = [
            {"label": "Read the input angle",
             "math": r"\(x = %s\)" % xd,
             "note": "Tangent repeats every 180° (π rad), not 360°."},
            {"label": "Evaluate as sin over cos",
             "math": r"\(\tan %s = \dfrac{\sin %s}{\cos %s} = %s\)"
                     % (xd, xd, xd, _fmt(y)),
             "note": "The ratio grows without bound as cos approaches zero."},
            {"label": "Where it sits on the curve",
             "math": r"\((%s,\ %s)\)" % (xd, _fmt(y)),
             "note": "Between asymptotes the curve sweeps from −∞ up to +∞."},
        ]
        return {
            "result": _fmt(y), "x": x, "y": round(y, 6), "undefined": False,
            "angle_unit": unit, "period_deg": 180,
            "steps": steps, "explanation": _expl(), "disclaimer": DISCLAIMER,
        }
    except (TypeError, ValueError):
        return _err("Please enter a valid number.")


def _expl():
    return [
        {"heading": "Why tangent has gaps",
         "body": "Tangent is sine divided by cosine. Wherever cosine is zero — at "
                 "90°, 270°, and every 180° apart — the division is undefined, so "
                 "the graph shoots off to infinity and a vertical asymptote appears."},
        {"heading": "Degrees or radians",
         "body": "Only the x-axis labels change between the two units; the branches "
                 "are the same. In radians the asymptotes sit at π/2, 3π/2, and so "
                 "on — odd multiples of π/2."},
        {"heading": "A shorter period",
         "body": "Unlike sine and cosine, tangent repeats every 180° (π rad), not "
                 "360°, and its range is all real numbers. Each branch rises "
                 "continuously from negative infinity to positive infinity between "
                 "two asymptotes."},
    ]


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
