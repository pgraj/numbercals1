from core.faqs import register_faqs

register_faqs("win-shares-impact", [
    {"q": "Is this real Win Shares?",
     "a": "No. Official Win Shares (from Basketball-Reference) use a detailed model of offence, defence and pace. This is a simplified approximation based on marginal scoring, clearly labelled illustrative."},
    {"q": "What does 'marginal' scoring mean?",
     "a": "Scoring above what a freely available replacement-level player would provide. Only the points above that baseline count toward wins, since the baseline is easy to replace."},
    {"q": "What is points-per-win?",
     "a": "Roughly how many extra points a team needs to convert into one extra win over a season. The model divides marginal points by this to estimate wins added."},
    {"q": "Why approximate at all?",
     "a": "To show the core idea, that individual production can be expressed in team wins, without the heavy machinery of the full model. The concept is sound even if the number is rough."},
    {"q": "Should I quote this number?",
     "a": "Not as a real Win Shares figure. Use it to understand the concept, then look up official Win Shares if you need a defensible value."},
])
