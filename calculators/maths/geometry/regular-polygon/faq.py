from core.faqs import register_faqs

register_faqs("regular-polygon", [
    {"q": "What is a regular polygon?",
     "a": "A shape where all sides and all angles are equal, like an equilateral triangle, a square, or a regular hexagon. This calculator handles any number of equal sides from three up."},
    {"q": "How is the interior angle found?",
     "a": "Each interior angle is (n - 2) times 180, divided by n, where n is the number of sides. A hexagon (n = 6) has 120-degree angles."},
    {"q": "Why does the area formula use a cotangent?",
     "a": "Because a regular polygon splits into n identical triangles meeting at the centre, and the cotangent of pi over n captures each triangle's geometry. It looks fancy but is just that triangle area times n."},
    {"q": "What happens as the number of sides grows?",
     "a": "The polygon gets closer and closer to a circle. With hundreds of sides, its area approaches pi r squared, which is one way mathematicians first estimated pi."},
    {"q": "Where is this useful?",
     "a": "Designing nuts and bolts (hexagons), tiling floors, building gazebos, and any structure made from equal-sided shapes."},
])
