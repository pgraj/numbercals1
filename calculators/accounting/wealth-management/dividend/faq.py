from core.faqs import register_faqs

register_faqs("dividend", [
    {"q": "What is a dividend?",
     "a": "A share of a company's profit paid out to shareholders, usually as cash. How much "
          "you receive depends on how many shares you hold and the dividend yield — the annual "
          "dividend expressed as a percentage of the share price."},
    {"q": "How is the annual dividend worked out?",
     "a": "Multiply the number of shares by the share price to get the amount invested, then "
          "multiply by the yield as a decimal. 500 shares at $20 with a 4% yield pays "
          "500 × 20 × 0.04 = $400 a year."},
    {"q": "What is dividend reinvestment (DRIP)?",
     "a": "Instead of taking the cash, you use each dividend to buy more shares automatically. "
          "Those extra shares then pay dividends of their own, so your income and holding grow "
          "on themselves — the same compounding effect that powers long-term wealth."},
    {"q": "How do I read the chart?",
     "a": "With reinvestment switched off, the bars show the same dividend income each year — a "
          "flat, steady stream. Switch DRIP on and the line curves upward instead, because each "
          "year's reinvested dividends enlarge the holding that pays the next dividend."},
    {"q": "Where is this used in real life?",
     "a": "Income investing — a retiree living off $400 a year per $10,000 of holdings at a 4% "
          "yield. Long-term growth — reinvesting dividends in an index fund so the position "
          "compounds for decades. Comparing stocks — using yield to judge which pays more income "
          "per dollar invested. Note this is a simplified model that assumes the share price holds steady."},
])
