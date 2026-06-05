from core.faqs import register_faqs
register_faqs("trig-ambiguous-case", [
    {"q": "What is the ambiguous case in trigonometry?",
     "a": "It arises when you know two sides and a non-included angle (SSA). The "
          "given side opposite the angle can sometimes form two different valid "
          "triangles, one triangle, or none at all."},
    {"q": "Why can there be two triangles?",
     "a": "The sine rule gives sin B, and both an acute angle and its obtuse "
          "supplement (180° − B) have the same sine. If both keep the angle sum "
          "under 180°, both produce a genuine triangle."},
    {"q": "Can you give a worked example?",
     "a": "With a = 6, b = 8, and A = 30°: sin B = 8·sin 30° / 6 ≈ 0.667, giving "
          "B ≈ 41.8° or B ≈ 138.2°. Both fit, so there are two triangles."},
    {"q": "How do I know how many triangles there are?",
     "a": "If the computed sine exceeds 1, no triangle exists. If only the acute "
          "angle keeps the total under 180°, there is one. If both the acute and "
          "obtuse options work, there are two."},
    {"q": "Where is this used in real life?",
     "a": "Surveyors, navigators, and engineers must recognise when measurements "
          "leave a position ambiguous, so they take an extra reading to decide "
          "which of the two possible triangles is the real one."},
])
