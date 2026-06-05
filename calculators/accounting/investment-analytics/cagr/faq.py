from core.faqs import register_faqs

register_faqs("cagr", [
    {"q": "What is CAGR?",
     "a": "Compound annual growth rate — the one steady yearly rate that would carry your "
          "starting value to your ending value over the period. It smooths out the bumpy "
          "real path into a single, comparable growth figure."},
    {"q": "How is CAGR calculated?",
     "a": "Divide the ending value by the beginning value, take the n-th root (where n is the "
          "number of years), then subtract 1. Grow $10,000 to $16,000 over 4 years and the "
          "CAGR is (16000/10000)^(1/4) − 1, about 12.5% a year."},
    {"q": "How is CAGR different from a simple average return?",
     "a": "A simple average just adds the yearly returns and divides, ignoring compounding and "
          "overstating volatile results. CAGR accounts for the fact that each year builds on "
          "the last, so it reflects what your money actually did."},
    {"q": "How do I read the chart?",
     "a": "The curve is the smooth path your investment would trace if it grew at exactly the "
          "CAGR every single year. The first and last points are pinned to your real start and "
          "end values; the bend between them shows compounding doing its work."},
    {"q": "Where is this used in real life?",
     "a": "Funds and shares — comparing a fund that returned 60% over 5 years (about 9.9% CAGR) "
          "against one that returned 50% over 3 years (about 14.5% CAGR). Business — measuring "
          "revenue growth across years. Property — annualising a multi-year gain. It is the "
          "fairest way to rank investments held for different lengths of time."},
])
