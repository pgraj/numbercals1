from core.faqs import register_faqs

register_faqs("trig-reciprocal", [
    {"q": 'What are sec, cosec and cot?',
     "a": 'They are the reciprocal trig functions: sec θ = 1/cos θ, cosec θ = 1/sin θ and cot θ = cos θ/sin θ (equivalently 1/tan θ).'},
    {"q": 'Can you show a worked example?',
     "a": 'sec 60° = 1/cos 60° = 1/0.5 = 2. The same angle in radians is 60° = π/3 ≈ 1.0472 rad; the toggle re-derives it in radians.'},
    {"q": 'Where are they undefined?',
     "a": 'sec and tan are undefined at 90° and 270° (cos = 0); cosec and cot are undefined at 0° and 180° (sin = 0). Their graphs have vertical asymptotes there.'},
    {"q": 'How do they connect to the Pythagorean identities?',
     "a": 'Dividing sin²+cos²=1 gives 1+tan²=sec² and 1+cot²=cosec², so the reciprocal functions appear directly in those identities.'},
    {"q": 'Where are they used?',
     "a": 'In calculus (the derivative of tan θ is sec²θ), in resolving forces, and anywhere the reciprocal of a ratio is the natural quantity.'},
])
