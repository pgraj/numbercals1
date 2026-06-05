from core.faqs import register_faqs

register_faqs("convert-mass", [
    {"q": "What does the Mass Converter do?",
     "a": "It converts convert mass between metric, avoirdupois and troy units, including metric and imperial tons, via the kilogram by first normalising your value to the SI base unit "
          "(kilogram) and then scaling to your chosen target unit. This hub-and-spoke "
          "approach guarantees every unit pair is internally consistent."},
    {"q": "Can you show a worked example?",
     "a": "5 pounds to kilograms: 5 × 0.45359237 = 2.268 kg (base), then ÷ 1 = 2.268 kg."},
    {"q": 'What is the difference between mass and weight?',
     "a": 'Mass (kilograms) is how much matter is present and never changes; weight is the force gravity exerts on that mass and varies with location. This tool converts mass. Note the three different "tons" — metric tonne 1000 kg, US short ton 907 kg, UK long ton 1016 kg.'},
    {"q": "Where is this used in real life?",
     "a": "Trade and shipping, precious metals (troy units), cooking and freight."},
    {"q": "What are the limits or edge cases?",
     "a": "Conversions are exact ratios where the units are defined exactly (most SI and "
          "imperial units) and best-available constants otherwise. Extremely large or small "
          "magnitudes are shown in general (g) format; round-tripping through the base unit "
          "may introduce tiny floating-point differences in the final decimal places."},
])
