from core.faqs import register_faqs

register_faqs("player-performance-impact", [
    {"q": "Is this an official player rating?",
     "a": "No. It is a transparent, made-up index that weights goals, assists, key passes and tackles. The weights are our choice for teaching, not an industry standard."},
    {"q": "Why normalise to per 90 minutes?",
     "a": "So a substitute who plays 20 minutes can be compared fairly with someone who plays the full match. Per-90 stats are the standard way analysts level the playing field."},
    {"q": "Why are goals and assists weighted highest?",
     "a": "Because they most directly affect the scoreline. The weights here (4 for a goal, 3 for an assist) reflect that, but you should treat the exact number as illustrative."},
    {"q": "Does this work for defenders?",
     "a": "Partly. It rewards tackles, but a defender's positioning and marking barely show up in basic stats, so the index understates them. Read it alongside the defensive calculator."},
    {"q": "How should I use the score?",
     "a": "As a rough, comparable snapshot, not a verdict. It is best for spotting big differences, not splitting hairs between similar players."},
])
