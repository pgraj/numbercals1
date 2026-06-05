from core.faqs import register_faqs

register_faqs("convert-time", [
    {"q": "What does the Time Converter do?",
     "a": "It converts convert time between nanoseconds and millennia via the second. month = 30 days, year = 365.25 days (julian) by first normalising your value to the SI base unit "
          "(second) and then scaling to your chosen target unit. This hub-and-spoke "
          "approach guarantees every unit pair is internally consistent."},
    {"q": "Can you show a worked example?",
     "a": "90 minutes to hours: 90 × 60 = 5400 s (base), then ÷ 3600 = 1.5 hr."},
    {"q": 'Why are a month and a year approximate here?',
     "a": 'Calendar months vary from 28 to 31 days, so this tool fixes a month at 30 days and uses the astronomical Julian year of 365.25 days (31,557,600 s). Smaller units are exact multiples of the SI second.'},
    {"q": "Where is this used in real life?",
     "a": "Project scheduling, physics, astronomy and historical timelines."},
    {"q": "What are the limits or edge cases?",
     "a": "Conversions are exact ratios where the units are defined exactly (most SI and "
          "imperial units) and best-available constants otherwise. Extremely large or small "
          "magnitudes are shown in general (g) format; round-tripping through the base unit "
          "may introduce tiny floating-point differences in the final decimal places."},
])
