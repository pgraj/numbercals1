from core.faqs import register_faqs

register_faqs("cube-volume", [
    {"q": "How do I find a cube's volume?",
     "a": "Cube the edge length: edge times edge times edge. An edge of 4 gives a volume of 64. All twelve edges of a cube are equal."},
    {"q": "What is the surface area?",
     "a": "Six times the edge squared, because a cube has six identical square faces. For an edge of 4 that is 6 times 16, or 96."},
    {"q": "What is the space diagonal?",
     "a": "The longest line inside the cube, running from one corner to the opposite corner through the middle. It equals the edge times the square root of 3."},
    {"q": "How is volume different from surface area?",
     "a": "Volume is the space inside (cubic units); surface area is the total skin outside (square units). One fills the box, the other wraps it."},
    {"q": "Where is this useful?",
     "a": "Packing boxes, storage tanks, dice, ice cubes, and any object close to a perfect cube where you need capacity or material."},
])
