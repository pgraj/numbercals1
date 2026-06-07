from core.faqs import register_faqs

register_faqs("trig-double-angle", [
    {"q": 'What are the double-angle formulae?',
     "a": 'sin 2A = 2 sinA cosA; cos 2A = cos²A − sin²A (also 2cos²A − 1 and 1 − 2sin²A); and tan 2A = 2tanA/(1 − tan²A). They come from putting B = A in the compound-angle formulae.'},
    {"q": 'Why are there three forms of cos 2A?',
     "a": 'Starting from cos²A − sin²A and using sin²A + cos²A = 1 you can replace one term to get 2cos²A − 1 or 1 − 2sin²A. Pick the form that leaves only the function you need.'},
    {"q": 'Can you show a worked example?',
     "a": 'For A = 30°, sin 2A = 2 sin30 cos30 = 2 × 0.5 × 0.8660 ≈ 0.8660 = sin 60°. The same angle in radians is 30° = π/6 ≈ 0.5236 rad; the toggle re-derives in radians.'},
    {"q": 'When is tan 2A undefined?',
     "a": 'When 1 − tan²A = 0, i.e. A is an odd multiple of 45° (π/4 rad), or when 2A is an odd multiple of 90°. The calculator flags these instead of returning a wrong number.'},
    {"q": 'Where are they used?',
     "a": 'Lowering powers for integration, deriving the half-angle formulae, and modelling frequency doubling in optics, AC power and signal processing.'},
])
