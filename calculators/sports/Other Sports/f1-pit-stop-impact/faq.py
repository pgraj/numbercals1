from core.faqs import register_faqs

register_faqs("f1-pit-stop-impact", [
    {"q": "What does this calculate?",
     "a": "Whether a pit stop pays off over the remaining laps: the time lost in the pit lane against the lap time gained on fresh tyres, then roughly how many track positions that is worth."},
    {"q": "Why does fresh rubber gain time?",
     "a": "Because worn tyres lose grip and slow the car each lap. New tyres are faster, and that per-lap gain accumulates over a stint, which can outweigh the one-off pit loss."},
    {"q": "How is the time turned into positions?",
     "a": "By dividing the net time by the average gap between cars. Close-packed fields turn small time swings into position changes; spread-out races need bigger gains to move up."},
    {"q": "Is this how real strategists work?",
     "a": "The core trade-off is exactly this, but real teams also model traffic, safety cars, tyre warm-up and rivals' plans. This captures the central arithmetic."},
    {"q": "What is an undercut?",
     "a": "Pitting earlier than a rival so your fresh tyres gain time while they are still on old ones, jumping them when they finally stop. This calculator shows the time logic behind it."},
])
