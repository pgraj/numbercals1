from core.faqs import register_faqs

register_faqs('product-x-minus-a-x-minus-b', [
    {"q": 'When is (x−a)(x−b) the form I need?',
     "a": 'Whenever a quadratic has two positive roots, it factors as (x−a)(x−b) where a and b are those roots. This is the everyday case in solving equations: if x²−5x+6 = 0 factors as (x−2)(x−3) = 0, the solutions are x=2 and x=3. The minus signs mean the roots are the positive numbers a and b themselves, so this form directly reveals where a parabola crosses the x-axis on the positive side.'},
    {"q": 'Why is the middle term negative but the constant positive?',
     "a": 'Expanding gives x² − ax − bx + ab = x² − (a+b)x + ab. Both cross-terms are negative (each x times a negative), so the middle coefficient is −(a+b). But the constant is (−a)(−b) = +ab, two negatives making a positive. So a quadratic with a negative middle term and positive constant has two positive roots - a quick diagnostic when you are factoring.'},
    {"q": 'How do I use the signs to guess the factorisation?',
     "a": 'Look at the constant and middle term. Positive constant means the two roots have the same sign; negative middle term then means both are positive, so you use (x−a)(x−b). If the constant were negative, the roots would have opposite signs. This sign analysis lets you predict the factored form before you find the actual numbers, which speeds up factoring enormously.'},
    {"q": 'Where does this show up in applications?',
     "a": 'Anywhere a quadratic model has two positive solutions: the two times a projectile is at a given height, the two price points that yield a target profit, the two dimensions giving a required area. Factoring as (x−a)(x−b) hands you both solutions directly. It is the same identity as (x+a)(x+b) with sign-flipped roots, and together they cover quadratics with positive roots.'},
    {"q": 'Is this useful for mental multiplication?',
     "a": 'It can be, when two numbers are written as offsets below a base. For example 47×48 with x=50: (50−3)(50−2) = 2500 − 5·50 + 6 = 2500 − 250 + 6 = 2256. The identity organises the arithmetic into an easy square, a quick middle term, and a small product. But its main value remains factorising and solving quadratics.'},
])
