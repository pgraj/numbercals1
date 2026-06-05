from core.faqs import register_faqs
register_faqs("trig-cosine-rule", [
    {"q": "What is the cosine rule?",
     "a": "The cosine rule states c² = a² + b² − 2ab·cos C for any triangle, where "
          "C is the angle opposite side c. It links all three sides with one "
          "angle."},
    {"q": "When should I use the cosine rule instead of the sine rule?",
     "a": "Use the cosine rule when you have two sides and the included angle "
          "(SAS) to find the third side, or all three sides (SSS) to find an "
          "angle — cases the sine rule cannot start from."},
    {"q": "Can you give a worked example?",
     "a": "With a = 5, b = 7, and the included angle C = 60°: c² = 25 + 49 − "
          "2·5·7·cos 60° = 74 − 35 = 39, so c = √39 ≈ 6.24. The same angle in "
          "radians is 60° = π/3 ≈ 1.0472 rad; switch the Degrees/Radians toggle "
          "and the working updates to match."},
    {"q": "How is it related to Pythagoras?",
     "a": "When C = 90° (π/2 ≈ 1.5708 rad), cos C = 0 and the formula reduces to "
          "c² = a² + b² — exactly Pythagoras' theorem. The cosine rule is its "
          "generalisation to any angle."},
    {"q": "Where is this used in real life?",
     "a": "Navigators and surveyors compute distances across awkward terrain, "
          "engineers analyse forces and frameworks, and it is used in GPS, "
          "robotics arm geometry, and computer graphics."},
])
