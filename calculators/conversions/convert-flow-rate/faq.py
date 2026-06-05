from core.faqs import register_faqs

register_faqs("convert-flow-rate", [
    {"q": "What does the Flow Rate Converter do?",
     "a": "It converts convert volumetric flow rate between m³/s, cfm, l/min and l/s via cubic metres per second by first normalising your value to the SI base unit "
          "(cubic metre per second) and then scaling to your chosen target unit. This hub-and-spoke "
          "approach guarantees every unit pair is internally consistent."},
    {"q": "Can you show a worked example?",
     "a": "60 L/min to L/s: 60 × 1.6667e-5 = 0.001 m³/s, then ÷ 0.001 = 1 L/s."},
    {"q": 'What is the difference between volumetric and mass flow?',
     "a": 'Volumetric flow (m³/s, CFM, L/min) measures volume per second; mass flow (kg/s) measures mass per second. They are linked by density but are not interchangeable units. This converter handles volumetric flow.'},
    {"q": "Where is this used in real life?",
     "a": "HVAC ducting (CFM), plumbing and process pipework sizing."},
    {"q": "What are the limits or edge cases?",
     "a": "Conversions are exact ratios where the units are defined exactly (most SI and "
          "imperial units) and best-available constants otherwise. Extremely large or small "
          "magnitudes are shown in general (g) format; round-tripping through the base unit "
          "may introduce tiny floating-point differences in the final decimal places."},
])
