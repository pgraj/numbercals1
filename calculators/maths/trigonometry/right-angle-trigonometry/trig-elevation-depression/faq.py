from core.faqs import register_faqs

register_faqs("trig-elevation-depression", [
    {"q": "What is an angle of elevation?",
     "a": "It is the angle measured upward from the horizontal to an object "
          "above your eye level — for example, looking up to the top of a tower. "
          "An angle of depression is the matching downward angle to something "
          "below you."},
    {"q": "Why are elevation and depression angles equal?",
     "a": "Between the same two points, the angle of elevation from the lower "
          "point equals the angle of depression from the higher point, because "
          "they are alternate angles between parallel horizontal lines."},
    {"q": "Can you give a worked example?",
     "a": "Standing 50 m from a tower with an angle of elevation of 40°, the "
          "height is distance × tan θ = 50 × tan 40° ≈ 41.95 m above eye level."},
    {"q": "Which ratio do these problems use?",
     "a": "Almost always tangent, because the height is the side opposite the "
          "angle and the horizontal distance is the side adjacent to it, and "
          "tangent links exactly those two sides."},
    {"q": "Where is this used in real life?",
     "a": "Surveyors measure building and mountain heights, air-traffic "
          "controllers track aircraft, lifeguards and coastguards judge distances "
          "to boats, and forestry workers estimate tree heights."},
])
