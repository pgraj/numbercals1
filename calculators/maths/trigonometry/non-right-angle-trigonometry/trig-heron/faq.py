from core.faqs import register_faqs
register_faqs("trig-heron", [
    {"q": "What is Heron's formula?",
     "a": "Heron's formula gives a triangle's area from its three sides alone: "
          "Area = √(s(s−a)(s−b)(s−c)), where s = (a+b+c)/2 is the semi-perimeter. "
          "No angle or height is needed."},
    {"q": "What is the semi-perimeter?",
     "a": "The semi-perimeter s is half the triangle's perimeter, (a+b+c)/2. Each "
          "factor in the formula, (s−a), (s−b), (s−c), is the semi-perimeter minus "
          "one side."},
    {"q": "Can you give a worked example?",
     "a": "For a 3-4-5 triangle: s = (3+4+5)/2 = 6, so Area = √(6·3·2·1) = √36 = 6 "
          "square units — matching the familiar right-triangle area."},
    {"q": "When is Heron's formula most useful?",
     "a": "When you know all three side lengths but no angle and cannot easily "
          "measure the height — common for land plots, awkward shapes, or "
          "triangles defined only by coordinates."},
    {"q": "Where is this used in real life?",
     "a": "Surveyors and civil engineers find land and plot areas from side "
          "measurements, architects and builders work out triangular areas, and it "
          "is used in computer graphics to find the area of triangular faces."},
])
