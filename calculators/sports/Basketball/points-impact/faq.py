from core.faqs import register_faqs

register_faqs("points-impact", [
    {"q": "What is true shooting percentage?",
     "a": "A scoring-efficiency measure that credits the extra value of three-pointers and free throws, unlike plain field-goal percentage. It answers how well a player turns shooting chances into points."},
    {"q": "Why the 0.44 for free throws?",
     "a": "Because not every free throw is a separate trip to the line (some come in pairs, and-ones, or technicals). The 0.44 factor is the standard estimate of free-throw possessions used across the NBA."},
    {"q": "What counts as a good true shooting percentage?",
     "a": "Around 55% is solid and roughly 60% or above is elite for a high-volume scorer. It varies by role and era, so compare like with like."},
    {"q": "Why is this better than points per game?",
     "a": "Because scoring a lot while missing a lot hurts the team. True shooting shows whether the points came efficiently, which points-per-game hides."},
    {"q": "Is this a real, standard metric?",
     "a": "Yes. True shooting percentage is widely used by analysts and broadcasters as the headline scoring-efficiency stat."},
])
