"""y = cos x — Trigonometric Functions & Graphs cluster (Stage 2)."""
import math

from core.registry import register

DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or system "
    "errors. They are provided for general reference only — always verify results "
    "independently before relying on them for academic or professional decisions."
)


@register(
    slug="trig-cosine-graph",
    name="y = cos x",
    section="maths",
    sub="Trigonometric Functions & Graphs",
    topic="Trigonometry",
    order=0,
    summary=(
        "Plot and evaluate the cosine function y = cos x, seeing its amplitude, "
        "period, and range, with a linked animation where a point moving around "
        "the unit circle traces the cosine wave so you can see why it leads the "
        "sine curve by ninety degrees."
    ),
    formula="y = cos x  (amplitude 1, period 360° = 2π)",
    tags=[
        "cosine graph", "y = cos x", "cosine curve", "amplitude", "period",
        "phase", "trigonometry", "CBSE Class 11", "A-Level", "GCSE Higher",
        "Common Core HSF-TF", "Singapore A-Math", "France Premiere",
        "Germany Klasse 10", "ACARA Year 11", "UAE Grade 11",
    ],
    viz_template="viz/trig-cosine-graph.html",
)
def compute(angle_deg=None):
    try:
        if angle_deg is None or angle_deg == "":
            return _err("Enter an angle in degrees.")
        x = float(angle_deg)
        y = math.cos(math.radians(x))
        steps = [
            {"label": "Read the input angle",
             "math": r"\(x = %s^\circ\)" % _fmt(x),
             "note": "The horizontal axis is the angle."},
            {"label": "Evaluate the cosine",
             "math": r"\(y = \cos %s^\circ = %s\)" % (_fmt(x), _fmt(y)),
             "note": "This is the horizontal coordinate of the unit-circle point."},
            {"label": "Where it sits on the curve",
             "math": r"\((%s^\circ,\ %s)\)" % (_fmt(x), _fmt(y)),
             "note": "cos starts at its maximum of 1 and repeats every 360°."},
        ]
        return {
            "result": _fmt(y), "x": x, "y": round(y, 6),
            "amplitude": 1, "period_deg": 360,
            "steps": steps,
            "explanation": [
                {"heading": "Cosine leads sine",
                 "body": "The cosine curve is the sine curve shifted left by 90°. It "
                         "starts at its maximum value of 1 when x = 0, falls to 0 at "
                         "90°, reaches −1 at 180°, and returns to 1 at 360°."},
                {"heading": "Same shape, different start",
                 "body": "Cosine has the same amplitude (1), period (360° or 2π), and "
                         "range (−1 to 1) as sine. It is the horizontal coordinate of "
                         "the unit-circle point, which is why it begins at 1."},
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
