from core.faqs import register_faqs

register_faqs("convert-viscosity", [
    {"q": "What does the Viscosity Converter do?",
     "a": "It converts convert dynamic viscosity (pa·s, poise, cp) and kinematic viscosity (m²/s, stokes, cst). pick one family by first normalising your value to the SI base unit "
          "(pascal-second) and then scaling to your chosen target unit. This hub-and-spoke "
          "approach guarantees every unit pair is internally consistent."},
    {"q": "Can you show a worked example?",
     "a": "1 Pa·s to cP: 1 × 1 = 1 Pa·s, then ÷ 0.001 = 1000 cP."},
    {"q": 'What is the difference between dynamic and kinematic viscosity?',
     "a": 'Dynamic viscosity (Pa·s, poise) is raw resistance to flow; kinematic viscosity (m²/s, stokes) is dynamic viscosity divided by density. They describe different things, so convert within one family only — never mix Pa·s with m²/s.'},
    {"q": "Where is this used in real life?",
     "a": "Lubricant grading, food processing and fluid-dynamics design."},
    {"q": "What are the limits or edge cases?",
     "a": "Conversions are exact ratios where the units are defined exactly (most SI and "
          "imperial units) and best-available constants otherwise. Extremely large or small "
          "magnitudes are shown in general (g) format; round-tripping through the base unit "
          "may introduce tiny floating-point differences in the final decimal places."},
])
