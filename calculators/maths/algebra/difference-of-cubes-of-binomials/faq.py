from core.faqs import register_faqs

register_faqs('difference-of-cubes-of-binomials', [
    {"q": 'What is the point of (a+b)³ − (a−b)³?',
     "a": 'Subtracting the two cubes does the opposite of adding them: now the even-in-b terms (a³ and 3ab²) cancel, and the odd-in-b terms double, leaving 6a²b + 2b³. So adding the cubes keeps the symmetric part, while subtracting keeps the antisymmetric part. Together, the sum and difference let you isolate either half of an expression - exactly the even/odd separation used throughout applied maths.'},
    {"q": 'Why do these particular terms survive?',
     "a": 'In (a+b)³ − (a−b)³, the a³ terms (both +a³) cancel, and the 3ab² terms (both +3ab²) cancel, because subtraction removes what is identical. But +3a²b minus −3a²b gives +6a²b, and +b³ minus −b³ gives +2b³ - the terms that had opposite signs now reinforce. So subtraction keeps exactly the terms that addition cancelled, and vice versa. The two identities are perfect complements.'},
    {"q": 'Where is this used practically?',
     "a": "In extracting the antisymmetric or 'odd' part of a relationship. In signal processing, the odd part of a signal is found by f(x) − f(−x) over 2, structurally identical to this difference of cubes. It also gives a quick way to compute differences of paired cubes mentally: 12³ − 8³ with a=10, b=2 is 6·100·2 + 2·8 = 1200 + 16 = 1216, instantly."},
    {"q": 'How do the sum and difference versions work together?',
     "a": 'They are a matched pair: (a+b)³ + (a−b)³ = 2a³ + 6ab² captures the even-in-b part, and (a+b)³ − (a−b)³ = 6a²b + 2b³ captures the odd-in-b part. Add those two results and you recover 2(a+b)³; subtract them and you get 2(a−b)³. This is the algebraic skeleton of decomposing anything into symmetric and antisymmetric pieces and then reassembling it.'},
    {"q": 'Is there a real-world computation where this matters?',
     "a": 'Yes - anywhere you need just the part of a change that behaves antisymmetrically. In physics, separating a force or field into symmetric and antisymmetric components simplifies analysis; in data, isolating the odd component of a paired difference highlights directional effects. The cube case is a clean, hand-checkable example of a technique that scales to functions and signals.'},
])
