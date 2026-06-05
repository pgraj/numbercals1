"""Area with the sine rule (½ab·sin C) — Non-Right-Angle Trigonometry cluster.

The companion area formula to the sine and cosine rules: once a triangle is
solved, its area is ½·a·b·sin C from two sides and their included angle. Accepts
`angle_unit` ("deg"|"rad") so the included angle C is read, and every step shown,
in the unit the student selects via the shared toggle.
"""
import math

from core.registry import register

DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or system "
    "errors. They are provided for general reference only — always verify results "
    "independently before relying on them for academic or professional decisions."
)


@register(
    slug="trig-sine-rule-area",
    name="Area of any triangle (½·a·b·sin C)",
    section="maths",
    sub="Non-Right-Angle Trigonometry",
    topic="Trigonometry",
    order=0,
    summary=(
        "Find the area of any triangle from two sides and their included angle "
        "using one half a b sine C — the area companion to the sine and cosine "
        "rules — in degrees or radians, with the triangle drawn in the standard a, "
        "b, c labelling and the area shaded."
    ),
    formula="Area = ½·a·b·sin C  (a, b sides; C the angle between them)",
    tags=[
        "area of triangle", "half ab sin C", "sine rule area", "included angle",
        "oblique triangle", "trigonometry", "CBSE Class 11", "GCSE Higher",
        "Common Core HSG-SRT.D.9", "Singapore E-Math", "France Premiere",
        "Germany Klasse 10", "ACARA Year 10", "UAE Grade 10",
    ],
    viz_template="viz/trig-sine-rule-area.html",
)
def compute(a=None, b=None, angle_C=None, angle_unit="deg"):
    try:
        unit = "rad" if str(angle_unit) == "rad" else "deg"

        def num(x):
            if x is None or x == "":
                return None
            return float(x)

        a_, b_, C_in = num(a), num(b), num(angle_C)
        if a_ is None or b_ is None or C_in is None:
            return _err("Enter sides a and b and the included angle C.")
        if a_ <= 0 or b_ <= 0:
            return _err("Side lengths must be greater than zero.")
        C_deg = C_in if unit == "deg" else math.degrees(C_in)
        if not (0 < C_deg < 180):
            lim = "0 and 180°" if unit == "deg" else "0 and π rad"
            return _err("The included angle must be between %s." % lim)

        area = 0.5 * a_ * b_ * math.sin(math.radians(C_deg))
        c_ = math.sqrt(a_ * a_ + b_ * b_ - 2 * a_ * b_ * math.cos(math.radians(C_deg)))
        Cdisp = _ang(C_deg, unit)

        steps = [
            {"label": "Write the area formula",
             "math": r"\(\text{Area} = \tfrac{1}{2}\,a\,b\,\sin C\)",
             "note": "Here a and b are two sides and C is the angle enclosed between them."},
            {"label": "Substitute",
             "math": r"\(\text{Area} = \tfrac{1}{2}(%s)(%s)\sin %s\)"
                     % (_fmt(a_), _fmt(b_), Cdisp),
             "note": "a = %s, b = %s, included angle C = %s." % (_fmt(a_), _fmt(b_), Cdisp)},
            {"label": "Evaluate",
             "math": r"\(\text{Area} = %s\)" % _fmt(area),
             "note": "Units are the side units squared."},
            {"label": "Third side (cosine rule link)",
             "math": r"\(c = \sqrt{a^2+b^2-2ab\cos C} = %s\)" % _fmt(c_),
             "note": "Once you have the area you often want the opposite side too."},
        ]
        return {
            "result": _fmt(area),
            "a": a_, "b": b_, "angle_C": C_deg, "angle_unit": unit,
            "angle_C_display": Cdisp, "area": round(area, 6), "c": round(c_, 6),
            "steps": steps,
            "explanation": [
                {"heading": "The area tool of the toolkit",
                 "body": "Alongside the sine and cosine rules for sides and angles, "
                         "½·a·b·sin C completes the set for oblique triangles: it "
                         "gives the area directly from two sides and the angle "
                         "between them, with no need for the perpendicular height."},
                {"heading": "Choosing the right pair",
                 "body": "The angle must be the one enclosed by the two sides you "
                         "use. With the standard labelling, sides a and b enclose "
                         "angle C, sides b and c enclose A, and sides a and c "
                         "enclose B — pick whichever pair you know."},
            ],
            "disclaimer": DISCLAIMER,
        }
    except (TypeError, ValueError):
        return _err("Please enter valid numbers.")


def _ang(deg, unit):
    if unit == "rad":
        return _fmt(math.radians(deg)) + r"\,\text{rad}"
    return _fmt(deg) + r"^\circ"


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
