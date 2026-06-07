from core.faqs import register_faqs

register_faqs("bowling-impact", [
    {"q": "Is this an official rating?",
     "a": "No. It is a transparent index combining wickets with runs saved against a par economy. The 25-run value per wicket is our teaching choice."},
    {"q": "Why value a wicket at 25 runs?",
     "a": "As a rough run-equivalent: a wicket both removes a batter and slows scoring. Twenty-five is an illustrative figure, not an official conversion, so adjust it if you disagree."},
    {"q": "What are 'runs saved'?",
     "a": "How many fewer runs the bowler conceded than a par bowler would have over the same overs. Bowling tighter than par adds to the score; leaking runs subtracts."},
    {"q": "Does this capture pressure?",
     "a": "Not directly. Bowling a tight spell at the death is worth more than the same figures in a quiet phase, which this simplified index does not weigh."},
    {"q": "How should I read it?",
     "a": "As a combined view of wicket-taking and containment, useful for comparison, but illustrative rather than official."},
])
