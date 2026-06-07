from core.faqs import register_faqs

register_faqs("rw-ferris-wheel", [
    {"q": 'How does a Ferris wheel make a sine wave?',
     "a": "As the wheel turns steadily, a car's height rises and falls smoothly, tracing one sine cycle per full turn. The model is h(t) = R·sin(2πt/T − π/2) + R + clearance."},
    {"q": 'What do the parts mean?',
     "a": "R is the wheel's radius, T the time for one turn, and clearance the gap from the ground to the lowest point. The −π/2 phase starts the car at the bottom."},
    {"q": 'Can you show a worked example?',
     "a": 'With R = 10, T = 30 s, clearance 2, at t = 7.5 s (a quarter turn, 90°) the car is at axle height: h = 12. At the top (t = 15 s) it reaches 2R + clearance = 22.'},
    {"q": 'Where is the highest and lowest point?',
     "a": 'Lowest = clearance (the bottom), highest = 2R + clearance (the top), and the axle sits at R + clearance — the midline of the sine wave.'},
    {"q": 'Does the angle work in radians?',
     "a": 'Yes — the turned angle can be shown in degrees or radians via the toggle; 90° is π/2 ≈ 1.5708 rad.'},
])
