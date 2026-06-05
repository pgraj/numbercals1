from core.faqs import register_faqs

register_faqs("trig-angles", [
    {"q": "What are the main types of angle?",
     "a": "An acute angle is less than 90°, a right angle is exactly 90°, an "
          "obtuse angle is between 90° and 180°, a straight angle is exactly "
          "180°, and a reflex angle is more than 180° but less than 360°."},
    {"q": "What is the difference between complementary and supplementary angles?",
     "a": "Complementary angles add up to 90°, while supplementary angles add up "
          "to 180°. For example, 30° and 60° are complementary, and 110° and 70° "
          "are supplementary."},
    {"q": "Can you give a worked example?",
     "a": "Take 135°. It is larger than 90° but smaller than 180°, so it is "
          "obtuse. It has no complement (only angles under 90° do), but its "
          "supplement is 180° − 135° = 45°."},
    {"q": "Why does a reflex angle go beyond 180°?",
     "a": "A reflex angle measures the larger opening between two rays — the way "
          "round that is more than a straight line. Every angle below 180° has a "
          "reflex partner that completes the full 360° turn."},
    {"q": "Where is this used in real life?",
     "a": "Carpenters and builders check right angles for square corners, "
          "navigators and pilots work with reflex and acute bearings, surveyors "
          "measure angles of slopes, and graphic designers and animators rotate "
          "objects by precise angles."},
])
