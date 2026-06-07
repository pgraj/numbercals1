from core.faqs import register_faqs

register_faqs("cone-volume", [
    {"q": "How do I find a cone's volume?",
     "a": "One third of pi times radius squared times height. A cone holds exactly a third of the cylinder that would fit around it with the same base and height."},
    {"q": "What is the slant height?",
     "a": "The distance from the base edge up to the tip, along the sloping surface. It is the square root of radius squared plus height squared, by Pythagoras."},
    {"q": "Why is the volume only a third of a cylinder?",
     "a": "It is a geometric fact, provable with calculus or by filling: three identical cones exactly fill their matching cylinder. The factor of one third is exact."},
    {"q": "What is the surface area of a cone?",
     "a": "The base circle plus the curved surface: pi r times (r + slant height). Leave out the base if the cone is open, like an ice-cream cone."},
    {"q": "Where is this used?",
     "a": "Ice-cream cones, funnels, party hats, piles of sand or grain, and the pointed tops of towers and roofs."},
])
