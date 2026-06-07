from core.faqs import register_faqs

register_faqs("churn-rate-impact", [
    {"q": "What is churn?",
     "a": "The rate at which customers leave. A 5% monthly churn means you lose 5% of your customers each month, which compounds alarmingly over a year."},
    {"q": "Why compound churn over 12 months?",
     "a": "Because each month's loss is taken from a shrinking base. The calculator uses 1 minus (1 minus monthly churn) to the power 12 to get the true annual loss, which is less than simply multiplying by 12."},
    {"q": "Why is cutting churn so valuable?",
     "a": "Because it protects revenue you already have and lengthens customer lifetime. Dropping monthly churn from 5% to 3% can save a striking number of customers over a year."},
    {"q": "Is churn only a subscription problem?",
     "a": "No, but it bites hardest there, since the whole model depends on recurring revenue. Any business with repeat customers should watch it."},
    {"q": "How does churn relate to lifetime value?",
     "a": "Lower churn means customers stay longer, which directly raises their lifetime value. The LTV calculators show that link in money terms."},
])
