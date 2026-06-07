from core.faqs import register_faqs

register_faqs("training-load-impact", [
    {"q": "What is ACWR?",
     "a": "The acute:chronic workload ratio, comparing this week's training load with a rolling four-week average. It flags whether you have ramped up too fast."},
    {"q": "Why does a sudden spike raise injury risk?",
     "a": "Because the body adapts gradually. Loading far above what it is used to (a high ratio) is linked in research to higher injury rates, while steady progression is safer."},
    {"q": "What is the sweet spot?",
     "a": "Studies often cite a ratio around 0.8 to 1.3 as lower risk. Below that may mean detraining; well above it is the danger zone the calculator warns about."},
    {"q": "Is ACWR settled science?",
     "a": "It is widely used but also debated, with critics noting it depends heavily on how load is measured. Treat it as a useful guide, not gospel."},
    {"q": "How do I measure 'load'?",
     "a": "Commonly as session duration times perceived effort, or via distance and intensity from a tracker. Use the same method for both figures so the ratio is meaningful."},
])
