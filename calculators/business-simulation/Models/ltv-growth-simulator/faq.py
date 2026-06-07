from core.faqs import register_faqs

register_faqs("ltv-growth-simulator", [
    {"q": "How is lifetime value linked to churn?",
     "a": "Tightly. Expected customer lifespan is roughly one divided by the churn rate, so halving churn doubles the lifespan and therefore the lifetime value."},
    {"q": "Why use 1 divided by churn for lifespan?",
     "a": "Because if a fixed fraction leaves each month, the average customer stays about that many months' reciprocal. A 4% monthly churn implies an average life of about 25 months."},
    {"q": "Which lever grows LTV fastest?",
     "a": "Usually cutting churn, because of that reciprocal effect, small churn reductions can lengthen lifespan dramatically. Lifting ARPU or margin helps too, but more linearly."},
    {"q": "Why multiply by gross margin?",
     "a": "Because lifetime value should be profit, not revenue. The margin converts the revenue a customer brings into the profit they actually generate."},
    {"q": "How does LTV guide the business?",
     "a": "It caps what you can sensibly spend to acquire customers and signals whether the unit economics work. Rising LTV gives room to invest more in growth."},
])
