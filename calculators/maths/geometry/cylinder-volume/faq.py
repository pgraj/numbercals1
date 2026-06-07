from core.faqs import register_faqs

register_faqs("cylinder-volume", [
    {"q": "How do I find a cylinder's volume?",
     "a": "Multiply the circular base area (pi r squared) by the height. A radius of 3 and height of 7 gives about 198 cubic units."},
    {"q": "What is the lateral surface area?",
     "a": "The curved side only, equal to 2 pi r times height. Imagine unrolling the curved wall into a flat rectangle; that rectangle's area is the lateral surface."},
    {"q": "What is the total surface area?",
     "a": "The curved side plus the two circular ends: 2 pi r times (r + h). Use lateral area when the ends are open, like a pipe, and total area when they are capped, like a can."},
    {"q": "When do I use lateral versus total?",
     "a": "Lateral for labels around a tin or paint on a pipe's outside; total when you also cover the top and bottom, like wrapping a closed can."},
    {"q": "Where is this useful?",
     "a": "Cans, pipes, tanks, silos, rollers, and anything tube-shaped where you need capacity or surface material."},
])
