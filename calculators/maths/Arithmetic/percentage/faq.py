from core.faqs import register_faqs

register_faqs("percentage", [
    {"q": "How do I find a percentage of a number?",
     "a": "Divide the percentage by 100 and multiply by the number. 15% of 200 "
          "is (15 / 100) × 200 = 30."},
    {"q": "How do I work out what percentage one number is of another?",
     "a": "Divide the part by the whole and multiply by 100. 30 out of 200 is "
          "(30 / 200) × 100 = 15%."},
    {"q": "What is percentage change?",
     "a": "It measures how much a value grew or shrank, as a percentage of the "
          "original: (new − old) / old × 100. From 120 to 150 is a 25% increase."},
    {"q": "Where is this used in real life?",
     "a": "Shopping discounts — a 30% off $80 jacket saves 0.30 × 80 = $24. "
          "Exam scores — 45 out of 60 is (45/60) × 100 = 75%. Tax and tips — "
          "a 10% GST on a $50 bill adds $5. Percentages turn up anywhere two "
          "amounts are compared as 'out of a hundred'."},
    {"q": "Why is the pie chart useful here?",
     "a": "The shaded slice is the part you calculated and the rest is what "
          "remains, so you can see at a glance how big the percentage is "
          "relative to the whole."},
])
