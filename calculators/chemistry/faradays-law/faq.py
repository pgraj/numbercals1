from core.faqs import register_faqs

register_faqs('faradays-law', [
    {"q": "What does Faraday's law state?",
     "a": 'The mass deposited at an electrode is proportional to the electric charge passed (current × time). Double the charge, double the metal.'},
    {"q": 'Where is it used day to day?',
     "a": 'Electroplating jewellery and car parts with gold, silver or chrome; refining copper for wires; anodising aluminium. Anywhere electricity deposits or dissolves metal.'},
    {"q": 'What is the Faraday constant (96500)?',
     "a": 'The charge carried by one mole of electrons. It bridges electric charge and moles of substance, so you can turn amps and seconds into grams.'},
    {"q": 'What is equivalent weight here?',
     "a": 'Molar mass divided by the electrons needed per ion. Copper from Cu²⁺ needs 2 electrons, so its equivalent weight is 63.5 ÷ 2.'},
    {"q": 'How does the example give 0.02 g?',
     "a": 'Charge = 2 A × 965 s = 1930 C. Divided by 96500 gives 0.02 mole-equivalents, and with E = 1 that is 0.02 g.'},
])
