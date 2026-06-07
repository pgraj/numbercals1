from core.faqs import register_faqs

register_faqs("trig-complex-numbers-euler", [
    {"q": "What is Euler's formula?",
     "a": 'e^{iθ} = cos θ + i sin θ. It links the exponential function to trigonometry, so a complex number of modulus r and argument θ is r·e^{iθ} = r(cos θ + i sin θ).'},
    {"q": "What is de Moivre's theorem?",
     "a": '(r(cos θ + i sin θ))ⁿ = rⁿ(cos nθ + i sin nθ): raise the modulus to the power and multiply the argument by n.'},
    {"q": 'Can you show a worked example?',
     "a": 'For z = 2(cos 40° + i sin 40°), z³ = 2³(cos 120° + i sin 120°) = 8(cos 120° + i sin 120°). In radians the argument is 40° ≈ 0.6981 rad and the result argument is 120° ≈ 2.0944 rad.'},
    {"q": 'What is the Argand diagram?',
     "a": 'A plane where the horizontal axis is the real part and the vertical axis the imaginary part, so a complex number is a point — and z and zⁿ can be drawn as rays from the origin.'},
    {"q": 'Where is this used?',
     "a": 'Deriving multiple-angle identities, finding the n roots of a complex number, AC circuit phasors, and the Fourier transform.'},
])
