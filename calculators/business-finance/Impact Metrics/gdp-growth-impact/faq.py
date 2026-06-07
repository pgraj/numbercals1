from core.faqs import register_faqs

register_faqs("gdp-growth-impact", [
    {"q": "What does GDP growth mean here?",
     "a": "It applies a one-period growth rate to a starting GDP figure, showing the new level and the absolute increase in output."},
    {"q": "Is real GDP growth this simple?",
     "a": "This is the headline arithmetic. Real economics separates real from nominal growth (stripping out inflation) and compounds over many years, but the single-period maths is exactly this."},
    {"q": "Can I model a recession?",
     "a": "Yes, enter a negative growth rate to see GDP contract. A couple of negative quarters in a row is the rough definition of a recession."},
    {"q": "Why express growth as a percentage at all?",
     "a": "Because it lets you compare economies of wildly different sizes. A 6% growth rate means the same proportional progress whether the economy is tiny or enormous."},
    {"q": "What units should I use?",
     "a": "Any consistent unit, usually billions. The calculator does not care about the unit; it just scales the number you give it."},
])
