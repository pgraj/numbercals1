from core.faqs import register_faqs

register_faqs("sphere-volume", [
    {"q": "How do I find a sphere's volume?",
     "a": "Use four-thirds times pi times the radius cubed. A radius of 5 gives about 524. Volume grows fast because it depends on the cube of the radius."},
    {"q": "Can I work backwards from the volume or surface area?",
     "a": "Yes. This calculator accepts radius, diameter, volume or surface area, and finds the rest. Doubling back from volume uses a cube root."},
    {"q": "What is the surface area of a sphere?",
     "a": "Four times pi times the radius squared. Interestingly it is exactly four times the area of the circle you would get by slicing the sphere through its centre."},
    {"q": "Why does volume grow so quickly with radius?",
     "a": "Because it depends on radius cubed. Doubling the radius multiplies the volume by eight, which is why a slightly bigger ball holds much more."},
    {"q": "Where is this used?",
     "a": "Balls and bearings, planets and bubbles, tanks and domes, and dosing anything stored in roughly spherical containers."},
])
