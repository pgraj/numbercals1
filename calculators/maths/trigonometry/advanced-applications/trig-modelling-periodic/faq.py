from core.faqs import register_faqs

register_faqs("trig-modelling-periodic", [
    {"q": 'What does y = A sin(B(x − C)) + D model?',
     "a": 'Any simple periodic signal. A is the amplitude, B sets the period, C is the horizontal (phase) shift and D is the midline the wave oscillates about.'},
    {"q": 'How do I read off the features?',
     "a": 'Amplitude = |A|; period = 360°/B (or 2π/B in radians); midline y = D, so maximum = D + |A| and minimum = D − |A|; the curve shifts right by C.'},
    {"q": 'Can you show a worked example?',
     "a": 'y = 2 sin(2(x − 30°)) + 1 has amplitude 2, period 360°/2 = 180°, midline y = 1, maximum 3 and minimum −1. In radians the period is π ≈ 3.1416 rad.'},
    {"q": 'How do I fit one to data?',
     "a": 'Read the midline as the average of max and min, the amplitude as half their difference, the period from peak-to-peak spacing, and the shift from where a peak occurs.'},
    {"q": 'Where is it used?',
     "a": 'Tides, daylight hours, monthly temperature, AC voltage and many biological rhythms are all modelled with this single sinusoid.'},
])
