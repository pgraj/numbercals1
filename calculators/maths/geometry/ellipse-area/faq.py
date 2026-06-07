from core.faqs import register_faqs

register_faqs("ellipse-area", [
    {"q": "How do I find an ellipse's area?",
     "a": "Multiply pi by the two semi-axes: pi times a times b. It is the exact equivalent of a circle's pi r squared, but with two different radii instead of one."},
    {"q": "What are the semi-major and semi-minor axes?",
     "a": "Half of the longest diameter (semi-major, a) and half of the shortest diameter (semi-minor, b). When a equals b, the ellipse is just a circle."},
    {"q": "Why is the circumference only approximate?",
     "a": "Because an ellipse's perimeter has no simple exact formula. This calculator uses Ramanujan's approximation, which is astonishingly accurate for almost all ellipses."},
    {"q": "What happens if a equals b?",
     "a": "You get a circle. The area becomes pi r squared and the circumference approximation collapses to the exact 2 pi r. The ellipse formulas generalise the circle ones."},
    {"q": "Where do ellipses appear?",
     "a": "Planetary orbits, whispering galleries, elliptical tracks and tables, and the cross-section of many tanks and tunnels."},
])
