from core.faqs import register_faqs

register_faqs("trig-product-to-sum", [
    {"q": 'What are the product-to-sum formulae?',
     "a": '2 sinA cosB = sin(A+B) + sin(A−B); 2 cosA cosB = cos(A−B) + cos(A+B); and 2 sinA sinB = cos(A−B) − cos(A+B). They rewrite a product as a sum or difference.'},
    {"q": 'Can you show a worked example?',
     "a": '2 sin50° cos20° = sin70° + sin30° ≈ 0.9397 + 0.5 = 1.4397. In radians 50° ≈ 0.8727 and 20° ≈ 0.3491 rad; the toggle re-derives the same value in radians.'},
    {"q": 'Why are they useful?',
     "a": 'A sum is far easier to integrate than a product, so these identities are essential in calculus. The reverse, sum-to-product, factorises expressions and explains beats.'},
    {"q": 'What is a beat?',
     "a": 'When two notes of nearly equal frequency add, the sum-to-product identity shows the result as a slow amplitude wobble — the beat — riding on the average frequency.'},
    {"q": 'Where are they used?',
     "a": 'Musical beats, amplitude modulation in radio, and integrating products of sinusoids in physics and engineering.'},
])
