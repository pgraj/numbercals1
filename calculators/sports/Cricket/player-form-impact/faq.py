from core.faqs import register_faqs

register_faqs("player-form-impact", [
    {"q": "Is form a real, measurable thing?",
     "a": "Partly. Recent scores are real, but 'form' is a fuzzy, subjective idea. This index compares recent scores with a career average as a simple, transparent proxy."},
    {"q": "What does the index mean?",
     "a": "Above 1 means a player is scoring better than their career norm (in form); below 1 means worse. It is a ratio, so 1.2 is 20% above their usual level."},
    {"q": "Why can recent form be misleading?",
     "a": "Because a few innings is a small sample. One big score can flatter a struggling player, and one failure can mask good touch. Read it with caution."},
    {"q": "How many recent scores should I use?",
     "a": "Enough to smooth out noise but recent enough to mean something, often the last five to ten innings. The calculator averages whatever list you give it."},
    {"q": "Should selectors rely on this?",
     "a": "Only as one input. Form, fitness, conditions, opposition and role all matter. The index is a conversation starter, not a verdict."},
])
