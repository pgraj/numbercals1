from core.faqs import register_faqs

register_faqs("trig-half-angle", [
    {"q": 'What are the half-angle formulae?',
     "a": 'sin(A/2) = ±√((1−cosA)/2), cos(A/2) = ±√((1+cosA)/2), and tan(A/2) = (1−cosA)/sinA = sinA/(1+cosA). They come from rearranging the double-angle forms of cos 2θ.'},
    {"q": 'How do I choose the ± sign?',
     "a": 'By the quadrant the half-angle A/2 falls in. For example if A/2 is in the second quadrant, sin(A/2) is positive and cos(A/2) is negative. This calculator picks the sign from the actual half-angle.'},
    {"q": 'Can you show a worked example?',
     "a": 'For A = 60°, sin(A/2) = sin30° = √((1−cos60°)/2) = √((1−0.5)/2) = 0.5. In radians 60° = π/3 ≈ 1.0472 rad and A/2 = π/6; switch the toggle to see it that way.'},
    {"q": 'What is the t-formula?',
     "a": 'Writing t = tan(A/2) gives sinA = 2t/(1+t²), cosA = (1−t²)/(1+t²) and tanA = 2t/(1−t²). It turns trig equations into algebra and is key to integrating rational trig functions.'},
    {"q": 'Where are they used?',
     "a": 'The t-formula substitution in integration, solving certain trig equations, and deriving exact values for angles such as 15° and 22.5°.'},
])
