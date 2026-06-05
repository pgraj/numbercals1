from core.faqs import register_faqs

register_faqs("convert-length", [
    {"q": "What does the Length Converter do?",
     "a": "It converts convert length between metric, imperial and astronomical units — nanometres to light-years — via the metre by first normalising your value to the SI base unit "
          "(metre) and then scaling to your chosen target unit. This hub-and-spoke "
          "approach guarantees every unit pair is internally consistent."},
    {"q": "Can you show a worked example?",
     "a": "100 metres to feet: 100 × 1 = 100 m (base), then 100 ÷ 0.3048 ≈ 328.08 ft."},
    {"q": 'Why are metric conversions cleaner than imperial ones?',
     "a": 'Metric units step in powers of ten (1 km = 1000 m), so factors are round. Imperial units were pinned to the metre later, giving exact but odd factors like 1 mile = 1609.344 m. Both are exact; only the numbers look different.'},
    {"q": "Where is this used in real life?",
     "a": "Engineering drawings, navigation (nmi), astronomy (AU, light-years) and everyday DIY."},
    {"q": "What are the limits or edge cases?",
     "a": "Conversions are exact ratios where the units are defined exactly (most SI and "
          "imperial units) and best-available constants otherwise. Extremely large or small "
          "magnitudes are shown in general (g) format; round-tripping through the base unit "
          "may introduce tiny floating-point differences in the final decimal places."},
])
