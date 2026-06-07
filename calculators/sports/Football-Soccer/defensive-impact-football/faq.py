from core.faqs import register_faqs

register_faqs("defensive-impact-football", [
    {"q": "Is this an official defensive rating?",
     "a": "No, it is a transparent index that adds tackles, interceptions, clearances and blocks per 90 minutes, with our own weights. Treat it as illustrative."},
    {"q": "Why are blocks weighted double?",
     "a": "Because a block is often a last-ditch act that prevents a near-certain goal, so the index gives it extra credit. The exact weighting is a teaching choice."},
    {"q": "Does a high score mean a great defender?",
     "a": "Not necessarily. Busy defensive stats can mean a player is constantly under pressure, which might reflect a weak team rather than individual brilliance. Context matters."},
    {"q": "What does this miss?",
     "a": "Positioning, anticipation and the duels a defender wins simply by being in the right place, none of which show up in counting stats. The best defenders sometimes have quiet stat lines."},
    {"q": "How should I read it?",
     "a": "As a measure of defensive workload and activity, useful for comparison, but never the whole story of how good a defender is."},
])
