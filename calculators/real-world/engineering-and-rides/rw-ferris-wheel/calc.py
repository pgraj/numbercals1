"""Real-world trig: Ferris wheel height over time. Maths > Real-World Trigonometry > Engineering & Rides."""
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
 {"heading":"Circular motion as a sine wave","body":"As a Ferris wheel turns at a steady rate, the "
  "height of a car traces a sine curve in time. One full turn is one period T."},
 {"heading":"Building the model","body":"h(t) = R·sin(2\u03c0t/T \u2212 \u03c0/2) + R + clearance. The "
  "\u2212\u03c0/2 phase starts the car at the bottom; +R lifts the midline to the axle height; "
  "clearance is the gap from the ground to the lowest point."},
 {"heading":"Reading it","body":"At t = 0 the car is at the bottom (height = clearance); at t = T/2 it "
  "is at the top (2R + clearance); the midline (axle) is at R + clearance."},
]
@register(
    slug="rw-ferris-wheel", name="Ferris Wheel Height",
    section="maths", topic="Real-World Trigonometry", sub="Engineering & Rides", order=0,
    summary="Find the height of a Ferris-wheel car at any time using h(t) = R·sin(2\u03c0t/T \u2212 \u03c0/2) "
            "+ R + clearance, with the turning angle shown in degrees or radians.",
    formula="h(t) = R·sin(2\u03c0t/T \u2212 \u03c0/2) + R + clearance",
    tags=["ferris wheel","circular motion","periodic height","sine model","real world trigonometry"],
    viz_template="viz/rw-ferris-wheel.html",
    related=["rw-tide-prediction","trig-modelling-periodic"],
)
def compute(radius=10, period=30, clearance=2, time=7.5, angle_unit="deg", **_ignored):
    u="rad" if str(angle_unit)=="rad" else "deg"
    try: R=float(radius); T=float(period); cl=float(clearance); t=float(time)
    except (TypeError,ValueError):
        return {"error":"Radius, period, clearance and time must be numbers.","steps":[],"disclaimer":_DISCLAIMER}
    if T<=0: return {"error":"The period must be greater than zero.","steps":[],"disclaimer":_DISCLAIMER}
    if R<=0: return {"error":"The radius must be greater than zero.","steps":[],"disclaimer":_DISCLAIMER}
    turn_deg=(360.0*t/T)%360.0
    h=R*math.sin(2*math.pi*t/T - math.pi/2)+R+cl
    steps=[
        {"label":"State the model","math":r"\(h(t)=R\sin\!\left(\frac{2\pi t}{T}-\frac{\pi}{2}\right)+R+c\)",
         "note":"c is the ground clearance; the phase starts the car at the bottom."},
        {"label":"Angle turned by time t","math":rf"\(\frac{{2\pi t}}{{T}} = {_tex(turn_deg,u)}\)",
         "note":f"After {_f(t)} units, the wheel has turned {_disp(turn_deg,u)}."},
        {"label":"Substitute","math":rf"\(h={_f(R)}\sin({_tex(turn_deg,u)}-90^\circ)+{_f(R)}+{_f(cl)}\)",
         "note":"Insert R, the turned angle, and clearance."},
        {"label":"Height","math":rf"\(h \approx {_f(h)}\)","note":f"Between {_f(cl)} (bottom) and {_f(2*R+cl)} (top)."},
    ]
    return {"result":f"height \u2248 {_f(h)}","radius":R,"period":T,"clearance":cl,"time":t,
            "turn_deg":round(turn_deg,4),"height":round(h,4),"h_min":round(cl,4),"h_max":round(2*R+cl,4),
            "axle":round(R+cl,4),"angle_unit":u,"steps":steps,"explanation":_EXPLANATION,"disclaimer":_DISCLAIMER}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
