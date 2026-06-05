from core.faqs import register_faqs

register_faqs("logarithm", [
    {"q": "What is a logarithm?",
     "a": "A logarithm answers: to what power must the base be raised to get this "
          "number? log base 2 of 8 is 3, because 2 raised to the power 3 is 8."},
    {"q": "How do I compute a log to any base?",
     "a": "Use the change-of-base rule: log_b(x) = ln(x) / ln(b). This lets a "
          "calculator find a log to any base using natural logs."},
    {"q": "What is the difference between ln and log?",
     "a": "ln is the logarithm to base e (about 2.718), used widely in calculus "
          "and growth problems. 'log' usually means base 10 unless a base is given."},
    {"q": "Where is this used in real life?",
     "a": "Earthquakes — the Richter scale is base-10 logarithmic, so magnitude 6 "
          "is ten times stronger than 5. Sound — decibels measure loudness on a "
          "log scale. Acidity — pH is the negative log of hydrogen-ion "
          "concentration. Computing — log base 2 counts how many times you can "
          "halve a list, which is why searching a sorted list is fast."},
    {"q": "How does the graph help me understand logs?",
     "a": "The dashed guide lines trace your value up to the curve and across to "
          "the answer, so you can literally read log_base(value) off the y-axis."},
])
