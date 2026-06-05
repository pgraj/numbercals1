from core.faqs import register_faqs

register_faqs("convert-speed", [
    {"q": "What does the Speed Converter do?",
     "a": "It converts convert speed between m/s, km/h, mph, knots and ft/s via metres per second by first normalising your value to the SI base unit "
          "(metre per second) and then scaling to your chosen target unit. This hub-and-spoke "
          "approach guarantees every unit pair is internally consistent."},
    {"q": "Can you show a worked example?",
     "a": "100 km/h to m/s: 100 × 0.277778 = 27.78 m/s (base), then ÷ 1 = 27.78 m/s."},
    {"q": "How do I read the graph?",
     "a": "The horizontal bar plots your converted value on a scale alongside two or three "
          "real-world benchmark markers, so the number gains physical meaning rather than "
          "sitting in isolation."},
    {"q": "Where is this used in real life?",
     "a": "Aviation and marine navigation (knots), automotive and athletics."},
    {"q": "What are the limits or edge cases?",
     "a": "Conversions are exact ratios where the units are defined exactly (most SI and "
          "imperial units) and best-available constants otherwise. Extremely large or small "
          "magnitudes are shown in general (g) format; round-tripping through the base unit "
          "may introduce tiny floating-point differences in the final decimal places."},
])
