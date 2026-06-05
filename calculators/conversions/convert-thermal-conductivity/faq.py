from core.faqs import register_faqs

register_faqs("convert-thermal-conductivity", [
    {"q": "What does the Thermal Conductivity Converter do?",
     "a": "It converts convert thermal conductivity between w/(m·k) and btu/(hr·ft·°f) via the si base by first normalising your value to the SI base unit "
          "(watt per metre-kelvin) and then scaling to your chosen target unit. This hub-and-spoke "
          "approach guarantees every unit pair is internally consistent."},
    {"q": "Can you show a worked example?",
     "a": "400 W/(m·K) to BTU/(hr·ft·°F): 400 ÷ 1.7307 ≈ 231.1."},
    {"q": 'What do typical conductivity values look like?',
     "a": 'Still air ≈ 0.026, water ≈ 0.6, glass ≈ 1, steel ≈ 50, aluminium ≈ 240, copper ≈ 400 W/(m·K). Copper conducts heat roughly 15,000× better than air — which is why pans are metal and insulation traps air.'},
    {"q": "Where is this used in real life?",
     "a": "Insulation design, electronics cooling and materials selection."},
    {"q": "What are the limits or edge cases?",
     "a": "Conversions are exact ratios where the units are defined exactly (most SI and "
          "imperial units) and best-available constants otherwise. Extremely large or small "
          "magnitudes are shown in general (g) format; round-tripping through the base unit "
          "may introduce tiny floating-point differences in the final decimal places."},
])
