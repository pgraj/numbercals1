from core.faqs import register_faqs
register_faqs("trig-sine-rule", [
    {"q": "What is the sine rule?",
     "a": "The sine rule states that in any triangle, each side divided by the "
          "sine of its opposite angle gives the same value: a/sin A = b/sin B = "
          "c/sin C. It works for all triangles, not just right-angled ones."},
    {"q": "When should I use the sine rule?",
     "a": "Use it when you know a side and its opposite angle, plus one more side "
          "or angle — typically two angles and a side (AAS/ASA) or two sides and a "
          "non-included angle (SSA)."},
    {"q": "Can you give a worked example?",
     "a": "With a = 7 opposite A = 30°, to find b opposite B = 45°: b = a·sin B / "
          "sin A = 7·sin 45° / sin 30° ≈ 9.90."},
    {"q": "What is the ambiguous case?",
     "a": "When finding an angle from two sides and a non-included angle (SSA), "
          "the inverse sine can give two valid answers — an acute angle and its "
          "obtuse supplement — so up to two triangles may fit."},
    {"q": "Where is this used in real life?",
     "a": "Surveyors and navigators use it to find distances they cannot measure "
          "directly, engineers use it in trusses and structures, and it appears in "
          "astronomy and triangulation for positioning."},
])
