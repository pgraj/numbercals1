from core.faqs import register_faqs

register_faqs('x-plus-reciprocal-squared', [
    {"q": "What are these x + 1/x 'substitution identities' for?",
     "a": 'They are a powerful trick for problems involving a number and its reciprocal together - which appear in symmetric equations, certain physics oscillation problems, and competition maths. The key insight: if you know the value of x + 1/x, you can find x² + 1/x², x³ + 1/x³, and more WITHOUT ever finding x itself. Squaring x + 1/x gives x² + 2 + 1/x², so x² + 1/x² is just (x+1/x)² − 2. This lets you climb to higher powers from a single known value.'},
    {"q": 'Why does the −2 appear?',
     "a": 'Square x + 1/x: (x + 1/x)² = x² + 2·x·(1/x) + 1/x² = x² + 2 + 1/x², because the middle cross-term x·(1/x) equals exactly 1, doubled to 2. So x² + 1/x² = (x+1/x)² − 2. The constant 2 comes from that cross-term being exactly 1 - the beautiful feature of a number times its reciprocal. This clean cancellation is what makes reciprocal identities so tidy.'},
    {"q": 'Where do reciprocal expressions like x + 1/x actually arise?',
     "a": 'In any situation with a quantity and its inverse: gear ratios and their reciprocals, impedance and admittance in electronics, certain economic elasticities, and physics problems with symmetric variables. They are especially common in equations that stay the same when you replace x by 1/x (reciprocal-symmetric equations), where expressing everything in terms of x + 1/x dramatically simplifies the problem.'},
    {"q": 'How is this used to solve equations?',
     "a": 'Reciprocal-symmetric (palindromic) equations - where the coefficients read the same forwards and backwards - can be solved by substituting y = x + 1/x, which halves the degree of the equation. A quartic can become a quadratic in y. These identities provide the conversions you need (x² + 1/x² = y² − 2, and so on), turning a hard high-degree equation into a manageable one. This is a classic competition and advanced-algebra technique.'},
    {"q": 'Can I really find x² + 1/x² without knowing x?',
     "a": "Yes, and that is the whole point. If you are told x + 1/x = 3, then x² + 1/x² = 3² − 2 = 7 immediately - no need to solve for x (which would be an awkward surd). This 'work with the combination, not the variable' approach is enormously efficient and is why these identities are prized: they sidestep messy intermediate values and go straight to the answer."},
])
