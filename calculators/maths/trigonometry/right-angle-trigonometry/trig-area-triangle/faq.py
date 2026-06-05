from core.faqs import register_faqs

register_faqs("trig-area-triangle", [
    {"q": "When should I use Area = ½ab sin C?",
     "a": "Use it whenever you know two sides of a triangle and the angle "
          "between them but do not know the perpendicular height. It works for "
          "any triangle, not just right-angled ones."},
    {"q": "What is the included angle?",
     "a": "The included angle, C, is the angle formed between the two sides a and "
          "b that you are using. The formula only works with the angle that sits "
          "between those two sides."},
    {"q": "Can you give a worked example?",
     "a": "With sides a = 6 and b = 8 and an included angle C = 30°, the area is "
          "½ × 6 × 8 × sin 30° = ½ × 48 × 0.5 = 12 square units."},
    {"q": "How does it relate to ½ × base × height?",
     "a": "It is the same idea: b sin C is exactly the perpendicular height drawn "
          "to side a, so ½ab sin C is ½ × base × height in disguise — just more "
          "convenient when you know an angle instead of the height."},
    {"q": "Where is this used in real life?",
     "a": "Surveyors and land valuers find the area of irregular plots, "
          "architects and builders calculate triangular surfaces, engineers work "
          "out cross-sections, and game and graphics developers compute the area "
          "of triangular mesh faces."},
])
