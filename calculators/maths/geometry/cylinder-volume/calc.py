"""Cylinder — geometry > 3D Geometry. Volume, total surface area and lateral surface area."""
from core.registry import register
import math

@register(
    slug="cylinder-volume",
    name="Cylinder Volume Calculator",
    section="maths",
    sub="3D Solids",
    topic="Geometry",
    tags=["cylinder", "volume", "surface area", "lateral", "radius", "geometry"],
    formula="volume = \u03c0r\u00b2h ; lateral = 2\u03c0rh ; total = 2\u03c0r(r+h)",
    summary="Find a cylinder's volume, total surface area and lateral (curved side) surface area from its radius and height.",
    viz_template="viz/cylinder-volume.html",
)
def compute(radius: float = 3, height: float = 7):
    try:
        r = float(radius); h = float(height)
    except (TypeError, ValueError):
        return {"error": "Enter numbers for radius and height."}
    if r <= 0 or h <= 0:
        return {"error": "Radius and height must be greater than zero."}
    vol = math.pi * r * r * h
    lateral = 2 * math.pi * r * h
    total = 2 * math.pi * r * (r + h)
    steps = [
        {"label": "Volume", "math": r"\(V = \pi r^2 h = \pi \times " + ("%g" % r) + r"^2 \times " + ("%g" % h) + r" = " + ("%.4g" % vol) + r"\)", "note": "Base circle area times height."},
        {"label": "Lateral surface", "math": r"\(A_{side} = 2\pi r h = " + ("%.4g" % lateral) + r"\)", "note": "The curved wall, unrolled into a rectangle."},
        {"label": "Total surface", "math": r"\(A = 2\pi r(r + h) = " + ("%.4g" % total) + r"\)", "note": "Curved side plus the two circular ends."},
    ]
    return {
        "result": "Volume " + ("%.4g" % vol) + ", total SA " + ("%.4g" % total) + ", lateral SA " + ("%.4g" % lateral),
        "volume": round(vol, 6), "radius": r, "height": h, "surface_area": round(total, 6), "lateral_surface_area": round(lateral, 6),
        "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
