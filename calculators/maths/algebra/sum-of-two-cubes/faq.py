from core.faqs import register_faqs

register_faqs('sum-of-two-cubes', [
    {"q": 'Where is the sum of two cubes used in real life?',
     "a": 'Its biggest use is factorising and simplifying cubic expressions in algebra and calculus - turning a hard cubic into a linear factor times a quadratic, which is how you find roots and simplify fractions. It also appears in volume problems where two cubic quantities combine, and in engineering when summing two cubed terms (which arise in moments of inertia and certain flow equations). Recognising a³+b³ lets you break a stubborn cubic into pieces you can actually solve.'},
    {"q": 'Why does a³+b³ factor when a²+b² does not?',
     "a": 'Because (a+b) is always a factor of a³+b³ - you can verify that substituting a=−b makes a³+b³ equal zero, which by the factor theorem guarantees (a+b) divides it. Dividing out (a+b) leaves the quadratic a²−ab+b². A sum of squares has no such real root, so it does not factor over the real numbers. This is a neat illustration of the factor theorem: find a value that makes the expression zero, and you have found a factor.'},
    {"q": 'How do I remember the signs in (a+b)(a²−ab+b²)?',
     "a": "A common mnemonic is 'SOAP': Same, Opposite, Always Positive. The first bracket's sign is the Same as the original (a+b for a sum). The middle term of the second bracket is the Opposite (−ab). The last term is Always Positive (+b²). So a³+b³ = (a+b)(a²−ab+b²) and a³−b³ = (a−b)(a²+ab+b²). SOAP keeps the easily-confused signs straight."},
    {"q": 'Does this help solve cubic equations?',
     "a": 'Yes. If an equation has the form a³+b³ = 0 or can be rearranged into a sum of cubes, factoring it gives (a+b)(a²−ab+b²) = 0, so either a+b = 0 (an easy linear root) or the quadratic equals zero (solve with the quadratic formula). Breaking a cubic into a linear factor and a quadratic is one of the standard routes to finding all its roots, used throughout algebra and in engineering root-finding.'},
    {"q": 'Where does it show up in calculus or simplification?',
     "a": 'When evaluating limits or simplifying fractions involving cubes, like (x³+8)/(x+2), you factor the top as a sum of cubes: x³+2³ = (x+2)(x²−2x+4), cancel the (x+2), and the limit becomes computable. This factor-and-cancel move resolves many otherwise-indeterminate 0/0 limits and simplifies rational expressions, making the sum of cubes a routine tool in calculus.'},
])
