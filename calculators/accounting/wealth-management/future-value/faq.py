from core.faqs import register_faqs

register_faqs("future-value", [
    {"q": "What is future value?",
     "a": "What a sum of money today will be worth at some point in the future once it has "
          "grown at a given rate. It is the core idea behind the time value of money — a dollar "
          "now is worth more than a dollar later because it can earn returns in the meantime."},
    {"q": "What does FV = PV·(1 + r)^n mean?",
     "a": "PV is the present value (today's amount), r is the growth rate per period as a "
          "decimal, and n is the number of periods. Raising (1 + r) to the power n compounds "
          "the growth across every period to give FV, the future value."},
    {"q": "What counts as a period?",
     "a": "Whatever matches your rate. If r is an annual rate, n is a number of years; if it is "
          "a monthly rate, n is a number of months. The key is to keep the rate and the period "
          "on the same time basis."},
    {"q": "How do I read the chart?",
     "a": "Two bars sit side by side: the present value on the left and the projected future "
          "value on the right. The extra height of the right-hand bar is the growth your money "
          "earns over the periods — the taller it is, the harder compounding has worked."},
    {"q": "Where is this used in real life?",
     "a": "Saving — $5,000 at 6% for 10 years becomes about $8,954. Retirement planning — "
          "projecting what today's balance will be at 65. Comparing offers — deciding whether "
          "a lump sum now beats a larger amount promised years later, once growth is accounted for."},
])
