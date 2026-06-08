from core.faqs import register_faqs

register_faqs('sum-of-cubes-minus-3abc', [
    {"q": 'Does a³+b³+c³−3abc actually get used anywhere?',
     "a": 'Yes, more than you might expect. Its standout fact: if a+b+c = 0, then a³+b³+c³ = 3abc, because the first factor vanishes. This shortcut solves many competition and exam problems instantly. The identity also appears in linear algebra (it equals the determinant of a particular 3×3 circulant matrix), in solving systems of symmetric equations, and as a building block in number theory. It is a favourite because that one factorisation unlocks a surprising number of problems.'},
    {"q": "What is the famous 'if a+b+c=0' trick?",
     "a": 'When the three quantities sum to zero, the factor (a+b+c) is zero, so the whole right-hand side is zero, forcing a³+b³+c³−3abc = 0, i.e. a³+b³+c³ = 3abc. So whenever you can show three terms add to zero, their cubes sum to three times their product - no expansion needed. This turns hard-looking cube-sum problems into one-line answers and is one of the most quoted consequences of this identity.'},
    {"q": 'Why is the second factor a²+b²+c²−ab−bc−ca special?',
     "a": 'It can be rewritten as ½[(a−b)²+(b−c)²+(c−a)²], a sum of squares, which is always non-negative and equals zero only when a=b=c. This tells you a³+b³+c³−3abc is zero exactly when either a+b+c=0 or a=b=c. That neat structure - a sum of three squared differences - makes the factor useful in inequalities and in proving the AM-GM inequality for three numbers.'},
    {"q": 'Where does the determinant connection come in?',
     "a": 'The expression a³+b³+c³−3abc is precisely the determinant of the 3×3 matrix whose rows are cyclic shifts of (a, b, c). This links the identity to linear algebra and to circulant matrices, which appear in signal processing and solving systems with cyclic symmetry. So a school factorisation doubles as a determinant formula - a nice bridge between algebra and matrices.'},
    {"q": 'Is it useful for solving symmetric equations?',
     "a": 'Yes. Systems involving the symmetric quantities a+b+c, ab+bc+ca, and abc often simplify using this identity, because it connects the sum of cubes to those symmetric building blocks. Recognising the pattern lets you reduce a complicated symmetric system to relationships among a few key quantities, a technique used in algebra problem-solving and in the theory relating polynomial roots to coefficients.'},
])
