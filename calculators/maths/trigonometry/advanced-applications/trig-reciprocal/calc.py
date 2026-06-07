"""Reciprocal trig functions — sec, cosec, cot.  Stage 3 (Year 11 Advanced)."""
from __future__ import annotations
import math
from core.registry import register
_DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or system "
    "errors. They are provided for general reference only — always verify results "
    "independently before relying on them for academic or professional decisions.")
def _fmt(x):
    if x is None: return ""
    if abs(x - round(x)) < 1e-9: return str(int(round(x)))
    return ("%.4f" % x).rstrip("0").rstrip(".")
def _tex(deg,unit): return (_fmt(math.radians(deg))+r"\,\text{rad}") if unit=="rad" else (_fmt(deg)+r"^\circ")
def _disp(deg,unit): return (_fmt(math.radians(deg))+" rad") if unit=="rad" else (_fmt(deg)+"\u00b0")
_DEF = {
 "sec": ("sec", "cos", r"\sec\theta=\dfrac{1}{\cos\theta}"),
 "cosec": ("cosec", "sin", r"\operatorname{cosec}\theta=\dfrac{1}{\sin\theta}"),
 "cot": ("cot", "tan", r"\cot\theta=\dfrac{\cos\theta}{\sin\theta}"),
}
_EXPLANATION=[
 {"heading":"The three reciprocal ratios",
  "body":"Secant is one over cosine, cosecant is one over sine, and cotangent is cosine "
         "over sine (equivalently one over tangent). They complete the family of six "
         "trig functions."},
 {"heading":"Where they blow up",
  "body":"Each is undefined wherever its denominator is zero: sec and tan at 90°, 270° "
         "(cos = 0); cosec and cot at 0°, 180° (sin = 0). Their graphs have vertical "
         "asymptotes there."},
 {"heading":"Why they matter",
  "body":"They appear naturally in calculus (the derivative of tan is sec²), in the "
         "Pythagorean identities 1+tan²=sec² and 1+cot²=cosec², and in resolving forces "
         "along inclined directions."},
]
@register(
    slug="trig-reciprocal", name="Reciprocal Trig Functions",
    section="maths", sub="Advanced Applications", topic="Trigonometry", order=20,
    summary="Evaluate secant, cosecant and cotangent at any angle, with their "
            "definitions, undefined points and the working shown, in degrees or radians.",
    formula="sec θ = 1/cos θ; cosec θ = 1/sin θ; cot θ = cos θ/sin θ",
    tags=["reciprocal trig","secant","cosecant","cotangent","sec cosec cot",
          "Year 11 Mathematics Advanced"],
    viz_template="viz/trig-reciprocal.html",
    related=["trig-inverse-functions","trig-pythagorean-identities"],
)
def compute(fn="sec", angle=30, angle_unit="deg", **_ignored):
    unit="rad" if str(angle_unit)=="rad" else "deg"
    fn = fn if fn in _DEF else "sec"
    try: a_in=float(angle)
    except (TypeError,ValueError):
        return {"error":"Angle must be a number.","steps":[],"disclaimer":_DISCLAIMER}
    deg = math.degrees(a_in) if unit=="rad" else a_in
    r = math.radians(deg); s,c = math.sin(r),math.cos(r)
    name, base, idtex = _DEF[fn]
    if fn=="sec":
        if abs(c)<1e-12: return {"error":f"sec is undefined here (cos {_disp(deg,unit)} = 0).","steps":[],"disclaimer":_DISCLAIMER}
        val=1/c; basev=c
    elif fn=="cosec":
        if abs(s)<1e-12: return {"error":f"cosec is undefined here (sin {_disp(deg,unit)} = 0).","steps":[],"disclaimer":_DISCLAIMER}
        val=1/s; basev=s
    else:
        if abs(s)<1e-12: return {"error":f"cot is undefined here (sin {_disp(deg,unit)} = 0).","steps":[],"disclaimer":_DISCLAIMER}
        val=c/s; basev=math.tan(r)
    steps=[
        {"label":"Write the definition","math":rf"\({idtex}\)","note":f"{name} is built from {base}."},
        {"label":"Evaluate the base ratio","math":rf"\({base}\,{_tex(deg,unit)} = {_fmt(basev)}\)","note":"Compute the underlying function first."},
        {"label":"Take the reciprocal/ratio","math":rf"\({name}\,\theta \approx {_fmt(val)}\)","note":"Invert (or divide) to get the result."},
    ]
    return {"result":_fmt(val),"fn":fn,"angle_deg":deg,"angle_unit":unit,"value":round(val,6),
            "base":base,"base_value":round(basev,6),
            "steps":steps,"explanation":_EXPLANATION,"disclaimer":_DISCLAIMER}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
