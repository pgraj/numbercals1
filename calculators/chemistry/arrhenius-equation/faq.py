from core.faqs import register_faqs

register_faqs('arrhenius-equation', [
    {"q": 'What does the Arrhenius equation explain?',
     "a": 'Why reactions go faster when heated. Because temperature sits in an exponent, even a small rise gives a big jump in rate - roughly doubling for every 10°C.'},
    {"q": 'What is activation energy?',
     "a": "The energy 'hill' molecules must climb to react. A high hill means few make it over (slow); a low hill means many do (fast). Catalysts lower the hill."},
    {"q": 'Why does temperature have such a big effect?',
     "a": 'Because it sets the fraction of molecules with enough energy to clear the hill, and that fraction rises exponentially with temperature - so the rate climbs steeply, not linearly.'},
    {"q": 'How do catalysts fit in?',
     "a": 'They give a lower-energy path - a smaller hill - so k rises dramatically without adding heat, and the catalyst is not used up. Enzymes do this in your body.'},
    {"q": 'What are A and R?',
     "a": 'A is how often molecules collide with the right orientation (the top possible rate). R is the gas constant (8.314 J/mol·K) that keeps the units consistent in the exponent.'},
])
