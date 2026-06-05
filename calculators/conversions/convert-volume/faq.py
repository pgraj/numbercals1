from core.faqs import register_faqs

register_faqs("convert-volume", [
    {"q": "What does the Volume Converter do?",
     "a": "It converts convert volume between litres, us customary cooking units and cubic measures via the cubic metre by first normalising your value to the SI base unit "
          "(cubic metre) and then scaling to your chosen target unit. This hub-and-spoke "
          "approach guarantees every unit pair is internally consistent."},
    {"q": "Can you show a worked example?",
     "a": "1 US gallon to litres: 1 × 0.003785412 = 0.003785412 m³, then ÷ 0.001 = 3.785 L."},
    {"q": 'Is a US gallon the same as a UK gallon?',
     "a": 'No. A US gallon is 3.785 L while an Imperial (UK) gallon is 4.546 L. This converter uses US customary units, so a UK recipe pint will be larger than the US pint used here.'},
    {"q": "Where is this used in real life?",
     "a": "Cooking, fuel and chemical dosing, shipping and tank sizing."},
    {"q": "What are the limits or edge cases?",
     "a": "Conversions are exact ratios where the units are defined exactly (most SI and "
          "imperial units) and best-available constants otherwise. Extremely large or small "
          "magnitudes are shown in general (g) format; round-tripping through the base unit "
          "may introduce tiny floating-point differences in the final decimal places."},
])
