"""Product-to-sum (and sum-to-product) formulae.  Stage 3 (Extension)."""
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

# form: (label, identity-LaTeX, evaluator(A_rad,B_rad)->value, RHS-LaTeX builder)
_FORMS = {
    "2sincos": (r"2\sin A\cos B = \sin(A+B) + \sin(A-B)",
                lambda Ar,Br: 2*math.sin(Ar)*math.cos(Br)),
    "2coscos": (r"2\cos A\cos B = \cos(A-B) + \cos(A+B)",
                lambda Ar,Br: 2*math.cos(Ar)*math.cos(Br)),
    "2sinsin": (r"2\sin A\sin B = \cos(A-B) - \cos(A+B)",
                lambda Ar,Br: 2*math.sin(Ar)*math.sin(Br)),
}

_EXPLANATION = [
    {"heading":"Turning products into sums",
     "body":"Adding and subtracting the compound-angle formulae cancels terms and "
            "leaves a product equal to a sum (or difference) of single trig functions. "
            "That is exactly what you need to integrate a product of sines and cosines."},
    {"heading":"The three identities",
     "body":"2 sinA cosB = sin(A+B) + sin(A−B); 2 cosA cosB = cos(A−B) + cos(A+B); "
            "2 sinA sinB = cos(A−B) − cos(A+B). The reverse direction (sum to product) "
            "is used to factorise and to find beat frequencies."},
    {"heading":"Where they appear",
     "body":"Beats between two close musical notes, amplitude modulation in radio, and "
            "integrating products of trig functions in calculus all rely on these."},
]

@register(
    slug="trig-product-to-sum",
    name="Product-to-Sum Formulae",
    section="maths", sub="Trigonometric Identities", topic="Trigonometry",
    order=75,
    summary="Convert a product of sines and cosines into a sum or difference (and "
            "back), with the full identity worked step by step, in degrees or radians.",
    formula="2sinAcosB=sin(A+B)+sin(A−B); 2cosAcosB=cos(A−B)+cos(A+B)",
    tags=["product to sum", "sum to product", "2sinAcosB", "beats",
          "Extension"],
    viz_template="viz/trig-product-to-sum.html",
    related=["trig-compound-angles", "trig-double-angle"],
)
def compute(A=50, B=20, form="2sincos", angle_unit="deg", **_ignored):
    unit = "rad" if str(angle_unit)=="rad" else "deg"
    if form not in _FORMS: form="2sincos"
    try:
        a_in,b_in=float(A),float(B)
    except (TypeError,ValueError):
        return {"error":"Angles must be numbers.","steps":[],"disclaimer":_DISCLAIMER}
    Ad = math.degrees(a_in) if unit=="rad" else a_in
    Bd = math.degrees(b_in) if unit=="rad" else b_in
    Ar,Br = math.radians(Ad), math.radians(Bd)
    identity, fn = _FORMS[form]
    val = fn(Ar,Br)
    Ax,Bx=_ang_tex(Ad,unit),_ang_tex(Bd,unit)
    summ = Ad+Bd; diff = Ad-Bd
    steps=[
        {"label":"Write the identity","math":rf"\({identity}\)",
         "note":"Derived by adding/subtracting the compound-angle formulae."},
        {"label":"Substitute A and B","math":rf"\(A={Ax},\quad B={Bx}\)",
         "note":f"A+B = {_ang_plain(summ,unit)}, A−B = {_ang_plain(diff,unit)}."},
        {"label":"Evaluate both sides","math":rf"\(\text{{LHS}} \approx {_fmt(val)}\)",
         "note":"The product equals the sum/difference on the right."},
    ]
    return {
        "result":_fmt(val), "form":form, "A_deg":Ad, "B_deg":Bd,
        "sum_deg":summ, "diff_deg":diff, "angle_unit":unit, "value":round(val,6),
        "steps":steps, "explanation":_EXPLANATION, "disclaimer":_DISCLAIMER,
    }


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
