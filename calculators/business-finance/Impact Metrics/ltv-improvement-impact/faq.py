from core.faqs import register_faqs

register_faqs("ltv-improvement-impact", [
    {"q": "What is customer lifetime value?",
     "a": "The total profit you expect from a customer over their whole relationship with you. Here it is ARPU times gross margin times how many months they stay."},
    {"q": "What is ARPU?",
     "a": "Average Revenue Per User, the typical revenue one customer brings in per period. It is a building block of lifetime value."},
    {"q": "Which lever moves LTV most?",
     "a": "It depends on your numbers, which is why the calculator lets you change ARPU, margin and lifespan together. Often lengthening lifespan (reducing churn) is the quiet powerhouse."},
    {"q": "Why include gross margin?",
     "a": "Because revenue is not profit. Multiplying by margin turns the figure into the actual profit a customer generates, which is what their value really is."},
    {"q": "How does LTV guide spending?",
     "a": "It sets the ceiling on what you can sensibly pay to acquire a customer. If LTV rises, you can afford to spend more to win customers and still profit."},
])
