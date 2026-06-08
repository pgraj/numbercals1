from core.faqs import register_faqs

register_faqs('sum-of-squares-via-identity', [
    {"q": 'What is this identity actually telling me?',
     "a": "That adding the squares of a sum and a difference wipes out the cross-terms and leaves just twice the squares: the +2ab from (a+b)² and the −2ab from (a−b)² cancel. Its famous real-world form is the parallelogram law: the sum of the squares of a parallelogram's two diagonals equals the sum of the squares of all four sides. So this algebra identity is a geometry theorem in disguise, used in vector maths and physics."},
    {"q": 'Where is the parallelogram law used?',
     "a": "In vector geometry, mechanics, and signal processing. It relates the lengths of the sum and difference of two vectors to their individual lengths, which matters when combining forces, velocities, or signals. In quantum mechanics and functional analysis, the parallelogram law is the precise test for whether a notion of 'length' comes from an inner product (a dot product) - a foundational check. This humble identity underpins that deep criterion."},
    {"q": 'Why do the cross-terms cancel?',
     "a": "Expand both: (a+b)² = a²+2ab+b² and (a−b)² = a²−2ab+b². Adding them, the +2ab and −2ab cancel, and the a² and b² terms double, giving 2a²+2b² = 2(a²+b²). It is the same 'add the plus-version and minus-version to kill the asymmetric part' principle behind even/odd decomposition - here applied to squares instead of cubes."},
    {"q": 'Does it have a use in statistics or data?',
     "a": 'Yes, in variance and spread calculations where sums and differences of paired values appear. Combining the squared sum and squared difference of two measurements isolates the symmetric (combined magnitude) information from the asymmetric (difference) information. The identity guarantees a clean relationship between them, useful in error analysis and in algorithms that process paired data.'},
    {"q": 'Is there a quick computational use?',
     "a": 'It gives a shortcut for evaluating two squared quantities at once: if you need (a+b)² + (a−b)², just compute 2(a²+b²) directly - one multiplication and one doubling instead of two full squarings and an addition. For a=5, b=3: 2(25+9) = 68, versus 64+4 = 68. The identity turns four operations into two, a small but genuine saving in repeated calculations.'},
])
