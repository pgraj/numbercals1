from core.faqs import register_faqs
register_faqs("trig-transformations", [
    {"q": "What do A, B, C, and D do in y = A·sin(Bx + C) + D?",
     "a": "A is the amplitude (height), B sets the period as 360°/|B|, C produces "
          "a horizontal phase shift of −C/B, and D shifts the whole curve up or "
          "down to a new midline."},
    {"q": "How do I find the period from B?",
     "a": "Divide 360° (or 2π radians) by the absolute value of B. So y = "
          "sin(2x) has period 360°/2 = 180°, completing two full waves in the "
          "space the basic sine does one."},
    {"q": "Can you give a worked example?",
     "a": "For y = 2·sin(x), the amplitude is 2 and the period is 360°. At x = 90° "
          "the value is 2·sin 90° = 2 — twice the height of the basic sine curve."},
    {"q": "What is a phase shift?",
     "a": "It is a horizontal slide of the curve, equal to −C/B. A positive C "
          "moves the wave to the left and a negative C moves it to the right, "
          "without changing its shape."},
    {"q": "Where is this used in real life?",
     "a": "These transformations model real waves: tides (vertical shift for mean "
          "sea level), sound (amplitude for loudness, period for pitch), AC "
          "voltage, and daylight hours through the year."},
])
