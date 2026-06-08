from core.faqs import register_faqs

register_faqs('x-minus-reciprocal-squared', [
    {"q": 'How does the minus version differ from the plus version?',
     "a": 'Only in the sign of the constant. Squaring x − 1/x gives x² − 2 + 1/x² (the cross-term is now −2 because x·(1/x) = 1 enters with a minus). So x² + 1/x² = (x−1/x)² + 2. Compare with the plus case, where x² + 1/x² = (x+1/x)² − 2. The same target quantity, x² + 1/x², can be reached from EITHER x+1/x or x−1/x, just with +2 or −2. This pairing is elegant and useful.'},
    {"q": 'Why is it +2 here but −2 in the other identity?',
     "a": 'Because the cross-term flips sign. (x − 1/x)² = x² − 2·x·(1/x) + 1/x² = x² − 2 + 1/x². To isolate x² + 1/x², you move the −2 across as +2: x² + 1/x² = (x−1/x)² + 2. In the plus version the cross-term was +2, so it moved across as −2. The sign of the cross-term, set by whether you add or subtract the reciprocal, is the only difference.'},
    {"q": 'When would I know x − 1/x rather than x + 1/x?',
     "a": 'Different problems hand you different starting points. Some equations or physical setups naturally give the difference x − 1/x (for instance, antisymmetric or difference-based relationships), while others give the sum. Having both identities means whichever combination you are given, you can still find x² + 1/x² and higher powers. It makes your toolkit complete for reciprocal-based problems.'},
    {"q": 'Does this connect to the plus version in a useful way?',
     "a": 'Yes - together they let you cross-check and combine. Since x² + 1/x² = (x+1/x)² − 2 = (x−1/x)² + 2, you get the relationship (x+1/x)² − (x−1/x)² = 4, which is just the 4ab difference-of-squares identity with a=x, b=1/x. So the reciprocal identities are tied to the difference-of-squares pattern, showing how these formulas interlock rather than being isolated tricks.'},
    {"q": 'Where is this applied beyond exams?',
     "a": 'In physics and engineering problems with symmetric or antisymmetric reciprocal quantities, and in simplifying expressions before integration in calculus. Hyperbolic functions, for example, satisfy relations of exactly this form (cosh and sinh involve e^x ± e^−x, a continuous analogue of x ± 1/x), so the algebraic intuition built here transfers directly to those functions used throughout physics and engineering.'},
])
