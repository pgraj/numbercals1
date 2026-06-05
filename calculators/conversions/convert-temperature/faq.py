from core.faqs import register_faqs

register_faqs("convert-temperature", [
    {"q": "Why can't temperature use a simple multiplication?",
     "a": "Because Celsius and Fahrenheit place their zero points at different physical "
          "temperatures than Kelvin. Converting needs an affine transform — a multiply AND "
          "an offset — so we route every value through Kelvin, the absolute scale, first."},
    {"q": "Can you show a worked example?",
     "a": "100 °C to °F: 100 + 273.15 = 373.15 K, then (373.15 − 273.15) × 9/5 + 32 = 212 °F."},
    {"q": "How do I read the dial gauge?",
     "a": "The radial gauge maps your temperature onto colour-banded comfort zones — freezing, "
          "comfortable, hot and danger — with a needle pointing to where your value sits, so "
          "the number has immediate physical meaning."},
    {"q": "Where is this used in real life?",
     "a": "Weather, cooking, scientific work (Kelvin), and engineering thermodynamics, where "
          "Rankine still appears in some US aerospace and HVAC calculations."},
    {"q": "What are the limits?",
     "a": "Nothing can be colder than absolute zero (0 K = −273.15 °C). If a conversion would "
          "produce a sub-zero-Kelvin result, the calculator flags it rather than returning a "
          "physically impossible value."},
])
