from core.faqs import register_faqs
register_faqs("trig-cosine-graph", [
    {"q": "What does the graph of y = cos x look like?",
     "a": "It is a smooth wave identical in shape to the sine curve but starting "
          "at its maximum. At x = 0 it is 1, falls to 0 at 90°, reaches −1 at "
          "180°, returns to 0 at 270°, and back to 1 at 360°."},
    {"q": "How is the cosine graph related to the sine graph?",
     "a": "The cosine curve is the sine curve shifted 90° to the left: cos x = "
          "sin(x + 90°). They share the same amplitude, period, and range."},
    {"q": "Can you give a worked example?",
     "a": "At x = 60°, y = cos 60° = 0.5, so the point (60°, 0.5) lies on the "
          "curve. The same angle in radians is 60° = π/3 ≈ 1.0472 rad; the "
          "Degrees/Radians toggle marks the x-axis in multiples of π."},
    {"q": "What are its amplitude and period?",
     "a": "Amplitude 1 (it ranges between −1 and 1) and period 360° or 2π radians, "
          "after which the wave repeats exactly."},
    {"q": "Where is this used in real life?",
     "a": "Cosine waves model alternating current, sound and light, and any "
          "oscillation that starts at a peak; engineers use them for signal "
          "analysis, and they describe seasonal cycles and circular motion."},
])
