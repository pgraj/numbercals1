from core.faqs import register_faqs

register_faqs('equilibrium-constant', [
    {"q": 'What does K_c tell you?',
     "a": 'Which side a reversible reaction favours at balance. Big K_c = mostly products; small K_c = mostly reactants; near 1 = a real mix. It is a single number for the position of equilibrium.'},
    {"q": 'Does adding more reactant change K_c?',
     "a": 'No - K_c is fixed at a given temperature. Add reactant and the system makes more product to restore the same ratio. Only temperature changes K_c itself.'},
    {"q": 'Where is it used in industry?',
     "a": 'Optimising reactions like the Haber process for ammonia - choosing conditions that push K_c toward the product you want, to maximise yield.'},
    {"q": 'Why are pure solids and liquids left out?',
     "a": 'Their concentration does not change, so they are folded into K_c. Only gases and dissolved species, whose concentrations vary, appear in the expression.'},
    {"q": 'How does K_c relate to Q?',
     "a": 'Q is the same ratio at any moment. If Q < K_c the reaction goes forward; if Q > K_c it goes backward; if equal, it is at equilibrium.'},
])
