from core.faqs import register_faqs

register_faqs("mortgage-stress-test", [
    {"q": "What is a mortgage stress test?",
     "a": "A check of whether you could still afford repayments if interest rates rose. Lenders add a buffer to today's rate and see if the higher repayment still fits your budget."},
    {"q": "Why add a buffer?",
     "a": "Because rates change over a loan's life. Testing at a higher rate guards against being caught out if borrowing costs climb after you buy."},
    {"q": "How is the repayment calculated?",
     "a": "Using the standard amortising mortgage formula, which blends interest and principal into a level monthly payment over the term. The test recomputes it at the buffered rate."},
    {"q": "What is the income limit?",
     "a": "A ceiling on what share of your income should go to the mortgage, often around a third. The test passes if the stressed repayment stays under that limit."},
    {"q": "What if I fail the test?",
     "a": "Consider a smaller loan, a bigger deposit, a longer term, or waiting. Failing the buffer is a warning that a rate rise could stretch you uncomfortably."},
])
