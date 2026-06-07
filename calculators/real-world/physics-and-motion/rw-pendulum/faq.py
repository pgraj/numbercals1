from core.faqs import register_faqs

register_faqs("rw-pendulum", [
    {"q": "What sets a pendulum's period?",
     "a": 'T = 2π√(L/g): only the length L and gravity g (9.81 m/s²). Mass does not matter, and for small swings neither does the amplitude — which is why pendulum clocks keep time.'},
    {"q": 'How does the angle change over time?',
     "a": 'For small swings, θ(t) = θ₀·cos(2πt/T) — simple harmonic motion, starting at θ₀ and swinging symmetrically.'},
    {"q": 'Can you show a worked example?',
     "a": 'A 1 m pendulum has T = 2π√(1/9.81) ≈ 2.006 s. Starting at 10°, after 0.5 s it has nearly reached the far side.'},
    {"q": "Why does it say 'small angle'?",
     "a": 'The formula relies on sinθ ≈ θ in radians, valid for small swings. Beyond about 20° the true period grows slightly longer than 2π√(L/g).'},
    {"q": 'Degrees or radians?',
     "a": 'The swing angle can be entered and shown in either; 10° is about 0.1745 rad.'},
])
