from core.faqs import register_faqs
register_faqs("trig-sine-rule-area", [
    {"q": "How do I find a triangle's area with two sides and an angle?",
     "a": "Use Area = ½·a·b·sin C, where a and b are two sides and C is the angle "
          "between them. It works for any triangle and needs no perpendicular "
          "height."},
    {"q": "How is this different from the basic area formula?",
     "a": "The basic ½ × base × height needs the perpendicular height. This "
          "version replaces height with b·sin C, so you can find the area straight "
          "from two sides and their included angle — handy alongside the sine and "
          "cosine rules."},
    {"q": "Can you give a worked example?",
     "a": "With a = 8, b = 11, and the included angle C = 37°: Area = ½·8·11·sin "
          "37° ≈ 44·0.602 ≈ 26.5 square units. The same angle in radians is "
          "37° ≈ 0.6458 rad; flip the Degrees/Radians toggle and the working "
          "updates to match."},
    {"q": "Which angle do I use?",
     "a": "Always the angle enclosed by the two sides you chose. With standard "
          "labelling, sides a and b enclose angle C; if you use sides b and c, the "
          "included angle is A instead."},
    {"q": "Where is this used in real life?",
     "a": "Surveyors and land valuers find areas of irregular plots from measured "
          "sides and angles, architects compute triangular surfaces, and it is "
          "used in engineering cross-sections and 3D mesh modelling."},
])
