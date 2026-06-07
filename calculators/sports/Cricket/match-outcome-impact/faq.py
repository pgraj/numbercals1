from core.faqs import register_faqs

register_faqs("match-outcome-impact", [
    {"q": "Is this a real win predictor?",
     "a": "No. It is a simplified chase model comparing the required run rate with the current rate, plus wickets in hand. Real predictors use ball-by-ball data and history."},
    {"q": "What is required run rate?",
     "a": "The runs per over the chasing team needs to win, found by dividing runs still needed by overs left. As it climbs above the current rate, pressure mounts."},
    {"q": "Why do wickets in hand matter?",
     "a": "Because a team with wickets to spare can take risks and accelerate, while one near all-out must be cautious. The model nudges the probability up when more wickets remain."},
    {"q": "Why use a logistic curve?",
     "a": "To keep the probability between 0 and 100% and make it respond smoothly to the rate gap and wickets. It mirrors how a chase tilts gradually, then sharply."},
    {"q": "How accurate is it?",
     "a": "Roughly indicative at best. It is built to show the logic of a run chase, not to call the result. Treat the percentage as illustrative."},
])
