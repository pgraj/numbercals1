from core.faqs import register_faqs

register_faqs("injury-recovery-impact", [
    {"q": "Is this medical advice?",
     "a": "No, absolutely not. It is a rough planning estimate that scales a typical recovery window by severity and age. Always follow a qualified clinician for any real injury."},
    {"q": "Why does severity matter so much?",
     "a": "Because a minor strain and a torn ligament are worlds apart. The severity factor stretches the timeline sharply as the injury gets worse, which is why it dominates the estimate."},
    {"q": "Why does age affect recovery?",
     "a": "Older bodies tend to heal a little slower, so the model adds a small factor with age. Individual health and fitness matter at least as much, which a formula cannot capture."},
    {"q": "Why is this so simplified?",
     "a": "Because real recovery depends on the specific injury, the treatment, rehab quality and the individual, none of which a generic tool knows. It only sketches a ballpark."},
    {"q": "What should I actually do if injured?",
     "a": "See a doctor or physiotherapist. Use this only to get a rough sense of scale, never to decide when to return to play."},
])
