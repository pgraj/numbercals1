from core.faqs import register_faqs

register_faqs('square-a-minus-b-plus-c', [
    {"q": 'Where would the (a−b+c)² pattern come up?',
     "a": "In any net calculation of the shape 'start with a, subtract b, add c, then square the result' - then squared for an energy, error, or distance measure. Here a and c are positive and b is negative, so the a-c cross-term is positive while the a-b and b-c terms are negative. It is the mirror of (a+b−c)² with the roles of b and c swapped, and shows up wherever the middle quantity is the one being subtracted."},
    {"q": 'How can I remember which cross-terms are negative?',
     "a": "Use the sign-product rule: a pair's cross-term sign is the product of the two variables' signs in the bracket. For (a − b + c): a·b = (+)(−) = − → −2ab; b·c = (−)(+) = − → −2bc; c·a = (+)(+) = + → +2ca. So the two pairs that include the subtracted b are negative, and the a-c pair is positive. The squared terms are always positive. This single rule replaces memorising every variant."},
    {"q": 'Is this used in real measurement or physics contexts?',
     "a": "Yes, in resultant and residual calculations where the middle of three contributions opposes the others - a force or displacement that points the opposite way, then the magnitude is squared. It also appears in coordinate geometry when a point's signed offsets combine and you compute a squared distance. The specific sign pattern matters for getting the magnitude right."},
    {"q": 'Does recognising this pattern help in exams?',
     "a": 'Very much. Questions often present a six-term expression and ask you to factorise or simplify it. Spotting that a²+b²+c²−2ab−2bc+2ca is exactly (a−b+c)² turns a daunting expression into one tidy bracket, saving time and reducing mistakes. Reverse-recognition - expansion to factor - is a frequently tested and genuinely useful skill.'},
    {"q": 'Why build a separate calculator for this when it is so similar to the others?',
     "a": "Because seeing each signed variant verified numerically cements the underlying sign rule far better than reading them in a list. Plug in your own numbers, watch each term's sign and value appear, and confirm both sides match. After working through the variants, you stop memorising and start deriving them - which is the real goal."},
])
