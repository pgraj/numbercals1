from core.faqs import register_faqs

register_faqs("defensive-impact-basketball", [
    {"q": "Is this an official rating?",
     "a": "No. It is a transparent per-36-minute index combining steals, blocks and defensive rebounds, with our own weights. Treat it as illustrative."},
    {"q": "What are 'stocks'?",
     "a": "A nickname for steals plus blocks, the two headline defensive box-score stats. They capture disruptive defence but miss a lot of quieter work."},
    {"q": "Why per 36 minutes?",
     "a": "Because 36 minutes is close to a starter's workload, so per-36 stats let you compare a bench player fairly with a starter."},
    {"q": "What does this miss?",
     "a": "Most of defence: positioning, contests that do not become blocks, communication and the shots deterred just by being there. Box-score defence is famously incomplete."},
    {"q": "Why count defensive rebounds at half?",
     "a": "Because ending the opponent's possession matters, but a rebound is less purely defensive than a steal or block. The half-weight is a teaching choice you can disagree with."},
])
