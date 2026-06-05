"""Sine rule — Non-Right-Angle Trigonometry cluster (Stage 2).

a/sin A = b/sin B = c/sin C. Two modes:
  - find a side:  given one side, its opposite angle, and another opposite angle
  - find an angle: given two sides and one of their opposite angles

Accepts `angle_unit` ("deg"|"rad"): all angle INPUTS (the opposite angles) are
read in that unit, the computed angle (angle mode) is displayed in it, and every
step renders angles to match the toggle.
"""
import math

from core.registry import register

DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or system "
    "errors. They are provided for general reference only — always verify results "
    "independently before relying on them for academic or professional decisions."
)


@register(
    slug="trig-sine-rule",
    name="Sine rule",
    section="maths",
    sub="Non-Right-Angle Trigonometry",
    topic="Trigonometry",
    order=0,
    summary=(
        "Use the sine rule a over sin A equals b over sin B to find a missing side "
        "or angle in any triangle when you have a matching side and opposite "
        "angle, in degrees or radians, with a triangle diagram showing the equal "
        "ratios."
    ),
    formula="a / sin A = b / sin B = c / sin C",
    tags=[
        "sine rule", "law of sines", "non-right triangle", "oblique triangle",
        "trigonometry", "CBSE Class 11", "GCSE Higher", "Common Core HSG-SRT.D",
        "Singapore E-Math", "France Premiere", "Germany Klasse 10",
        "ACARA Year 10", "UAE Grade 10",
    ],
    viz_template="viz/trig-sine-rule.html",
)
def compute(mode="side", known_side=None, known_angle=None,
            other_angle=None, other_side=None, angle_unit="deg"):
    try:
        mode = (mode or "side").lower()
        unit = "rad" if str(angle_unit) == "rad" else "deg"

        def num(x):
            if x is None or x == "":
                return None
            return float(x)

        def to_deg(v):
            return v if unit == "deg" else math.degrees(v)

        if mode == "side":
            a = num(known_side)
            A_in = num(known_angle)
            B_in = num(other_angle)
            if a is None or A_in is None or B_in is None:
                return _err("Enter a side, its opposite angle, and the angle opposite the side you want.")
            A, B = to_deg(A_in), to_deg(B_in)
            if not (0 < A < 180) or not (0 < B < 180):
                lim = "0° and 180°" if unit == "deg" else "0 and π rad"
                return _err("Angles must be between %s." % lim)
            if a <= 0:
                return _err("The side length must be greater than zero.")
            if A + B >= 180:
                return _err("The two angles must total less than 180°.")
            b = a * math.sin(math.radians(B)) / math.sin(math.radians(A))
            steps = [
                {"label": "Write the sine rule",
                 "math": r"\(\dfrac{a}{\sin A} = \dfrac{b}{\sin B}\)",
                 "note": "Each side divided by the sine of its opposite angle is equal."},
                {"label": "Rearrange for the unknown side",
                 "math": r"\(b = \dfrac{a\,\sin B}{\sin A} = \dfrac{%s\,\sin %s}{\sin %s}\)"
                         % (_fmt(a), _ang(B, unit), _ang(A, unit)),
                 "note": "a = %s opposite A = %s; we want b opposite B = %s." % (_fmt(a), _ang(A, unit), _ang(B, unit))},
                {"label": "Evaluate",
                 "math": r"\(b = %s\)" % _fmt(b),
                 "note": "The side opposite the larger angle is the longer side."},
            ]
            return {
                "result": _fmt(b), "mode": "side", "value": round(b, 6),
                "a": a, "A": A, "B": B, "b": round(b, 6), "angle_unit": unit,
                "steps": steps, "explanation": _expl(), "disclaimer": DISCLAIMER,
            }

        elif mode == "angle":
            a = num(known_side)
            A_in = num(known_angle)
            b = num(other_side)
            if a is None or A_in is None or b is None:
                return _err("Enter two sides and the angle opposite one of them.")
            A = to_deg(A_in)
            if not (0 < A < 180):
                lim = "0° and 180°" if unit == "deg" else "0 and π rad"
                return _err("The angle must be between %s." % lim)
            if a <= 0 or b <= 0:
                return _err("Side lengths must be greater than zero.")
            ratio = b * math.sin(math.radians(A)) / a
            if ratio > 1:
                return _err("No triangle exists with those measurements (sine ratio exceeds 1).")
            B = math.degrees(math.asin(ratio))
            steps = [
                {"label": "Write the sine rule",
                 "math": r"\(\dfrac{a}{\sin A} = \dfrac{b}{\sin B}\)",
                 "note": "Rearranged here to solve for the unknown angle B."},
                {"label": "Make sin B the subject",
                 "math": r"\(\sin B = \dfrac{b\,\sin A}{a} = \dfrac{%s\,\sin %s}{%s}\)"
                         % (_fmt(b), _ang(A, unit), _fmt(a)),
                 "note": "Then take the inverse sine."},
                {"label": "Evaluate the angle",
                 "math": r"\(B = \sin^{-1}(%s) \approx %s\)" % (_fmt(ratio), _ang(B, unit)),
                 "note": "Watch for the ambiguous (SSA) case — a second obtuse angle 180°−B may also fit."},
            ]
            return {
                "result": _disp(B, unit), "mode": "angle", "value": round(B, 6),
                "a": a, "A": A, "b": b, "B": round(B, 6), "angle_unit": unit,
                "alt_angle": round(180 - B, 6),
                "steps": steps, "explanation": _expl(), "disclaimer": DISCLAIMER,
            }
        else:
            return _err("Choose a mode: side or angle.")
    except (TypeError, ValueError):
        return _err("Please enter valid numbers.")


def _ang(deg, unit):
    if unit == "rad":
        return _fmt(math.radians(deg)) + r"\,\text{rad}"
    return _fmt(deg) + r"^\circ"


def _disp(deg, unit):
    if unit == "rad":
        return _fmt(math.radians(deg)) + " rad"
    return _fmt(deg) + "\u00b0"


def _expl():
    return [
        {"heading": "When to use the sine rule",
         "body": "Use it whenever you have a side paired with its opposite angle, "
                 "plus one more side or angle. It works for any triangle, not just "
                 "right-angled ones, making it the first tool for oblique triangles."},
        {"heading": "Side opposite angle",
         "body": "The rule pairs each side with the angle directly across from it. "
                 "Label carefully: side a sits opposite angle A. The largest angle "
                 "always faces the longest side."},
    ]


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
