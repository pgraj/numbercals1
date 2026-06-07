from core.faqs import register_faqs
register_faqs("trig-radians", [
    {"q": "What is a radian?",
     "a": "A radian is the angle you get when the arc along a circle equals the "
          "circle's radius. A full turn is 2π radians, which is why 360° = 2π and "
          "180° = π radians."},
    {"q": "How do I convert between degrees and radians?",
     "a": "Multiply degrees by π/180 to get radians, or multiply radians by 180/π "
          "to get degrees. For example, 90° × π/180 = π/2 radians."},
    {"q": "Can you give a worked example?",
     "a": "To convert 180° to radians: 180 × π/180 = π ≈ 3.1416 radians. Going the "
          "other way, π/3 radians × 180/π = 60°."},
    {"q": "Why use radians instead of degrees?",
     "a": "Radians tie an angle directly to arc length and make the formulas of "
          "calculus and wave physics much simpler. Degrees are convenient for "
          "everyday angles, but advanced maths and science almost always use "
          "radians."},
    {"q": "Where is this used in real life?",
     "a": "Engineers and physicists use radians for rotational motion, angular "
          "velocity, and oscillations; computer graphics and robotics use them for "
          "rotation; and they are standard in signal processing and astronomy."},
    {"q": "How do I find arc length from an angle?",
     "a": "Use s = rθ, where r is the radius and θ is the angle in radians. For "
          "example, a radius of 5 with θ = 2 radians gives s = 5 × 2 = 10. If the "
          "angle is in degrees, convert it with ×π/180 first — switch the toggle and "
          "the calculator does this for you."},
    {"q": "How do I find the area of a sector?",
     "a": "Use A = ½r²θ with θ in radians. A radius of 4 and θ = π/2 (i.e. 90°) gives "
          "A = ½ × 16 × π/2 ≈ 12.57 square units. The sector is the fraction θ/2π of "
          "the whole circle, which is where the formula comes from."},
])
