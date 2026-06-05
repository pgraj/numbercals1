"""Heron's formula via the cosine rule — Non-Right-Angle Trigonometry (Stage 2).

This is the TRIGONOMETRIC route to a triangle's area, deliberately distinct from
the geometry calculator `geo-heron` (which simply applies the finished formula).
Here the area is built up through trigonometry:

    cosine rule  ->  cos C  ->  sin C (via sin²+cos²=1)  ->  Area = ½·a·b·sin C

and then shown to equal Heron's formula √(s(s−a)(s−b)(s−c)). The point for the
student is that Heron is not a magic result — it falls out of the cosine rule and
the half-ab-sin-C area formula once you simplify. (The angle C is only an
intermediate value here; the inputs are the three sides, so there is no deg/rad
input toggle on this calculator.)
"""
import math

from core.registry import register

DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or system "
    "errors. They are provided for general reference only — always verify results "
    "independently before relying on them for academic or professional decisions."
)


@register(
    slug="trig-heron",
    name="Heron's formula via the cosine rule",
    section="maths",
    sub="Non-Right-Angle Trigonometry",
    topic="Trigonometry",
    order=0,
    summary=(
        "Derive a triangle's area through trigonometry: use the cosine rule to find "
        "the included angle, then the area formula ½·a·b·sin C, and watch it simplify "
        "to Heron's formula — showing why the two routes give the same area."
    ),
    formula="Area = ½·a·b·sin C, with cos C = (a²+b²−c²)/(2ab) → Heron's √(s(s−a)(s−b)(s−c))",
    tags=[
        "cosine rule", "half ab sin c", "area of a triangle", "heron derivation",
        "included angle", "sine area formula", "non-right-angle",
        "CBSE Class 10", "GCSE Higher", "Singapore A-Math",
        "France Premiere", "ACARA Year 10", "UAE Grade 10",
    ],
    viz_template="viz/trig-heron.html",
    related=["trig-cosine-rule", "trig-sine-rule-area", "geo-heron"],
)
def compute(a=None, b=None, c=None):
    try:
        def num(x):
            if x is None or x == "":
                return None
            return float(x)

        a_, b_, c_ = num(a), num(b), num(c)
        if a_ is None or b_ is None or c_ is None:
            return _err("Enter all three side lengths.")
        if a_ <= 0 or b_ <= 0 or c_ <= 0:
            return _err("Side lengths must be greater than zero.")
        if a_ + b_ <= c_ or a_ + c_ <= b_ or b_ + c_ <= a_:
            return _err("Those side lengths cannot form a triangle (triangle inequality).")

        # C is the angle between sides a and b, opposite side c.
        cos_c = (a_ * a_ + b_ * b_ - c_ * c_) / (2 * a_ * b_)
        cos_c = max(-1.0, min(1.0, cos_c))   # guard rounding
        c_angle = math.degrees(math.acos(cos_c))
        sin_c = math.sqrt(max(0.0, 1 - cos_c * cos_c))
        area_trig = 0.5 * a_ * b_ * sin_c

        # Heron's, for the equivalence check.
        s = (a_ + b_ + c_) / 2
        area_heron = math.sqrt(s * (s - a_) * (s - b_) * (s - c_))

        steps = [
            {"label": "1 · Cosine rule for the included angle C",
             "math": r"\(\cos C = \dfrac{a^2+b^2-c^2}{2ab} = \dfrac{%s+%s-%s}{2\cdot%s\cdot%s} = %s\)"
                     % (_fmt(a_*a_), _fmt(b_*b_), _fmt(c_*c_), _fmt(a_), _fmt(b_), _fmt(cos_c)),
             "note": "C is the angle between sides a and b (opposite side c)."},
            {"label": "2 · The angle C",
             "math": r"\(C = \cos^{-1}(%s) \approx %s^\circ\)" % (_fmt(cos_c), _fmt(c_angle)),
             "note": "An intermediate value — we only need sin C next."},
            {"label": "3 · sin C from the Pythagorean identity",
             "math": r"\(\sin C = \sqrt{1-\cos^2 C} = \sqrt{1-(%s)^2} = %s\)"
                     % (_fmt(cos_c), _fmt(sin_c)),
             "note": "Using sin²C + cos²C = 1; C lies in (0°, 180°) so sin C ≥ 0."},
            {"label": "4 · Area from ½·a·b·sin C",
             "math": r"\(\text{Area} = \tfrac{1}{2}ab\sin C = \tfrac{1}{2}\cdot%s\cdot%s\cdot%s = %s\)"
                     % (_fmt(a_), _fmt(b_), _fmt(sin_c), _fmt(area_trig)),
             "note": "The standard area of any triangle from two sides and the angle between them."},
            {"label": "5 · The same area, via Heron's formula",
             "math": r"\(\sqrt{s(s-a)(s-b)(s-c)} = \sqrt{%s\cdot%s\cdot%s\cdot%s} = %s\)"
                     % (_fmt(s), _fmt(s - a_), _fmt(s - b_), _fmt(s - c_), _fmt(area_heron)),
             "note": "Heron's formula is what ½·a·b·sin C simplifies to once cos C is substituted — same number."},
        ]
        return {
            "result": _fmt(area_trig),
            "a": a_, "b": b_, "c": c_,
            "s": round(s, 6),
            "area": round(area_trig, 6),
            "cos_c": round(cos_c, 6),
            "angle_c": round(c_angle, 4),
            "sin_c": round(sin_c, 6),
            "area_heron": round(area_heron, 6),
            "steps": steps,
            "explanation": [
                {"heading": "Why this lives in trigonometry",
                 "body": "Unlike the geometry version, which just applies the finished "
                         "formula, this calculator derives the area the trigonometric "
                         "way: the cosine rule gives the included angle, and ½·a·b·sin C "
                         "gives the area. Heron's formula is simply what that expression "
                         "becomes after you substitute cos C and simplify — so the two "
                         "routes always agree."},
                {"heading": "From cos C to the area",
                 "body": "The cosine rule fixes cos C from the three sides. The "
                         "identity sin²C + cos²C = 1 then gives sin C, and the area "
                         "formula ½·a·b·sin C finishes the job — no height or "
                         "right angle needed anywhere."},
                {"heading": "The link to Heron",
                 "body": "If you carry the algebra through symbolically rather than "
                         "with numbers, ½·a·b·sin C collapses exactly to "
                         "√(s(s−a)(s−b)(s−c)). That is Heron's formula, recovered from "
                         "pure trigonometry."},
            ],
            "disclaimer": DISCLAIMER,
        }
    except (TypeError, ValueError):
        return _err("Please enter valid numbers for the sides.")


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
