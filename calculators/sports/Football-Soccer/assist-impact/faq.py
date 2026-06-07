from core.faqs import register_faqs

register_faqs("assist-impact", [
    {"q": "What is a goal involvement?",
     "a": "A goal or an assist. Adding them gives a single number for how directly a player contributes to scoring, which this calculator expresses per 90 minutes."},
    {"q": "Why is the assist share useful?",
     "a": "It shows whether a player is more of a creator or a finisher. A winger might be 70% assists, a striker the reverse, which tells you their role at a glance."},
    {"q": "Are assists undervalued?",
     "a": "Many argue so, since creating a great chance can be harder than finishing it. Looking at involvements rather than goals alone gives creators their due."},
    {"q": "Does this capture all creativity?",
     "a": "No. It misses the pass before the assist, key passes that are not converted, and build-up play. It is a headline figure, not the full creative picture."},
    {"q": "Why per 90 again?",
     "a": "Because raw totals favour players who simply play more. Per-90 rates let you compare a regular starter with someone who plays fewer minutes."},
])
