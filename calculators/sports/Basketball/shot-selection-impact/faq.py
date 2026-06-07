from core.faqs import register_faqs

register_faqs("shot-selection-impact", [
    {"q": "What is effective field goal percentage?",
     "a": "A shooting stat that credits three-pointers as worth more, since they score an extra point. It answers whether a player's shot mix is efficient, not just whether shots go in."},
    {"q": "Why does it beat plain field-goal percentage?",
     "a": "Because plain FG% treats a three the same as a two. A player hitting lots of threes can have a modest FG% but an excellent eFG%, which reflects their real scoring value."},
    {"q": "What is good shot selection?",
     "a": "Taking high-value shots: layups, dunks and threes, while avoiding inefficient long twos. A high eFG% usually signals smart shot selection."},
    {"q": "Is this a real metric?",
     "a": "Yes. Effective field goal percentage is a standard, widely used efficiency measure."},
    {"q": "How is it different from true shooting?",
     "a": "eFG% covers field goals only; true shooting also folds in free throws. Use eFG% to judge shot selection, true shooting for overall scoring efficiency."},
])
