from core.faqs import register_faqs

register_faqs("rhombus-area", [
    {"q": "How do I find a rhombus's area?",
     "a": "Multiply the two diagonals and halve the result: half of d1 times d2. The diagonals are the lines joining opposite corners."},
    {"q": "Why does the diagonal method work?",
     "a": "Because a rhombus's diagonals cross at right angles and cut it into four right triangles. Half the product of the diagonals neatly totals their area."},
    {"q": "How do I get the side and perimeter?",
     "a": "The diagonals bisect each other at right angles, so each half-diagonal forms a right triangle. The side is half the square root of d1 squared plus d2 squared, and the perimeter is four times that."},
    {"q": "Is a rhombus a square?",
     "a": "A square is a special rhombus with right angles and equal diagonals. A general rhombus has equal sides but its angles are not 90 degrees."},
    {"q": "Where is this useful?",
     "a": "Diamond-shaped tiles, kite design, jewellery, and patterns where you know the diagonals more easily than the angles."},
])
