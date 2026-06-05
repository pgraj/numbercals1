from core.faqs import register_faqs

register_faqs("trig-inverse", [
    {"q": "What are inverse trigonometric functions?",
     "a": "Inverse sine, cosine, and tangent (written sin⁻¹, cos⁻¹, tan⁻¹) turn "
          "a ratio of sides back into the angle that produced it. They undo the "
          "ordinary sine, cosine, and tangent."},
    {"q": "Which inverse function do I use?",
     "a": "Choose by the sides you know: opposite and hypotenuse use inverse "
          "sine, adjacent and hypotenuse use inverse cosine, and opposite and "
          "adjacent use inverse tangent."},
    {"q": "Can you show a worked example?",
     "a": "If the opposite is 5 and the hypotenuse is 10, then sin θ = 5/10 = "
          "0.5, so θ = sin⁻¹(0.5) = 30°."},
    {"q": "Where is the inverse button on a calculator?",
     "a": "It is usually the second function above the sin, cos, and tan keys, "
          "reached with a shift or 2nd key. Make sure the calculator is set to "
          "degrees when you expect an answer in degrees."},
    {"q": "Where is this used in real life?",
     "a": "Engineers find slope and ramp angles, pilots and sailors compute "
          "headings, construction crews check pitch and incline, and physicists "
          "and game developers work out launch and reflection angles."},
])
