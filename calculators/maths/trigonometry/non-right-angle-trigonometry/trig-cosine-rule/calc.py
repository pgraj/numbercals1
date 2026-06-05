"""Cosine rule — Non-Right-Angle Trigonometry cluster (Stage 2).

c² = a² + b² − 2ab·cos C. Two modes:
  - find a side: given two sides and the included angle (SAS)
  - find an angle: given all three sides (SSS)
"""
import math

from core.registry import register

DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or system "
    "errors. They are provided for general reference only — always verify results "
    "independently before relying on them for academic or professional decisions."
)


@register(
    slug="trig-cosine-rule",
    name="Cosine rule",
    section="maths",
    sub="Non-Right-Angle Trigonometry",
    topic="Trigonometry",
    order=0,
    summary=(
        "Use the cosine rule c squared equals a squared plus b squared minus 2ab "
        "cos C to find a third side from two sides and the included angle, or any "
        "angle from all three sides, with a triangle whose angle links back to "
        "Pythagoras at ninety degrees."
    ),
    formula="c² = a² + b² − 2ab·cos C",
    tags=[
        "cosine rule", "law of cosines", "non-right triangle", "SAS", "SSS",
        "trigonometry", "CBSE Class 11", "GCSE Higher", "Common Core HSG-SRT.D",
        "Singapore E-Math", "France Premiere", "Germany Klasse 10",
        "ACARA Year 10", "UAE Grade 10",
    ],
    viz_template="viz/trig-cosine-rule.html",
)
def compute(mode="side", a=None, b=None, angle_C=None, c=None):
    try:
        mode = (mode or "side").lower()

        def num(x):
            if x is None or x == "":
                return None
            return float(x)

        a_, b_, C_, c_ = num(a), num(b), num(angle_C), num(c)

        if mode == "side":
            if a_ is None or b_ is None or C_ is None:
                return _err("Enter two sides and the included angle C.")
            if a_ <= 0 or b_ <= 0:
                return _err("Side lengths must be greater than zero.")
            if not (0 < C_ < 180):
                return _err("The included angle must be between 0° and 180°.")
            c_val = math.sqrt(a_ * a_ + b_ * b_ - 2 * a_ * b_ * math.cos(math.radians(C_)))
            steps = [
                {"label": "Write the cosine rule",
                 "math": r"\(c^2 = a^2 + b^2 - 2ab\cos C\)",
                 "note": "Use it when you know two sides and the angle between them (SAS)."},
                {"label": "Substitute",
                 "math": r"\(c^2 = %s^2 + %s^2 - 2(%s)(%s)\cos %s^\circ\)"
                         % (_fmt(a_), _fmt(b_), _fmt(a_), _fmt(b_), _fmt(C_)),
                 "note": "a = %s, b = %s, included angle C = %s°." % (_fmt(a_), _fmt(b_), _fmt(C_))},
                {"label": "Take the square root",
                 "math": r"\(c = %s\)" % _fmt(c_val),
                 "note": "If C = 90°, the cosine term vanishes and this becomes Pythagoras."},
            ]
            return {
                "result": _fmt(c_val), "mode": "side", "value": round(c_val, 6),
                "a": a_, "b": b_, "angle_C": C_, "c": round(c_val, 6),
                "steps": steps, "explanation": _expl(), "disclaimer": DISCLAIMER,
            }

        elif mode == "angle":
            if a_ is None or b_ is None or c_ is None:
                return _err("Enter all three sides to find an angle.")
            if a_ <= 0 or b_ <= 0 or c_ <= 0:
                return _err("Side lengths must be greater than zero.")
            # triangle inequality
            if a_ + b_ <= c_ or a_ + c_ <= b_ or b_ + c_ <= a_:
                return _err("Those side lengths cannot form a triangle.")
            cosC = (a_ * a_ + b_ * b_ - c_ * c_) / (2 * a_ * b_)
            cosC = max(-1.0, min(1.0, cosC))
            C_val = math.degrees(math.acos(cosC))
            steps = [
                {"label": "Rearrange for the angle",
                 "math": r"\(\cos C = \dfrac{a^2 + b^2 - c^2}{2ab}\)",
                 "note": "C is the angle opposite side c. Use it when you know all three sides (SSS)."},
                {"label": "Substitute",
                 "math": r"\(\cos C = \dfrac{%s^2 + %s^2 - %s^2}{2(%s)(%s)} = %s\)"
                         % (_fmt(a_), _fmt(b_), _fmt(c_), _fmt(a_), _fmt(b_), _fmt(cosC)),
                 "note": "Then take the inverse cosine."},
                {"label": "Evaluate",
                 "math": r"\(C = \cos^{-1}(%s) \approx %s^\circ\)" % (_fmt(cosC), _fmt(C_val)),
                 "note": "The inverse cosine handles obtuse angles directly, with no ambiguity."},
            ]
            return {
                "result": _fmt(C_val) + "\u00b0", "mode": "angle", "value": round(C_val, 6),
                "a": a_, "b": b_, "c": c_, "angle_C": round(C_val, 6),
                "steps": steps, "explanation": _expl(), "disclaimer": DISCLAIMER,
            }
        else:
            return _err("Choose a mode: side or angle.")
    except (TypeError, ValueError):
        return _err("Please enter valid numbers.")


def _expl():
    return [
        {"heading": "When the sine rule won't do",
         "body": "The cosine rule covers the two cases the sine rule cannot start "
                 "with: two sides and the included angle (SAS) to find the third "
                 "side, and all three sides (SSS) to find any angle."},
        {"heading": "It contains Pythagoras",
         "body": "When the angle C is 90°, cos C is zero and the formula collapses "
                 "to c² = a² + b² — Pythagoras' theorem. The cosine rule is the "
                 "general version that works for every angle."},
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
