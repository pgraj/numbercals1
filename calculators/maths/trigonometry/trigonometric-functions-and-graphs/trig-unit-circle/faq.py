from core.faqs import register_faqs

register_faqs("trig-unit-circle", [
    {"q": "What is the unit circle?",
     "a": "The unit circle is a circle of radius 1 centred at the origin. For an "
          "angle θ measured anticlockwise from the positive x-axis, the point "
          "where the angle's arm meets the circle has coordinates (cos θ, sin θ)."},
    {"q": "Why are the coordinates exactly cosine and sine?",
     "a": "Because the radius is 1, the right triangle drawn from the point has a "
          "hypotenuse of 1. The adjacent side is then cos θ and the opposite side "
          "is sin θ, so the point sits at (cos θ, sin θ) with no scaling needed."},
    {"q": "Can you give a worked example?",
     "a": "At θ = 60°, the point on the unit circle is (cos 60°, sin 60°) = (0.5, "
          "0.866). It lies in Quadrant I, where both coordinates are positive. The "
          "same angle in radians is 60° = π/3 ≈ 1.0472 rad — flip the "
          "Degrees/Radians toggle to enter and read it either way."},
    {"q": "How does the unit circle extend trigonometry past 90°?",
     "a": "Right-angle trig only defines ratios for acute angles, but the unit "
          "circle defines sine and cosine for every angle, including obtuse, "
          "reflex, and negative ones. The sign of each coordinate depends on the "
          "quadrant, which is why the sine and cosine graphs rise and fall."},
    {"q": "Why are radians natural on the unit circle?",
     "a": "On a circle of radius 1, the arc length swept equals the angle measured "
          "in radians. A full turn is 2π, a right angle is π/2, and a straight "
          "angle is π — which is why higher mathematics measures angles this way."},
    {"q": "Where is this used in real life?",
     "a": "Engineers and physicists model anything that oscillates or rotates — "
          "alternating current, sound and light waves, springs, and orbits. "
          "Computer graphics and game developers use it for rotation and circular "
          "motion, and navigators use it for circular bearings."},
])
