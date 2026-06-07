from core.faqs import register_faqs

register_faqs("rw-ac-circuit", [
    {"q": 'Why is mains voltage a sine wave?',
     "a": 'Generators produce voltage that rises and falls sinusoidally: v(t) = V·sin(2πft + φ), where V is the peak, f the frequency, and φ the phase.'},
    {"q": 'What is the frequency in Australia?',
     "a": '50 Hz — fifty full cycles per second, so the period is T = 1/50 = 0.02 s.'},
    {"q": 'Can you show a worked example?',
     "a": 'With V = 325 V and f = 50 Hz, a quarter-period in (t = 0.005 s) reaches the peak: v ≈ 325 V.'},
    {"q": 'Why is 230 V quoted, not 325 V?',
     "a": '230 V is the RMS (effective) value; the peak is V = 230×√2 ≈ 325 V. RMS is what determines heating and power.'},
    {"q": 'Does phase use radians?',
     "a": 'The phase φ can be entered in degrees or radians; the toggle converts it. Internally the 2πft term is always in radians.'},
])
