from core.faqs import register_faqs

register_faqs('gibbs-free-energy', [
    {"q": 'What does Gibbs free energy tell you?',
     "a": 'Whether a reaction happens on its own. Negative ΔG = spontaneous; positive = needs an energy push; zero = at equilibrium. It is the master test for the direction of change.'},
    {"q": 'How do ΔH and ΔS compete?',
     "a": 'Reactions are favoured by releasing energy (negative ΔH) and increasing disorder (positive ΔS). Temperature sets how much the disorder term counts.'},
    {"q": 'Why does temperature flip some reactions?',
     "a": 'Because the TΔS term grows with temperature. A reaction can be non-spontaneous when cold and spontaneous when hot - like ice melting above 0°C.'},
    {"q": 'How does ΔG connect to batteries?',
     "a": 'ΔG = −nFE: a negative ΔG means a positive voltage, a battery that works. ΔG is the energy available to do useful work.'},
    {"q": 'How does the example come out spontaneous?',
     "a": 'ΔG = −100 − (298)(0.1) = −129.8 kJ/mol. Both terms push it negative, so it is strongly spontaneous.'},
])
