from core.faqs import register_faqs

register_faqs("simple-interest", [
    {"q": "What is simple interest?",
     "a": "Interest worked out only on the original amount you started with (the "
          "principal). The rate is applied to that same figure every year, so the "
          "interest added each year is identical and the total grows in a straight line."},
    {"q": "What does the formula I = P·r·t mean?",
     "a": "P is the principal (the starting amount), r is the yearly interest rate "
          "written as a decimal — for example 5% becomes 0.05 — and t is the time in "
          "years. Multiply the three together and you get I, the total interest. The "
          "maturity value A is simply the principal plus that interest."},
    {"q": "How is simple interest different from compound interest?",
     "a": "Simple interest is charged only on the original principal, so each year adds "
          "the same fixed amount and the growth is a straight line. Compound interest is "
          "charged on the running balance, so it earns interest on earlier interest and "
          "curves upward — pulling ahead of simple interest over time."},
    {"q": "How do I read the chart?",
     "a": "The bottom band of each bar is the principal, which never changes height. The "
          "band stacked on top is the interest, which gets taller in equal steps each "
          "year. Because every step is the same size, the top of the bars rises in a "
          "straight line — that straight-line growth is the signature of simple interest."},
    {"q": "Where is this used in real life?",
     "a": "Short-term personal and car loans often quote simple interest — borrow $10,000 "
          "at 6% for 3 years and you owe $1,800 in interest. Some fixed-term deposits and "
          "bonds pay simple interest — $5,000 at 4% for 2 years earns $400. Late-payment "
          "and many car finance charges are also figured this way, so it is worth knowing "
          "the exact cost before you sign."},
])
