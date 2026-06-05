from core.faqs import register_faqs

register_faqs("convert-power", [
    {"q": "What does the Power Converter do?",
     "a": "It converts convert power between watts, kw, mw, mechanical and metric horsepower via the watt by first normalising your value to the SI base unit "
          "(watt) and then scaling to your chosen target unit. This hub-and-spoke "
          "approach guarantees every unit pair is internally consistent."},
    {"q": "Can you show a worked example?",
     "a": "150 mech hp to kW: 150 × 745.7 = 111855 W, then ÷ 1000 ≈ 111.86 kW."},
    {"q": 'Why are there two kinds of horsepower?',
     "a": 'Mechanical (imperial) horsepower is 745.7 W; metric horsepower (PS/CV on European cars) is 735.5 W. They differ by about 1.4%, so a 100 hp and a 100 PS engine are not quite identical.'},
    {"q": "Where is this used in real life?",
     "a": "Automotive (hp), electrical engineering and renewable generation."},
    {"q": "What are the limits or edge cases?",
     "a": "Conversions are exact ratios where the units are defined exactly (most SI and "
          "imperial units) and best-available constants otherwise. Extremely large or small "
          "magnitudes are shown in general (g) format; round-tripping through the base unit "
          "may introduce tiny floating-point differences in the final decimal places."},
])
