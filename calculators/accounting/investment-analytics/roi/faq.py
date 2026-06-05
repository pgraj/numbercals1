from core.faqs import register_faqs

register_faqs("roi", [
    {"q": "What is ROI?",
     "a": "Return on investment — the profit (or loss) on something expressed as a percentage "
          "of what it cost you. It turns a raw dollar gain into a figure you can compare "
          "fairly across investments of very different sizes."},
    {"q": "How is ROI worked out?",
     "a": "Take the current value, subtract what you paid, then divide that gain by the cost "
          "and multiply by 100. Buy for $1,000, now worth $1,250, and the ROI is "
          "(1250 − 1000) / 1000 × 100 = 25%."},
    {"q": "What does a negative ROI mean?",
     "a": "The investment is worth less than you paid, so you are sitting on a loss. An ROI of "
          "−20% means a fifth of your money has been wiped out on paper. Selling would lock "
          "that loss in."},
    {"q": "How do I read the chart?",
     "a": "Two bars sit side by side: what you put in and what it is worth now. If the current-"
          "value bar is taller, the gap above the invested bar is your profit; if it is "
          "shorter, the shortfall is your loss. The big ROI figure summarises that gap as a percentage."},
    {"q": "Where is this used in real life?",
     "a": "Shares — $5,000 of stock now worth $6,500 is a 30% ROI. Property — comparing a "
          "renovation's cost against the value it added. Business — judging whether a "
          "marketing spend earned its keep. Because ROI ignores how long it took, pair it with "
          "a time-aware measure like CAGR for multi-year holdings."},
])
