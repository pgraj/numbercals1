"""Real-world trig problem solver — a small selector of applied problem types.  Stage 3."""
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
 {"heading":"Trigonometry in the world",
  "body":"Right-angle trig and the sine rule turn real measurements into answers: the "
         "height of a tree from its shadow angle, the reach of a leaning ladder, or the "
         "height of a seat on a rotating wheel at a given time."},
 {"heading":"Choosing the model",
  "body":"Each problem maps to a trig relationship — tan for elevation/height, sine for a "
         "ladder against a wall, a sinusoid for circular motion. Identify the right-angle "
         "triangle or the periodic motion, then substitute."},
 {"heading":"Reading the answer",
  "body":"Always check the answer is physically sensible: a height shorter than the "
         "hypotenuse, an angle between 0° and 90°, a wheel height between ground and the "
         "top of the circle."},
]
@register(
    slug="trig-real-world-problems", name="Real-World Trig Problems",
    section="maths", sub="Advanced Applications", topic="Trigonometry", order=60,
    summary="Solve common applied trigonometry problems — angle of elevation, a leaning "
            "ladder, and height on a rotating wheel — with full working, in degrees or "
            "radians.",
    formula="elevation: h = d·tanθ; ladder: h = L·sinθ; wheel: y = D + R·sin(ωt)",
    tags=["real world trig","angle of elevation","ladder problem","ferris wheel",
          "applied trigonometry","Year 11 Mathematics Advanced"],
    viz_template="viz/trig-real-world-problems.html",
    related=["trig-modelling-periodic","trig-waves-applications"],
)
def compute(problem="elevation", angle_unit="deg",
            d=20, theta=35, L=5, wall_angle=70,
            R=10, centre=12, omega=6, t=10, **_ignored):
    unit="rad" if str(angle_unit)=="rad" else "deg"
    problem = problem if problem in ("elevation","ladder","wheel") else "elevation"
    try:
        if problem=="elevation":
            dist=float(d); ain=float(theta)
            ang = math.degrees(ain) if unit=="rad" else ain
            h = dist*math.tan(math.radians(ang))
            steps=[
                {"label":"Model as a right triangle","math":r"\(\tan\theta = \dfrac{\text{height}}{\text{distance}}\)",
                 "note":"The line of sight is the hypotenuse."},
                {"label":"Rearrange for height","math":rf"\(h = d\tan\theta = {_fmt(dist)}\tan {_tex(ang,unit)}\)",
                 "note":"Multiply distance by tan of the elevation angle."},
                {"label":"Result","math":rf"\(h \approx {_fmt(h)}\)","note":"Height in the same units as the distance."},
            ]
            res=f"height ≈ {_fmt(h)}"; extra={"height":round(h,4),"distance":dist,"angle_deg":ang}
        elif problem=="ladder":
            length=float(L); ain=float(wall_angle)
            ang = math.degrees(ain) if unit=="rad" else ain
            h=length*math.sin(math.radians(ang))
            reach=length*math.cos(math.radians(ang))
            steps=[
                {"label":"Model the ladder","math":r"\(\text{height} = L\sin\theta,\quad \text{base} = L\cos\theta\)",
                 "note":"θ is the angle to the ground."},
                {"label":"Height up the wall","math":rf"\(h = {_fmt(length)}\sin {_tex(ang,unit)} \approx {_fmt(h)}\)",
                 "note":"Vertical reach."},
                {"label":"Base distance","math":rf"\(b = {_fmt(length)}\cos {_tex(ang,unit)} \approx {_fmt(reach)}\)",
                 "note":"How far the foot sits from the wall."},
            ]
            res=f"reaches {_fmt(h)} up the wall"; extra={"height":round(h,4),"base":round(reach,4),"length":length,"angle_deg":ang}
        else:  # wheel
            radius=float(R); cen=float(centre); w=float(omega); tt=float(t)
            ang_deg=w*tt  # degrees of rotation if omega in deg/sec; treat as degrees
            y=cen+radius*math.sin(math.radians(ang_deg))
            steps=[
                {"label":"Model circular motion","math":r"\(y = D + R\sin(\omega t)\)",
                 "note":"D is the centre height, R the radius."},
                {"label":"Angle turned","math":rf"\(\omega t = {_fmt(w)}\times {_fmt(tt)} = {_disp(ang_deg,unit)}\)",
                 "note":"How far around the wheel has turned."},
                {"label":"Height of the seat","math":rf"\(y = {_fmt(cen)} + {_fmt(radius)}\sin {_tex(ang_deg,unit)} \approx {_fmt(y)}\)",
                 "note":"Between ground and the top of the wheel."},
            ]
            res=f"seat height ≈ {_fmt(y)}"; extra={"height":round(y,4),"radius":radius,"centre":cen,"angle_deg":ang_deg}
    except (TypeError,ValueError):
        return {"error":"Please enter valid numbers for the chosen problem.","steps":[],"disclaimer":_DISCLAIMER}
    out={"result":res,"problem":problem,"angle_unit":unit,
         "steps":steps,"explanation":_EXPLANATION,"disclaimer":_DISCLAIMER}
    out.update(extra)
    return out


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
