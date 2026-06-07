from core.faqs import register_faqs

register_faqs("economy-rate-impact", [
    {"q": "What is economy rate?",
     "a": "Runs conceded per over by a bowler. An economy of 5.25 means the bowler gives away 5.25 runs each over on average."},
    {"q": "Why convert balls to overs?",
     "a": "Because an over is six balls, and bowlers often finish on part-overs. The calculator converts extra balls to fractions of an over so the rate is accurate."},
    {"q": "Is a low economy always best?",
     "a": "In limited-overs cricket it is prized, but a bowler who takes wickets while going for a few more runs can be more valuable. Economy is one of two key bowling measures, alongside wickets."},
    {"q": "How does economy differ from bowling average?",
     "a": "Average is runs per wicket; economy is runs per over. Economy rewards containment, average rewards taking wickets. Top bowlers do both."},
    {"q": "Is this the standard definition?",
     "a": "Yes. Runs conceded divided by overs bowled is the universally accepted economy rate."},
])
