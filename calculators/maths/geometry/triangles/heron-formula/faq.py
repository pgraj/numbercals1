from core.faqs import register_faqs
register_faqs("geo-heron", [
    {"q": "What is Heron's formula?",
     "a": "Heron's formula gives a triangle's area from its three sides alone: "
          "Area = sqrt(s(s-a)(s-b)(s-c)), where s = (a+b+c)/2 is the "
          "semi-perimeter. No angle or height is needed."},
    {"q": "Why is this in Geometry rather than Trigonometry?",
     "a": "Because the formula uses only side lengths, with no angle anywhere in "
          "it — that makes it a result of pure geometry. Trigonometry studies the "
          "relationship between sides and angles; Heron's formula needs no angle, "
          "so its natural home is geometry."},
    {"q": "Can you give a worked example?",
     "a": "For a 3-4-5 triangle: s = (3+4+5)/2 = 6, so Area = sqrt(6 x 3 x 2 x 1) "
          "= sqrt(36) = 6 square units, matching the familiar right-triangle area."},
    {"q": "Who discovered it?",
     "a": "It is credited to Hero (or Heron) of Alexandria, who proved it in his "
          "work Metrica around 60 AD, though it may have been known to Archimedes "
          "two centuries earlier and was found independently in China by Qin "
          "Jiushao in 1247."},
    {"q": "Where is this used in real life?",
     "a": "Surveyors and civil engineers find land and plot areas from side "
          "measurements, architects and builders work out triangular areas, and "
          "it is used in computer graphics to find the area of triangular faces "
          "in 3D meshes."},
])
