from core.faqs import register_faqs

register_faqs("compound-interest", [
    {"q": "What is compound interest?",
     "a": "Interest calculated not only on your original amount but also on the "
          "interest already added. Because each period earns interest on a "
          "slightly larger balance, the total grows faster over time."},
    {"q": "What does the formula A = P(1 + r/n)^(nt) mean?",
     "a": "P is the starting principal, r the yearly rate (as a decimal), n how "
          "many times a year interest is added, and t the number of years. A is "
          "the final amount once all the compounding is done."},
    {"q": "How is compound interest different from simple interest?",
     "a": "Simple interest is calculated only on the original principal, so it "
          "grows in a straight line. Compound interest grows on the running "
          "balance, so the curve bends upward and pulls ahead over time."},
    {"q": "Where is this used in real life?",
     "a": "Savings — $1,000 at 5% compounded monthly grows to about $1,647 in ten "
          "years. Loans and credit cards — the balance you owe compounds the same "
          "way, which is why debt grows quickly. Inflation — prices compound, so "
          "money loses value over time at a compounding rate."},
    {"q": "What does the growth chart show?",
     "a": "The curve plots your balance year by year, with a dashed line at the "
          "original principal, so you can see how much of the final amount is "
          "interest versus your starting deposit."},
])
