"""Real-world trig: 2D screen/point rotation. Maths > Real-World Trigonometry > Graphics & Technology."""
from __future__ import annotations
import math
from core.registry import register
_DISCLAIMER = ("These values are estimates and may contain computation, formula, or system errors. "
    "They are provided for general reference only — always verify results independently before "
    "relying on them for academic or professional decisions.")
def _f(x):
    if x is None: return ""
    if abs(x-round(x))<1e-9: return str(int(round(x)))
    return ("%.4f"%x).rstrip("0").rstrip(".")
def _disp(deg,u): return (_f(math.radians(deg))+" rad") if u=="rad" else (_f(deg)+"\u00b0")
def _tex(deg,u): return (_f(math.radians(deg))+r"\,\text{rad}") if u=="rad" else (_f(deg)+r"^\circ")
_EXPLANATION=[
 {"heading":"Rotating a point","body":"To rotate a point (x, y) about the origin by angle \u03b8: "
  "x\u2032 = x·cos\u03b8 \u2212 y·sin\u03b8 and y\u2032 = x·sin\u03b8 + y·cos\u03b8. This is the rotation matrix at work."},
 {"heading":"Where it is used","body":"Every time a phone screen reorients, a game sprite spins, or a "
  "graphic is turned, these two formulas (or the matrix form) compute the new coordinates."},
 {"heading":"A check","body":"Rotating (3, 0) by 90\u00b0 gives (0, 3) \u2014 the point swings a quarter turn "
  "anticlockwise. Negative angles rotate clockwise."},
]
@register(
    slug="rw-screen-rotation", name="2D Rotation (Graphics)",
    section="maths", topic="Real-World Trigonometry", sub="Graphics & Technology", order=0,
    summary="Rotate a point (x, y) about the origin by an angle using x\u2032 = x·cos\u03b8 \u2212 y·sin\u03b8, "
            "y\u2032 = x·sin\u03b8 + y·cos\u03b8, with the angle in degrees or radians.",
    formula="x\u2032 = x·cos\u03b8 \u2212 y·sin\u03b8;  y\u2032 = x·sin\u03b8 + y·cos\u03b8",
    tags=["rotation","2D rotation","rotation matrix","graphics","screen rotation","real world trigonometry"],
    viz_template="viz/rw-screen-rotation.html",
    related=["trig-polar-coordinates","trig-compound-angles"],
)
def compute(x=3, y=0, angle=90, angle_unit="deg", **_ignored):
    u="rad" if str(angle_unit)=="rad" else "deg"
    try: xv=float(x); yv=float(y); ain=float(angle)
    except (TypeError,ValueError):
        return {"error":"x, y and the angle must be numbers.","steps":[],"disclaimer":_DISCLAIMER}
    deg = math.degrees(ain) if u=="rad" else ain
    r=math.radians(deg); c=math.cos(r); s=math.sin(r)
    xp=xv*c-yv*s; yp=xv*s+yv*c
    steps=[
        {"label":"Rotation formulas","math":r"\(x'=x\cos\theta-y\sin\theta,\quad y'=x\sin\theta+y\cos\theta\)",
         "note":"Rotate about the origin by \u03b8."},
        {"label":"Substitute","math":rf"\(x'={_f(xv)}\cos {_tex(deg,u)}-{_f(yv)}\sin {_tex(deg,u)}\)",
         "note":"Insert the point and angle."},
        {"label":"Rotated point","math":rf"\((x',y') \approx ({_f(xp)},\ {_f(yp)})\)",
         "note":"The new coordinates after rotation."},
    ]
    return {"result":f"(x\u2032, y\u2032) \u2248 ({_f(xp)}, {_f(yp)})","x":xv,"y":yv,"angle_deg":round(deg,4),
            "xp":round(xp,4),"yp":round(yp,4),"angle_unit":u,
            "steps":steps,"explanation":_EXPLANATION,"disclaimer":_DISCLAIMER}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
