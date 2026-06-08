from core.faqs import register_faqs

register_faqs('cube-of-sum', [
    {"q": 'Where is (a+b)³ used in real life?',
     "a": 'Most visibly in anything involving volume and three-dimensional growth. Enlarging a cube of side a by an extra amount b on each dimension gives a new volume (a+b)³, and the expansion shows exactly what is added: the original cube a³, three slabs of 3a²b, three bars of 3ab², and the tiny corner cube b³. This is why a small increase in size produces a large jump in volume (and material cost) - the 3a²b slabs dominate. It also powers fast mental cubing: 21³ = (20+1)³ = 8000 + 1200 + 60 + 1 = 9261.'},
    {"q": 'What do the coefficients 1, 3, 3, 1 mean?',
     "a": "They are the binomial coefficients - the fourth row of Pascal's triangle. They count how many ways each combination of a's and b's arises when you multiply (a+b)(a+b)(a+b). There is one way to pick all a's (a³), three ways to pick two a's and one b (3a²b), three ways to pick one a and two b's (3ab²), and one way to pick all b's (b³). The same 1-3-3-1 pattern appears in probability (three coin flips) and is a gateway to the general binomial theorem."},
    {"q": 'How does this connect to volume in engineering or 3D printing?',
     "a": "When a solid cube is scaled up uniformly, its volume grows as the cube of the scale factor, and (a+b)³ breaks down exactly where the extra material goes. Engineers use this to estimate how much a small dimensional increase raises volume, weight, and cost - critical in casting, packaging, and 3D printing where material scales with volume. The dominant 3a²b term explains why doubling a cube's side multiplies its volume eightfold, not twofold."},
    {"q": 'Is (a+b)³ useful for mental arithmetic?',
     "a": 'Yes, for cubing numbers near a round value. 31³ = (30+1)³ = 27000 + 2700 + 90 + 1 = 29791. 12³ = (10+2)³ = 1000 + 600 + 120 + 8 = 1728. The round cube is easy, and the middle terms are quick multiplications. This is a staple technique in mental-maths and competitive exams, far faster than multiplying the number by itself three times.'},
    {"q": 'Does it appear in finance or growth models?',
     "a": 'Compounding over three periods, or three-stage growth, can expand using this shape, and more generally the binomial expansion (of which this is a small case) underlies compound-interest and probability formulas. The deeper value is recognising the cubic growth pattern: when something grows in all three of length, width, and depth at once, totals rise as a cube, and (a+b)³ shows precisely how the increments stack up.'},
])
