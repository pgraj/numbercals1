from core.faqs import register_faqs

register_faqs("beam-deflection", [
    {"q": "Is this suitable for designing a real beam?",
     "a": "No. It is an educational estimate using the textbook formula for one simple case. Real design needs code-based load factors, multiple load cases and a qualified structural engineer."},
    {"q": "What case does it cover?",
     "a": "A simply-supported beam (resting on a support at each end) carrying a single point load right at the centre. The deflection is greatest at midspan, which is what it reports."},
    {"q": "What is the formula?",
     "a": "Deflection equals P L cubed over 48 E I, where P is the load, L the span, E the material's stiffness (Young's modulus) and I the cross-section's moment of inertia."},
    {"q": "Why does span matter so much?",
     "a": "Because deflection depends on the span cubed. Doubling the span makes the beam sag eight times as much, all else equal, which is why long spans need much stiffer sections."},
    {"q": "What are E and I?",
     "a": "E (Young's modulus) measures how stiff the material is, around 200 GPa for steel. I (moment of inertia) measures how the cross-section's shape resists bending, bigger for deeper sections."},
])
