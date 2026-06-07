from core.faqs import register_faqs

register_faqs("tax-rate-change-impact", [
    {"q": "What does this calculate?",
     "a": "The tax owed and the take-home left when a flat tax rate changes. It is a quick way to see how a budget announcement might hit your pocket."},
    {"q": "Is real income tax this simple?",
     "a": "No. Most countries use progressive brackets, where different slices of income are taxed at different rates. This flat-rate version is a teaching simplification, useful for a single-rate estimate."},
    {"q": "What is take-home pay?",
     "a": "The money left after tax, which is what actually reaches you. The calculator shows it before and after the rate change so you can see the difference directly."},
    {"q": "Can I use it for company tax?",
     "a": "Yes, for a rough view. Corporate tax is often closer to a flat rate on profit, so the model fits a bit more neatly there than for personal income."},
    {"q": "Why does a few percent matter?",
     "a": "Because it applies to your whole taxable income. A 3-point rise on a decent salary quietly removes a noticeable sum every year."},
])
