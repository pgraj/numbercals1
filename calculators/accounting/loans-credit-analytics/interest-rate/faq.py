from core.faqs import register_faqs

register_faqs("interest-rate", [
    {"q": "What does this calculator find?",
     "a": "The hidden interest rate behind a deal. If you know how much you put in, how much it "
          "grows to, and over how long, it works backwards to the annual rate that connects "
          "them — assuming the interest compounds once a year."},
    {"q": "How is the rate recovered from the formula?",
     "a": "Divide the final amount by the principal to get the total growth factor, take the "
          "n-th root to spread it evenly across the years, then subtract 1. Turn $1,000 into "
          "$1,500 over 5 years and the implied rate is (1500/1000)^(1/5) − 1, about 8.4% a year."},
    {"q": "What is the effective annual rate?",
     "a": "The rate that captures the true yearly cost or return once compounding is taken into "
          "account. With simple annual compounding it matches the nominal rate; with more "
          "frequent compounding the effective rate would sit slightly higher."},
    {"q": "How do I read the sensitivity chart?",
     "a": "The middle line grows at the implied rate. The lines above and below show what would "
          "happen at two percentage points higher or lower. The fan that opens up between them "
          "shows how even a small change in rate compounds into a large difference over time."},
    {"q": "Where is this used in real life?",
     "a": "Comparing deposits — finding the true rate behind a 'double your money in 9 years' "
          "claim (about 8%). Loans — uncovering the effective rate when only the total repayment "
          "is quoted. Investments — back-solving the annual return that took a starting balance "
          "to today's value, so you can compare it fairly against other options."},
])
