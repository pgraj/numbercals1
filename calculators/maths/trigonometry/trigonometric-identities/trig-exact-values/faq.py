from core.faqs import register_faqs

register_faqs("trig-exact-values", [
    {"q": "Which angles have exact trigonometric values?",
     "a": "The standard special angles: 0, 30°, 45°, 60° and 90°, plus all of their "
          "reflections around the circle (120°, 135°, 150°, 180° … up to 360°). Their "
          "sin, cos and tan can be written exactly as surds — like √3/2 or √2/2 — with "
          "no calculator needed."},
    {"q": "Where do the exact values come from?",
     "a": "From two set-square triangles and the unit circle. The 45-45-90 triangle "
          "(sides 1 : 1 : √2) gives the 45° values, and the 30-60-90 triangle "
          "(sides 1 : √3 : 2) gives the 30° and 60° values. The axis angles "
          "(0, 90°, 180°, 270°) are read straight off the unit circle."},
    {"q": "Can you show a worked example?",
     "a": "Take θ = 150°. It sits in quadrant 2 with a reference angle of 30°, so the "
          "magnitudes match 30°: sin = 1/2, cos = √3/2, tan = √3/3. CAST says only sin "
          "is positive in quadrant 2, so sin 150° = 1/2, cos 150° = −√3/2 and "
          "tan 150° = −√3/3. The same angle in radians is 150° = 5π/6 ≈ 2.6180 rad, and "
          "the toggle re-derives the working in radians."},
    {"q": "What is the CAST rule?",
     "a": "CAST tells you which functions are positive in each quadrant, reading "
          "anticlockwise from quadrant 4: All in Q1, Sin in Q2, Tan in Q3, Cos in Q4. "
          "You find the value from the reference angle's triangle, then CAST fixes the "
          "sign."},
    {"q": "Why is tan undefined at 90° and 270°?",
     "a": "tan θ = sin θ / cos θ, and at 90° and 270° the cosine is 0, so the division "
          "is undefined. The calculator flags this rather than returning a misleading "
          "number."},
])
