from core.faqs import register_faqs

register_faqs('boiling-point-elevation', [
    {"q": 'Why does dissolved solute raise the boiling point?',
     "a": "Solute lowers the solvent's vapour pressure, and a liquid boils when its vapour pressure matches the air pressure - so it must be heated hotter to boil. The boiling point rises with the number of dissolved particles."},
    {"q": 'Does salt really make pasta water boil hotter?',
     "a": "Yes, but only by a fraction of a degree at cooking amounts (water's K_b is just 0.52). It does not noticeably speed cooking - salt is added for taste. The effect is real but small."},
    {"q": 'What is the boiling constant K_b?',
     "a": 'A property of the solvent - degrees the boiling point rises per unit molality. For water it is 0.52, the boiling-point twin of the freezing constant K_f.'},
    {"q": 'Where does this matter industrially?',
     "a": 'Anywhere solutions are concentrated by boiling - sugar refining, condensed milk, salt production - because the boiling point keeps rising as the solution thickens. Engine coolant also uses it to resist boiling on hot climbs.'},
    {"q": 'How does the example give about 0.52°C?',
     "a": "With K_b = 0.52 and m = 1, the rise is 0.52 × 1 = 0.52°C, so the solution boils near 100.52°C. For salts that split into ions you multiply by the van 't Hoff factor."},
])
