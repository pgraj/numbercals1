from core.faqs import register_faqs

register_faqs("lineup-impact", [
    {"q": "What is net rating?",
     "a": "Points scored minus points allowed per 100 possessions while a lineup is on court. It is the standard way to judge how well a five-man unit performs."},
    {"q": "Why per 100 possessions?",
     "a": "Because teams play at different paces. Standardising to 100 possessions lets you compare a fast and a slow lineup fairly, by removing the effect of tempo."},
    {"q": "What is a good net rating?",
     "a": "Positive means outscoring opponents. Elite lineups post double-digit net ratings, but small samples are noisy, so a few minutes together can mislead."},
    {"q": "What are offensive and defensive ratings?",
     "a": "The two halves of net rating: points scored per 100 (offence) and points allowed per 100 (defence). A great lineup is strong at both."},
    {"q": "Is this a real metric?",
     "a": "Yes. Net rating is a core team and lineup metric used throughout modern basketball analysis."},
])
