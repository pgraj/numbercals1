from core.faqs import register_faqs

register_faqs("circle-area", [
    {"q": "How do I find a circle's area?",
     "a": "Multiply pi by the radius squared. With a radius of 5, the area is pi times 25, about 78.5. The radius is the distance from the centre to the edge."},
    {"q": "Can I solve from the diameter or circumference?",
     "a": "Yes. This calculator lets you enter any one of radius, diameter, area or circumference, and it works out the rest. Diameter is just twice the radius."},
    {"q": "What is the difference between circumference and area?",
     "a": "Circumference is the distance around the circle (a length); area is the space inside it (a square measure). They use different formulas: 2 pi r versus pi r squared."},
    {"q": "What is pi?",
     "a": "The ratio of any circle's circumference to its diameter, roughly 3.14159. It appears in every circle formula because all circles share this same proportion."},
    {"q": "Where is this used?",
     "a": "Sizing a circular table or rug, working out pizza value for money, pipe cross-sections, or how much edging a round garden bed needs."},
])
