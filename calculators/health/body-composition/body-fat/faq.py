from core.faqs import register_faqs

register_faqs("body-fat", [
    {"q": "What is the US Navy body-fat method?",
     "a": "It estimates body-fat percentage from a few tape measurements — neck and waist for men, "
          "plus hips for women — together with height. It was developed so body composition could be "
          "checked without special equipment, using only a tape measure. It is an approximation, not "
          "the lab-grade accuracy of a DEXA scan or hydrostatic weighing."},
    {"q": "Why does it need height, and why inches?",
     "a": "The formula includes a height term, so an accurate height changes the result — that is why "
          "height is one of the inputs here even though some summaries leave it out. The equation was "
          "published using inches, so this calculator takes its measurements in inches to match the "
          "original coefficients exactly."},
    {"q": "What counts as fat mass and lean mass?",
     "a": "Fat mass is the weight of body fat. Lean mass is everything else — muscle, bone, organs, "
          "and water. Your total body weight is the two added together, so once the percentage is "
          "known, multiplying by your weight splits it into those two parts."},
    {"q": "How do I read the donut?",
     "a": "The ring is your whole body weight. One arc is fat mass and the other is lean mass, sized "
          "by their share of the total. Seeing them side by side makes the percentage concrete: a "
          "thin fat arc and a large lean arc means most of your weight is muscle, bone and water."},
    {"q": "Where is this used in real life?",
     "a": "It is a practical field estimate — used by the military, gyms, and anyone tracking change "
          "over time with just a tape measure. Because it is approximate, the most useful thing is the "
          "trend: measuring the same way each month shows direction even if the absolute number is a "
          "little off. For a precise figure, a clinical body-composition scan is the gold standard."},
])
