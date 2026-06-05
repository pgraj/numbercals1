from core.faqs import register_faqs

register_faqs("rw-bullet-trajectory", [
    {"q": 'How is an impact angle worked out?',
     "a": 'From two reference marks — where a projectile entered and where it struck — investigators measure the horizontal travel and the vertical drop between them. The inverse tangent of drop over travel gives the angle of impact.'},
    {"q": 'Is this the same maths used for blood-spatter analysis?',
     "a": 'Yes. The width-to-length shape of a blood drop gives an impact angle through an inverse-sine relationship, and directionality plus angles let analysts triangulate the origin point in three dimensions — the same trigonometric ideas.'},
    {"q": 'Why use inverse tangent rather than tangent?',
     "a": 'Tangent turns a known angle into a side ratio; here the situation is reversed — the side lengths are measured and the angle is unknown — so the inverse tangent (arctan) is used to recover the angle from the ratio.'},
    {"q": 'How reliable is trajectory reconstruction?',
     "a": 'It gives a sound estimate when the reference points are clearly identified and measured accurately, but real projectiles can deflect or tumble, so analysts treat the result as one line of evidence among several.'},
    {"q": 'Where is this used in real life?',
     "a": 'Crime-scene reconstruction, ballistics, accident investigation and blood-spatter analysis all rely on impact angles to place a source or rebuild a sequence of events from physical marks alone.'},
])
