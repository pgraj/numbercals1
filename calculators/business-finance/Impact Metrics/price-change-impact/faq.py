from core.faqs import register_faqs

register_faqs("price-change-impact", [
    {"q": "What is price elasticity of demand?",
     "a": "A measure of how sensitive buyers are to price. An elasticity of -1.2 means a 1% price rise loses about 1.2% of sales. The minus sign reflects that higher prices usually mean fewer units."},
    {"q": "Why can raising prices reduce revenue?",
     "a": "Because if demand is elastic (sensitive), the units you lose can outweigh the extra you earn per sale. The calculator multiplies the new price by the new quantity to show the net effect."},
    {"q": "What is an inelastic product?",
     "a": "One where buyers barely change their habits when prices move, like petrol or medicine (elasticity between 0 and -1). For these, price rises tend to lift revenue."},
    {"q": "Where do I get an elasticity figure?",
     "a": "From past sales data, market research, or industry benchmarks. It is an estimate, so it is worth trying a range of values to see how the answer shifts."},
    {"q": "Can quantity go negative?",
     "a": "No. The calculator floors it at zero, since you cannot sell a negative number of units even if the model's percentage drop is severe."},
])
