"""Brick quantity — engineering > Civil. Bricks for a wall incl. mortar joint and wastage."""
from core.registry import register
import math

@register(
    slug="brick-quantity",
    name="Brick Quantity Calculator",
    section="engineering",
    sub="Civil",
    tags=["brick", "wall", "quantity", "mortar", "wastage", "civil", "estimation"],
    formula="bricks = wall area / (brick face area incl. mortar joint) \u00d7 (1 + wastage)",
    summary="Estimate how many bricks a wall needs, allowing for the mortar joint around each brick and a wastage percentage. For estimation only.",
    viz_template="viz/brick-quantity.html",
)
def compute(wall_length_m: float = 5, wall_height_m: float = 2.5,
            brick_length_mm: float = 230, brick_height_mm: float = 76,
            mortar_joint_mm: float = 10, wastage_percent: float = 5):
    try:
        L = float(wall_length_m); H = float(wall_height_m)
        bl = float(brick_length_mm); bh = float(brick_height_mm)
        joint = float(mortar_joint_mm); waste = float(wastage_percent)
    except (TypeError, ValueError):
        return {"error": "Enter numbers only."}
    if L <= 0 or H <= 0:
        return {"error": "Wall length and height must be greater than zero."}
    if bl <= 0 or bh <= 0:
        return {"error": "Brick dimensions must be greater than zero."}
    if joint < 0 or waste < 0:
        return {"error": "Joint and wastage cannot be negative."}
    wall_area = L * H                                  # m^2
    # effective brick face incl. one mortar joint on length and height, in metres
    eff_l = (bl + joint) / 1000.0
    eff_h = (bh + joint) / 1000.0
    brick_face = eff_l * eff_h                         # m^2 per brick (single skin)
    if brick_face <= 0:
        return {"error": "Brick face area came out non-positive \u2014 check inputs."}
    raw = wall_area / brick_face
    with_waste = raw * (1 + waste / 100.0)
    bricks = int(math.ceil(with_waste))
    steps = [
        {"label": "Wall area", "math": r"\(" + ("%g \\times %g = %.3g" % (L, H, wall_area)) + r"\,\text{m}^2\)", "note": "Single-skin wall face."},
        {"label": "Brick + joint", "math": r"\((" + ("%g+%g" % (bl, joint)) + r")\times(" + ("%g+%g" % (bh, joint)) + r")\,\text{mm} = " + ("%.4g" % (brick_face * 1e4)) + r"\,\text{cm}^2\)", "note": "Each brick 'claims' half a joint on every side."},
        {"label": "Bricks + wastage", "math": r"\(" + ("%.0f" % raw) + r" \times (1+" + ("%g" % waste) + r"\%) \approx " + str(bricks) + r"\)", "note": "Rounded up; single-skin wall."},
    ]
    return {
        "result": ("\u2248 " + str(bricks) + " bricks for a " + ("%g" % L) + " \u00d7 " + ("%g" % H)
                   + " m single-skin wall (incl. " + ("%g" % waste) + "% wastage)"),
        "wall_area_m2": round(wall_area, 3), "bricks_before_wastage": int(math.ceil(raw)),
        "bricks_estimate": bricks,
        "disclaimer": "Estimation only, for a single-skin wall. Double-skin or different bonds change the count; confirm with your supplier.",
        "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
