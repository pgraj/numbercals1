from core.faqs import register_faqs

register_faqs("trig-solving-equations", [
    {"q": 'How do I solve a trig equation over a domain?',
     "a": "Take the principal value from the inverse function, then use the function's symmetry to find the partner solutions, keeping only those inside the stated domain (usually one full turn)."},
    {"q": 'Can you show a worked example?',
     "a": 'For sin x = 0.5 over [0°,360°): sin⁻¹(0.5) = 30°, and the supplement 180°−30° = 150°, so x = 30° or 150°. In radians the domain is [0,2π) and the answers are π/6 ≈ 0.5236 and 5π/6 ≈ 2.6180 rad.'},
    {"q": 'Why can an equation have no solution?',
     "a": 'sin x and cos x always lie between −1 and 1, so sin x = 2 has no solution. tan x can equal any real number, so a tangent equation always has solutions.'},
    {"q": 'How many solutions are there in one turn?',
     "a": 'Usually two for sine and cosine (a value and its symmetric partner) and one for tangent per 180°, but at special values such as sin x = 1 the two partners coincide into a single solution.'},
    {"q": 'Where is this used?',
     "a": 'Finding when an oscillation reaches a given value — times of a given tide height, phase angles in AC circuits, or launch angles that hit a target.'},
])
