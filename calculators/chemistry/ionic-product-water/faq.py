from core.faqs import register_faqs

register_faqs('ionic-product-water', [
    {"q": 'What is the ionic product of water?',
     "a": 'Even pure water slightly splits into H⁺ and OH⁻. K_w is the product of their concentrations, fixed at about 10⁻¹⁴ at 25°C, locking the two ions together.'},
    {"q": 'Why is it important?',
     "a": 'Knowing one ion gives the other, since the product is fixed. It underlies the whole pH scale and links acidity to basicity.'},
    {"q": 'Why is neutral water pH 7?',
     "a": 'In pure water H⁺ = OH⁻, and since their product is 10⁻¹⁴ each is 10⁻⁷, giving pH 7 - the natural midpoint.'},
    {"q": 'Does K_w change with temperature?',
     "a": "Yes - water ionises more when warm, so K_w rises and neutral pH dips slightly below 7 in hot water. The '7 = neutral' rule is for 25°C."},
    {"q": 'How does the example give 10⁻¹⁴?',
     "a": '[H⁺] = 10⁻⁷ and [OH⁻] = 10⁻⁷ multiply to 10⁻¹⁴ - exactly the value for neutral water.'},
])
