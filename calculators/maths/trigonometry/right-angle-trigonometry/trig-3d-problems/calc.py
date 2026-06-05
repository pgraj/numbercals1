"""3D trigonometry — Right-Angle Trigonometry cluster.

Work through a cuboid in two right-angled steps: the base diagonal by Pythagoras,
then the space diagonal, and the angle the space diagonal makes with the base.
"""
import math

from core.registry import register

DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or system "
    "errors. They are provided for general reference only — always verify results "
    "independently before relying on them for academic or professional decisions."
)


@register(
    slug="trig-3d-problems",
    name="3D trigonometry",
    section="maths",
    sub="Right-Angle Trigonometry",
    topic="Trigonometry",
    order=0,
    summary=(
        "Solve three-dimensional problems on a cuboid step by step: find the base "
        "diagonal, then the space diagonal, then the angle it makes with the base, "
        "with a wireframe box that highlights each right-angled triangle in turn."
    ),
    formula="diagonal = √(l² + w² + h²) · angle = tan⁻¹(h / √(l²+w²))",
    tags=[
        "3d trigonometry", "space diagonal", "cuboid", "pythagoras in 3d",
        "angle to base", "trigonometry", "CBSE Class 10", "GCSE Higher",
        "Common Core HSG-SRT", "Singapore Sec 4", "Germany Klasse 10",
        "ACARA Year 10", "NSW Stage 5.3", "UAE Grade 10",
    ],
    viz_template="viz/trig-3d-problems.html",
)
def compute(length=None, width=None, height=None):
    try:
        def num(x):
            if x is None or x == "":
                return None
            return float(x)

        l, w, h = num(length), num(width), num(height)
        if l is None or w is None or h is None:
            return _err("Enter the length, width, and height of the cuboid.")
        if l <= 0 or w <= 0 or h <= 0:
            return _err("All three dimensions must be greater than zero.")

        base_diag = math.hypot(l, w)
        space_diag = math.sqrt(l * l + w * w + h * h)
        angle = math.degrees(math.atan2(h, base_diag))

        steps = [
            {"label": "Step 1 — base diagonal (Pythagoras)",
             "math": r"\(d_{\text{base}} = \sqrt{l^2 + w^2} = \sqrt{%s^2 + %s^2} = %s\)"
                     % (_fmt(l), _fmt(w), _fmt(base_diag)),
             "note": "First solve the right triangle lying flat on the base."},
            {"label": "Step 2 — space diagonal",
             "math": r"\(d = \sqrt{d_{\text{base}}^2 + h^2} = \sqrt{%s^2 + %s^2} = %s\)"
                     % (_fmt(base_diag), _fmt(h), _fmt(space_diag)),
             "note": "Now stand a second right triangle up using the base diagonal and the height."},
            {"label": "Step 3 — angle to the base",
             "math": r"\(\theta = \tan^{-1}\!\left(\dfrac{h}{d_{\text{base}}}\right) = \tan^{-1}\!\left(\dfrac{%s}{%s}\right) \approx %s^\circ\)"
                     % (_fmt(h), _fmt(base_diag), _fmt(angle)),
             "note": "The space diagonal rises from the base by this angle."},
        ]
        return {
            "result": _fmt(space_diag),
            "length": l, "width": w, "height": h,
            "base_diag": round(base_diag, 6),
            "space_diag": round(space_diag, 6),
            "angle": round(angle, 4),
            "steps": steps,
            "explanation": [
                {"heading": "Break 3D into two flat triangles",
                 "body": "Every cuboid diagonal problem reduces to two right-angled "
                         "triangles: one lying on the base to get the base diagonal, "
                         "then one standing upright that uses the base diagonal and "
                         "the height."},
                {"heading": "The combined formula",
                 "body": "Chaining the two Pythagoras steps gives the neat result that "
                         "the space diagonal equals the square root of l² + w² + h². "
                         "The angle to the base then comes from inverse tangent."},
            ],
            "disclaimer": DISCLAIMER,
        }
    except (TypeError, ValueError):
        return _err("Please enter valid numbers for the dimensions.")


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
