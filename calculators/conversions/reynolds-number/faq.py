from core.faqs import register_faqs

register_faqs("reynolds-number", [
    {"q": "What is the Re (Reynolds Number)?",
     "a": "The Reynolds number is the ratio of inertial to viscous forces in a flow. Below ~2,300 flow is laminar and orderly; above ~4,000 it is turbulent and chaotic; in between lies the transition band."},
    {"q": "Can you show a worked example?",
     "a": "ρ=1.225, v=50, L=2, μ=1.81e-5 → Re = (1.225·50·2)/1.81e-5 ≈ 6.77×10⁶ → Turbulent."},
    {"q": "How do I read the graph?",
     "a": "The visualisation places your computed Re against colour-coded regime zones, "
          "with a live marker so you can see at a glance which flow or transfer regime your "
          "inputs fall into and how close you are to the next threshold."},
    {"q": "Where is this used in real life?",
     "a": "Aerodynamics, pipe flow, ship hydrodynamics and any design where transition to turbulence matters."},
    {"q": "What are the limits or edge cases?",
     "a": "All inputs must be physically valid; a zero in the denominator (e.g. zero viscosity, "
          "velocity or conductivity) is rejected rather than producing infinity. Regime "
          "thresholds are standard textbook values and can shift with geometry and conditions."},
])
