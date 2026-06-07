from core.faqs import register_faqs

register_faqs("profit-impact", [
    {"q": "Why model revenue and cost changes together?",
     "a": "Because profit is the gap between them, and that gap is sensitive. A small revenue rise with costs held flat can lift profit a lot, which is the leverage this calculator reveals."},
    {"q": "What is operating leverage?",
     "a": "The effect where a modest change in revenue produces a larger percentage change in profit, because many costs do not move with sales. The profit-change percentage here hints at it."},
    {"q": "Can profit go negative?",
     "a": "Yes. If costs rise faster than revenue, the new profit can drop below zero into a loss, and the calculator will show that plainly."},
    {"q": "Is this gross or net profit?",
     "a": "It is a simple revenue-minus-cost profit. Whether that is gross or net depends on what you include in 'cost'; put in total costs for a bottom-line view."},
    {"q": "How would a manager use this?",
     "a": "To pressure-test a plan: 'if we grow sales 10% but costs creep up 5%, what actually happens to the bottom line?' The answer is often more encouraging, or more alarming, than the raw percentages suggest."},
])
