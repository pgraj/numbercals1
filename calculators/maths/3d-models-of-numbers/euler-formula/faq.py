# -*- coding: utf-8 -*-
from core.faqs import register_faqs

register_faqs("euler-formula", [
    {"q": "What is Euler's formula?", "a": 'e^(iθ) = cos θ + i sin θ. It says that raising e to an imaginary power traces a circle in the complex plane.'},
    {"q": 'Why is the helix shape?', "a": 'The angle θ runs along one axis while cosine and sine spin around it, so a circle stretched over time becomes a helix.'},
    {"q": "What is Euler's identity?", "a": 'Setting θ = π gives e^(iπ) + 1 = 0, linking five fundamental constants - e, i, π, 1 and 0 - in one line.'},
    {"q": 'Where is it used?', "a": 'Electrical engineering, signal processing and physics all use it to handle waves as rotating arrows (phasors).'},
    {"q": 'Do I need imaginary numbers for real life?', "a": 'Yes, indirectly - the maths of AC electricity, radio and audio is far simpler written with i, even though the final answers are real.'},
])
