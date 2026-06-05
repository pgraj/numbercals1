from core.faqs import register_faqs

register_faqs("nusselt-number", [
    {"q": "What is the Nu (Nusselt Number)?",
     "a": "The Nusselt number is the ratio of convective to conductive heat transfer across a boundary. Nu≈1 means conduction only; large Nu means convection is carrying most of the heat."},
    {"q": "Can you show a worked example?",
     "a": "h=100, L=0.5, k=0.6 → Nu = (100·0.5)/0.6 ≈ 83.3 → convection dominates conduction."},
    {"q": "How do I read the graph?",
     "a": "The visualisation places your computed Nu against colour-coded regime zones, "
          "with a live marker so you can see at a glance which flow or transfer regime your "
          "inputs fall into and how close you are to the next threshold."},
    {"q": "Where is this used in real life?",
     "a": "Sizing heat exchangers, electronics cooling and any forced/natural convection problem."},
    {"q": "What are the limits or edge cases?",
     "a": "All inputs must be physically valid; a zero in the denominator (e.g. zero viscosity, "
          "velocity or conductivity) is rejected rather than producing infinity. Regime "
          "thresholds are standard textbook values and can shift with geometry and conditions."},
])
