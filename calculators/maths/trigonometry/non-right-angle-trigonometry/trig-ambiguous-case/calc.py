"""Ambiguous case (SSA) — Non-Right-Angle Trigonometry cluster (Stage 2).

Given two sides and a non-included angle (SSA), determine whether 0, 1, or 2
triangles are possible, and give the angle(s). Accepts `angle_unit` ("deg"|"rad"):
the known angle A is read in that unit, and every angle in the working and results
(B, C, and the supplement) is displayed in it.
"""
import math

from core.registry import register

DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or system "
    "errors. They are provided for general reference only — always verify results "
    "independently before relying on them for academic or professional decisions."
)


@register(
    slug="trig-ambiguous-case",
    name="Ambiguous case (SSA)",
    section="maths",
    sub="Non-Right-Angle Trigonometry",
    topic="Trigonometry",
    order=0,
    summary=(
        "Resolve the ambiguous SSA case where two sides and a non-included angle "
        "may give no triangle, one triangle, or two different triangles, in degrees "
        "or radians, with both valid triangles drawn side by side and an "
        "explanation of which case applies and why."
    ),
    formula="sin B = b·sin A / a  →  B or 180°−B may both be valid",
    tags=[
        "ambiguous case", "SSA", "two triangles", "sine rule", "non-right triangle",
        "trigonometry", "CBSE Class 11", "A-Level", "Common Core HSG-SRT.D",
        "Singapore A-Math", "France Premiere", "Germany Klasse 10",
        "ACARA Year 11", "UAE Grade 11",
    ],
    viz_template="viz/trig-ambiguous-case.html",
)
def compute(a=None, b=None, A=None, angle_unit="deg"):
    """a = side opposite the known angle A; b = the other given side."""
    try:
        unit = "rad" if str(angle_unit) == "rad" else "deg"

        def num(x):
            if x is None or x == "":
                return None
            return float(x)

        a_, b_, A_in = num(a), num(b), num(A)
        if a_ is None or b_ is None or A_in is None:
            return _err("Enter side a (opposite angle A), side b, and angle A.")
        if a_ <= 0 or b_ <= 0:
            return _err("Side lengths must be greater than zero.")
        A_ = A_in if unit == "deg" else math.degrees(A_in)
        if not (0 < A_ < 180):
            lim = "0° and 180°" if unit == "deg" else "0 and π rad"
            return _err("Angle A must be between %s." % lim)

        sinB = b_ * math.sin(math.radians(A_)) / a_
        steps = [
            {"label": "Apply the sine rule for sin B",
             "math": r"\(\sin B = \dfrac{b\,\sin A}{a} = \dfrac{%s\,\sin %s}{%s} = %s\)"
                     % (_fmt(b_), _ang(A_, unit), _fmt(a_), _fmt(sinB)),
             "note": "B is the angle opposite side b."},
        ]

        if sinB > 1 + 1e-12:
            steps.append({"label": "No solution",
                          "math": r"\(\sin B = %s > 1\)" % _fmt(sinB),
                          "note": "No angle has a sine above 1, so side a is too short to reach — no triangle exists."})
            return {"result": "No triangle", "count": 0, "a": a_, "b": b_, "A": A_,
                    "angle_unit": unit, "sinB": round(sinB, 6),
                    "steps": steps, "explanation": _expl(), "disclaimer": DISCLAIMER}

        sinB = min(1.0, sinB)
        B1 = math.degrees(math.asin(sinB))
        B2 = 180 - B1
        two = (A_ + B2 < 180) and (abs(B2 - B1) > 1e-9)

        if two:
            C1 = 180 - A_ - B1
            C2 = 180 - A_ - B2
            steps.append({"label": "Two possible angles",
                          "math": r"\(B = %s \text{ or } B = 180^\circ - %s = %s\)"
                                  % (_ang(B1, unit), _ang(B1, unit), _ang(B2, unit)),
                          "note": "Both keep the angle sum under 180°, so two distinct triangles fit."})
            steps.append({"label": "Remaining angle in each",
                          "math": r"\(C = %s \text{ or } %s\)" % (_ang(C1, unit), _ang(C2, unit)),
                          "note": "Each choice of B gives a different third angle and triangle."})
            return {"result": "Two triangles (B = %s or %s)" % (_disp(B1, unit), _disp(B2, unit)),
                    "count": 2, "a": a_, "b": b_, "A": A_, "angle_unit": unit,
                    "B1": round(B1, 4), "B2": round(B2, 4),
                    "C1": round(C1, 4), "C2": round(C2, 4),
                    "sinB": round(sinB, 6),
                    "steps": steps, "explanation": _expl(), "disclaimer": DISCLAIMER}
        else:
            C1 = 180 - A_ - B1
            steps.append({"label": "One triangle",
                          "math": r"\(B = %s,\ C = %s\)" % (_ang(B1, unit), _ang(C1, unit)),
                          "note": "The obtuse alternative would push the angle sum past 180°, so only one triangle works."})
            return {"result": "One triangle (B = %s)" % _disp(B1, unit),
                    "count": 1, "a": a_, "b": b_, "A": A_, "angle_unit": unit,
                    "B1": round(B1, 4), "C1": round(C1, 4),
                    "sinB": round(sinB, 6),
                    "steps": steps, "explanation": _expl(), "disclaimer": DISCLAIMER}
    except (TypeError, ValueError):
        return _err("Please enter valid numbers.")


def _ang(deg, unit):
    """LaTeX-friendly angle in the chosen unit (for step math)."""
    if unit == "rad":
        return _fmt(math.radians(deg)) + r"\,\text{rad}"
    return _fmt(deg) + r"^\circ"


def _disp(deg, unit):
    """Plain-text angle in the chosen unit (for the result string)."""
    if unit == "rad":
        return _fmt(math.radians(deg)) + " rad"
    return _fmt(deg) + "\u00b0"


def _expl():
    return [
        {"heading": "Why SSA is ambiguous",
         "body": "When you know two sides and an angle not between them, the side "
                 "opposite the known angle can sometimes swing to meet the base in "
                 "two places. That produces two valid triangles — the inverse sine "
                 "gives one angle, and its supplement may give another."},
        {"heading": "Zero, one, or two",
         "body": "If the computed sine exceeds 1 the side is too short and no "
                 "triangle forms. If only the acute angle keeps the angle sum under "
                 "180° there is one triangle. If both the acute and obtuse options "
                 "fit, there are two."},
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
