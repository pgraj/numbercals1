from core.faqs import register_faqs

register_faqs("xg-impact", [
    {"q": "What is xG?",
     "a": "Expected Goals, a measure of chance quality. Each shot is given a value between 0 and 1 for how likely an average player would be to score it, so a tap-in might be 0.8 and a long-range pot-shot 0.03."},
    {"q": "Where do the xG values come from?",
     "a": "Proper xG models are trained on thousands of shots using angle, distance, body part and more. This calculator sums the per-shot values you provide, so it is only as good as those inputs."},
    {"q": "What does it mean to over-perform xG?",
     "a": "Scoring more goals than your total xG suggests clinical finishing, or a hot streak. Under-performing suggests wasteful finishing or bad luck, which often regresses over time."},
    {"q": "Why compare xG for and against?",
     "a": "Because it shows whether you created better chances than you allowed. A positive xG difference over many games is a strong sign of a good team, even if results lag."},
    {"q": "Is high xG a guarantee of winning?",
     "a": "No. xG measures chance quality, not the final score. Finishing, goalkeeping and luck all sit between xG and the result, which is exactly why the comparison is interesting."},
])
