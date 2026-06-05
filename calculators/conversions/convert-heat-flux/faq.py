from core.faqs import register_faqs

register_faqs("convert-heat-flux", [
    {"q": "What does the Heat Flux Converter do?",
     "a": "It converts convert heat flux density between w/m² and btu/(hr·ft²) via the si base by first normalising your value to the SI base unit "
          "(watt per square metre) and then scaling to your chosen target unit. This hub-and-spoke "
          "approach guarantees every unit pair is internally consistent."},
    {"q": "Can you show a worked example?",
     "a": "1000 W/m² to BTU/(hr·ft²): 1000 ÷ 3.1546 ≈ 317.0."},
    {"q": 'What do typical heat-flux values look like?',
     "a": 'Skin comfort loses about 50 W/m²; bright sunlight delivers about 1000 W/m² (the basis of solar panel ratings); a spacecraft heat shield in re-entry can exceed 1,000,000 W/m².'},
    {"q": "Where is this used in real life?",
     "a": "Solar engineering, re-entry thermal protection and heat-exchanger design."},
    {"q": "What are the limits or edge cases?",
     "a": "Conversions are exact ratios where the units are defined exactly (most SI and "
          "imperial units) and best-available constants otherwise. Extremely large or small "
          "magnitudes are shown in general (g) format; round-tripping through the base unit "
          "may introduce tiny floating-point differences in the final decimal places."},
])
