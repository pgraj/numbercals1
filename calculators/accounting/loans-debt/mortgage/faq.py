from core.faqs import register_faqs

register_faqs("mortgage", [
    {"q": "What does a mortgage payment actually include?",
     "a": "More than just the loan. A typical monthly payment bundles principal and interest "
          "(repaying the loan plus the lender's charge) with a slice of your yearly property "
          "tax and home insurance. Lenders often call this combined figure PITI."},
    {"q": "How is the principal-and-interest part worked out?",
     "a": "It uses the standard repayment formula on the amount you actually borrow — the home "
          "price minus your deposit. The monthly rate is the annual rate divided by 12, and "
          "the term is the number of years times 12 months."},
    {"q": "Why split out tax and insurance?",
     "a": "Because they are not loan costs — they are ongoing charges on the property that "
          "don't shrink as you repay the loan. Seeing them separately stops you from "
          "mistaking the true cost of owning for just the loan repayment."},
    {"q": "How do I read the pie chart?",
     "a": "The whole pie is one month's payment. The largest slice is usually principal and "
          "interest; the smaller slices are the monthly share of property tax and insurance. "
          "Raising the tax or insurance figures grows their slices without touching the loan."},
    {"q": "Where is this used in real life?",
     "a": "Budgeting before you buy — a $500,000 home with $100,000 down at 6% over 30 years is "
          "roughly $2,398 in principal and interest, before tax and insurance. Comparing "
          "suburbs — two homes at the same price can have very different payments once council "
          "rates and insurance differ. Refinancing — re-running the numbers at a new rate shows "
          "the monthly saving instantly."},
])
