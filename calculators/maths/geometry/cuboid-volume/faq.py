from core.faqs import register_faqs

register_faqs("cuboid-volume", [
    {"q": "How do I calculate a cuboid's volume?",
     "a": "Multiply length by width by height. A 6 by 4 by 3 box holds 72 cubic units. A cuboid is just a rectangular box with three possibly different dimensions."},
    {"q": "What is the surface area of a cuboid?",
     "a": "Twice the sum of the three face pairs: 2(lw + lh + wh). A box has three pairs of matching rectangular faces, so this adds them all up."},
    {"q": "What is the space diagonal?",
     "a": "The longest straight line inside the box, from one corner to the far opposite corner. It is the square root of length squared plus width squared plus height squared."},
    {"q": "Is a cube a special cuboid?",
     "a": "Yes. When all three dimensions are equal, a cuboid becomes a cube, and the formulas simplify accordingly."},
    {"q": "Where would I use this?",
     "a": "Shipping cartons, rooms, fish tanks, wardrobes, and working out how much a rectangular container can hold or how much material wraps it."},
])
