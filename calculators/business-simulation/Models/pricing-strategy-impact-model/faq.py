from core.faqs import register_faqs

register_faqs("pricing-strategy-impact-model", [
    {"q": "Why model profit, not just revenue?",
     "a": "Because a price rise that grows revenue can still cut profit if you lose too many sales, and a price cut can lift profit if volume jumps enough. Profit is what actually matters."},
    {"q": "How does elasticity drive this?",
     "a": "It sets how much demand responds to the price change. The more elastic (sensitive) buyers are, the more units you lose when you raise prices, which can erase the gain."},
    {"q": "Why does unit cost matter here?",
     "a": "Because profit is price minus cost times quantity. Knowing the cost reveals whether selling more units at a lower price actually pays, or just adds busywork."},
    {"q": "Can cutting prices raise profit?",
     "a": "Yes, if demand is elastic enough that the extra volume more than offsets the thinner margin. The model shows exactly when that happens for your numbers."},
    {"q": "Where do I get an elasticity estimate?",
     "a": "From past pricing experiments, market research, or industry norms. Since it is uncertain, test a range of values to see how sensitive your decision is."},
])
