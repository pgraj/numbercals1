from core.faqs import register_faqs

register_faqs("biot-number", [
    {"q": "What is the Bi (Biot Number)?",
     "a": "The Biot number compares heat transfer at a body's surface to conduction within it. Bi<0.1 means the body heats almost uniformly (lumped-capacitance valid); larger Bi means strong internal gradients."},
    {"q": "Can you show a worked example?",
     "a": "h=50, L=0.05, kₛ=50 → Bi = (50·0.05)/50 = 0.05 → below 0.1, lumped-capacitance valid."},
    {"q": "Where is this used in real life?",
     "a": "Transient heating/cooling: quenching, food processing and deciding if lumped-capacitance applies."},
    {"q": "What are the limits or edge cases?",
     "a": "All inputs must be physically valid; a zero in the denominator (e.g. zero viscosity, "
          "velocity or conductivity) is rejected rather than producing infinity. Regime "
          "thresholds are standard textbook values and can shift with geometry and conditions."},
    {"q": 'What decision does the Biot number actually drive?',
     "a": 'It tells you whether you can treat an object as a single uniform temperature. If Bi < 0.1, internal conduction keeps up with the surface and the simple lumped-capacitance model is valid. If Bi > 1, the core lags the surface badly and you must model temperature varying through the body.'},
])
