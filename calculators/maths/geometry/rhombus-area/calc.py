"""Rhombus — geometry > 2D Geometry. Area from the two diagonals; perimeter from the side."""
from core.registry import register
import math

@register(
    slug="rhombus-area",
    name="Rhombus Area Calculator",
    section="maths",
    sub="2D Shapes",
    topic="Geometry",
    tags=["rhombus", "area", "diagonals", "perimeter", "geometry"],
    formula="area = \u00bd\u00d7d\u2081\u00d7d\u2082 ; side = \u00bd\u221a(d\u2081\u00b2+d\u2082\u00b2) ; perimeter = 4\u00d7side",
    summary="Find a rhombus's area from its two diagonals, and its perimeter from the side length (which the diagonals also give you).",
    viz_template="viz/rhombus-area.html",
)
def compute(diagonal_1: float = 6, diagonal_2: float = 8):
    try:
        d1 = float(diagonal_1); d2 = float(diagonal_2)
    except (TypeError, ValueError):
        return {"error": "Enter numbers for the two diagonals."}
    if d1 <= 0 or d2 <= 0:
        return {"error": "Diagonals must be greater than zero."}
    area = 0.5 * d1 * d2
    side = 0.5 * math.sqrt(d1 * d1 + d2 * d2)
    perim = 4 * side
    steps = [
        {"label": "Area", "math": r"\(A = \tfrac{1}{2}\,d_1 d_2 = \tfrac{1}{2} \times " + ("%g" % d1) + r" \times " + ("%g" % d2) + r" = " + ("%g" % area) + r"\)", "note": "Half the product of the diagonals."},
        {"label": "Side", "math": r"\(s = \tfrac{1}{2}\sqrt{d_1^2 + d_2^2} = " + ("%.4g" % side) + r"\)", "note": "The diagonals bisect at right angles, so Pythagoras gives the side."},
        {"label": "Perimeter", "math": r"\(P = 4s = " + ("%.4g" % perim) + r"\)", "note": "All four sides are equal."},
    ]
    return {
        "result": "Area " + ("%g" % area) + ", side " + ("%.4g" % side) + ", perimeter " + ("%.4g" % perim),
        "area": round(area, 6), "diagonal_1": d1, "diagonal_2": d2, "side": round(side, 6), "perimeter": round(perim, 6), "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
