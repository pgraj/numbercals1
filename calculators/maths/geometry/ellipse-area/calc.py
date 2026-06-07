"""Ellipse — geometry > 2D Geometry. Area exactly; circumference via Ramanujan approximation."""
from core.registry import register
import math

@register(
    slug="ellipse-area",
    name="Ellipse Area Calculator",
    section="maths",
    sub="2D Shapes",
    topic="Geometry",
    tags=["ellipse", "area", "circumference", "semi-axis", "geometry"],
    formula="area = \u03c0ab ; circumference \u2248 \u03c0[3(a+b) \u2212 \u221a((3a+b)(a+3b))] (Ramanujan)",
    summary="Find an ellipse's area exactly from its semi-major and semi-minor axes, plus a very accurate approximate circumference (Ramanujan's formula).",
    viz_template="viz/ellipse-area.html",
)
def compute(semi_major_a: float = 6, semi_minor_b: float = 4):
    try:
        a = float(semi_major_a); b = float(semi_minor_b)
    except (TypeError, ValueError):
        return {"error": "Enter numbers for the two semi-axes."}
    if a <= 0 or b <= 0:
        return {"error": "Semi-axes must be greater than zero."}
    area = math.pi * a * b
    circ = math.pi * (3 * (a + b) - math.sqrt((3 * a + b) * (a + 3 * b)))
    steps = [
        {"label": "Area", "math": r"\(A = \pi a b = \pi \times " + ("%g" % a) + r" \times " + ("%g" % b) + r" = " + ("%.4g" % area) + r"\)", "note": "Exact, just like a circle but with two different radii."},
        {"label": "Circumference", "math": r"\(C \approx \pi\left[3(a+b) - \sqrt{(3a+b)(a+3b)}\right] = " + ("%.4g" % circ) + r"\)", "note": "Ellipse perimeter has no simple exact formula; Ramanujan's is extremely close."},
    ]
    return {
        "result": "Area " + ("%.4g" % area) + ", circumference \u2248 " + ("%.4g" % circ),
        "area": round(area, 6), "semi_major_a": a, "semi_minor_b": b, "circumference": round(circ, 6), "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
