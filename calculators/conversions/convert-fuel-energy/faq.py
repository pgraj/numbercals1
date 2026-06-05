from core.faqs import register_faqs

register_faqs("convert-fuel-energy", [
    {"q": "What does the Chemical Specific Energy Converter do?",
     "a": "It converts convert specific (gravimetric) energy of fuels between mj/kg, btu/lb, kwh/kg and cal/g by first normalising your value to the SI base unit "
          "(megajoule per kilogram) and then scaling to your chosen target unit. This hub-and-spoke "
          "approach guarantees every unit pair is internally consistent."},
    {"q": "Can you show a worked example?",
     "a": "46 MJ/kg to BTU/lb: 46 × 1 = 46 MJ/kg, then ÷ 0.002326 ≈ 19776 BTU/lb."},
    {"q": 'Why does hydrogen look so much better than petrol?',
     "a": 'By mass, hydrogen stores ~142 MJ/kg versus petrol at ~46 MJ/kg. But hydrogen is extremely light, so per litre it stores far less unless compressed or liquefied. Specific energy (per kg) and energy density (per litre) tell different halves of the story.'},
    {"q": "Where is this used in real life?",
     "a": "Fuel selection, battery vs combustion comparison and energy density studies."},
    {"q": "What are the limits or edge cases?",
     "a": "Conversions are exact ratios where the units are defined exactly (most SI and "
          "imperial units) and best-available constants otherwise. Extremely large or small "
          "magnitudes are shown in general (g) format; round-tripping through the base unit "
          "may introduce tiny floating-point differences in the final decimal places."},
])
