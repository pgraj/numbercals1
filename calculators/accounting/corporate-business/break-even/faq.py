from core.faqs import register_faqs

register_faqs("break-even", [
    {"q": "What is the break-even point?",
     "a": "The level of sales where you are neither making a profit nor a loss — total revenue "
          "exactly covers total cost. Sell one more unit and you are in profit; one fewer and "
          "you are in loss."},
    {"q": "What is the contribution margin in the formula?",
     "a": "It is the selling price minus the variable cost of one unit — the slice of each sale "
          "left over to chip away at the fixed costs. Break-even units are simply the fixed "
          "costs divided by this per-unit contribution."},
    {"q": "Why must price be greater than variable cost?",
     "a": "If each unit costs more to make than it sells for, every sale deepens the loss and the "
          "fixed costs are never recovered — there is no break-even point at all. That is why "
          "the calculator flags it."},
    {"q": "How do I read the break-even graph?",
     "a": "Two lines climb from left to right: total revenue and total cost. They cross at the "
          "break-even point. To the left of the crossing, cost sits above revenue — the loss "
          "zone. To the right, revenue pulls ahead — the profit zone."},
    {"q": "Where is this used in real life?",
     "a": "Pricing a product — with $10,000 fixed costs and a $15 margin per unit you must sell "
          "667 units to break even. Launch decisions — checking whether the expected sales clear "
          "that bar. Cost control — seeing how cutting fixed rent or raising price lowers the "
          "units you need before profit begins."},
])
