from core.faqs import register_faqs

register_faqs("trig-real-world-problems", [
    {"q": 'What problems does this solve?',
     "a": 'Three common applied types: the angle of elevation (height from distance and angle), a leaning ladder (reach up a wall), and a rotating wheel (seat height at a given time).'},
    {"q": 'Can you show a worked example?',
     "a": 'Angle of elevation: a point 20 m away at 35° gives height = 20 × tan 35° ≈ 14.0 m. Switch to radians and 35° becomes ≈ 0.6109 rad with the same result.'},
    {"q": 'How is the ladder problem modelled?',
     "a": 'A ladder of length L at angle θ to the ground reaches L sin θ up the wall and sits L cos θ out from it — a right-angle triangle with the ladder as hypotenuse.'},
    {"q": 'How is the rotating wheel modelled?',
     "a": 'As y = D + R sin(ωt): centre height D, radius R, angular speed ω and time t. It is the same sinusoidal model used for any circular motion.'},
    {"q": 'Why check the answer is sensible?',
     "a": 'A height should be shorter than the hypotenuse, an elevation angle between 0° and 90°, and a wheel seat between the ground and the top of the circle.'},
])
