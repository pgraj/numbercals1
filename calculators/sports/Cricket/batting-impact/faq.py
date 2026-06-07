from core.faqs import register_faqs

register_faqs("batting-impact", [
    {"q": "Is this an official rating?",
     "a": "No. It is a transparent index that rewards both runs and scoring speed relative to a format's par strike rate. The weighting is our teaching choice, not an official metric."},
    {"q": "What is a par strike rate?",
     "a": "A rough benchmark for normal scoring in a format, around 130 for T20 and lower for one-day or Test cricket. Beating par lifts your impact score; falling short lowers it."},
    {"q": "Why blend runs and tempo?",
     "a": "Because 50 off 30 balls is more valuable than 50 off 60 in a run chase. Volume alone misses tempo, which this score tries to capture."},
    {"q": "Does this judge match situation?",
     "a": "Only loosely, through the par strike rate you choose. A fuller impact metric would weigh the game state, pressure and opposition, which this simplifies."},
    {"q": "How should I use it?",
     "a": "As a quick comparative read that values aggressive, productive batting, not as an authoritative rating."},
])
