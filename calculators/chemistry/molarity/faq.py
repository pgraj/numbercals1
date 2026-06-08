from core.faqs import register_faqs

register_faqs('molarity', [
    {"q": 'What is molarity in simple terms?',
     "a": "It is how strong a solution is, measured as the number of moles of dissolved stuff in each litre of solution. A higher molarity means a more concentrated solution. It is the chemist's everyday way of saying 'how much is dissolved in here'."},
    {"q": 'Why turn grams into moles first?',
     "a": 'Because reactions and concentrations are about the number of particles, not their weight. A gram of a light substance has far more particles than a gram of a heavy one. Dividing mass by molar mass converts grams into moles, which counts the actual particles.'},
    {"q": 'What is the difference from molality?',
     "a": 'Molarity is per litre of solution (a volume), molality is per kilogram of solvent (a mass). Molarity changes a little with temperature because liquids expand; molality never does. Labs use molarity for convenience, molality for precise temperature-sensitive work.'},
    {"q": 'Why does 4.9 g of H₂SO₄ in 1 litre give 0.05 M?',
     "a": "Sulfuric acid weighs about 98 g per mole, so 4.9 g is 4.9 ÷ 98 = 0.05 mole. In 1 litre that is 0.05 mol/L, or 0.05 M. The clean numbers make it easy to see the 'moles per litre' idea."},
    {"q": 'What mistake do students make most?',
     "a": 'Using the volume of water added instead of the final solution volume. Molarity is defined by the total volume after everything is mixed, which can differ from the water you started with. Also forgetting to convert millilitres to litres.'},
])
