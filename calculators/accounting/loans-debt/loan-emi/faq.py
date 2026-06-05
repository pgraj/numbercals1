from core.faqs import register_faqs

register_faqs("loan-emi", [
    {"q": "What is an EMI?",
     "a": "EMI stands for Equated Monthly Instalment — the fixed amount you pay the lender "
          "every month until the loan is cleared. Each payment is the same size, but its "
          "split changes: early payments are mostly interest, later ones mostly principal."},
    {"q": "What do the parts of the EMI formula mean?",
     "a": "P is the loan amount, r is the monthly interest rate (the annual rate divided by "
          "12 and by 100 to make it a decimal), and n is the number of monthly payments. "
          "The formula spreads the principal plus all the interest evenly across n months."},
    {"q": "Why is so much of the total an interest charge?",
     "a": "Interest is charged on the balance still owing, and at the start almost the whole "
          "loan is outstanding. On a long tenure the interest stacks up — which is exactly "
          "what the donut chart makes visible at a glance."},
    {"q": "How do I read the donut chart?",
     "a": "The full ring is everything you will hand over across the life of the loan. One "
          "slice is the original amount you borrowed (the principal); the other slice is the "
          "interest the lender keeps. The bigger the interest slice, the more the loan costs "
          "you beyond what you borrowed."},
    {"q": "Where is this used in real life?",
     "a": "Home loans — a $400,000 mortgage at 6% over 30 years has an EMI near $2,398. Car "
          "loans — $30,000 at 8% over 5 years is about $608 a month. Personal loans use the "
          "same maths. Comparing the total-interest slice across offers shows which loan is "
          "genuinely cheaper, not just which has the smaller monthly payment."},
])
