from core.faqs import register_faqs
register_faqs("trig-period-amplitude", [
    {"q": "What is amplitude?",
     "a": "Amplitude is the distance from the midline of a wave to its peak — how "
          "tall the wave is. For y = A·sin(Bx), the amplitude is the absolute "
          "value of A. It is a pure number, the same whether the x-axis is in "
          "degrees or radians."},
    {"q": "What is the period?",
     "a": "The period is the horizontal length of one complete cycle before the "
          "wave repeats. For y = A·sin(Bx) it is 360°/|B|, or 2π/|B| in radians — "
          "the same physical width, just labelled in different units."},
    {"q": "Can you give a worked example?",
     "a": "For y = 3·sin(2x), the amplitude is 3 and the period is 360°/2 = 180° "
          "(equivalently 2π/2 = π radians). The wave is three units tall and "
          "completes a full cycle every 180°. Flip the Degrees/Radians toggle to "
          "see the x-axis marked in multiples of π."},
    {"q": "How are amplitude and frequency related?",
     "a": "Amplitude (height) and frequency (cycles per unit) are independent. B "
          "controls frequency and period; A controls amplitude. Doubling B halves "
          "the period without touching the height."},
    {"q": "Where is this used in real life?",
     "a": "Amplitude and period describe sound (loudness and pitch), light, radio "
          "waves, springs and pendulums, AC electricity, and any repeating signal "
          "studied in physics and engineering."},
])
