from core.faqs import register_faqs

register_faqs("trapezoid-area", [
    {"q": "How do I find a trapezoid's area?",
     "a": "Average the two parallel sides, then multiply by the height: half of (a + b) times h. The height is the perpendicular gap between the parallel sides."},
    {"q": "What is a trapezoid (or trapezium)?",
     "a": "A four-sided shape with exactly one pair of parallel sides. The names vary by country, but the shape and formula are the same."},
    {"q": "Why average the parallel sides?",
     "a": "Because the shape is wider at one parallel side than the other. Averaging them gives the equivalent width of a rectangle with the same area."},
    {"q": "How is the perimeter calculated?",
     "a": "Just add all four sides together: the two parallel sides plus the two slanted legs. You need all four lengths for the perimeter."},
    {"q": "Where is it used?",
     "a": "Cross-sections of canals and embankments, table tops, roof trusses, and any tapering panel in design and construction."},
])
