"""Polar coordinates — (r, θ) ↔ (x, y).  Stage 3 (Extension)."""
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
_EXPLANATION=[
 {"heading":"Two ways to name a point",
  "body":"Rectangular coordinates (x, y) give a point by how far across and up it is. "
         "Polar coordinates (r, θ) give it by distance r from the origin and the angle θ "
         "from the positive x-axis. Both describe the same point."},
 {"heading":"Converting between them",
  "body":"From polar to rectangular: x = r cos θ, y = r sin θ. From rectangular to polar: "
         "r = √(x² + y²) and θ = atan2(y, x), which picks the correct quadrant."},
 {"heading":"Where polar shines",
  "body":"Circular and spiral motion, radar and navigation, and many curves (cardioids, "
         "roses) are far simpler in polar form than in x–y."},
]
@register(
    slug="trig-polar-coordinates", name="Polar Coordinates",
    section="maths", sub="Advanced Applications", topic="Trigonometry", order=70,
    summary="Convert between polar (r, θ) and rectangular (x, y) coordinates both ways, "
            "plotted on a polar grid, with θ in degrees or radians.",
    formula="x = r cos θ, y = r sin θ; r = √(x²+y²), θ = atan2(y, x)",
    tags=["polar coordinates","rectangular to polar","r theta","atan2",
          "Extension"],
    viz_template="viz/trig-polar-coordinates.html",
    scholar="leonhard-euler",
    related=["trig-complex-numbers-euler","trig-inverse-functions"],
)
def compute(mode="to_rect", r=5, theta=53.13, x=3, y=4, angle_unit="deg", **_ignored):
    unit="rad" if str(angle_unit)=="rad" else "deg"
    mode = mode if mode in ("to_rect","to_polar") else "to_rect"
    try:
        if mode=="to_rect":
            rr=float(r); ain=float(theta)
            ang = math.degrees(ain) if unit=="rad" else ain
            xx=rr*math.cos(math.radians(ang)); yy=rr*math.sin(math.radians(ang))
            steps=[
                {"label":"Formulas","math":r"\(x = r\cos\theta,\quad y = r\sin\theta\)","note":"Polar to rectangular."},
                {"label":"Substitute","math":rf"\(x={_fmt(rr)}\cos {_tex(ang,unit)},\ y={_fmt(rr)}\sin {_tex(ang,unit)}\)","note":"Insert r and θ."},
                {"label":"Result","math":rf"\((x,y) \approx ({_fmt(xx)},\ {_fmt(yy)})\)","note":"Rectangular coordinates."},
            ]
            res=f"(x, y) ≈ ({_fmt(xx)}, {_fmt(yy)})"
            ext={"x":round(xx,4),"y":round(yy,4),"r":rr,"theta_deg":ang}
        else:
            xx=float(x); yy=float(y)
            rr=math.hypot(xx,yy); ang=math.degrees(math.atan2(yy,xx))
            steps=[
                {"label":"Formulas","math":r"\(r=\sqrt{x^2+y^2},\quad \theta=\operatorname{atan2}(y,x)\)","note":"Rectangular to polar."},
                {"label":"Distance","math":rf"\(r=\sqrt{{{_fmt(xx)}^2+{_fmt(yy)}^2}}={_fmt(rr)}\)","note":"Distance from the origin."},
                {"label":"Angle","math":rf"\(\theta=\operatorname{{atan2}}({_fmt(yy)},{_fmt(xx)})={_tex(ang,unit)}\)","note":"Measured from the positive x-axis."},
            ]
            res=f"(r, θ) ≈ ({_fmt(rr)}, {_disp(ang,unit)})"
            ext={"x":xx,"y":yy,"r":round(rr,4),"theta_deg":round(ang,4)}
    except (TypeError,ValueError):
        return {"error":"Please enter valid numbers.","steps":[],"disclaimer":_DISCLAIMER}
    out={"result":res,"mode":mode,"angle_unit":unit,
         "steps":steps,"explanation":_EXPLANATION,"disclaimer":_DISCLAIMER}
    out.update(ext); return out


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
