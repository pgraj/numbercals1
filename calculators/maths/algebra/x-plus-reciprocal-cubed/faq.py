from core.faqs import register_faqs

register_faqs('x-plus-reciprocal-cubed', [
    {"q": 'How do I get to the cube from just knowing x + 1/x?',
     "a": 'Cube the known value. (x + 1/x)³ expands to x³ + 3x + 3/x + 1/x³, which is x³ + 1/x³ plus 3(x + 1/x). So x³ + 1/x³ = (x+1/x)³ − 3(x+1/x) = a³ − 3a. Just as with the squared version, you reach a higher power purely from the value a = x + 1/x, never needing x itself. If x + 1/x = 2, then x³ + 1/x³ = 8 − 6 = 2, instantly.'},
    {"q": 'Where does the −3a term come from?',
     "a": 'From the middle terms of the cube. Expanding (x + 1/x)³ gives x³ + 3x²·(1/x) + 3x·(1/x²) + 1/x³ = x³ + 3x + 3/x + 1/x³. The two middle terms, 3x and 3/x, together make 3(x + 1/x) = 3a. To isolate x³ + 1/x³ you subtract them off, giving a³ − 3a. The coefficient 3 is the binomial coefficient, and the cross-terms simplify neatly because x·(1/x) = 1.'},
    {"q": 'Why are these climbing identities (square, then cube) so useful together?',
     "a": 'They form a ladder. From a = x + 1/x you get x² + 1/x² = a² − 2, then x³ + 1/x³ = a³ − 3a, and you can keep going to fourth and fifth powers using recurrence relations. Each rung is built from the ones below. This lets you evaluate high powers of x + 1/x-type expressions efficiently, which is exactly what competition problems and certain physics and engineering recurrences demand.'},
    {"q": 'Do these reciprocal-power identities appear in real applications?',
     "a": 'Yes - in signal processing and physics through their close cousins. Quantities like e^(iθ) + e^(−iθ) = 2cos θ behave exactly like x + 1/x with x on the unit circle, and powers of them relate to multiple-angle formulas (cos 3θ in terms of cos θ, etc.). So these identities are the algebraic backbone of the trigonometric multiple-angle formulas used throughout waves, oscillations, and Fourier analysis.'},
    {"q": 'Is there a pattern to the constants −2, −3a, and so on?',
     "a": 'Yes - they come from a recurrence. If you write p(n) = xⁿ + 1/xⁿ, then p(n) = a·p(n−1) − p(n−2), starting from p(0) = 2 and p(1) = a. This gives p(2) = a²−2, p(3) = a³−3a, p(4) = a⁴−4a²+2, and so on (the Chebyshev-like pattern). Recognising the recurrence means you never have to re-derive each one; you just step up the ladder.'},
])
