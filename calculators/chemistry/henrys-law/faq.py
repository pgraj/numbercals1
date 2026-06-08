from core.faqs import register_faqs

register_faqs('henrys-law', [
    {"q": "In one sentence, what is Henry's law?",
     "a": 'The more you press a gas against the surface of a liquid, the more of that gas dissolves into it - dissolved amount is directly proportional to the pressure above.'},
    {"q": 'Why does soda fizz when I open it but not before?',
     "a": "Sealed, the bottle holds a high CO₂ pressure that keeps lots of gas dissolved quietly. Opening it drops the pressure to normal air, so the liquid can no longer hold that much gas and the excess escapes as fizz. This is Henry's law happening in your hand."},
    {"q": 'Why does warm soda go flat faster than cold soda?',
     "a": "Gases dissolve less in warm liquids, so Henry's constant changes with temperature in a way that lets warm drinks hold less gas. A warm cola therefore loses its dissolved CO₂ faster and foams more when opened. Keeping drinks cold keeps the fizz in."},
    {"q": "What does a big Henry's constant mean?",
     "a": 'A big kₕ means the gas strongly resists dissolving, so you need a lot of pressure to push even a little in. A small kₕ means the gas dissolves easily. It is a fixed property of each particular gas-and-liquid pair at a given temperature.'},
    {"q": "Where else does Henry's law matter?",
     "a": "In your blood carrying oxygen and carbon dioxide, in fish needing dissolved oxygen in water (warm water holds less, which stresses them), in carbonating drinks at a factory, and in scuba diving where it explains decompression sickness. Anywhere a gas meets a liquid, Henry's law sets how much dissolves."},
])
