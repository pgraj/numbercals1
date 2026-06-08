from core.faqs import register_faqs

register_faqs('mole-fraction', [
    {"q": 'What does mole fraction tell you?',
     "a": "What share of all the particles in a mixture is one component, counted in moles. A mole fraction of one-third means one in three particles is that component. It is always between 0 and 1, and all components' fractions add to 1."},
    {"q": 'Where is it used?',
     "a": "In gas mixtures (a gas's mole fraction is its share of the pressure) and in solutions (it drives vapour pressure and the colligative properties). It is the natural measure whenever the proportion of particles matters."},
    {"q": 'Why not just use mass percent?',
     "a": 'Because behaviour depends on the number of particles, not weight. Equal masses of a light and a heavy substance have very different particle counts. Mole fraction counts particles directly, which is why gas and solution laws use it.'},
    {"q": 'Why do mole fractions add up to 1?',
     "a": 'Because every particle belongs to one component, so the shares must account for the whole - and the whole, as a fraction, is 1. In the example x_A = 1/3 and x_B = 2/3, which sum to 1. It is a built-in error check.'},
    {"q": 'How do I get it from masses?',
     "a": "First convert each mass to moles (divide by molar mass), then divide each component's moles by the total. You cannot use masses directly because equal masses hold different numbers of moles. That conversion step is where students slip up."},
])
