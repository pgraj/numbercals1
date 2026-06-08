from core.faqs import register_faqs

register_faqs('vant-hoff-factor', [
    {"q": "What is the van 't Hoff factor?",
     "a": "The number of particles a dissolved substance actually makes, divided by what you'd expect if it stayed whole. Sugar gives i ≈ 1 (no split), table salt i ≈ 2 (Na⁺ + Cl⁻), calcium chloride i ≈ 3."},
    {"q": 'Why does it matter?',
     "a": 'Because freezing-point drop, boiling-point rise, and osmotic pressure all depend on the number of particles. A salt that splits in two affects them about twice as much as a non-splitting solute - which is why salt melts ice so well.'},
    {"q": 'Why is the real factor often a bit less than the whole number?',
     "a": "In real solutions some separated ions briefly pair up again, so the effective particle count is slightly below the ideal. NaCl's ideal i is 2 but measured values are around 1.8-1.9."},
    {"q": 'How does it connect observed and calculated?',
     "a": 'i = observed ÷ calculated. If a salt drops the freezing point twice as much as a non-splitting solute would, the observed is double the calculated, so i = 2. Measuring an effect reveals how many particles formed.'},
    {"q": 'Can it tell us what a solute does in solution?',
     "a": 'Yes - i above 1 means it splits into ions, i below 1 means particles join together (association). So measuring i reveals the actual behaviour of the dissolved substance.'},
])
