from core.faqs import register_faqs
register_faqs("trig-heron", [
    {"q": "How does this differ from the geometry Heron's formula calculator?",
     "a": "The geometry version applies the finished formula √(s(s−a)(s−b)(s−c)) "
          "directly. This trigonometry version derives the area instead: it uses "
          "the cosine rule to find the included angle, then the area formula "
          "½·a·b·sin C, and shows that the result is exactly Heron's formula."},
    {"q": "Why does ½·a·b·sin C give the same answer as Heron's formula?",
     "a": "Substitute cos C = (a²+b²−c²)/(2ab) from the cosine rule into "
          "sin C = √(1−cos²C), then into ½·a·b·sin C. After simplifying, the "
          "expression collapses to √(s(s−a)(s−b)(s−c)) — Heron's formula. The two "
          "are algebraically identical, so they always agree."},
    {"q": "Can you give a worked example?",
     "a": "For a 3-4-5 triangle, the angle between sides 3 and 4 has "
          "cos C = (9+16−25)/(2·3·4) = 0, so C = 90° and sin C = 1. Then "
          "Area = ½·3·4·1 = 6 — the same as Heron's √(6·3·2·1) = 6 square units."},
    {"q": "What is the included angle C here?",
     "a": "C is the angle between sides a and b, the side opposite it being c. The "
          "cosine rule pins it down from the three side lengths. It is only an "
          "intermediate step — what the area formula actually needs is sin C."},
    {"q": "Where is this used in real life?",
     "a": "The cosine-rule-to-area route is common in surveying and navigation, "
          "where two distances and the angle between them are known, and in "
          "computer graphics and physics, where triangle areas are computed from "
          "vectors whose included angle comes from a dot product."},
])
