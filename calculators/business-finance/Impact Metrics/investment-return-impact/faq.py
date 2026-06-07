from core.faqs import register_faqs

register_faqs("investment-return-impact", [
    {"q": "How does compounding work?",
     "a": "Each year's return is earned on the growing balance, not just the original sum, so growth accelerates over time. This is why long horizons matter so much for investing."},
    {"q": "Why does the rate matter so much over time?",
     "a": "Because compounding magnifies small differences. Over decades, a couple of extra percent a year can roughly double the final pot, which is why fees and rates get so much attention."},
    {"q": "Is this guaranteed?",
     "a": "No. The calculator assumes a steady annual return, but real markets bounce around. It is a projection to understand compounding, not a promise of returns."},
    {"q": "What about regular contributions?",
     "a": "This version compounds a single lump sum. Adding monthly contributions would grow it faster, which a dedicated SIP or savings calculator handles."},
    {"q": "How do I compare this to inflation?",
     "a": "Run the inflation calculator at the same horizon. If your investment rate beats inflation, you are building real wealth; if not, you are losing purchasing power despite the bigger number."},
])
