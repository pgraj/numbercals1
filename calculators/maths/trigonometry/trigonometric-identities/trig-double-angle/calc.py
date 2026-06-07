"""Double-angle formulae — sin 2A, cos 2A (three forms), tan 2A.

Stage 3 (NSW Year 11 Mathematics Advanced / Extension 1).
"""
from __future__ import annotations
import math
from core.registry import register

_DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or system "
    "errors. They are provided for general reference only — always verify results "
    "independently before relying on them for academic or professional decisions."
)

def _fmt(x):
    if x is None: return ""
    if abs(x - round(x)) < 1e-9: return str(int(round(x)))
    return ("%.4f" % x).rstrip("0").rstrip(".")

def _ang_tex(deg, unit):
    return (_fmt(math.radians(deg)) + r"\,\text{rad}") if unit=="rad" else (_fmt(deg)+r"^\circ")
def _ang_plain(deg, unit):
    return (_fmt(math.radians(deg)) + " rad") if unit=="rad" else (_fmt(deg)+"\u00b0")

_COS_FORMS = {
    "cos2-sin2": (r"\cos^2 A - \sin^2 A", lambda c,s: c*c - s*s),
    "2cos2-1":   (r"2\cos^2 A - 1",       lambda c,s: 2*c*c - 1),
    "1-2sin2":   (r"1 - 2\sin^2 A",       lambda c,s: 1 - 2*s*s),
}

_EXPLANATION = [
    {"heading": "Double-angle from compound-angle",
     "body": "Put B = A in the compound-angle formulae and they collapse to the "
             "double-angle ones: sin 2A = 2 sin A cos A, and cos 2A in three equivalent "
             "forms. They turn a doubled angle into expressions in the single angle."},
    {"heading": "Three faces of cos 2A",
     "body": "cos 2A = cos²A − sin²A is the base form; using sin²A + cos²A = 1 you can "
             "rewrite it as 2cos²A − 1 or 1 − 2sin²A. Pick whichever leaves only the "
             "function you need — invaluable when integrating or solving."},
    {"heading": "Where they are used",
     "body": "Halving powers of sine and cosine for integration, deriving half-angle "
             "formulae, and modelling the frequency-doubling that appears in optics, "
             "AC power and signal mixing."},
]

@register(
    slug="trig-double-angle",
    name="Double-Angle Formulae",
    section="maths", sub="Trigonometric Identities", topic="Trigonometry",
    order=65,
    summary="Evaluate sin 2A, cos 2A and tan 2A with full working, switching between "
            "the three equivalent forms of cos 2A, in degrees or radians.",
    formula="sin2A=2sinAcosA; cos2A=cos²A−sin²A=2cos²A−1=1−2sin²A; tan2A=2tanA/(1−tan²A)",
    tags=["double angle", "sin 2A", "cos 2A", "tan 2A", "cos2A three forms",
          "Year 11 Mathematics Advanced", "Extension 1"],
    viz_template="viz/trig-double-angle.html",
    related=["trig-compound-angles", "trig-half-angle"],
)
def compute(A=30, func="sin", cos_form="cos2-sin2", angle_unit="deg", **_ignored):
    unit = "rad" if str(angle_unit) == "rad" else "deg"
    func = func if func in ("sin","cos","tan") else "sin"
    if cos_form not in _COS_FORMS: cos_form = "cos2-sin2"
    try:
        a_in = float(A)
    except (TypeError, ValueError):
        return {"error":"Angle must be a number.","steps":[],"disclaimer":_DISCLAIMER}
    Ad = math.degrees(a_in) if unit=="rad" else a_in
    Ar = math.radians(Ad); s,c = math.sin(Ar), math.cos(Ar)
    Ax = _ang_tex(Ad, unit); two = 2*Ad

    if func=="sin":
        val = 2*s*c
        steps=[
            {"label":"Write the identity","math":r"\(\sin 2A = 2\sin A\cos A\)",
             "note":"Set B = A in sin(A+B)."},
            {"label":"Substitute","math":rf"\(A={Ax}\)","note":"Evaluate sin A and cos A."},
            {"label":"Expand","math":rf"\(2({_fmt(s)})({_fmt(c)})\)","note":"Multiply out."},
            {"label":"Result","math":rf"\(\sin 2A \approx {_fmt(val)}\)",
             "note":f"Direct check: sin({_ang_plain(two,unit)}) = {_fmt(math.sin(math.radians(two)))}."},
        ]
    elif func=="cos":
        tex, fn = _COS_FORMS[cos_form]; val = fn(c,s)
        steps=[
            {"label":"Choose the cos 2A form","math":rf"\(\cos 2A = {tex}\)",
             "note":"All three forms are equal; this one is selected."},
            {"label":"Substitute","math":rf"\(A={Ax}\)","note":"Evaluate the needed ratios."},
            {"label":"Evaluate","math":rf"\(\cos 2A \approx {_fmt(val)}\)",
             "note":f"Direct check: cos({_ang_plain(two,unit)}) = {_fmt(math.cos(math.radians(two)))}."},
            {"label":"The other two forms agree","math":
             rf"\(\cos^2A-\sin^2A = 2\cos^2A-1 = 1-2\sin^2A = {_fmt(val)}\)",
             "note":"Confirming the three forms give the same value."},
        ]
    else:  # tan
        if abs(c) < 1e-12:
            return {"error":"tan A is undefined here, so tan 2A cannot be formed.",
                    "steps":[],"disclaimer":_DISCLAIMER}
        t = math.tan(Ar); denom = 1 - t*t
        if abs(denom) < 1e-12:
            return {"error":"tan 2A is undefined here — the denominator 1−tan²A is zero "
                            "(A is an odd multiple of 45°/π·4).","steps":[],"disclaimer":_DISCLAIMER}
        if abs(math.cos(math.radians(two))) < 1e-12:
            return {"error":"tan 2A is undefined here (2A is an odd multiple of 90°).",
                    "steps":[],"disclaimer":_DISCLAIMER}
        val = 2*t/denom
        steps=[
            {"label":"Write the identity","math":r"\(\tan 2A = \dfrac{2\tan A}{1-\tan^2 A}\)",
             "note":"Set B = A in tan(A+B)."},
            {"label":"Substitute","math":rf"\(A={Ax},\ \tan A={_fmt(t)}\)","note":"Evaluate tan A."},
            {"label":"Evaluate","math":rf"\(\dfrac{{2({_fmt(t)})}}{{1-({_fmt(t)})^2}} \approx {_fmt(val)}\)",
             "note":f"Direct check: tan({_ang_plain(two,unit)}) = {_fmt(math.tan(math.radians(two)))}."},
        ]
    return {
        "result":_fmt(val), "func":func, "cos_form":cos_form,
        "A_deg":Ad, "two_deg":two, "angle_unit":unit, "value":round(val,6),
        "steps":steps, "explanation":_EXPLANATION, "disclaimer":_DISCLAIMER,
    }


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
