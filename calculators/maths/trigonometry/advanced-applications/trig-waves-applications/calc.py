"""Wave superposition — a sin x + b cos x = R sin(x + α).  Stage 3 (Adv / Ext 1)."""
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
 {"heading":"Combining two waves into one",
  "body":"Any sum a sin x + b cos x of two waves of the same frequency is itself a single "
         "wave R sin(x + α). The amplitude R and phase shift α are found from a and b."},
 {"heading":"Finding R and α",
  "body":"R = √(a² + b²) is the resultant amplitude (Pythagoras on the coefficients), and "
         "α = arctan(b/a) — using atan2 to land in the right quadrant — is the phase shift."},
 {"heading":"Why it matters",
  "body":"It is how alternating currents combine, how two speakers' outputs add, and how a "
         "horizontal-plus-vertical oscillation becomes one tilted sinusoid."},
]
@register(
    slug="trig-waves-applications", name="Wave Superposition (a sinx + b cosx)",
    section="maths", sub="Advanced Applications", topic="Trigonometry", order=30,
    summary="Combine a sin x + b cos x into a single wave R sin(x + α), finding the "
            "resultant amplitude and phase shift, in degrees or radians.",
    formula="a sin x + b cos x = R sin(x + α), R = √(a²+b²), α = arctan(b/a)",
    tags=["wave superposition","a sinx + b cosx","R sin(x+alpha)","phase shift",
          "amplitude","Year 11 Mathematics Advanced","Extension 1"],
    viz_template="viz/trig-waves-applications.html",
    related=["trig-modelling-periodic","trig-compound-angles"],
)
def compute(a=3, b=4, angle_unit="deg", **_ignored):
    unit="rad" if str(angle_unit)=="rad" else "deg"
    try: av,bv=float(a),float(b)
    except (TypeError,ValueError):
        return {"error":"a and b must be numbers.","steps":[],"disclaimer":_DISCLAIMER}
    R=math.hypot(av,bv)
    if R<1e-12:
        return {"error":"With a = 0 and b = 0 there is no wave to combine.","steps":[],"disclaimer":_DISCLAIMER}
    alpha=math.degrees(math.atan2(bv,av))
    steps=[
        {"label":"Set up the resultant form","math":r"\(a\sin x + b\cos x = R\sin(x+\alpha)\)",
         "note":"Match amplitude and phase on both sides."},
        {"label":"Resultant amplitude","math":rf"\(R=\sqrt{{a^2+b^2}}=\sqrt{{{_fmt(av)}^2+{_fmt(bv)}^2}}={_fmt(R)}\)",
         "note":"Pythagoras on the two coefficients."},
        {"label":"Phase shift","math":rf"\(\alpha=\arctan\!\left(\dfrac{{b}}{{a}}\right)={_tex(alpha,unit)}\)",
         "note":"Using atan2 so the quadrant is correct."},
        {"label":"Result","math":rf"\({_fmt(av)}\sin x + {_fmt(bv)}\cos x = {_fmt(R)}\sin(x + {_disp(alpha,unit)})\)",
         "note":"A single wave with that amplitude and phase."},
    ]
    return {"result":f"{_fmt(R)} sin(x + {_disp(alpha,unit)})","a":av,"b":bv,
            "R":round(R,6),"alpha_deg":round(alpha,4),"angle_unit":unit,
            "steps":steps,"explanation":_EXPLANATION,"disclaimer":_DISCLAIMER}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
