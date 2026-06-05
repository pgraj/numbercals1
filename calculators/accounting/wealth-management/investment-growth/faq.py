from core.faqs import register_faqs

register_faqs("investment-growth", [
    {"q": "What does this calculator show?",
     "a": "How a lump sum plus regular yearly top-ups grows when returns compound. It separates "
          "the money you put in from the growth that money then generates, so you can see how "
          "much of your final wealth is your own cash versus earnings."},
    {"q": "What do the parts of the formula mean?",
     "a": "P is your starting principal and grows on its own. PMT is each year's contribution, "
          "and the bracketed term grows that whole stream of contributions. r is the annual "
          "return as a decimal and t is the number of years. Adding the two parts gives the "
          "total future value."},
    {"q": "Why do small regular contributions add up to so much?",
     "a": "Each contribution doesn't just sit there — it earns returns for every year that "
          "follows, and those returns earn returns of their own. Over a long horizon the "
          "compounded earnings can dwarf the cash you actually paid in."},
    {"q": "How do I read the area chart?",
     "a": "The chart stacks three layers over time: your original principal at the base, the "
          "contributions you have added on top of that, and the compounded earnings on top "
          "again. The widening earnings band shows compounding accelerating in the later years."},
    {"q": "Where is this used in real life?",
     "a": "Superannuation and retirement saving — $10,000 plus $6,000 a year at 7% for 30 years "
          "grows to well over $600,000, most of it earnings. Education funds — saving steadily "
          "for a child's university costs. Long-term share investing — seeing why starting "
          "early beats contributing more later."},
])
