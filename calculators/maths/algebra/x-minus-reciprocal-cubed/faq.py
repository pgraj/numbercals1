from core.faqs import register_faqs

register_faqs('x-minus-reciprocal-cubed', [
    {"q": 'How does the difference-cube version work?',
     "a": 'Cube the known difference. (x − 1/x)³ = x³ − 3x + 3/x − 1/x³ = (x³ − 1/x³) − 3(x − 1/x). So x³ − 1/x³ = (x−1/x)³ + 3(x−1/x) = a³ + 3a. Note it gives x³ − 1/x³ (a difference) because the reciprocal entered with a minus. As always, you reach the cube straight from a = x − 1/x without solving for x: if x − 1/x = 2, then x³ − 1/x³ = 8 + 6 = 14.'},
    {"q": 'Why is the sign +3a here instead of −3a?',
     "a": 'Because the cross-terms keep a positive sign after rearranging. Expanding (x − 1/x)³ gives x³ − 3x + 3/x − 1/x³; the middle terms −3x + 3/x equal −3(x − 1/x) = −3a. Moving them to isolate x³ − 1/x³ flips them to +3a. In the sum version the middle terms gave −3a after rearranging. The difference of signs traces back to whether you started with a sum or difference of reciprocals.'},
    {"q": 'How do the four substitution identities fit together?',
     "a": 'They cover the two starting points (x + 1/x and x − 1/x) and the two power levels (squared and cubed) shown on the revision sheet. From x + 1/x you get x² + 1/x² and x³ + 1/x³; from x − 1/x you get x² + 1/x² (same target, different constant) and x³ − 1/x³. Together they let you handle whichever reciprocal combination a problem gives and climb to whichever power you need.'},
    {"q": 'Where would the difference form x − 1/x come up?',
     "a": 'In antisymmetric reciprocal situations and in the algebra behind hyperbolic functions. The expression e^x − e^(−x) (which defines sinh) behaves like x − 1/x with x = e^something, and its powers relate to multiple-argument formulas for sinh - directly parallel to how x − 1/x cubed works here. So this identity foreshadows hyperbolic-function manipulations used in physics, engineering, and calculus.'},
    {"q": 'Is there a quick way to verify I have the right sign?',
     "a": 'Plug in a simple value. With x = 2: x − 1/x = 2 − 0.5 = 1.5, and x³ − 1/x³ = 8 − 0.125 = 7.875. Check against a³ + 3a = 1.5³ + 3·1.5 = 3.375 + 4.5 = 7.875. They match, confirming the +3a sign. This calculator does exactly that check for any x you enter, so you can always confirm the formula rather than trusting memory.'},
])
