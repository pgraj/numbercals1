"""y = tan x — Trigonometric Functions & Graphs cluster (Stage 2)."""
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
        "180°, and an unbounded range, shown on a graph where the curve diverges "
        "towards each asymptote."
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
def compute(angle_deg=None):
    try:
        if angle_deg is None or angle_deg == "":
            return _err("Enter an angle in degrees.")
        x = float(angle_deg)
        # undefined where cos x = 0, i.e. x = 90 + 180k
        if abs((x - 90) % 180) < 1e-9:
            return {
                "result": "undefined", "x": x, "y": None, "undefined": True,
                "period_deg": 180,
                "steps": [
                    {"label": "Check the cosine",
                     "math": r"\(\cos %s^\circ = 0\)" % _fmt(x),
                     "note": "Tangent is sin x / cos x, so it is undefined when cos x is zero."},
                    {"label": "This is an asymptote",
                     "math": r"\(\tan %s^\circ \to \pm\infty\)" % _fmt(x),
                     "note": "The graph has a vertical asymptote here; there is no value."},
                ],
                "explanation": _expl(), "disclaimer": DISCLAIMER,
            }
        y = math.tan(math.radians(x))
        steps = [
            {"label": "Read the input angle",
             "math": r"\(x = %s^\circ\)" % _fmt(x),
             "note": "Tangent repeats every 180°, not 360°."},
            {"label": "Evaluate as sin over cos",
             "math": r"\(\tan %s^\circ = \dfrac{\sin %s^\circ}{\cos %s^\circ} = %s\)"
                     % (_fmt(x), _fmt(x), _fmt(x), _fmt(y)),
             "note": "The ratio grows without bound as cos approaches zero."},
            {"label": "Where it sits on the curve",
             "math": r"\((%s^\circ,\ %s)\)" % (_fmt(x), _fmt(y)),
             "note": "Between asymptotes the curve sweeps from −∞ up to +∞."},
        ]
        return {
            "result": _fmt(y), "x": x, "y": round(y, 6), "undefined": False,
            "period_deg": 180,
            "steps": steps, "explanation": _expl(), "disclaimer": DISCLAIMER,
        }
    except (TypeError, ValueError):
        return _err("Please enter a valid number of degrees.")


def _expl():
    return [
        {"heading": "Why tangent has gaps",
         "body": "Tangent is sine divided by cosine. Wherever cosine is zero — at "
                 "90°, 270°, and every 180° apart — the division is undefined, so "
                 "the graph shoots off to infinity and a vertical asymptote appears."},
        {"heading": "A shorter period",
         "body": "Unlike sine and cosine, tangent repeats every 180°, not 360°, and "
                 "its range is all real numbers. Each branch rises continuously from "
                 "negative infinity to positive infinity between two asymptotes."},
    ]


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
