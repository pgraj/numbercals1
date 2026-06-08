from core.faqs import register_faqs

register_faqs('difference-of-two-squares', [
    {"q": 'Where is the difference of two squares actually used?',
     "a": "It is the fastest mental-maths trick for certain multiplications and the workhorse of factorisation. To multiply 53×47, notice they are 50+3 and 50−3, so the product is 50²−3² = 2500−9 = 2491 - instantly. Any two numbers equally spaced around a round middle multiply this way: 97×103 = 100²−3² = 9991. Beyond arithmetic, it is the first thing you try when factorising, it simplifies fractions and limits in calculus, and it appears in cryptography (Fermat's factorisation method, which underlies attacks on poorly chosen encryption keys, is built on a²−b²)."},
    {"q": 'Why does a²−b² factor but a²+b² does not (over real numbers)?',
     "a": "Because a²−b² can be written as a difference, and a difference of squares always splits into (a−b)(a+b) - you can check by expanding: the cross-terms −ab and +ab cancel, leaving a²−b². A SUM of squares, a²+b², has no such real factorisation; the cross-terms would not cancel. (It does factor using complex numbers, which is why this identity is a gateway to complex algebra.) Recognising 'difference, yes; sum, no' is one of the most useful instincts in algebra."},
    {"q": 'How is this used to multiply numbers quickly?',
     "a": 'Spot two numbers symmetric around an easy midpoint. 18×22: midpoint 20, gap 2, so 20²−2² = 400−4 = 396. 95×105: midpoint 100, gap 5, so 10000−25 = 9975. The method turns a two-digit multiplication into one square minus a tiny square. It is a favourite of mental-calculation and competitive-exam techniques because it is so much faster than long multiplication.'},
    {"q": 'What is the cryptography connection?',
     "a": "Fermat's factorisation method tries to write a number N as a²−b², because then N = (a−b)(a+b) immediately gives two factors. For numbers that are products of two close primes - exactly the weak case in RSA encryption when keys are chosen carelessly - this difference-of-squares approach can crack them quickly. So this humble school identity sits at the foundation of why certain encryption keys are insecure, a striking example of pure algebra meeting real security."},
    {"q": 'Does it help in calculus or simplifying fractions?',
     "a": 'Constantly. Expressions like (x²−9)/(x−3) simplify by factoring the top as (x−3)(x+3), cancelling to (x+3) - which is how you evaluate limits that otherwise look like 0/0. Rationalising denominators with surds uses it too: multiplying by the conjugate turns (√a − √b) in a denominator into a clean a−b via this identity. It is one of the most frequently applied factorisations in all of mathematics.'},
])
