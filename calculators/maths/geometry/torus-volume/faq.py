from core.faqs import register_faqs

register_faqs("torus-volume", [
    {"q": "What is a torus?",
     "a": "A doughnut shape: a circle of tube swept around a central axis. It is described by two radii, R from the centre to the tube's centre, and r the tube's own radius."},
    {"q": "How do I find its volume?",
     "a": "Use 2 pi squared times R times r squared. It is the same as taking a cylinder of length 2 pi R (the path the tube travels) and tube radius r, then bending it into a ring."},
    {"q": "What is the surface area?",
     "a": "4 pi squared times R times r. Like the volume, it comes from the tube's circumference times the distance its centre travels around the ring."},
    {"q": "Why must r be smaller than R?",
     "a": "So the doughnut has a hole. If r reaches or exceeds R, the tube overlaps itself in the middle and the simple formulas no longer describe a clean ring, which is why the calculator checks it."},
    {"q": "Where do toruses appear?",
     "a": "Doughnuts and bagels, inner tubes and O-rings, lifebuoys, and the magnetic confinement chambers of fusion reactors."},
])
