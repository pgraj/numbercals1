from core.faqs import register_faqs

register_faqs('sum-of-cubes-of-binomials', [
    {"q": 'What is surprising or useful about (a+b)³ + (a−b)³?',
     "a": "When you add the two cubes, the terms with odd powers of b cancel out completely, leaving only 2a³ + 6ab² - just two terms instead of eight. This 'cancellation of opposites' is the useful idea: adding a quantity's plus-version and minus-version wipes out the asymmetric parts and doubles the symmetric ones. It is the same principle behind splitting any function into even and odd parts, which is widely used in physics and signal processing."},
    {"q": 'Why do the b and b³ terms disappear?',
     "a": 'Because they have opposite signs in the two expansions. (a+b)³ has +3a²b and +b³; (a−b)³ has −3a²b and −b³. Add them and those pairs cancel to zero. Meanwhile a³ appears as +a³ in both (giving 2a³) and 3ab² appears as +3ab² in both (giving 6ab²). So the odd-in-b terms cancel and the even-in-b terms double - a clean, memorable pattern.'},
    {"q": "Where is this 'add the opposites' trick used?",
     "a": 'It is the heart of even/odd decomposition. Any function can be split into an even part (symmetric, like cos) and an odd part (antisymmetric, like sin) by adding and subtracting f(x) and f(−x). Engineers use this in Fourier analysis and signal processing to separate symmetric and antisymmetric components. The algebra here is a concrete, finite example of that powerful general technique.'},
    {"q": 'Is it handy for mental arithmetic?',
     "a": 'Yes, for quickly evaluating paired cubes. To find 12³ + 8³, note these are (10+2)³ + (10−2)³ with a=10, b=2, so the answer is 2·1000 + 6·10·4 = 2000 + 240 = 2240 - much faster than cubing each separately. Whenever two numbers are symmetric around a round middle value, this collapse gives their cube-sum almost instantly.'},
    {"q": 'Does this connect to any deeper maths?',
     "a": "It is a small instance of how symmetry simplifies expressions. Recognising that combining symmetric inputs cancels asymmetric terms shows up in solving equations, evaluating integrals (where odd functions over symmetric ranges vanish), and in physics conservation arguments. Learning to spot 'the odd parts will cancel' saves enormous effort across maths and science."},
])
