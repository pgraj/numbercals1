"""Real-world trig: tide prediction. Maths > Real-World Trigonometry > Oceanography."""
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
 {"heading":"Tides as a sine wave","body":"Tide height rises and falls roughly sinusoidally: "
  "h(t) = A·sin(2\u03c0t/T) + mean. A is the tidal amplitude, T the period, and the mean is the average "
  "sea level."},
 {"heading":"The tidal period","body":"A semi-diurnal tide repeats about every 12.42 hours (two highs and "
  "two lows a day), set by the Moon's pull. T = 12.42 h is the usual value."},
 {"heading":"Reading a tide chart","body":"High tide is mean + A, low tide is mean \u2212 A. The model gives a "
  "quick estimate between published high/low times \u2014 real tide tables add several harmonic terms."},
]
@register(
    slug="rw-tide-prediction", name="Tide Height Prediction",
    section="maths", topic="Real-World Trigonometry", sub="Oceanography", order=0,
    summary="Estimate tide height at any time with h(t) = A·sin(2\u03c0t/T) + mean level, with the tidal "
            "phase angle in degrees or radians.",
    formula="h(t) = A·sin(2\u03c0t/T) + mean",
    tags=["tide prediction","tidal height","sine model","oceanography","periodic","real world trigonometry"],
    viz_template="viz/rw-tide-prediction.html",
    related=["rw-ferris-wheel","trig-modelling-periodic"],
)
def compute(amplitude=2.0, period=12.42, mean_level=3.0, time=3.105, angle_unit="deg", **_ignored):
    u="rad" if str(angle_unit)=="rad" else "deg"
    try: A=float(amplitude); T=float(period); mean=float(mean_level); t=float(time)
    except (TypeError,ValueError):
        return {"error":"Amplitude, period, mean level and time must be numbers.","steps":[],"disclaimer":_DISCLAIMER}
    if T<=0: return {"error":"The period must be greater than zero.","steps":[],"disclaimer":_DISCLAIMER}
    phase_deg=(360.0*t/T)%360.0
    h=A*math.sin(2*math.pi*t/T)+mean
    steps=[
        {"label":"State the model","math":r"\(h(t)=A\sin\!\left(\frac{2\pi t}{T}\right)+\text{mean}\)",
         "note":"A amplitude, T period, mean average sea level."},
        {"label":"Phase at time t","math":rf"\(\frac{{2\pi t}}{{T}} = {_tex(phase_deg,u)}\)",
         "note":f"After {_f(t)} h the tide is {_disp(phase_deg,u)} through its cycle."},
        {"label":"Substitute","math":rf"\(h={_f(A)}\sin({_tex(phase_deg,u)})+{_f(mean)}\)","note":"Insert the values."},
        {"label":"Tide height","math":rf"\(h \approx {_f(h)}\)",
         "note":f"High = {_f(mean+A)}, low = {_f(mean-A)}."},
    ]
    return {"result":f"height \u2248 {_f(h)}","amplitude":A,"period":T,"mean":mean,"time":t,
            "phase_deg":round(phase_deg,4),"height":round(h,4),"high":round(mean+A,4),"low":round(mean-A,4),
            "angle_unit":u,"steps":steps,"explanation":_EXPLANATION,"disclaimer":_DISCLAIMER}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
