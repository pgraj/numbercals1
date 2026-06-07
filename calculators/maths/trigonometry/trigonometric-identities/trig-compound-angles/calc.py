"""Compound-angle formulae — sin/cos/tan of (A ± B).

Stage 3 (NSW Year 11 Mathematics Advanced / Extension 1). Evaluates the chosen
compound-angle identity at two angles, with the full expansion worked step by
step and the result shown in the angle unit the student picks.
"""
from __future__ import annotations
import math
from core.registry import register

_DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or system "
    "errors. They are provided for general reference only — always verify results "
    "independently before relying on them for academic or professional decisions."
)

_FN = ("sin", "cos", "tan")


def _fmt(x):
    if x is None:
        return ""
    if abs(x - round(x)) < 1e-9:
        return str(int(round(x)))
    return ("%.4f" % x).rstrip("0").rstrip(".")


def _ang_tex(deg, unit):
    if unit == "rad":
        return _fmt(math.radians(deg)) + r"\,\text{rad}"
    return _fmt(deg) + r"^\circ"


def _ang_plain(deg, unit):
    if unit == "rad":
        return _fmt(math.radians(deg)) + " rad"
    return _fmt(deg) + "\u00b0"


_EXPLANATION = [
    {"heading": "What the compound-angle formulae do",
     "body": "They expand the sine, cosine or tangent of a sum or difference of two "
             "angles into expressions using only the sines, cosines and tangents of "
             "the separate angles — so you can evaluate things like sin 75° = "
             "sin(45° + 30°) exactly."},
    {"heading": "Watching the signs",
     "body": "Sine keeps the sign of the bracket (sin(A+B) uses +, sin(A−B) uses −). "
             "Cosine flips it (cos(A+B) uses −). Tangent has the sign in the numerator "
             "and the opposite sign in the denominator."},
    {"heading": "Why they matter",
     "body": "Every later identity — double-angle, half-angle, product-to-sum — is "
             "derived from these. They are the workhorse of trigonometric manipulation "
             "and of resolving waves into components."},
]


@register(
    slug="trig-compound-angles",
    name="Compound-Angle Formulae",
    section="maths",
    sub="Trigonometric Identities",
    topic="Trigonometry",
    order=60,
    summary="Expand and evaluate sin(A±B), cos(A±B) and tan(A±B) with the full "
            "compound-angle working shown step by step, in degrees or radians.",
    formula="sin(A±B)=sinA cosB ± cosA sinB; cos(A±B)=cosA cosB ∓ sinA sinB",
    tags=["compound angle", "sin(A+B)", "cos(A+B)", "tan(A+B)", "angle sum",
          "angle difference", "Year 11 Mathematics Advanced", "Extension 1"],
    viz_template="viz/trig-compound-angles.html",
    related=["trig-double-angle", "trig-exact-values"],
)
def compute(A=45, B=30, func="sin", sign="+", angle_unit="deg", **_ignored):
    unit = "rad" if str(angle_unit) == "rad" else "deg"
    func = func if func in _FN else "sin"
    sgn = "-" if str(sign) == "-" else "+"
    try:
        a_in, b_in = float(A), float(B)
    except (TypeError, ValueError):
        return {"error": "Angles must be numbers.", "steps": [], "disclaimer": _DISCLAIMER}

    Ad = math.degrees(a_in) if unit == "rad" else a_in
    Bd = math.degrees(b_in) if unit == "rad" else b_in
    Ar, Br = math.radians(Ad), math.radians(Bd)
    sA, cA, sB, cB = math.sin(Ar), math.cos(Ar), math.sin(Br), math.cos(Br)
    Ax, Bx = _ang_tex(Ad, unit), _ang_tex(Bd, unit)
    combo = Ad + Bd if sgn == "+" else Ad - Bd
    combo_r = math.radians(combo)

    if func == "sin":
        val = sA * cB + (1 if sgn == "+" else -1) * cA * sB
        expand = (rf"\sin A\cos B {sgn} \cos A\sin B")
        subst = (rf"({_fmt(sA)})({_fmt(cB)}) {sgn} ({_fmt(cA)})({_fmt(sB)})")
        identity = rf"\sin(A {sgn} B) = \sin A\cos B {sgn} \cos A\sin B"
        check = math.sin(combo_r)
    elif func == "cos":
        opp = "-" if sgn == "+" else "+"
        val = cA * cB + (-1 if sgn == "+" else 1) * sA * sB
        expand = (rf"\cos A\cos B {opp} \sin A\sin B")
        subst = (rf"({_fmt(cA)})({_fmt(cB)}) {opp} ({_fmt(sA)})({_fmt(sB)})")
        identity = rf"\cos(A {sgn} B) = \cos A\cos B {opp} \sin A\sin B"
        check = math.cos(combo_r)
    else:  # tan
        # undefined guards: cos of A, B, or A±B = 0
        if abs(cA) < 1e-12 or abs(cB) < 1e-12 or abs(math.cos(combo_r)) < 1e-12:
            return {"error": "tan is undefined here (one of A, B, or A±B is an odd "
                             "multiple of 90°/π·2).", "steps": [], "disclaimer": _DISCLAIMER}
        tA, tB = math.tan(Ar), math.tan(Br)
        denom = 1 - (1 if sgn == "+" else -1) * tA * tB
        if abs(denom) < 1e-12:
            return {"error": "tan is undefined here — the denominator 1∓tanA·tanB is "
                             "zero.", "steps": [], "disclaimer": _DISCLAIMER}
        num_sgn = sgn
        den_sgn = "-" if sgn == "+" else "+"
        val = (tA + (1 if sgn == "+" else -1) * tB) / denom
        expand = rf"\dfrac{{\tan A {num_sgn} \tan B}}{{1 {den_sgn} \tan A\tan B}}"
        subst = rf"\dfrac{{{_fmt(tA)} {num_sgn} {_fmt(tB)}}}{{1 {den_sgn} ({_fmt(tA)})({_fmt(tB)})}}"
        identity = rf"\tan(A {sgn} B) = \dfrac{{\tan A {num_sgn} \tan B}}{{1 {den_sgn} \tan A\tan B}}"
        check = math.tan(combo_r)

    steps = [
        {"label": "Write the identity",
         "math": rf"\({identity}\)",
         "note": f"The {func} compound-angle formula for a {'sum' if sgn=='+' else 'difference'}."},
        {"label": "Substitute the angles",
         "math": rf"\(A = {Ax},\quad B = {Bx}\)",
         "note": f"Evaluate each ratio at A and B."},
        {"label": "Expand",
         "math": rf"\({func}(A {sgn} B) = {expand} = {subst}\)",
         "note": "Insert the numeric values of each ratio."},
        {"label": "Result",
         "math": rf"\({func}(A {sgn} B) \approx {_fmt(val)}\)",
         "note": f"Direct check: {func}({_ang_plain(combo, unit)}) = {_fmt(check)}."},
    ]
    return {
        "result": _fmt(val),
        "func": func, "sign": sgn,
        "A_deg": Ad, "B_deg": Bd, "combo_deg": combo,
        "angle_unit": unit,
        "value": round(val, 6),
        "steps": steps, "explanation": _EXPLANATION, "disclaimer": _DISCLAIMER,
    }


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
