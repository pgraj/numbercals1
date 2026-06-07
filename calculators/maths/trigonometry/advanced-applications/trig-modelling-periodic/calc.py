"""Modelling periodic phenomena — y = A sin(B(x − C)) + D.  Stage 3 (Adv)."""
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
 {"heading":"The general sinusoidal model",
  "body":"y = A sin(B(x − C)) + D describes any simple periodic signal. A is the amplitude, "
         "B sets the period, C is the horizontal (phase) shift and D is the midline the "
         "wave oscillates about."},
 {"heading":"Reading off the features",
  "body":"Amplitude = |A|; period = 360°/B (or 2π/B in radians); the midline is y = D, so "
         "the maximum is D + |A| and the minimum is D − |A|; the curve is shifted right by C."},
 {"heading":"Where it is used",
  "body":"Tides, daylight hours, average monthly temperature, AC voltage and biological "
         "rhythms are all fitted with exactly this model."},
]
def _period_tex(unit, period_deg):
    turn = r"2\pi" if unit == "rad" else r"360^\circ"
    val = _disp(period_deg, unit)
    return r"\(\dfrac{" + turn + r"}{|B|} = " + val + r"\)"


@register(
    slug="trig-modelling-periodic", name="Modelling Periodic Phenomena",
    section="maths", sub="Advanced Applications", topic="Trigonometry", order=50,
    summary="Explore y = A sin(B(x − C)) + D and read off amplitude, period, phase shift "
            "and midline for a periodic model, in degrees or radians.",
    formula="y = A sin(B(x − C)) + D — amplitude |A|, period 360°/B, midline D",
    tags=["periodic model","sinusoidal model","amplitude period phase","tides",
          "midline","Year 11 Mathematics Advanced"],
    viz_template="viz/trig-modelling-periodic.html",
    related=["trig-waves-applications","trig-period-amplitude"],
)
def compute(A=2, B=2, C=30, D=1, angle_unit="deg", **_ignored):
    unit="rad" if str(angle_unit)=="rad" else "deg"
    try: Av,Bv,Cv,Dv=float(A),float(B),float(C),float(D)
    except (TypeError,ValueError):
        return {"error":"A, B, C and D must be numbers.","steps":[],"disclaimer":_DISCLAIMER}
    if abs(Bv)<1e-12:
        return {"error":"B must be non-zero (it sets the period).","steps":[],"disclaimer":_DISCLAIMER}
    period_deg=360.0/abs(Bv)
    amp=abs(Av); ymax=Dv+amp; ymin=Dv-amp
    steps=[
        {"label":"Amplitude","math":rf"\(|A| = |{_fmt(Av)}| = {_fmt(amp)}\)","note":"Half the peak-to-trough height."},
        {"label":"Period","math":_period_tex(unit, period_deg),
         "note":"One full cycle in x."},
        {"label":"Phase shift and midline","math":rf"\(\text{{shift right by }} C={_fmt(Cv)},\quad \text{{midline }} y=D={_fmt(Dv)}\)",
         "note":f"Maximum y = {_fmt(ymax)}, minimum y = {_fmt(ymin)}."},
    ]
    return {"result":f"amplitude {_fmt(amp)}, period {_disp(period_deg,unit)}, midline y={_fmt(Dv)}",
            "A":Av,"B":Bv,"C":Cv,"D":Dv,"amplitude":amp,"period_deg":round(period_deg,4),
            "ymax":round(ymax,4),"ymin":round(ymin,4),"angle_unit":unit,
            "steps":steps,"explanation":_EXPLANATION,"disclaimer":_DISCLAIMER}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
