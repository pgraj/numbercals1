from core.faqs import register_faqs

register_faqs('product-x-plus-a-x-plus-b', [
    {"q": 'Where is (x+a)(x+b) used in real life?',
     "a": "It is the engine behind factorising quadratics, which is one of the most-used skills in all of algebra. Reading it backwards: to factor x²+5x+6, you look for two numbers that add to 5 and multiply to 6 (namely 2 and 3), giving (x+2)(x+3). That single trick solves quadratic equations, finds where parabolas cross the axis (projectile landing points, profit break-even points, optimal pricing), and simplifies algebraic fractions. Every time you 'find two numbers that add and multiply', you are using this identity in reverse."},
    {"q": 'Why does the middle coefficient become (a+b) and the constant ab?',
     "a": 'Multiply it out: (x+a)(x+b) = x·x + x·b + a·x + a·b = x² + (a+b)x + ab. The x-term collects both cross-products, so its coefficient is the SUM a+b, while the constant is the PRODUCT ab. This sum-and-product structure is exactly why factoring works in reverse: given the quadratic, you hunt for two numbers whose sum is the middle coefficient and whose product is the constant.'},
    {"q": 'How does this help solve real quadratic problems?',
     "a": "A ball's height, a company's profit, the area of a bordered rectangle - all are often quadratics. To find when height is zero (landing time) or profit is zero (break-even), you set the quadratic to zero and factor it using this identity in reverse, then read off the solutions. Factoring turns 'solve this equation' into 'find two numbers that add and multiply', which is far quicker than the quadratic formula when the numbers are nice."},
    {"q": "Is this connected to Vieta's formulas?",
     "a": "Directly. Vieta's formulas say that for a quadratic x²+px+q, the sum of its roots is −p and the product is q. That is exactly this identity read in reverse: if the roots are −a and −b, then p = a+b and q = ab. So (x+a)(x+b) is the concrete, visible version of the deep relationship between a polynomial's roots and its coefficients - a relationship that extends to cubics and beyond."},
    {"q": 'Where does it appear outside pure maths?',
     "a": 'In any model that is quadratic: physics (projectile motion, energy), economics (revenue and cost curves, optimisation), geometry (areas that depend on two added lengths), and probability. Whenever a relationship has a squared term plus a linear term plus a constant, this identity is how you factor and solve it. It is also the basis for completing the square and for understanding parabola shapes.'},
])
