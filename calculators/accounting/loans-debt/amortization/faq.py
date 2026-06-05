from core.faqs import register_faqs

register_faqs("amortization", [
    {"q": "What is amortisation?",
     "a": "The process of paying off a loan with equal regular payments, where each payment is "
          "split between interest and repaying the principal. An amortisation schedule lists "
          "that split for every period until the balance reaches zero."},
    {"q": "Why does the interest portion shrink over time?",
     "a": "Interest is charged on the balance still owing. Early on that balance is large, so "
          "most of each payment is interest. As the balance falls, the interest charged falls "
          "with it, leaving more of the same payment to chip away at the principal."},
    {"q": "Is the monthly payment always the same?",
     "a": "On a standard fixed-rate loan, yes — the EMI stays constant. What changes is the "
          "mix inside it: the interest slice gradually gives way to the principal slice as the "
          "loan winds down."},
    {"q": "How do I read the stacked area chart?",
     "a": "Time runs left to right across the loan term. The interest band starts thick and "
          "tapers towards zero, while the principal band starts thin and grows to fill the space. "
          "The crossover point is where you begin repaying more loan than interest each year."},
    {"q": "Where is this used in real life?",
     "a": "Home loans — seeing that on a 30-year mortgage the first years barely dent the "
          "principal. Car loans — judging how much you still owe if you sell early. Extra "
          "repayments — understanding why paying more in the early years saves the most interest, "
          "since it attacks the balance while interest charges are highest."},
])
