from core.faqs import register_faqs

register_faqs("trig-pythagorean-identities", [
    {"q": "What are the Pythagorean identities?",
     "a": "They are three always-true relationships between the trig functions: "
          "sin²θ + cos²θ = 1, 1 + tan²θ = sec²θ, and 1 + cot²θ = cosec²θ. The first "
          "comes straight from Pythagoras' theorem applied to the unit circle, and "
          "the other two follow by dividing it through by cos²θ and sin²θ."},
    {"q": "Can you show a worked example?",
     "a": "Take θ = 30°. Then sin 30° = 0.5 and cos 30° ≈ 0.8660. Squaring gives "
          "0.25 and 0.75, and 0.25 + 0.75 = 1 exactly — the identity holds. Switch "
          "the toggle to radians and θ = 0.5236 rad gives the same result."},
    {"q": "Why is it called an identity and not an equation?",
     "a": "An equation is true only for particular values; an identity is true for "
          "every value of the variable. sin²θ + cos²θ = 1 holds for any angle θ at "
          "all, which is why it can be used to rewrite expressions freely."},
    {"q": "Where is this used in real life?",
     "a": "Everywhere oscillations and rotations appear: AC electrical engineering "
          "(power factor), signal processing, computer graphics rotations, GPS and "
          "navigation, and physics — wherever sin and cos need to be swapped or "
          "simplified, these identities do the work."},
    {"q": "What happens at angles where tan or cot blow up?",
     "a": "The tan/sec form needs cos θ ≠ 0, and the cot/cosec form needs sin θ ≠ 0. "
          "At θ = 90°, for example, cos θ = 0, so sec and tan are undefined and the "
          "calculator flags this rather than returning a misleading number."},
])
