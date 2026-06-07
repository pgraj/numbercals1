from core.faqs import register_faqs
register_faqs("acceleration", [
    {"q": "What is acceleration, in simple words?",
     "a": "Acceleration is how quickly your speed changes. If a car gains 5 metres per "
          "second of speed every second, its acceleration is 5 m/s\u00b2."},
    {"q": "What do u, v and t mean?",
     "a": "u is your starting velocity, v is your final velocity, and t is the time taken. "
          "The formula is a = (v \u2212 u) \u00f7 t \u2014 the change in velocity divided "
          "by the time."},
    {"q": "Can you show an example?",
     "a": "A car goes from rest (u = 0) to 20 m/s (v = 20) in 4 seconds. Acceleration = "
          "(20 \u2212 0) \u00f7 4 = 5 m/s\u00b2. It gains 5 m/s of speed every second."},
    {"q": "What does negative acceleration mean?",
     "a": "It means slowing down (deceleration). If the final velocity is less than the "
          "starting velocity, v \u2212 u is negative, so the acceleration comes out "
          "negative \u2014 the object is braking."},
    {"q": "What are the units?",
     "a": "Velocity is in metres per second (m/s) and time in seconds, so acceleration is "
          "in metres per second squared (m/s\u00b2). For comparison, gravity speeds a "
          "falling object up by about 9.81 m/s\u00b2."},
    {"q": "Where do I see acceleration in real life?",
     "a": "A car pulling away from traffic lights, a plane speeding up for take-off, or a "
          "ball you drop falling faster and faster \u2014 all are acceleration."},
])
