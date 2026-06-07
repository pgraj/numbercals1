from core.faqs import register_faqs

register_faqs("revenue-impact", [
    {"q": "What does this calculator show?",
     "a": "How a percentage change in revenue translates into actual money. A 12% rise sounds abstract until you see it turn 100,000 into 112,000 with a 12,000 gain."},
    {"q": "Why bother converting a percentage to a figure?",
     "a": "Because decisions are made in dollars, not percentages. Seeing the real gain or loss helps you judge whether a 12% target is worth the effort and cost behind it."},
    {"q": "Can I use it for a fall in revenue?",
     "a": "Yes. Enter a negative percentage and it shows the drop and the new lower figure, which is handy for stress-testing a bad quarter."},
    {"q": "Is this the same as profit?",
     "a": "No. This is top-line revenue, the total money coming in. Profit is what is left after costs, which the Profit Impact calculator handles."},
    {"q": "Where would a business use this?",
     "a": "Sales forecasting, board updates, and quickly sizing the rupee or dollar value of a growth target before committing budget to it."},
])
