"""Real-world trig: sound beats. Maths > Real-World Trigonometry > Acoustics & Music."""
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
_EXPLANATION=[
 {"heading":"What a beat is","body":"Two tones of nearly equal frequency add to a sound that throbs in "
  "loudness. The throb rate is the beat frequency, f_beat = |f\u2081 \u2212 f\u2082|."},
 {"heading":"The trig behind it","body":"sin(2\u03c0f\u2081t) + sin(2\u03c0f\u2082t) factors into a fast tone at "
  "the average frequency, multiplied by a slow envelope at half the difference \u2014 that envelope is what "
  "you hear pulsing."},
 {"heading":"Using it","body":"Musicians tune by listening for beats: as two strings approach the same "
  "pitch, the beats slow and vanish at unison. Two notes 440 Hz and 444 Hz give 4 beats per second."},
]
@register(
    slug="rw-sound-beat", name="Sound Beat Frequency",
    section="maths", topic="Real-World Trigonometry", sub="Acoustics & Music", order=0,
    summary="Find the beat frequency of two close tones, f_beat = |f\u2081 \u2212 f\u2082|, and see how the two "
            "waves combine into a pulsing envelope.",
    formula="f_beat = |f\u2081 \u2212 f\u2082|;  sin(2\u03c0f\u2081t) + sin(2\u03c0f\u2082t)",
    tags=["sound beats","beat frequency","superposition","tuning","acoustics","real world trigonometry"],
    viz_template="viz/rw-sound-beat.html",
    related=["rw-ac-circuit","trig-waves-applications"],
)
def compute(freq1=440, freq2=444, **_ignored):
    try: f1=float(freq1); f2=float(freq2)
    except (TypeError,ValueError):
        return {"error":"Both frequencies must be numbers.","steps":[],"disclaimer":_DISCLAIMER}
    if f1<=0 or f2<=0: return {"error":"Frequencies must be greater than zero.","steps":[],"disclaimer":_DISCLAIMER}
    fbeat=abs(f1-f2); favg=(f1+f2)/2
    steps=[
        {"label":"Combine the two tones","math":r"\(\sin(2\pi f_1 t)+\sin(2\pi f_2 t)\)","note":"Equal-amplitude tones."},
        {"label":"Factor (sum-to-product)","math":r"\(=2\cos\!\left(2\pi\tfrac{f_1-f_2}{2}t\right)\sin\!\left(2\pi\tfrac{f_1+f_2}{2}t\right)\)",
         "note":"A slow envelope times a fast tone."},
        {"label":"Beat frequency","math":rf"\(f_{{beat}}=|f_1-f_2|=|{_f(f1)}-{_f(f2)}|={_f(fbeat)}\text{{ Hz}}\)",
         "note":f"You hear {_f(fbeat)} loudness pulses per second."},
    ]
    return {"result":f"beat \u2248 {_f(fbeat)} Hz","freq1":f1,"freq2":f2,"beat":round(fbeat,4),
            "avg":round(favg,4),"steps":steps,"explanation":_EXPLANATION,"disclaimer":_DISCLAIMER}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
