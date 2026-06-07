from core.faqs import register_faqs

register_faqs("cac-impact-simulator", [
    {"q": "What is the LTV:CAC ratio?",
     "a": "Lifetime value divided by acquisition cost. It shows how many times over a customer repays the cost of winning them, the headline test of unit economics."},
    {"q": "Why is 3:1 a common target?",
     "a": "Because it leaves room for all the other costs of running the business while still profiting per customer. Below 3:1 is often seen as thin; below 1:1 means you lose money on each customer."},
    {"q": "What is payback period?",
     "a": "How many months of a customer's margin it takes to recover their acquisition cost. Shorter is better, since cash comes back faster to fund more growth."},
    {"q": "Can a ratio be too high?",
     "a": "Possibly. A very high ratio can mean you are underspending on growth and could profitably acquire more customers. It is a balance, not a maximise-at-all-costs number."},
    {"q": "How do I improve these?",
     "a": "Lower CAC through better targeting and conversion, or raise LTV by cutting churn and lifting margin. The simulator lets you see each move's effect on the ratio and payback."},
])
