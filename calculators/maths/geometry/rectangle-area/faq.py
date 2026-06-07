from core.faqs import register_faqs

register_faqs("rectangle-area", [
    {"q": "How do I calculate a rectangle's area?",
     "a": "Multiply length by width. A 8 m by 5 m room is 40 square metres. Unlike a square, the two dimensions differ, so you need both."},
    {"q": "What is the perimeter?",
     "a": "The distance all the way around: twice the length plus twice the width, or 2(l + w). For 8 by 5 that is 26 units, which is how much fencing or skirting you would need."},
    {"q": "How is the diagonal found?",
     "a": "With Pythagoras: the square root of length squared plus width squared. It is the longest straight line across the rectangle, corner to corner."},
    {"q": "Can a rectangle be a square?",
     "a": "Yes, a square is just a rectangle whose length and width are equal. The same formulas work; the diagonal then simplifies to side times root 2."},
    {"q": "Where would I use this?",
     "a": "Flooring, painting walls, sizing a garden bed, or checking whether a rectangular table will fit diagonally through a hallway."},
])
