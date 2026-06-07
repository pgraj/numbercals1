from core.faqs import register_faqs

register_faqs("transfer-value-impact", [
    {"q": "Is this a real market valuation?",
     "a": "No. It is a transparent toy model showing how factors like age, contract length and form push a fee up or down. Real valuations involve clubs, agents, demand and a lot of negotiation."},
    {"q": "Why does contract length matter so much?",
     "a": "Because a player with under a year left can leave for free soon, so their selling club has little leverage and the fee collapses. A long contract protects the value."},
    {"q": "Why does value peak in the mid-twenties?",
     "a": "Because that is typically a player's prime: proven ability with years still ahead. Younger players carry uncertainty; older ones have fewer seasons left, so the model tapers value after the late twenties."},
    {"q": "What is the form index?",
     "a": "A simple multiplier where 1.0 is average. Above 1 reflects a hot streak that inflates value; below 1 a slump that deflates it."},
    {"q": "Why include this if it is not real?",
     "a": "Because it makes the logic of the transfer market visible. The direction each factor pushes value is realistic, even though the exact figure is illustrative."},
])
