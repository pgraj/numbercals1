"""Small-angle approximations — sin x ≈ x, tan x ≈ x, cos x ≈ 1 − x²/2 (radians)."""
from __future__ import annotations
import math
from core.registry import register
_DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or system "
    "errors. They are provided for general reference only — always verify results "
    "independently before relying on them for academic or professional decisions.")
def _fmt(x, p=6):
    if x is None: return ""
    if abs(x - round(x)) < 1e-9: return str(int(round(x)))
    return (("%."+str(p)+"f") % x).rstrip("0").rstrip(".")
_EXPLANATION=[
 {"heading":"When angles are tiny",
  "body":"For small angles measured in radians, sin x ≈ x, tan x ≈ x and cos x ≈ 1 − x²/2. "
         "The smaller the angle, the better these approximations are."},
 {"heading":"Why radians are essential",
  "body":"These hold only in radians — the approximations come from the functions' series "
         "expansions, where x is the radian measure. In degrees they are wrong, so this "
         "calculator works in radians."},
 {"heading":"Where they are used",
  "body":"The pendulum equation, optics (small-angle lens and diffraction formulae) and "
         "physics generally rely on sin x ≈ x to turn hard equations into simple ones."},
]
@register(
    slug="trig-small-angle-approximation", name="Small-Angle Approximation",
    section="maths", sub="Advanced Applications", topic="Trigonometry", order=40,
    summary="Compare sin x, tan x and cos x with their small-angle approximations "
            "(x, x and 1 − x²/2) and see the error, for small angles in radians.",
    formula="sin x ≈ x, tan x ≈ x, cos x ≈ 1 − x²/2  (x in radians)",
    tags=["small angle approximation","sin x approx x","cos x approx","pendulum",
          "Year 11 Mathematics Advanced"],
    viz_template="viz/trig-small-angle-approximation.html",
    related=["trig-waves-applications","trig-radians"],
)
def compute(x=0.1, fn="sin", **_ignored):
    # radians-native: x is always radians here (no deg/rad toggle).
    fn = fn if fn in ("sin","cos","tan") else "sin"
    try: xr=float(x)
    except (TypeError,ValueError):
        return {"error":"x must be a number (in radians).","steps":[],"disclaimer":_DISCLAIMER}
    if fn=="sin":
        true=math.sin(xr); approx=xr; atex=r"\sin x \approx x"
    elif fn=="tan":
        true=math.tan(xr); approx=xr; atex=r"\tan x \approx x"
    else:
        true=math.cos(xr); approx=1-xr*xr/2; atex=r"\cos x \approx 1-\tfrac{x^2}{2}"
    err=abs(true-approx); pct=(err/abs(true)*100) if abs(true)>1e-12 else 0.0
    steps=[
        {"label":"The approximation (radians)","math":rf"\({atex}\)","note":"Valid for small x in radians."},
        {"label":"True value","math":rf"\({fn} ({_fmt(xr)}) = {_fmt(true)}\)","note":"Computed exactly."},
        {"label":"Approximate value","math":rf"\(\approx {_fmt(approx)}\)","note":"From the formula above."},
        {"label":"Error","math":rf"\(|{_fmt(true)}-{_fmt(approx)}| = {_fmt(err)}\ ({_fmt(pct,3)}\%)\)",
         "note":"The approximation improves as x shrinks."},
    ]
    return {"result":f"{fn} x ≈ {_fmt(approx)} (true {_fmt(true)})","fn":fn,"x":xr,
            "true_value":round(true,8),"approx_value":round(approx,8),
            "error_value":round(err,8),"pct":round(pct,5),"angle_unit":"rad",
            "steps":steps,"explanation":_EXPLANATION,"disclaimer":_DISCLAIMER}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
