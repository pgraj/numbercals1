from core.faqs import register_faqs

register_faqs("portfolio-risk-impact", [
    {"q": "What is portfolio risk?",
     "a": "How much the value of your combined investments tends to swing, measured as volatility. Lower volatility means a steadier ride."},
    {"q": "What is diversification?",
     "a": "Spreading money across assets that do not move in lockstep. When one zigs and another zags, the combined swing is smaller than either alone, which this calculator demonstrates."},
    {"q": "What does correlation do here?",
     "a": "It measures how two assets move together, from -1 (opposite) to +1 (identical). The lower the correlation, the bigger the diversification benefit, because the assets cushion each other."},
    {"q": "Why is portfolio risk less than the average of the parts?",
     "a": "Because of that cushioning. Unless the assets are perfectly correlated, combining them cancels out some of the swings, so total risk falls below the weighted average."},
    {"q": "Is this the real formula the professionals use?",
     "a": "Yes, this is the standard two-asset portfolio variance formula from modern portfolio theory. Real portfolios extend it to many assets, but the principle is identical."},
])
