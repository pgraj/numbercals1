"""Concrete volume — engineering > Civil. Volume + bags estimate for slabs/footings/columns.
Quantity estimation only, NOT structural design."""
from core.registry import register
import math

@register(
    slug="concrete-volume",
    name="Concrete Volume Calculator",
    section="engineering",
    sub="Civil",
    tags=["concrete", "volume", "slab", "footing", "column", "civil", "estimation"],
    formula="rectangular: L\u00d7W\u00d7D ; column: \u03c0r\u00b2\u00d7H ; + wastage allowance",
    summary="Estimate the concrete volume needed for a slab, footing or column, with a wastage allowance and a rough bag count. For quantity estimation only \u2014 not structural design.",
    viz_template="viz/concrete-volume.html",
)
def compute(shape: str = "rectangular", length: float = 4, width: float = 3,
            depth: float = 0.15, diameter: float = 0.3, height: float = 3,
            wastage_percent: float = 5, bag_yield_m3: float = 0.0166):
    sh = str(shape or "rectangular").strip().lower()
    try:
        waste = float(wastage_percent); bag = float(bag_yield_m3)
    except (TypeError, ValueError):
        return {"error": "Enter numbers only."}
    if waste < 0:
        return {"error": "Wastage percent cannot be negative."}
    if bag <= 0:
        return {"error": "Bag yield must be greater than zero."}
    if sh in ("column", "circular", "cylinder"):
        try:
            d = float(diameter); H = float(height)
        except (TypeError, ValueError):
            return {"error": "Enter numbers for diameter and height."}
        if d <= 0 or H <= 0:
            return {"error": "Diameter and height must be greater than zero."}
        base = math.pi * (d / 2) ** 2 * H
        shape_note = "Circular column: \u03c0r\u00b2 \u00d7 height."
        dims = r"\(\pi (" + ("%g/2" % d) + r")^2 \times " + ("%g" % H) + r"\)"
    else:
        try:
            L = float(length); W = float(width); D = float(depth)
        except (TypeError, ValueError):
            return {"error": "Enter numbers for length, width and depth."}
        if L <= 0 or W <= 0 or D <= 0:
            return {"error": "Length, width and depth must be greater than zero."}
        base = L * W * D
        shape_note = "Rectangular slab/footing: length \u00d7 width \u00d7 depth."
        dims = r"\(" + ("%g \\times %g \\times %g" % (L, W, D)) + r"\)"
    with_waste = base * (1 + waste / 100.0)
    bags = with_waste / bag
    steps = [
        {"label": "Net volume", "math": dims + r"\(= " + ("%.4g" % base) + r"\,\text{m}^3\)", "note": shape_note},
        {"label": "Add wastage", "math": r"\(" + ("%.4g" % base) + r" \times (1 + " + ("%g" % waste) + r"\%) = " + ("%.4g" % with_waste) + r"\,\text{m}^3\)", "note": "Allows for spillage and over-excavation."},
        {"label": "Bags (approx)", "math": r"\(" + ("%.4g" % with_waste) + r" / " + ("%g" % bag) + r" \approx " + ("%.0f" % math.ceil(bags)) + r"\)", "note": "Using ~" + ("%g" % bag) + " m\u00b3 per bag; check your bag's actual yield."},
    ]
    return {
        "result": ("\u2248 " + ("%.3f" % with_waste) + " m\u00b3 of concrete (incl. " + ("%g" % waste)
                   + "% wastage); about " + ("%.0f" % math.ceil(bags)) + " bags"),
        "net_volume_m3": round(base, 4), "volume_with_wastage_m3": round(with_waste, 4),
        "bags_estimate": int(math.ceil(bags)),
        "disclaimer": "Quantity estimation only \u2014 not a structural design. Confirm mix, cover and quantities with an engineer.",
        "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
