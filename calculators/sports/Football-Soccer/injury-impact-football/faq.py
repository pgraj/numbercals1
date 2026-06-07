from core.faqs import register_faqs

register_faqs("injury-impact-football", [
    {"q": "What does this estimate?",
     "a": "The league points a team is likely to forgo while a key player is injured, based on how many matches they miss and the team's points-per-game with and without them."},
    {"q": "Where do I get the points-per-game figures?",
     "a": "From the team's record in matches the player did and did not play. The gap between those two rates is the player's rough value to results."},
    {"q": "Is this precise?",
     "a": "No. Football has too many variables for that, and small samples are noisy. It is a back-of-envelope estimate to size the impact, not a guarantee."},
    {"q": "Why points rather than goals?",
     "a": "Because points are what decide league position and qualification. Translating an injury into lost points speaks the language of the table directly."},
    {"q": "Can one player really swing this much?",
     "a": "Sometimes. A standout player can be worth a noticeable points-per-game difference, which over a long injury adds up to a meaningful chunk of a season."},
])
