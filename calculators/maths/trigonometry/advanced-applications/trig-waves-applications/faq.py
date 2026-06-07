from core.faqs import register_faqs

register_faqs("trig-waves-applications", [
    {"q": 'What does a sin x + b cos x = R sin(x + α) mean?',
     "a": 'Two waves of the same frequency, one a sine and one a cosine, always add to a single sine wave with amplitude R and phase shift α.'},
    {"q": 'How do I find R and α?',
     "a": 'R = √(a² + b²) by Pythagoras on the coefficients, and α = arctan(b/a) (using atan2 for the right quadrant).'},
    {"q": 'Can you show a worked example?',
     "a": '3 sin x + 4 cos x: R = √(9+16) = 5 and α = arctan(4/3) ≈ 53.13°, so it equals 5 sin(x + 53.13°). In radians α ≈ 0.9273 rad; the toggle shows it that way.'},
    {"q": 'Why is this useful?',
     "a": 'It combines two oscillations into one, which is how alternating currents, sound from two sources, and combined displacements are simplified.'},
    {"q": 'What if a and b are both zero?',
     "a": 'Then R = 0 and there is no wave to combine; the calculator flags this.'},
])
