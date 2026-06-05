from core.faqs import register_faqs

register_faqs("rw-star-parallax", [
    {"q": 'What is stellar parallax?',
     "a": 'It is the tiny apparent shift of a nearby star against the distant background as the Earth moves from one side of its orbit to the other. Half of that total shift, measured as an angle, is the parallax angle.'},
    {"q": 'What is a parsec?',
     "a": 'A parsec is the distance at which a star shows a parallax of one arcsecond across a one-astronomical-unit baseline. Because the angle is so small, distance in parsecs is simply one divided by the parallax in arcseconds.'},
    {"q": 'Why does the small-angle approximation work here?',
     "a": 'The baseline (one AU) is minuscule compared with the distance to any star, so the parallax angle is a tiny fraction of a degree. For such small angles the tangent of the angle is almost exactly the angle itself in radians.'},
    {"q": 'How far can parallax measure?',
     "a": 'Ground-based parallax reaches a few hundred light-years before the angle becomes too small to measure. Space missions like Gaia extend it to tens of thousands of light-years by measuring angles far more precisely.'},
    {"q": 'Where is this used in real life?',
     "a": 'Parallax is the foundation of the cosmic distance ladder — the only direct, geometry-based way to measure how far away stars are, and the calibration on which every longer-range distance method ultimately rests.'},
])
