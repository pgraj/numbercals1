from core.faqs import register_faqs

register_faqs('normality', [
    {"q": 'What is normality?',
     "a": "It is concentration measured in reactive equivalents per litre, instead of moles per litre. An equivalent is one unit of reacting power - one proton for an acid, one electron for a redox reaction. It tells you the solution's reactive capacity directly."},
    {"q": 'How is it different from molarity?',
     "a": 'Molarity counts moles; normality counts reactive units. They link by N = M × (units per molecule). Sulfuric acid gives 2 protons, so its normality is twice its molarity - 0.05 M but 0.1 N.'},
    {"q": 'What is equivalent weight?',
     "a": 'It is the molar mass divided by how many reactive units each molecule provides. For H₂SO₄ (2 protons), it is 98 ÷ 2 = 49 - the value in the example. It expresses reactive capacity per gram.'},
    {"q": 'Why is normality handy in titrations?',
     "a": 'Because at the endpoint, equivalents of acid equal equivalents of base: N₁V₁ = N₂V₂. That one neat relationship lets you find an unknown concentration without separately tracking protons or electrons.'},
    {"q": 'Is normality still used?',
     "a": 'Less in modern teaching (molarity is preferred), but heavily in analytical chemistry, water testing, and titration work where the equivalents idea genuinely simplifies the maths. Knowing both is a core lab skill.'},
])
