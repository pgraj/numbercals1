from core.faqs import register_faqs

register_faqs("break-even-property-advanced", [
    {"q": "What does break-even mean here?",
     "a": "The number of years until the property's combined returns (rental cashflow plus capital growth) recover the cash you invested up front."},
    {"q": "Why include capital growth, not just rent?",
     "a": "Because for many investors growth is the bigger return. Counting only cashflow would overstate how long it takes to get your money back."},
    {"q": "Is the straight-line assumption realistic?",
     "a": "It is a simplification. Real growth is lumpy, not steady, so the true break-even bounces around. The figure is a planning estimate, not a precise date."},
    {"q": "What if cashflow is negative?",
     "a": "Then growth has to do the heavy lifting. If the combined annual return is positive overall, you still break even, just more slowly."},
    {"q": "How does this differ from a simple payback?",
     "a": "A basic payback often counts only cashflow. This advanced version folds in capital growth, which is essential for property where growth usually dominates."},
])
