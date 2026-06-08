from core.faqs import register_faqs

register_faqs('hess-law', [
    {"q": "What does Hess's law say?",
     "a": "The total heat of a reaction is the same no matter how many steps it takes - because energy depends only on the start and end states (enthalpy is a 'state function')."},
    {"q": 'Why is it useful?',
     "a": 'It lets you find the heat of a reaction that is hard to measure directly, by adding up easier reactions that sum to it.'},
    {"q": "What does 'state function' mean?",
     "a": 'A quantity that depends only on the current state, not the path taken - like altitude between two towns being fixed whatever road you drive. Enthalpy is one.'},
    {"q": 'Exothermic vs endothermic?',
     "a": 'Negative ΔH = releases heat (exothermic, like burning). Positive ΔH = absorbs heat (endothermic, like a cold pack). The sign tells you which.'},
    {"q": 'How does the example give −150?',
     "a": 'ΔH = −400 − (−250) = −150 kJ/mol. Products sit lower in energy than reactants, so it releases 150 kJ - exothermic.'},
])
