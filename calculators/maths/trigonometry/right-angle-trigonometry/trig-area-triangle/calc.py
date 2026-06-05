"""Area of a triangle (½·a·b·sinC) — Right-Angle Trigonometry cluster.

Find the area of any triangle from two sides and their included angle, using
Area = ½ · a · b · sin C. (Common Core lists this as HSG-SRT.D.9.)
"""
import math

from core.registry import register

DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or system "
    "errors. They are provided for general reference only — always verify results "
    "independently before relying on them for academic or professional decisions."
)


@register(
    slug="trig-area-triangle",
    name="Area of a triangle (½·a·b·sinC)",
    section="maths",
    sub="Right-Angle Trigonometry",
    topic="Trigonometry",
    order=0,
    summary=(
        "Find the area of any triangle from two sides and the angle between them "
        "with the formula one half a b sine C, useful when you do not know the "
        "perpendicular height, shown with the triangle shaded by its area."
    ),
    formula="Area = ½ · a · b · sin C",
    tags=[
        "area of triangle", "sine rule for area", "included angle",
        "half ab sin C", "trigonometry", "CBSE Class 10", "GCSE",
        "Common Core HSG-SRT.D.9", "Singapore Sec 3", "France 1re",
        "Germany Klasse 10", "ACARA Year 10", "NSW Stage 5", "UAE Grade 10",
    ],
    viz_template="viz/trig-area-triangle.html",
)
def compute(a=None, b=None, angle_C=None):
    try:
        def num(x):
            if x is None or x == "":
                return None
            return float(x)

        a, b, C = num(a), num(b), num(angle_C)
        if a is None or b is None or C is None:
            return _err("Enter two sides a and b and the included angle C.")
        if a <= 0 or b <= 0:
            return _err("Side lengths must be greater than zero.")
        if not (0 < C < 180):
            return _err("The included angle must be between 0° and 180°.")

        area = 0.5 * a * b * math.sin(math.radians(C))
        steps = [
            {"label": "Write the formula",
             "math": r"\(\text{Area} = \tfrac{1}{2}\,a\,b\,\sin C\)",
             "note": "C is the angle between the two given sides a and b."},
            {"label": "Substitute the values",
             "math": r"\(\text{Area} = \tfrac{1}{2}\times %s \times %s \times \sin %s^\circ\)"
                     % (_fmt(a), _fmt(b), _fmt(C)),
             "note": "a = %s, b = %s, included angle C = %s°." % (_fmt(a), _fmt(b), _fmt(C))},
            {"label": "Evaluate",
             "math": r"\(\text{Area} = %s\)" % _fmt(area),
             "note": "Units are the side units squared."},
        ]
        return {
            "result": _fmt(area),
            "a": a, "b": b, "angle_C": C, "area": round(area, 6),
            "steps": steps,
            "explanation": [
                {"heading": "Why this beats ½·base·height",
                 "body": "The familiar ½ × base × height needs the perpendicular "
                         "height. When you instead know two sides and the angle "
                         "between them, ½·a·b·sin C gives the area directly — no "
                         "height required."},
                {"heading": "The included angle matters",
                 "body": "C must be the angle enclosed by sides a and b. Using a "
                         "different angle gives the wrong area, because sin C captures "
                         "exactly how 'open' the two sides are."},
            ],
            "disclaimer": DISCLAIMER,
        }
    except (TypeError, ValueError):
        return _err("Please enter valid numbers.")


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
