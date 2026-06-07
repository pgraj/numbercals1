"""Square — geometry > 2D Geometry. Area, perimeter and diagonal from the side length."""
from core.registry import register
import math

@register(
    slug="square-area",
    name="Square Area Calculator",
    section="maths",
    sub="2D Shapes",
    topic="Geometry",
    tags=["square", "area", "perimeter", "diagonal", "geometry"],
    formula="area = side\u00b2 ; perimeter = 4\u00d7side ; diagonal = side\u00d7\u221a2",
    summary="Find the area, perimeter and diagonal of a square from its side length.",
    viz_template="viz/square-area.html",
)
def compute(side: float = 5):
    try:
        s = float(side)
    except (TypeError, ValueError):
        return {"error": "Enter a number for the side length."}
    if s <= 0:
        return {"error": "Side length must be greater than zero."}
    area = s * s
    perim = 4 * s
    diag = s * math.sqrt(2)
    steps = [
        {"label": "Area", "math": r"\(A = s^2 = " + ("%g" % s) + r"^2 = " + ("%g" % area) + r"\)", "note": "Side multiplied by itself."},
        {"label": "Perimeter", "math": r"\(P = 4s = 4 \times " + ("%g" % s) + r" = " + ("%g" % perim) + r"\)", "note": "All four equal sides."},
        {"label": "Diagonal", "math": r"\(d = s\sqrt{2} = " + ("%g" % s) + r" \times 1.4142 = " + ("%.4g" % diag) + r"\)", "note": "Corner to corner, via Pythagoras."},
    ]
    return {
        "result": "Area " + ("%g" % area) + ", perimeter " + ("%g" % perim) + ", diagonal " + ("%.4g" % diag),
        "area": round(area, 6), "side": s, "perimeter": round(perim, 6), "diagonal": round(diag, 6), "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
