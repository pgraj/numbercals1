from core.faqs import register_faqs

register_faqs("mach-number", [
    {"q": "What is the M (Mach Number)?",
     "a": "The Mach number is an object's speed divided by the local speed of sound. It tells you whether compressibility effects matter — subsonic below 0.8, transonic near 1, supersonic above 1.2, and hypersonic above 5."},
    {"q": "Can you show a worked example?",
     "a": "v=340, γ=1.4, R=287, T=288 → a=√(1.4·287·288)=340.2 → M ≈ 1.0 → Transonic."},
    {"q": "How do I read the graph?",
     "a": "The visualisation places your computed M against colour-coded regime zones, "
          "with a live marker so you can see at a glance which flow or transfer regime your "
          "inputs fall into and how close you are to the next threshold."},
    {"q": "Where is this used in real life?",
     "a": "Aircraft and missile design, wind-tunnel testing and compressible-flow analysis."},
    {"q": "What are the limits or edge cases?",
     "a": "All inputs must be physically valid; a zero in the denominator (e.g. zero viscosity, "
          "velocity or conductivity) is rejected rather than producing infinity. Regime "
          "thresholds are standard textbook values and can shift with geometry and conditions."},
])
