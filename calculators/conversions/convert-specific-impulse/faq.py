from core.faqs import register_faqs

register_faqs("convert-specific-impulse", [
    {"q": "What does the Specific Impulse Converter do?",
     "a": "It converts convert rocket specific impulse between seconds and effective exhaust velocity (n·s/kg = m/s) using g₀ by first normalising your value to the SI base unit "
          "(newton-second per kilogram) and then scaling to your chosen target unit. This hub-and-spoke "
          "approach guarantees every unit pair is internally consistent."},
    {"q": "Can you show a worked example?",
     "a": "300 s to m/s: 300 × 9.80665 = 2942 N·s/kg, then ÷ 1 = 2942 m/s."},
    {"q": 'Why is specific impulse given in both seconds and m/s?',
     "a": 'They are the same efficiency expressed two ways: the effective exhaust velocity in m/s equals the value in seconds multiplied by g₀ = 9.80665 m/s². The "seconds" figure is popular because it is identical in metric and imperial systems.'},
    {"q": "Where is this used in real life?",
     "a": "Rocket propulsion analysis and launch-vehicle trade studies."},
    {"q": "What are the limits or edge cases?",
     "a": "Conversions are exact ratios where the units are defined exactly (most SI and "
          "imperial units) and best-available constants otherwise. Extremely large or small "
          "magnitudes are shown in general (g) format; round-tripping through the base unit "
          "may introduce tiny floating-point differences in the final decimal places."},
])
