"""Half-angle formulae — sin(A/2), cos(A/2), tan(A/2) and the t-formula.

Stage 3 (NSW Extension 1).
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

_EXPLANATION = [
    {"heading":"Half-angle from double-angle",
     "body":"Rearranging cos 2θ = 1 − 2sin²θ and cos 2θ = 2cos²θ − 1 (with θ = A/2) "
            "gives sin(A/2) = ±√((1−cosA)/2) and cos(A/2) = ±√((1+cosA)/2). The sign is "
            "fixed by the quadrant the half-angle lands in."},
    {"heading":"The t-formula",
     "body":"Writing t = tan(A/2) gives the rational substitutions sin A = 2t/(1+t²), "
            "cos A = (1−t²)/(1+t²) and tan A = 2t/(1−t²). They turn trig equations into "
            "algebra and are central to integrating rational trig functions."},
    {"heading":"Choosing the sign",
     "body":"Because the square root could be ±, decide the sign from where A/2 sits: "
            "if A/2 is in the first or second quadrant sin(A/2) is positive, and so on. "
            "This calculator picks the sign from the actual half-angle."},
]

@register(
    slug="trig-half-angle",
    name="Half-Angle Formulae",
    section="maths", sub="Trigonometric Identities", topic="Trigonometry",
    order=70,
    summary="Evaluate sin(A/2), cos(A/2) and tan(A/2) from cos A using the half-angle "
            "formulae, with correct sign by quadrant and the t-formula link, in degrees "
            "or radians.",
    formula="sin(A/2)=±√((1−cosA)/2); cos(A/2)=±√((1+cosA)/2); tan(A/2)=(1−cosA)/sinA",
    tags=["half angle", "sin(A/2)", "cos(A/2)", "tan(A/2)", "t-formula",
          "tan half angle", "Extension 1"],
    viz_template="viz/trig-half-angle.html",
    related=["trig-double-angle", "trig-compound-angles"],
)
def compute(A=60, func="sin", angle_unit="deg", **_ignored):
    unit = "rad" if str(angle_unit)=="rad" else "deg"
    func = func if func in ("sin","cos","tan") else "sin"
    try:
        a_in=float(A)
    except (TypeError,ValueError):
        return {"error":"Angle must be a number.","steps":[],"disclaimer":_DISCLAIMER}
    Ad = math.degrees(a_in) if unit=="rad" else a_in
    Ar = math.radians(Ad); cA, sA = math.cos(Ar), math.sin(Ar)
    half = Ad/2.0; hr = math.radians(half)
    Ax=_ang_tex(Ad,unit); Hx=_ang_tex(half,unit)

    if func=="sin":
        mag = math.sqrt(max(0.0,(1-cA)/2)); val = math.copysign(mag, math.sin(hr)) if mag>1e-12 else 0.0
        steps=[
            {"label":"Half-angle formula","math":r"\(\sin\tfrac{A}{2}=\pm\sqrt{\dfrac{1-\cos A}{2}}\)",
             "note":"From cos A = 1 − 2sin²(A/2)."},
            {"label":"Substitute cos A","math":rf"\(\cos A=\cos {Ax}={_fmt(cA)}\)","note":"Evaluate cos A."},
            {"label":"Compute the magnitude","math":rf"\(\sqrt{{\dfrac{{1-({_fmt(cA)})}}{{2}}}}={_fmt(mag)}\)",
             "note":"Then fix the sign by quadrant."},
            {"label":"Result","math":rf"\(\sin\tfrac{{A}}{{2}}=\sin {Hx}\approx {_fmt(val)}\)",
             "note":f"A/2 = {_ang_plain(half,unit)}; sign taken from its quadrant."},
        ]
    elif func=="cos":
        mag = math.sqrt(max(0.0,(1+cA)/2)); val = math.copysign(mag, math.cos(hr)) if mag>1e-12 else 0.0
        steps=[
            {"label":"Half-angle formula","math":r"\(\cos\tfrac{A}{2}=\pm\sqrt{\dfrac{1+\cos A}{2}}\)",
             "note":"From cos A = 2cos²(A/2) − 1."},
            {"label":"Substitute cos A","math":rf"\(\cos A={_fmt(cA)}\)","note":"Evaluate cos A."},
            {"label":"Compute the magnitude","math":rf"\(\sqrt{{\dfrac{{1+({_fmt(cA)})}}{{2}}}}={_fmt(mag)}\)",
             "note":"Then fix the sign by quadrant."},
            {"label":"Result","math":rf"\(\cos\tfrac{{A}}{{2}}=\cos {Hx}\approx {_fmt(val)}\)",
             "note":f"A/2 = {_ang_plain(half,unit)}."},
        ]
    else:  # tan
        if abs(sA) < 1e-12 and abs(1+cA) < 1e-12:
            return {"error":"tan(A/2) is undefined here (A is an odd multiple of 180°).",
                    "steps":[],"disclaimer":_DISCLAIMER}
        if abs(sA) < 1e-12:
            # A multiple of 360 -> A/2 multiple of 180 -> tan 0
            val = math.tan(hr)
        else:
            val = (1-cA)/sA
        steps=[
            {"label":"Half-angle (rational form)","math":r"\(\tan\tfrac{A}{2}=\dfrac{1-\cos A}{\sin A}=\dfrac{\sin A}{1+\cos A}\)",
             "note":"Two equivalent surd-free forms."},
            {"label":"Substitute","math":rf"\(\cos A={_fmt(cA)},\ \sin A={_fmt(sA)}\)","note":"Evaluate at A."},
            {"label":"Result","math":rf"\(\tan\tfrac{{A}}{{2}}=\dfrac{{1-({_fmt(cA)})}}{{{_fmt(sA)}}}\approx {_fmt(val)}\)",
             "note":f"Direct check: tan({_ang_plain(half,unit)}) = {_fmt(math.tan(hr))}."},
        ]
    return {
        "result":_fmt(val), "func":func, "A_deg":Ad, "half_deg":half,
        "angle_unit":unit, "value":round(val,6),
        "steps":steps, "explanation":_EXPLANATION, "disclaimer":_DISCLAIMER,
    }


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
