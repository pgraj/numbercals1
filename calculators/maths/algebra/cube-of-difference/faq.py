from core.faqs import register_faqs

register_faqs('cube-of-difference', [
    {"q": 'Where would I use (a−b)³ in practice?',
     "a": 'In volume-reduction and mental-cubing problems. Shrinking a cube of side a by an amount b on each side leaves a volume (a−b)³, and the expansion shows what is removed and added back. The signs alternate (+, −, +, −) because you are subtracting. It also cubes numbers just below a round value fast: 19³ = (20−1)³ = 8000 − 1200 + 60 − 1 = 6859, 98³ = (100−2)³ = 1000000 − 60000 + 1200 − 8 = 941192.'},
    {"q": 'Why do the signs alternate plus, minus, plus, minus?',
     "a": 'Because each b carries a minus sign, and the terms contain increasing powers of b. The term with b⁰ (a³) is positive; with b¹ (−3a²b) the single minus makes it negative; with b² (3ab²) two minuses cancel to positive; with b³ (−b³) three minuses give negative. So the sign flips with each power of b. This alternating pattern is the cubic version of the minus sign in (a−b)², and tracking it correctly is a common exam challenge.'},
    {"q": 'Does this show up in physics or engineering?',
     "a": 'Yes, when a quantity that depends on the cube of a dimension is reduced. Removing a uniform layer from a cubic object, computing how much volume or mass is lost, follows (a−b)³. It also appears in expansions used in calculus and numerical methods, where small decrements are cubed. Anywhere a three-dimensional measure shrinks, this identity quantifies the change including the corrective terms.'},
    {"q": 'How does it help with quick mental cubing?',
     "a": 'Pick the nearest round number as a and the small gap as b, then apply a³ − 3a²b + 3ab² − b³. For 29³: nearest is 30, so (30−1)³ = 27000 − 2700 + 90 − 1 = 24389. The big cube is easy, and each successive term is smaller, so even stopping after two or three terms gives a good estimate. Combined with (a+b)³, you can cube most two-digit numbers mentally.'},
    {"q": 'Is the alternating-sign idea useful beyond this formula?',
     "a": 'Very - it generalises. The expansion of (a−b)ⁿ for any power n has the same binomial coefficients as (a+b)ⁿ but with alternating signs, which is central to the binomial theorem, Taylor series in calculus, and inclusion-exclusion counting. Mastering the sign pattern in the cube case builds the intuition you need for those more advanced tools.'},
])
