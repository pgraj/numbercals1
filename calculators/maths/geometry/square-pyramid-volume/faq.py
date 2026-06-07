from core.faqs import register_faqs

register_faqs("square-pyramid-volume", [
    {"q": "How do I find a square pyramid's volume?",
     "a": "One third of the base area times the height: a third of edge squared times height. Like a cone, a pyramid is a third of the box around it."},
    {"q": "What is the slant height?",
     "a": "The distance from the middle of a base edge up to the apex, along a triangular face. It is the square root of height squared plus half the base edge squared."},
    {"q": "How is the surface area worked out?",
     "a": "The square base plus the four triangular faces: base edge squared plus two times base edge times slant height. The slant height sizes the triangles."},
    {"q": "Why divide by three for the volume?",
     "a": "Because any pyramid fills exactly one third of the prism with the same base and height, a result that holds for all pyramids and cones alike."},
    {"q": "Where is this seen?",
     "a": "The Egyptian pyramids, roof shapes, tent designs, and architectural spires with a square footprint."},
])
