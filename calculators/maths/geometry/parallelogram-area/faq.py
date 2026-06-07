from core.faqs import register_faqs

register_faqs("parallelogram-area", [
    {"q": "How is a parallelogram's area found?",
     "a": "Base times perpendicular height, just like a rectangle. The slant does not change the area, because sliding the top across does not add or remove space."},
    {"q": "Why not use the slanted side as the height?",
     "a": "Because the height must be the straight-up distance between the two bases, not the length of the tilted side. Using the side would overstate the area."},
    {"q": "How do I get the perimeter?",
     "a": "Add up all four sides: twice the base plus twice the slanted side, or 2(base + side). Opposite sides are equal in a parallelogram."},
    {"q": "Is a rectangle a parallelogram?",
     "a": "Yes. A rectangle is a parallelogram with right angles, so its height equals its side. Squares and rhombuses are parallelograms too."},
    {"q": "Where does this come up?",
     "a": "Plots of land that lean, structural braces, and many tiling and design patterns built from slanted four-sided shapes."},
])
