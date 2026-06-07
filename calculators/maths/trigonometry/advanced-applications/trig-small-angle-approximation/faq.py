from core.faqs import register_faqs

register_faqs("trig-small-angle-approximation", [
    {"q": 'What are the small-angle approximations?',
     "a": 'For small angles in radians, sin x ≈ x, tan x ≈ x and cos x ≈ 1 − x²/2. The smaller the angle, the better the fit.'},
    {"q": 'Why must the angle be in radians?',
     "a": "The approximations come from the functions' series expansions in radians. In degrees they are simply wrong, so this calculator works in radians."},
    {"q": 'Can you show a worked example?',
     "a": 'At x = 0.1 rad, sin x = 0.09983… while the approximation gives 0.1 — an error of about 0.17%. At x = 0.01 the error is far smaller still.'},
    {"q": "How small is 'small'?",
     "a": 'There is no hard cut-off, but below about 0.1–0.2 rad (roughly 6°–12°) the error is well under 1% for sine and tangent.'},
    {"q": 'Where are they used?',
     "a": 'The simple pendulum (sin θ ≈ θ), optics (small-angle diffraction and lens formulae) and linearising equations in physics and engineering.'},
])
