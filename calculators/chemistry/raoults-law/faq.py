from core.faqs import register_faqs

register_faqs('raoults-law', [
    {"q": "In one sentence, what is Raoult's law?",
     "a": 'Dissolving something in a liquid makes the liquid evaporate less, and the vapour pressure drops in proportion to how much of the liquid is still pure solvent.'},
    {"q": 'Why does dissolving solute lower vapour pressure?',
     "a": 'Evaporation happens at the surface. Dissolved solute particles sit among the solvent at the surface and block some solvent molecules from escaping, so fewer turn to vapour and the vapour pressure falls. The more solute, the bigger the effect.'},
    {"q": 'How does this connect to boiling and freezing?',
     "a": "Lower vapour pressure means the solution must be heated hotter before it boils (its vapour pressure reaches air pressure later), and it freezes at a lower temperature too. So Raoult's law is the root cause behind salted water boiling higher and icy roads being salted to melt."},
    {"q": 'What does the little circle in P_A° mean?',
     "a": "The circle (°) means 'pure' - P_A° is the vapour pressure of the solvent before anything is dissolved in it. P_A without the circle is the lower vapour pressure after solute has been added. The law links the two by the solvent's mole fraction."},
    {"q": "Where is Raoult's law used?",
     "a": 'In distillation - separating crude oil into petrol and diesel, purifying solvents, and making spirits - because it predicts what evaporates from a mixture and in what proportion. It also explains everyday things like salty water evaporating slower and is the foundation of the colligative properties.'},
])
