from core.faqs import register_faqs

register_faqs("trig-polar-coordinates", [
    {"q": 'What are polar coordinates?',
     "a": 'A point given by its distance r from the origin and the angle θ from the positive x-axis, written (r, θ), instead of by (x, y).'},
    {"q": 'How do I convert between forms?',
     "a": 'Polar to rectangular: x = r cos θ, y = r sin θ. Rectangular to polar: r = √(x² + y²) and θ = atan2(y, x), which gives the correct quadrant.'},
    {"q": 'Can you show a worked example?',
     "a": '(r, θ) = (5, 53.13°) gives x = 5 cos 53.13° ≈ 3 and y = 5 sin 53.13° ≈ 4. In radians 53.13° ≈ 0.9273 rad; the toggle shows θ that way.'},
    {"q": 'Why use atan2 instead of arctan?',
     "a": 'arctan(y/x) loses the quadrant, so a point in the third quadrant could be confused with the first. atan2(y, x) uses both signs to return the correct angle.'},
    {"q": 'Where are polar coordinates used?',
     "a": 'Radar and navigation, circular and spiral motion, and curves like cardioids and roses that are far simpler in polar form.'},
])
