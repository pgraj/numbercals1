from core.faqs import register_faqs

register_faqs("trig-sin-cos-tan", [
    {"q": "How do I find a missing side with trigonometry?",
     "a": "Identify the angle and the two sides involved, choose the ratio that "
          "uses exactly those sides (sine, cosine, or tangent), then rearrange so "
          "the unknown side is the subject and substitute the known values."},
    {"q": "Which ratio should I use?",
     "a": "Use sine for the opposite and hypotenuse, cosine for the adjacent and "
          "hypotenuse, and tangent for the opposite and adjacent. Label the sides "
          "first, then the right ratio is obvious."},
    {"q": "Can you give a worked example?",
     "a": "With an angle of 30° and a hypotenuse of 10, to find the opposite side "
          "use opposite = hypotenuse × sin θ = 10 × sin 30° = 10 × 0.5 = 5. The same "
          "angle in radians is 30° = π/6 ≈ 0.5236 rad; switch the toggle and the "
          "working re-derives unchanged."},
    {"q": "Do I multiply or divide?",
     "a": "If the unknown is on the top of the ratio you multiply; if it is on "
          "the bottom you divide. Always keep your calculator in the same angle "
          "mode — degrees or radians — as the angle you were given."},
    {"q": "Where is this used in real life?",
     "a": "Builders work out ramp and roof lengths, engineers size cables and "
          "supports, surveyors measure inaccessible distances, and computer "
          "graphics and robotics use these ratios to position and move objects."},
])
