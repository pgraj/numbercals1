from core.faqs import register_faqs

register_faqs("prandtl-number", [
    {"q": "What is the Pr (Prandtl Number)?",
     "a": "The Prandtl number compares how fast momentum diffuses versus heat. Pr<1 means heat spreads faster than momentum (thicker thermal layer); Pr>1 the reverse."},
    {"q": "Can you show a worked example?",
     "a": "Air: Cp=1005, μ=1.81e-5, k=0.0257 → Pr = (1005·1.81e-5)/0.0257 ≈ 0.708 → thermal layer slightly thicker."},
    {"q": "How do I read the graph?",
     "a": "The visualisation places your computed Pr against colour-coded regime zones, "
          "with a live marker so you can see at a glance which flow or transfer regime your "
          "inputs fall into and how close you are to the next threshold."},
    {"q": "Where is this used in real life?",
     "a": "Heat-exchanger design, boundary-layer analysis and convective heat-transfer correlations."},
    {"q": "What are the limits or edge cases?",
     "a": "All inputs must be physically valid; a zero in the denominator (e.g. zero viscosity, "
          "velocity or conductivity) is rejected rather than producing infinity. Regime "
          "thresholds are standard textbook values and can shift with geometry and conditions."},
])
