from core.faqs import register_faqs

register_faqs('molality', [
    {"q": 'Why use molality instead of molarity?',
     "a": 'Because it is per kilogram of solvent - a mass that does not change with temperature, unlike volume. So molality stays fixed when a solution is heated or cooled, which makes it the right choice for precise work and for freezing/boiling-point calculations.'},
    {"q": 'What is the difference between solvent and solution here?',
     "a": 'Molality uses the mass of the solvent alone (the dissolving liquid before adding solute). Molarity uses the total volume of the finished solution. Mixing these up is a common error.'},
    {"q": 'Where does molality show up day to day?',
     "a": 'Most visibly in antifreeze and road salt, where lowering the freezing point depends on molality. Also in raising boiling points for cooking and industry. Anywhere freezing or boiling points are deliberately shifted.'},
    {"q": 'Why does 1 mole in 1000 g give exactly 1 mol/kg?',
     "a": 'Because 1000 g is exactly 1 kilogram, so 1 mole in 1 kg is 1 mol/kg by definition - a deliberately clean example. The 1000 in the formula does the grams-to-kilograms conversion.'},
    {"q": 'Can molality and molarity ever be equal?',
     "a": 'For very dilute water solutions near 4°C they are nearly equal, because 1 litre of water weighs about 1 kg. As solutions get concentrated or use other solvents, the two values drift apart and must be converted using density.'},
])
