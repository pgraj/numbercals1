"""Real-world trig: simple pendulum. Maths > Real-World Trigonometry > Physics & Motion."""
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
 {"heading":"The simple pendulum","body":"For small swings, a pendulum's angle follows simple harmonic "
  "motion: \u03b8(t) = \u03b8\u2080·cos(2\u03c0t/T), swinging back and forth with period T."},
 {"heading":"The period formula","body":"T = 2\u03c0\u221a(L/g) depends only on the length L and gravity g "
  "(9.81 m/s\u00b2) \u2014 not on the mass or, for small angles, the amplitude. This is why pendulum clocks "
  "keep steady time."},
 {"heading":"Why 'small angle'","body":"The neat formula relies on sin\u03b8 \u2248 \u03b8 (in radians), which "
  "holds for small swings. Beyond about 20\u00b0 the real period grows slightly larger."},
]
@register(
    slug="rw-pendulum", name="Pendulum Period & Swing",
    section="maths", topic="Real-World Trigonometry", sub="Physics & Motion", order=0,
    summary="Find a pendulum's period T = 2\u03c0\u221a(L/g) and its angle \u03b8(t) = \u03b8\u2080·cos(2\u03c0t/T) "
            "at any time, with angles in degrees or radians.",
    formula="T = 2\u03c0\u221a(L/g);  \u03b8(t) = \u03b8\u2080·cos(2\u03c0t/T)",
    tags=["pendulum","simple harmonic motion","period","small angle","real world trigonometry","Physics"],
    viz_template="viz/rw-pendulum.html",
    related=["trig-small-angle-approximation","trig-modelling-periodic"],
)
def compute(length=1.0, theta0=10, time=0.5, g=9.81, angle_unit="deg", **_ignored):
    u="rad" if str(angle_unit)=="rad" else "deg"
    try: L=float(length); th0_in=float(theta0); t=float(time); gv=float(g)
    except (TypeError,ValueError):
        return {"error":"Length, angle, time and gravity must be numbers.","steps":[],"disclaimer":_DISCLAIMER}
    if L<=0: return {"error":"The length must be greater than zero.","steps":[],"disclaimer":_DISCLAIMER}
    if gv<=0: return {"error":"Gravity must be greater than zero.","steps":[],"disclaimer":_DISCLAIMER}
    th0_deg = math.degrees(th0_in) if u=="rad" else th0_in
    T=2*math.pi*math.sqrt(L/gv)
    th_deg = th0_deg*math.cos(2*math.pi*t/T)
    big = abs(th0_deg)>20
    steps=[
        {"label":"Period","math":rf"\(T=2\pi\sqrt{{L/g}}=2\pi\sqrt{{{_f(L)}/{_f(gv)}}}={_f(T)}\text{{ s}}\)",
         "note":"Depends only on length and gravity."},
        {"label":"Angle model","math":r"\(\theta(t)=\theta_0\cos\!\left(\frac{2\pi t}{T}\right)\)",
         "note":"Simple harmonic motion for small swings."},
        {"label":"Angle at time t","math":rf"\(\theta({_f(t)})={_tex(th0_deg,u)}\cos\!\left(\frac{{2\pi\cdot {_f(t)}}}{{{_f(T)}}}\right)\approx {_tex(th_deg,u)}\)",
         "note":f"The bob's angle from vertical at t = {_f(t)} s."},
    ]
    out={"result":f"T \u2248 {_f(T)} s,  \u03b8({_f(t)}) \u2248 {_disp(th_deg,u)}","length":L,"theta0_deg":round(th0_deg,4),
         "time":t,"g":gv,"period":round(T,6),"theta_deg":round(th_deg,4),"angle_unit":u,
         "steps":steps,"explanation":_EXPLANATION,"disclaimer":_DISCLAIMER}
    if big: out["note"]="For \u03b8\u2080 beyond about 20\u00b0 the small-angle model under-estimates the true period slightly."
    return out


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
