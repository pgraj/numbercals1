from core.faqs import register_faqs

register_faqs('rate-of-reaction', [
    {"q": 'What does rate of reaction measure?',
     "a": 'How fast a reaction goes - how quickly reactants are used up (or products made) per unit time. On a concentration-time graph it is the steepness of the curve.'},
    {"q": 'Why the minus sign?',
     "a": 'Because the reactant is being used up, so its change is negative. The minus flips it to a positive rate. If you track a product instead (which grows), no minus is needed.'},
    {"q": 'Where does it matter day to day?',
     "a": 'Food spoiling, medicine shelf life, fuel burning in an engine, cement setting, glow sticks. Anywhere a reaction needs to be sped up or slowed down in time.'},
    {"q": 'Why does the rate usually slow over time?',
     "a": 'Reactions need collisions, and as reactants run out there are fewer to collide, so the rate drops - the curve is steep at first and flattens later.'},
    {"q": 'How do you speed a reaction up?',
     "a": "Heat it, increase concentration or pressure, increase a solid's surface area, or add a catalyst. All make successful collisions more frequent or easier."},
])
