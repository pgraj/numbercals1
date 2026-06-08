from core.faqs import register_faqs

register_faqs('square-a-plus-b-minus-c', [
    {"q": 'When is the (a+b−c)² pattern useful?',
     "a": 'Whenever two quantities add and a third is subtracted before squaring - for instance, two gains and one loss, then measuring the squared net effect. The sign pattern follows directly from the bracket: a and b are positive so their cross-term 2ab is positive, while c is negative so any pair involving c (b-c and c-a) is negative. It is a compact way to handle net-of-deductions calculations that then feed into a squared (energy, error, or distance) quantity.'},
    {"q": 'How do I get the cross-term signs right every time?',
     "a": "Multiply the signs of the two variables in each pair. For (a + b − c): a·b is (+)(+) = + → +2ab; b·c is (+)(−) = − → −2bc; c·a is (−)(+) = − → −2ca. The square terms a², b², c² are always positive. This 'multiply the signs' rule works for every trinomial square, so once you internalise it you never have to memorise individual cases - you reconstruct any of them on the spot."},
    {"q": 'Does this appear in geometry or physics?',
     "a": 'Yes - in the law of cosines and in vector magnitudes where one component opposes the others. When you compute the squared length of a resultant formed by adding two vectors and subtracting a third, this is the expansion. Surveying and navigation, where you combine measured legs of a path with one leg in the opposite direction, produce exactly this sign pattern when the total displacement is squared.'},
    {"q": 'Is it used in finance or accounting?',
     "a": 'Indirectly, in variance-style calculations where two positive contributions and one offsetting one combine. More commonly, recognising the pattern is a simplification tool: an expression with three squares and these specific signed cross-terms can be collapsed to (a+b−c)², tidying up a formula. Compact expressions are less error-prone, which matters in spreadsheets and financial models.'},
    {"q": 'Why learn all these trinomial-square variants separately?',
     "a": "You do not have to memorise them as separate facts - they are all the same identity with different signs, governed by the 'multiply the signs of each pair' rule. Building a calculator for each just lets you see the rule in action across cases and verify numerically that your sign reasoning was right. Once the pattern clicks, you can expand any signed trinomial square confidently, which is a genuinely useful exam and engineering skill."},
])
