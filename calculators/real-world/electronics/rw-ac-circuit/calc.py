"""Real-world trig: AC circuit voltage. Maths > Real-World Trigonometry > Electronics."""
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
 {"heading":"Alternating current is a sine wave","body":"Mains voltage rises and falls as a sine curve: "
  "v(t) = V·sin(2\u03c0ft + \u03c6). V is the peak voltage, f the frequency (50 Hz in Australia), and "
  "\u03c6 the phase offset."},
 {"heading":"Frequency and period","body":"f cycles per second means the period is T = 1/f. At 50 Hz one "
  "full cycle takes 0.02 s. The 2\u03c0f converts cycles into radians of angle per second."},
 {"heading":"Peak vs RMS","body":"The peak V is the maximum; the everyday 'voltage' quoted (230 V in "
  "Australia) is the RMS value, V/\u221a2. A 230 V supply has a peak of about 325 V."},
]
@register(
    slug="rw-ac-circuit", name="AC Circuit Voltage",
    section="maths", topic="Real-World Trigonometry", sub="Electronics", order=0,
    summary="Find the instantaneous voltage of an AC supply with v(t) = V·sin(2\u03c0ft + \u03c6), with the "
            "phase angle in degrees or radians.",
    formula="v(t) = V·sin(2\u03c0ft + \u03c6)",
    tags=["AC circuit","alternating current","voltage","frequency","phase","real world trigonometry"],
    viz_template="viz/rw-ac-circuit.html",
    related=["rw-sound-beat","trig-waves-applications"],
)
def compute(peak=325, freq=50, phase=0, time=0.005, angle_unit="deg", **_ignored):
    u="rad" if str(angle_unit)=="rad" else "deg"
    try: V=float(peak); f=float(freq); ph_in=float(phase); t=float(time)
    except (TypeError,ValueError):
        return {"error":"Peak, frequency, phase and time must be numbers.","steps":[],"disclaimer":_DISCLAIMER}
    if f<=0: return {"error":"Frequency must be greater than zero.","steps":[],"disclaimer":_DISCLAIMER}
    ph_deg = math.degrees(ph_in) if u=="rad" else ph_in
    arg = 2*math.pi*f*t + math.radians(ph_deg)
    v = V*math.sin(arg)
    T = 1.0/f
    rms = V/math.sqrt(2)
    steps=[
        {"label":"State the model","math":r"\(v(t)=V\sin(2\pi f t + \varphi)\)","note":"V peak, f frequency, \u03c6 phase."},
        {"label":"Period","math":rf"\(T=1/f=1/{_f(f)}={_f(T)}\text{{ s}}\)","note":"One full cycle."},
        {"label":"Substitute","math":rf"\(v={_f(V)}\sin(2\pi\cdot{_f(f)}\cdot{_f(t)}+{_tex(ph_deg,u)})\)",
         "note":"Insert peak, frequency, time and phase."},
        {"label":"Instantaneous voltage","math":rf"\(v \approx {_f(v)}\text{{ V}}\)",
         "note":f"RMS (quoted) voltage = V/\u221a2 \u2248 {_f(rms)} V."},
    ]
    return {"result":f"v \u2248 {_f(v)} V","peak":V,"freq":f,"phase_deg":round(ph_deg,4),"time":t,
            "voltage":round(v,4),"period":round(T,6),"rms":round(rms,4),"angle_unit":u,
            "steps":steps,"explanation":_EXPLANATION,"disclaimer":_DISCLAIMER}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
