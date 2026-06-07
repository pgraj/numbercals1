"""Torus — geometry > 3D Geometry. Volume and surface area of a doughnut shape."""
from core.registry import register
import math

@register(
    slug="torus-volume",
    name="Torus Volume Calculator",
    section="maths",
    sub="3D Solids",
    topic="Geometry",
    tags=["torus", "doughnut", "volume", "surface area", "geometry"],
    formula="volume = 2\u03c0\u00b2 R r\u00b2 ; surface area = 4\u03c0\u00b2 R r",
    summary="Find the volume and surface area of a torus (doughnut) from R, the distance from the centre to the tube centre, and r, the tube radius.",
    viz_template="viz/torus-volume.html",
)
def compute(major_radius_R: float = 5, tube_radius_r: float = 2):
    try:
        R = float(major_radius_R); r = float(tube_radius_r)
    except (TypeError, ValueError):
        return {"error": "Enter numbers for the major and tube radii."}
    if R <= 0 or r <= 0:
        return {"error": "Both radii must be greater than zero."}
    if r >= R:
        return {"error": "Tube radius r must be smaller than major radius R for a ring torus."}
    vol = 2 * math.pi ** 2 * R * r * r
    sa = 4 * math.pi ** 2 * R * r
    steps = [
        {"label": "Volume", "math": r"\(V = 2\pi^2 R r^2 = 2\pi^2 \times " + ("%g" % R) + r" \times " + ("%g" % r) + r"^2 = " + ("%.4g" % vol) + r"\)", "note": "Like a cylinder of length 2\u03c0R bent into a ring."},
        {"label": "Surface area", "math": r"\(A = 4\pi^2 R r = " + ("%.4g" % sa) + r"\)", "note": "The full outer skin of the doughnut."},
    ]
    return {
        "result": "Volume " + ("%.4g" % vol) + ", surface area " + ("%.4g" % sa),
        "volume": round(vol, 6), "surface_area": round(sa, 6), "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
