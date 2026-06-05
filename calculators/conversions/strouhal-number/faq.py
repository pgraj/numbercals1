from core.faqs import register_faqs

register_faqs("strouhal-number", [
    {"q": "What is the St (Strouhal Number)?",
     "a": "The Strouhal number relates vortex shedding frequency to flow speed and body size. It predicts the rhythm of wakes behind bluff bodies and the risk of resonant vibration."},
    {"q": "Can you show a worked example?",
     "a": "f=20, L=0.1, v=10 → St = (20·0.1)/10 = 0.20 → typical von Kármán wake range."},
    {"q": "How do I read the graph?",
     "a": "The visualisation places your computed St against colour-coded regime zones, "
          "with a live marker so you can see at a glance which flow or transfer regime your "
          "inputs fall into and how close you are to the next threshold."},
    {"q": "Where is this used in real life?",
     "a": "Predicting vortex-induced vibration on chimneys, cables, bridges and heat-exchanger tubes."},
    {"q": "What are the limits or edge cases?",
     "a": "All inputs must be physically valid; a zero in the denominator (e.g. zero viscosity, "
          "velocity or conductivity) is rejected rather than producing infinity. Regime "
          "thresholds are standard textbook values and can shift with geometry and conditions."},
])
