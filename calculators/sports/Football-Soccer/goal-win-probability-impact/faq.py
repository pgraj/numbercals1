from core.faqs import register_faqs

register_faqs("goal-win-probability-impact", [
    {"q": "Are these real betting odds?",
     "a": "No. This is a simplified teaching model based on goal difference and time remaining. Real bookmaker and analytics models use far more data, so treat these numbers as illustrative."},
    {"q": "Why does the same goal matter more late in a game?",
     "a": "Because there is less time for the opponent to respond. The model weights time remaining, so a goal in the 85th minute swings the win probability more than one in the 20th."},
    {"q": "What is a logistic curve and why use it?",
     "a": "It is an S-shaped function that keeps probabilities between 0 and 100% and changes fastest in the middle. It naturally captures how a tight game is more uncertain than a blowout."},
    {"q": "Can I model conceding a goal?",
     "a": "Yes, choose 'against' and it lowers your goal difference, showing how much win probability you shed."},
    {"q": "Why is this useful even if it is simplified?",
     "a": "It builds intuition for why teams defend leads differently late on, and why a single goal can feel decisive. The shape of the swing is realistic even though the exact numbers are not official."},
])
