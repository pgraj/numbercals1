from core.faqs import register_faqs

register_faqs('solubility-product', [
    {"q": 'What is the solubility product?',
     "a": 'For a barely-soluble salt, K_sp is the product of its dissolved ion concentrations at saturation - the point where no more will dissolve. Small K_sp = very insoluble.'},
    {"q": 'How does it predict a precipitate?',
     "a": 'Compare the actual ion product with K_sp. Above K_sp, solid precipitates out until it falls back to K_sp; below, more can dissolve.'},
    {"q": 'Where does it matter?',
     "a": 'Kidney stones, kettle and pipe scale, tooth enamel dissolving in acid, and water treatment that precipitates out toxic metals. It is the chemistry of dissolved versus solid.'},
    {"q": 'What is the common-ion effect?',
     "a": "Adding more of one of the salt's ions makes it less soluble - since the product is fixed, raising one ion forces the salt to precipitate. A chloride salt dissolves less in salty water."},
    {"q": 'How does the example give 10⁻¹⁰?',
     "a": '[A⁺] = 10⁻⁵ and [B⁻] = 10⁻⁵ multiply to 10⁻¹⁰ - a very small number, showing a sparingly soluble salt.'},
])
