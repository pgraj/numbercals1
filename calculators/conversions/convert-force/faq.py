from core.faqs import register_faqs

register_faqs("convert-force", [
    {"q": "What does the Force & Thrust Converter do?",
     "a": "It converts convert force and thrust between newtons, kilonewtons, pound-force and kilogram-force via the newton by first normalising your value to the SI base unit "
          "(newton) and then scaling to your chosen target unit. This hub-and-spoke "
          "approach guarantees every unit pair is internally consistent."},
    {"q": "Can you show a worked example?",
     "a": "1 kgf to newtons: 1 × 9.80665 = 9.80665 N, then ÷ 1 = 9.807 N."},
    {"q": 'Why are there "gravity" units like kgf and lbf?',
     "a": 'Kilogram-force and pound-force express force as the weight of a familiar mass: 1 kgf = 9.80665 N, 1 lbf = 4.4482 N. They feel intuitive but the newton is the proper SI unit. Engine and rocket thrust is just a force, usually quoted in kN.'},
    {"q": "Where is this used in real life?",
     "a": "Structural loads, propulsion (thrust) and mechanical design."},
    {"q": "What are the limits or edge cases?",
     "a": "Conversions are exact ratios where the units are defined exactly (most SI and "
          "imperial units) and best-available constants otherwise. Extremely large or small "
          "magnitudes are shown in general (g) format; round-tripping through the base unit "
          "may introduce tiny floating-point differences in the final decimal places."},
])
