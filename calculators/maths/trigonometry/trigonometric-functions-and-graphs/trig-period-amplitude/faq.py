from core.faqs import register_faqs
register_faqs("trig-period-amplitude", [
    {"q": "What is amplitude?",
     "a": "Amplitude is the distance from the midline of a wave to its peak — how "
          "tall the wave is. For y = A·sin(Bx), the amplitude is the absolute "
          "value of A."},
    {"q": "What is the period?",
     "a": "The period is the horizontal length of one complete cycle before the "
          "wave repeats. For y = A·sin(Bx) it is 360°/|B|, or 2π/|B| in radians."},
    {"q": "Can you give a worked example?",
     "a": "For y = 3·sin(2x), the amplitude is 3 and the period is 360°/2 = 180°. "
          "The wave is three units tall and completes a full cycle every 180°."},
    {"q": "How are amplitude and frequency related?",
     "a": "Amplitude (height) and frequency (cycles per unit) are independent. B "
          "controls frequency and period; A controls amplitude. Doubling B halves "
          "the period without touching the height."},
    {"q": "Where is this used in real life?",
     "a": "Amplitude and period describe sound (loudness and pitch), light, radio "
          "waves, springs and pendulums, AC electricity, and any repeating signal "
          "studied in physics and engineering."},
])
