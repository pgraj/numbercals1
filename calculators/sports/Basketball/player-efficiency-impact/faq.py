from core.faqs import register_faqs

register_faqs("player-efficiency-impact", [
    {"q": "Is EFF a real metric?",
     "a": "Yes. Efficiency (EFF) is a long-standing box-score rating used by the NBA: positive contributions (points, rebounds, assists, steals, blocks) minus misses and turnovers."},
    {"q": "What are its limitations?",
     "a": "It rewards volume and can flatter players who shoot a lot, and it undervalues defence and efficiency. Advanced metrics like PER and BPM try to fix that, but EFF is simple and transparent."},
    {"q": "Why subtract missed shots and turnovers?",
     "a": "Because they are wasted possessions that hurt the team. Counting only the good stuff would reward a player who scores 20 but misses 25 shots, which EFF rightly penalises."},
    {"q": "Can I use per-game or season totals?",
     "a": "Either, as long as you are consistent. Per-game is best for comparing players; season totals show cumulative contribution."},
    {"q": "What is a good EFF?",
     "a": "Star players often post per-game EFF in the mid-20s and up. Compare within the same league and era for it to mean much."},
])
