"""Trapezoid — geometry > 2D Geometry. Area from parallel sides and height; perimeter from all sides."""
from core.registry import register

@register(
    slug="trapezoid-area",
    name="Trapezoid Area Calculator",
    section="maths",
    sub="2D Shapes",
    topic="Geometry",
    tags=["trapezoid", "trapezium", "area", "perimeter", "geometry"],
    formula="area = \u00bd(a+b)\u00d7h ; perimeter = a+b+c+d",
    summary="Find the area and perimeter of a trapezoid (trapezium) from its two parallel sides, height and the two slanted sides.",
    viz_template="viz/trapezoid-area.html",
)
def compute(parallel_a: float = 8, parallel_b: float = 5, height: float = 4,
            leg_c: float = 5, leg_d: float = 5):
    try:
        a = float(parallel_a); b = float(parallel_b); h = float(height)
        c = float(leg_c); d = float(leg_d)
    except (TypeError, ValueError):
        return {"error": "Enter numbers only."}
    if a <= 0 or b <= 0 or h <= 0:
        return {"error": "Parallel sides and height must be greater than zero."}
    if c < 0 or d < 0:
        return {"error": "Leg lengths cannot be negative."}
    area = 0.5 * (a + b) * h
    perim = a + b + c + d
    steps = [
        {"label": "Area", "math": r"\(A = \tfrac{1}{2}(a + b)\,h = \tfrac{1}{2}(" + ("%g + %g" % (a, b)) + r") \times " + ("%g" % h) + r" = " + ("%g" % area) + r"\)", "note": "Average of the parallel sides, times height."},
        {"label": "Perimeter", "math": r"\(P = a + b + c + d = " + ("%g" % perim) + r"\)", "note": "All four sides added."},
    ]
    return {
        "result": "Area " + ("%g" % area) + ", perimeter " + ("%g" % perim),
        "area": round(area, 6), "parallel_a": a, "parallel_b": b, "height": h, "perimeter": round(perim, 6), "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
