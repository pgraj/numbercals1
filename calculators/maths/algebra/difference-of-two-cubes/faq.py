from core.faqs import register_faqs

register_faqs('difference-of-two-cubes', [
    {"q": 'Where is the difference of two cubes used?',
     "a": 'Like the sum of cubes, its main role is factorising cubics for solving equations and simplifying calculus expressions. It turns a³−b³ into a linear factor (a−b) times a quadratic, exposing the easy root a=b and reducing the rest to a solvable quadratic. It appears in volume-difference problems (the change when a cube shrinks), in engineering formulas with cubed terms, and frequently in limit calculations like (x³−8)/(x−2).'},
    {"q": 'How do the signs differ from the sum of cubes?',
     "a": "Use SOAP: Same, Opposite, Always Positive. For a difference, the first bracket is the Same sign (a−b). The middle term of the quadratic is the Opposite sign (+ab here, because the original was a minus). The last term is Always Positive (+b²). So a³−b³ = (a−b)(a²+ab+b²). The only differences from the sum version are the first bracket's sign and the middle term's sign - SOAP captures both."},
    {"q": 'Why is (a−b) always a factor of a³−b³?',
     "a": 'Because setting a=b makes a³−b³ equal zero, and by the factor theorem any value that makes an expression zero corresponds to a factor. Since a=b zeroes it, (a−b) must divide a³−b³ exactly. Performing that division leaves the quadratic a²+ab+b². This is the same logic as the sum of cubes, just mirrored, and it is a clean example of how spotting a root instantly gives you a factor.'},
    {"q": 'How does it simplify limits in calculus?',
     "a": 'Consider the limit of (x³−8)/(x−2) as x approaches 2 - plugging in gives 0/0. Factor the numerator as a difference of cubes: x³−2³ = (x−2)(x²+2x+4). Cancel the (x−2) with the denominator, leaving x²+2x+4, which at x=2 is 12. The difference of cubes is exactly what resolves this indeterminate form, and such cancellations are a staple of introductory calculus.'},
    {"q": 'Is it used in any engineering or geometry context?',
     "a": 'Yes - whenever a quantity proportional to the cube of a dimension changes between two values. The difference in volume between two cubes, or in certain stiffness and inertia terms that depend on the cube of a length, can be factored this way to reveal how the change scales. Factoring also helps simplify ratios of such quantities, which is useful when comparing two designs or sizes.'},
])
