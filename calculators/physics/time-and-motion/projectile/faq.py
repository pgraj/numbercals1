from core.faqs import register_faqs

register_faqs("projectile", [
    {"q": "What is projectile motion?",
     "a": "It is the curved path an object follows when thrown or launched, "
          "pulled down by gravity while it keeps moving forward. The shape of "
          "that path is a parabola."},
    {"q": "How is the range calculated?",
     "a": "Range is how far the projectile travels horizontally before landing: "
          "R = v² · sin(2θ) / g, where v is launch speed, θ the launch angle, and "
          "g gravity. The sin(2θ) term is why 45° gives the greatest distance."},
    {"q": "Why does 45 degrees give the longest range?",
     "a": "Range depends on sin(2θ), which is largest when 2θ = 90°, i.e. θ = 45°. "
          "Steeper angles gain height but lose distance; shallower angles lose "
          "air time. 45° balances the two (ignoring air resistance)."},
    {"q": "Where is this used in real life?",
     "a": "Sport — the arc of a basketball shot, a long jump, or a golf drive. "
          "Engineering — water from a fountain or sprinkler, and the path of "
          "fireworks. Ballistics and safety — predicting where a launched object "
          "lands. Any time something is thrown and only gravity acts on it, this "
          "describes its flight."},
    {"q": "What is flight time and peak height?",
     "a": "Flight time is how long it stays in the air, 2v·sin(θ)/g. Peak height "
          "is the highest point it reaches, v²·sin²(θ)/(2g) — both grow with a "
          "steeper launch angle."},
])
