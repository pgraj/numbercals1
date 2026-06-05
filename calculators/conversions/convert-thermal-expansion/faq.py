from core.faqs import register_faqs

register_faqs("convert-thermal-expansion", [
    {"q": "What does the Thermal Expansion Coefficient Converter do?",
     "a": "It converts convert linear thermal expansion coefficient between 1/k and 1/°f by first normalising your value to the SI base unit "
          "(per kelvin) and then scaling to your chosen target unit. This hub-and-spoke "
          "approach guarantees every unit pair is internally consistent."},
    {"q": "Can you show a worked example?",
     "a": "1.2e-5 /K to 1/°F: 1.2e-5 ÷ 1.8 ≈ 6.67e-6 /°F."},
    {"q": 'Why is there no 32° offset when converting to 1/°F?',
     "a": 'Because the coefficient applies to a temperature DIFFERENCE, not an actual temperature. A change of 1 K equals a change of 1.8 °F, so α in 1/°F = α in 1/K ÷ 1.8. The 32° offset only applies when converting real temperatures, not differences.'},
    {"q": "Where is this used in real life?",
     "a": "Precision instruments, bridge joints and aerospace structures."},
    {"q": "What are the limits or edge cases?",
     "a": "Conversions are exact ratios where the units are defined exactly (most SI and "
          "imperial units) and best-available constants otherwise. Extremely large or small "
          "magnitudes are shown in general (g) format; round-tripping through the base unit "
          "may introduce tiny floating-point differences in the final decimal places."},
])
