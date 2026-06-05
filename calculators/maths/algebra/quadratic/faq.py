from core.faqs import register_faqs

register_faqs("quadratic", [
    {"q": "What is a quadratic equation?",
     "a": "An equation of the form ax² + bx + c = 0, where the highest power of x "
          "is 2. Its graph is a parabola, a smooth U-shaped (or ∩-shaped) curve."},
    {"q": "What is the quadratic formula?",
     "a": "x = (−b ± √(b² − 4ac)) / 2a. The ± gives the two possible solutions, "
          "which are the points where the parabola crosses the x-axis."},
    {"q": "What does the discriminant tell me?",
     "a": "The discriminant is b² − 4ac. If it is positive there are two real "
          "roots; if zero, one repeated root; if negative, no real roots — the "
          "parabola never touches the x-axis and the roots are complex."},
    {"q": "Where is this used in real life?",
     "a": "Projectile paths — the height of a thrown ball over time is a quadratic, "
          "and the roots tell you when it lands. Area problems — finding a "
          "rectangle's dimensions from its area and perimeter. Business — profit "
          "models that rise then fall, where the roots mark break-even points and "
          "the vertex marks maximum profit."},
    {"q": "How does the parabola graph help?",
     "a": "The curve shows the roots as the points where it crosses the x-axis "
          "and the vertex as its turning point, so you can see at a glance how "
          "many real solutions the equation has."},
])
