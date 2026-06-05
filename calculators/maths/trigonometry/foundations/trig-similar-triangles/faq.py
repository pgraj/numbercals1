from core.faqs import register_faqs

register_faqs("trig-similar-triangles", [
    {"q": "What makes two triangles similar?",
     "a": "Two triangles are similar when their corresponding angles are equal "
          "and their corresponding sides are in the same ratio. They have the "
          "same shape but can be different sizes."},
    {"q": "What is the scale factor?",
     "a": "The scale factor is the constant ratio between corresponding sides. If "
          "one triangle's side of 3 matches another's side of 6, the scale factor "
          "is 6 ÷ 3 = 2, so every side of the second triangle is twice as long."},
    {"q": "Can you show a worked example?",
     "a": "If side a₁ = 3 corresponds to a₂ = 6, the scale factor is 2. A side "
          "b₁ = 4 in the first triangle then matches b₂ = 4 × 2 = 8 in the "
          "second."},
    {"q": "How does this connect to trigonometry?",
     "a": "Because similar right triangles share the same angles, their side "
          "ratios stay fixed. That constant ratio is exactly what sine, cosine, "
          "and tangent measure, so similarity is the foundation of trigonometry."},
    {"q": "Where is this used in real life?",
     "a": "Architects and engineers use scale models and drawings, "
          "cartographers shrink real distances onto maps, photographers and film "
          "crews use similar-triangle optics for focus and framing, and surveyors "
          "find heights of tall objects from their shadows."},
])
