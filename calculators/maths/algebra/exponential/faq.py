from core.faqs import register_faqs

register_faqs("exponential", [
    {"q": "What does y = a·b^x mean?",
     "a": "Starting from a, you multiply by the base b once for every step in x. "
          "With a = 2 and b = 3, x = 4 gives 2 × 3 × 3 × 3 × 3 = 162."},
    {"q": "What is the difference between growth and decay?",
     "a": "If the base is greater than 1 the curve rises (growth); if the base is "
          "between 0 and 1 it falls toward zero (decay)."},
    {"q": "How is this different from a linear equation?",
     "a": "A line adds the same amount each step; an exponential multiplies by the "
          "same factor each step, so it changes far faster as x grows."},
    {"q": "Where is this used in real life?",
     "a": "Populations — bacteria doubling each hour follow b = 2. Radioactive "
          "decay and medicine half-lives use a base between 0 and 1. Money — "
          "compound interest is exponential growth. Epidemics — early case counts "
          "often grow exponentially, which is why they rise so suddenly."},
    {"q": "What do the dots on the graph mean?",
     "a": "Each dot marks an integer power (b⁰, b¹, b², …). Reading them left to "
          "right shows the value multiplying by the base at every step."},
])
