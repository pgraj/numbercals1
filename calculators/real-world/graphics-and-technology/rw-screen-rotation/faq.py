from core.faqs import register_faqs

register_faqs("rw-screen-rotation", [
    {"q": 'How do you rotate a point?',
     "a": 'About the origin by angle θ: x′ = x·cosθ − y·sinθ and y′ = x·sinθ + y·cosθ. These are the rows of the 2-D rotation matrix.'},
    {"q": 'Where is this used?',
     "a": 'Whenever a screen reorients, a game sprite spins, or a graphic turns — the device computes new coordinates with exactly these formulas.'},
    {"q": 'Can you show a worked example?',
     "a": 'Rotating (3, 0) by 90°: x′ = 3·cos90° − 0 = 0, y′ = 3·sin90° + 0 = 3, giving (0, 3) — a quarter turn anticlockwise.'},
    {"q": 'Which way is positive?',
     "a": 'Positive angles rotate anticlockwise (the maths convention); negative angles rotate clockwise.'},
    {"q": 'Degrees or radians?',
     "a": 'Either — the toggle converts the angle; 90° is π/2 ≈ 1.5708 rad, and the result is the same.'},
])
