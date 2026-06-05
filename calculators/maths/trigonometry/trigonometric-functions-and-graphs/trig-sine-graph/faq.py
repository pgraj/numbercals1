from core.faqs import register_faqs

register_faqs("trig-sine-graph", [
    {"q": "What does the graph of y = sin x look like?",
     "a": "It is a smooth wave that oscillates between −1 and 1. Starting at 0, it "
          "rises to a maximum of 1 at 90°, returns to 0 at 180°, drops to a "
          "minimum of −1 at 270°, and comes back to 0 at 360°, then repeats."},
    {"q": "What are its amplitude and period?",
     "a": "The amplitude is 1 — the curve reaches a maximum of 1 and a minimum of "
          "−1. The period is 360° (or 2π radians), meaning the whole pattern "
          "repeats every full turn."},
    {"q": "Can you give a worked example?",
     "a": "At x = 30°, y = sin 30° = 0.5, so the point (30°, 0.5) lies on the "
          "curve. At x = 90° the curve reaches its peak, y = 1."},
    {"q": "How does the unit circle make the wave?",
     "a": "The sine of an angle is the height of the matching point on the unit "
          "circle. As the point goes round, its height traces out the wave — which "
          "is why the curve rises and falls and repeats every 360°."},
    {"q": "Where is this used in real life?",
     "a": "Sine waves model sound, light, radio signals, and alternating current; "
          "engineers use them for vibrations and oscillations, musicians and audio "
          "engineers for tones, and they describe tides, daylight hours, and many "
          "other naturally repeating patterns."},
])
