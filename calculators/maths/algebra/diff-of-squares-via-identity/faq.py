from core.faqs import register_faqs

register_faqs('diff-of-squares-via-identity', [
    {"q": 'What is useful about (a+b)² − (a−b)² = 4ab?',
     "a": "Subtracting the squared difference from the squared sum cancels the a² and b² terms and leaves only 4ab - it isolates the product. This gives a clever way to compute a product from two squares, and it is the discrete cousin of a key calculus and physics idea: the 'polarisation identity', which recovers a product (or inner product) from squared magnitudes. It is used wherever you can measure squares or energies but need the cross-term."},
    {"q": 'How does it let me find a product from squares?',
     "a": 'Rearranged, ab = [(a+b)² − (a−b)²]/4. So if you know the squares of the sum and difference, you get the product without multiplying a and b directly. This matters in settings where squared quantities (energies, powers, magnitudes) are what you can measure, but you need the product term - the polarisation identity in physics and signal processing does exactly this to extract correlations from energy measurements.'},
    {"q": 'Why do the squared terms cancel here?',
     "a": '(a+b)² = a²+2ab+b² and (a−b)² = a²−2ab+b². Subtracting, the a² and b² terms cancel (they are identical in both), and the +2ab minus −2ab gives +4ab. So subtraction removes the symmetric squares and doubles the cross-term twice over, leaving 4ab. It is the perfect partner to the sum version, which keeps the squares and cancels the cross-term.'},
    {"q": 'Where is the polarisation idea applied?',
     "a": 'In physics and engineering, to extract a product or correlation from squared (energy/power) measurements - for example finding how two signals correlate from the energies of their sum and difference. In mathematics, the polarisation identity reconstructs an inner product (dot product) from a norm, which is foundational in geometry and quantum mechanics. This simple algebra identity is the finite, hand-checkable seed of that powerful technique.'},
    {"q": 'Is there a neat arithmetic trick here?',
     "a": "Yes: it computes a product as a quarter of a difference of squares. For a=5, b=3: [(8)² − (2)²]/4 = (64−4)/4 = 60/4 = 15 = 5·3. Historically, 'quarter-square multiplication' used exactly this identity with precomputed tables of squares to multiply large numbers quickly, before electronic calculators - a real engineering application of this identity."},
])
