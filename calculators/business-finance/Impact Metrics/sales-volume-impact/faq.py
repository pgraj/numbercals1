from core.faqs import register_faqs

register_faqs("sales-volume-impact", [
    {"q": "What is sales volume?",
     "a": "The number of units sold, as opposed to the money they bring in. This calculator shows how a percentage change in volume moves the unit count."},
    {"q": "Why track volume separately from revenue?",
     "a": "Because price and volume can move in opposite directions. Selling more units at a discount can lift volume while revenue stalls, and you only spot that by watching both."},
    {"q": "How do I read a negative result?",
     "a": "A negative percentage shrinks the volume, showing how many units you would lose. Useful for modelling the effect of a supply problem or a weaker season."},
    {"q": "Does this account for price?",
     "a": "No, it is purely a unit count. Pair it with the Price Change Impact calculator to see how price and volume interact on revenue."},
    {"q": "Who uses volume figures?",
     "a": "Operations and supply-chain teams especially, since they plan production and stock around units, not dollars."},
])
