from core.faqs import register_faqs

register_faqs('difference-of-squares-general', [
    {"q": "What does the 'general form' A²−B² add over a²−b²?",
     "a": "It stresses that A and B can be entire expressions, not just single variables. So 4x²−9 is (2x)²−3² = (2x−3)(2x+3); and (x+1)²−(y−2)² factors as ((x+1)−(y−2))((x+1)+(y−2)). Treating whole chunks as a single A or B is a powerful habit: once you see any expression as 'something squared minus something else squared', the factorisation is automatic, however complicated those somethings are."},
    {"q": 'Can you give a real factorisation that uses the general form?',
     "a": 'Take 16x⁴ − 81. See it as (4x²)² − 9², which factors to (4x²−9)(4x²+9). Then 4x²−9 is itself a difference of squares, (2x−3)(2x+3). So the whole thing becomes (2x−3)(2x+3)(4x²+9) - a complete factorisation reached by applying the general form twice. This repeated application is exactly how factoring higher-degree polynomials works in practice.'},
    {"q": 'Where does this matter in engineering or signal processing?',
     "a": 'Factoring polynomials into simpler pieces is central to control systems and signal processing, where the roots of polynomials (poles and zeros) determine how a system behaves. The difference-of-squares form is one of the basic factorisations used to break transfer-function polynomials into manageable factors, helping engineers analyse stability and frequency response. Recognising A²−B² patterns in these polynomials speeds up that analysis.'},
    {"q": "How does seeing 'A and B as expressions' help in exams?",
     "a": "Many factorisation questions disguise a difference of squares inside a larger expression. Spotting that 25−(x+y)² is 5²−(x+y)², or that x⁴−16 is (x²)²−4², lets you crack problems that look intimidating. Examiners deliberately test this pattern-recognition. Training yourself to ask 'is this one square minus another square?' - where the squares might be complex terms - is one of the highest-value factorisation skills."},
    {"q": 'Why treat this as separate from the basic a²−b²?',
     "a": "Conceptually it is the same identity, but the lesson is different: the basic version teaches the pattern, the general version teaches that the pattern applies to whole expressions, enabling layered and repeated factorisation. Having both, and verifying each numerically, helps students make the leap from 'I can factor a²−b²' to 'I can spot a difference of squares anywhere, even nested inside something bigger' - which is where the real power lies."},
])
