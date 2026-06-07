from core.faqs import register_faqs

register_faqs("square-area", [
    {"q": "How do I find the area of a square?",
     "a": "Multiply the side by itself. A square with 5 cm sides has an area of 5 x 5 = 25 cm squared. Every side is equal, so you only need one measurement."},
    {"q": "What is the diagonal of a square?",
     "a": "The line from one corner to the opposite corner. It equals the side times the square root of 2 (about 1.414), because the diagonal splits the square into two right triangles."},
    {"q": "Why is the diagonal longer than the side?",
     "a": "Because it cuts straight across the square rather than along an edge. Pythagoras tells us it is the square root of two sides squared, which always beats a single side."},
    {"q": "What units does the area come out in?",
     "a": "Square units of whatever you put in. Sides in metres give area in square metres; sides in inches give square inches. The calculator just follows your input."},
    {"q": "Where is this useful?",
     "a": "Tiling a square floor, sizing a square plot of land, or working out fabric for a square cloth. The diagonal helps when you need to fit a square through a doorway."},
])
