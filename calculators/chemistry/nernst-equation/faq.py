from core.faqs import register_faqs

register_faqs('nernst-equation', [
    {"q": 'What does the Nernst equation do?',
     "a": "Finds a cell's actual voltage under real conditions, not just the ideal standard value - correcting for the real concentrations via Q."},
    {"q": "Why does a battery's voltage drop as it's used?",
     "a": 'As it runs, reactants are consumed and Q rises, so the equation gives a lower voltage. When it reaches equilibrium the voltage hits zero - the battery is dead.'},
    {"q": 'What is the 0.0591 term?',
     "a": 'A bundled constant for 25°C: it is RT/F converted from natural log to base-10 log, the value that appears for room-temperature cells.'},
    {"q": 'Why divide by n?',
     "a": 'n is the electrons moved per cycle. Reactions moving more electrons are less sensitive to concentration per volt, so dividing by n scales the correction.'},
    {"q": 'Where is it used?',
     "a": 'Batteries and fuel cells, electroplating, corrosion protection, and the electrical signals of nerve and muscle cells. pH meters use it too.'},
])
