"""Euler's formula and de Moivre's theorem.  Stage 3 (Extension 2)."""
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
def _disp(deg,unit): return (_fmt(math.radians(deg))+" rad") if unit=="rad" else (_fmt(deg)+"\u00b0")
def _tex(deg,unit): return (_fmt(math.radians(deg))+r"\,\text{rad}") if unit=="rad" else (_fmt(deg)+r"^\circ")
def _cpx(re_, im_):
    rs=_fmt(re_); 
    if abs(im_)<1e-12: return rs
    sign="+" if im_>=0 else "-"
    return f"{rs} {sign} {_fmt(abs(im_))}i"
_EXPLANATION=[
 {"heading":"Euler's formula",
  "body":"e^{iθ} = cos θ + i sin θ ties the exponential to trigonometry. A complex number "
         "of modulus r and argument θ is r·e^{iθ} = r(cos θ + i sin θ) — its point on the "
         "Argand plane."},
 {"heading":"De Moivre's theorem",
  "body":"Raising to a power is easy in this form: (r(cos θ + i sin θ))ⁿ = "
         "rⁿ(cos nθ + i sin nθ). The modulus is raised to the power and the argument is "
         "multiplied by n."},
 {"heading":"Why it matters",
  "body":"It derives multiple-angle identities, finds the n roots of a complex number, and "
         "underlies AC circuit phasors and the Fourier transform."},
]
@register(
    slug="trig-complex-numbers-euler", name="Euler's Formula & de Moivre",
    section="maths", sub="Advanced Applications", topic="Trigonometry", order=80,
    summary="Apply Euler's formula e^{iθ} = cos θ + i sin θ and de Moivre's theorem to "
            "write and power complex numbers, plotted on an Argand diagram, in degrees or "
            "radians.",
    formula="e^{iθ} = cos θ + i sin θ; (r(cosθ+isinθ))ⁿ = rⁿ(cos nθ + i sin nθ)",
    tags=["Euler's formula","de Moivre","complex numbers","Argand diagram",
          "cos θ + i sin θ","Extension 2"],
    viz_template="viz/trig-complex-numbers-euler.html",
    scholar="leonhard-euler",
    related=["trig-polar-coordinates","trig-compound-angles"],
)
def compute(modulus=2, theta=40, power=3, angle_unit="deg", **_ignored):
    unit="rad" if str(angle_unit)=="rad" else "deg"
    try: mod=float(modulus); ain=float(theta); n=float(power)
    except (TypeError,ValueError):
        return {"error":"Modulus, angle and power must be numbers.","steps":[],"disclaimer":_DISCLAIMER}
    ang = math.degrees(ain) if unit=="rad" else ain
    rad=math.radians(ang)
    re0,im0 = mod*math.cos(rad), mod*math.sin(rad)
    new_mod = mod**n; new_ang = ang*n
    rn=math.radians(new_ang)
    re1,im1 = new_mod*math.cos(rn), new_mod*math.sin(rn)
    steps=[
        {"label":"Write in Euler / polar form","math":rf"\(z = {_fmt(mod)}(\cos {_tex(ang,unit)} + i\sin {_tex(ang,unit)}) = {_fmt(mod)}e^{{i\theta}}\)",
         "note":f"z ≈ {_cpx(re0,im0)} on the Argand plane."},
        {"label":"Apply de Moivre","math":rf"\(z^{{{_fmt(n)}}} = {_fmt(mod)}^{{{_fmt(n)}}}(\cos {_fmt(n)}\theta + i\sin {_fmt(n)}\theta)\)",
         "note":"Modulus to the power; argument times n."},
        {"label":"Evaluate","math":rf"\(z^{{{_fmt(n)}}} = {_fmt(new_mod)}(\cos {_tex(new_ang,unit)} + i\sin {_tex(new_ang,unit)})\)",
         "note":f"Modulus {_fmt(new_mod)}, argument {_disp(new_ang,unit)}."},
        {"label":"Rectangular form","math":rf"\(z^{{{_fmt(n)}}} \approx {_cpx(re1,im1)}\)","note":"Back in a + bi form."},
    ]
    return {"result":f"{_fmt(new_mod)}(cos {_disp(new_ang,unit)} + i sin {_disp(new_ang,unit)})",
            "modulus":mod,"theta_deg":ang,"power":n,
            "z_re":round(re0,4),"z_im":round(im0,4),
            "result_mod":round(new_mod,4),"result_ang_deg":round(new_ang,4),
            "result_re":round(re1,4),"result_im":round(im1,4),"angle_unit":unit,
            "steps":steps,"explanation":_EXPLANATION,"disclaimer":_DISCLAIMER}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
