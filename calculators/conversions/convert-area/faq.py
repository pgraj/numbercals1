from core.faqs import register_faqs

register_faqs("convert-area", [
    {"q": "What does the Area Converter do?",
     "a": "It converts convert area between metric and imperial units, including acres and hectares, via the square metre by first normalising your value to the SI base unit "
          "(square metre) and then scaling to your chosen target unit. This hub-and-spoke "
          "approach guarantees every unit pair is internally consistent."},
    {"q": "Can you show a worked example?",
     "a": "2 acres to square metres: 2 × 4046.856 = 8093.71 m² (base), then ÷ 1 = 8093.71 m²."},
    {"q": "How do I read the graph?",
     "a": "The horizontal bar plots your converted value on a scale alongside two or three "
          "real-world benchmark markers, so the number gains physical meaning rather than "
          "sitting in isolation."},
    {"q": "Where is this used in real life?",
     "a": "Real estate (acres/hectares), flooring, land surveying and agriculture."},
    {"q": "What are the limits or edge cases?",
     "a": "Conversions are exact ratios where the units are defined exactly (most SI and "
          "imperial units) and best-available constants otherwise. Extremely large or small "
          "magnitudes are shown in general (g) format; round-tripping through the base unit "
          "may introduce tiny floating-point differences in the final decimal places."},
])
