from core.faqs import register_faqs

register_faqs("trig-intro-ratios", [
    {"q": "What does SOH-CAH-TOA stand for?",
     "a": "It is a memory aid for the three ratios: Sine = Opposite ÷ "
          "Hypotenuse, Cosine = Adjacent ÷ Hypotenuse, and Tangent = Opposite ÷ "
          "Adjacent, all taken with respect to one acute angle."},
    {"q": "How do I know which side is opposite or adjacent?",
     "a": "Stand at the angle you care about. The hypotenuse is always opposite "
          "the right angle (the longest side). The opposite side is across from "
          "your angle, and the adjacent side is the remaining one beside it."},
    {"q": "Can you give a worked example?",
     "a": "In a 3-4-5 right triangle with opposite = 3, adjacent = 4 and "
          "hypotenuse = 5: sine = 3/5 = 0.6, cosine = 4/5 = 0.8, and tangent = "
          "3/4 = 0.75."},
    {"q": "Why do the ratios stay the same for any size triangle?",
     "a": "All right triangles with the same acute angle are similar, so their "
          "side ratios are identical regardless of size. That is why each ratio "
          "depends only on the angle."},
    {"q": "Where is this used in real life?",
     "a": "Surveyors and builders find heights and distances, engineers resolve "
          "forces into components, sailors and pilots navigate, sound and music "
          "engineers model waves, and game developers compute movement and "
          "lighting angles."},
])
