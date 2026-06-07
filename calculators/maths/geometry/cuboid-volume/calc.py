"""Cuboid — geometry > 3D Geometry. Volume, surface area and space diagonal of a rectangular box."""
from core.registry import register
import math

@register(
    slug="cuboid-volume",
    name="Cuboid Volume Calculator",
    section="maths",
    sub="3D Solids",
    topic="Geometry",
    tags=["cuboid", "box", "volume", "surface area", "diagonal", "geometry"],
    formula="volume = l\u00d7w\u00d7h ; surface area = 2(lw+lh+wh) ; diagonal = \u221a(l\u00b2+w\u00b2+h\u00b2)",
    summary="Find the volume, surface area and space diagonal of a cuboid (rectangular box) from its length, width and height.",
    viz_template="viz/cuboid-volume.html",
)
def compute(length: float = 6, width: float = 4, height: float = 3):
    try:
        l = float(length); w = float(width); h = float(height)
    except (TypeError, ValueError):
        return {"error": "Enter numbers for length, width and height."}
    if l <= 0 or w <= 0 or h <= 0:
        return {"error": "All dimensions must be greater than zero."}
    vol = l * w * h
    sa = 2 * (l * w + l * h + w * h)
    diag = math.sqrt(l * l + w * w + h * h)
    steps = [
        {"label": "Volume", "math": r"\(V = l w h = " + ("%g \\times %g \\times %g" % (l, w, h)) + r" = " + ("%g" % vol) + r"\)", "note": "Length times width times height."},
        {"label": "Surface area", "math": r"\(A = 2(lw + lh + wh) = " + ("%g" % sa) + r"\)", "note": "Three pairs of matching faces."},
        {"label": "Space diagonal", "math": r"\(d = \sqrt{l^2+w^2+h^2} = " + ("%.4g" % diag) + r"\)", "note": "The longest straight line inside the box."},
    ]
    return {
        "result": "Volume " + ("%g" % vol) + ", surface area " + ("%g" % sa) + ", space diagonal " + ("%.4g" % diag),
        "volume": round(vol, 6), "length": l, "width": w, "height": h, "surface_area": round(sa, 6), "space_diagonal": round(diag, 6), "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
