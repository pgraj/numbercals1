from core.faqs import register_faqs

register_faqs("convert-angular-velocity", [
    {"q": "What does the Angular Velocity Converter do?",
     "a": "It converts convert angular velocity between rad/s, rpm and deg/s via radians per second by first normalising your value to the SI base unit "
          "(radian per second) and then scaling to your chosen target unit. This hub-and-spoke "
          "approach guarantees every unit pair is internally consistent."},
    {"q": "Can you show a worked example?",
     "a": "3000 RPM to rad/s: 3000 × 0.10472 ≈ 314.16 rad/s."},
    {"q": 'How do I convert RPM to rad/s?',
     "a": 'One revolution is 2π radians and a minute is 60 seconds, so 1 RPM = 2π/60 ≈ 0.10472 rad/s. Radians per second is the form physics needs because it plugs straight into v = ω·r to get rim speed.'},
    {"q": "Where is this used in real life?",
     "a": "Rotating machinery, motors, turbines and gearbox design."},
    {"q": "What are the limits or edge cases?",
     "a": "Conversions are exact ratios where the units are defined exactly (most SI and "
          "imperial units) and best-available constants otherwise. Extremely large or small "
          "magnitudes are shown in general (g) format; round-tripping through the base unit "
          "may introduce tiny floating-point differences in the final decimal places."},
])
