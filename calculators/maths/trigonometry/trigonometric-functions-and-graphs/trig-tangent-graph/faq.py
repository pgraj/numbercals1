from core.faqs import register_faqs
register_faqs("trig-tangent-graph", [
    {"q": "Why does the tangent graph have gaps?",
     "a": "Tangent equals sine divided by cosine. Wherever cosine is zero — at "
          "90°, 270°, and every 180° apart — the value is undefined, creating "
          "vertical asymptotes the curve never crosses."},
    {"q": "What is the period of y = tan x?",
     "a": "The tangent function repeats every 180°, half the 360° period of sine "
          "and cosine. Its range is all real numbers, from negative infinity to "
          "positive infinity."},
    {"q": "Can you give a worked example?",
     "a": "At x = 45°, tan 45° = 1. As x approaches 90°, tan x grows without bound "
          "toward infinity, and at exactly 90° it is undefined."},
    {"q": "What happens near an asymptote?",
     "a": "Just below 90° the tangent is very large and positive; just above 90° "
          "it is very large and negative. The curve shoots up to +∞ on one side "
          "and comes up from −∞ on the other."},
    {"q": "Where is this used in real life?",
     "a": "Tangent describes slopes and gradients, the steepness of ramps and "
          "roofs, and angles of elevation; it appears in optics, surveying, and in "
          "computer graphics when working out viewing angles."},
])
