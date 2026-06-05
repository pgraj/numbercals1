"""Similar triangles & ratios — Foundations cluster of the Trigonometry topic.

Given a pair of corresponding sides (which fixes the scale factor) and one more
side, find its matching side in the other triangle by proportion.
"""
from core.registry import register

DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or system "
    "errors. They are provided for general reference only — always verify results "
    "independently before relying on them for academic or professional decisions."
)


@register(
    slug="trig-similar-triangles",
    name="Similar triangles & ratios",
    section="maths",
    sub="Foundations",
    topic="Trigonometry",
    order=0,
    summary=(
        "Find an unknown side of a triangle that is similar to another using the "
        "constant ratio between corresponding sides, with a visual that scales the "
        "two triangles together and shows the fixed scale factor."
    ),
    formula="a₁ / a₂ = b₁ / b₂  (corresponding sides are in proportion)",
    tags=[
        "similar triangles", "scale factor", "proportion", "ratio",
        "corresponding sides", "trigonometry", "CBSE Class 10", "GCSE", "KS3",
        "Common Core Grade 8", "Singapore Sec 2", "France 3e",
        "Germany Klasse 9", "ACARA Year 9", "UAE Grade 8",
    ],
    viz_template="viz/trig-similar-triangles.html",
)
def compute(a1=None, a2=None, b1=None):
    """Triangle 1 side a1 corresponds to triangle 2 side a2 (sets the scale).
    Given b1 in triangle 1, find b2 in triangle 2."""
    try:
        def num(x):
            if x is None or x == "":
                return None
            return float(x)

        a1, a2, b1 = num(a1), num(a2), num(b1)
        if a1 is None or a2 is None or b1 is None:
            return _err("Enter the corresponding pair a₁ and a₂, plus the side b₁.")
        if a1 <= 0 or a2 <= 0 or b1 <= 0:
            return _err("Side lengths must be greater than zero.")

        scale = a2 / a1
        b2 = b1 * scale

        steps = [
            {"label": "Find the scale factor",
             "math": r"\(k = \dfrac{a_2}{a_1} = \dfrac{%s}{%s} = %s\)"
                     % (_fmt(a2), _fmt(a1), _fmt(scale)),
             "note": "Corresponding sides of similar triangles share one constant ratio."},
            {"label": "Apply it to the known side",
             "math": r"\(b_2 = b_1 \times k = %s \times %s\)" % (_fmt(b1), _fmt(scale)),
             "note": "Multiply the matching side in the first triangle by the scale factor."},
            {"label": "Result",
             "math": r"\(b_2 = %s\)" % _fmt(b2),
             "note": "Every pair of corresponding sides keeps this same ratio."},
        ]
        return {
            "result": _fmt(b2),
            "a1": a1, "a2": a2, "b1": b1, "b2": b2, "scale": scale,
            "steps": steps,
            "explanation": [
                {"heading": "What 'similar' means",
                 "body": "Similar triangles have the same shape but not necessarily "
                         "the same size: their angles match exactly and every pair of "
                         "corresponding sides is in the same ratio, the scale factor."},
                {"heading": "Why one ratio is enough",
                 "body": "Because the scale factor is constant, knowing it from one "
                         "pair of sides lets you find any other side by multiplying or "
                         "dividing — the basis of map scales and scale models."},
            ],
            "disclaimer": DISCLAIMER,
        }
    except (TypeError, ValueError):
        return _err("Please enter valid numbers for the sides.")


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
