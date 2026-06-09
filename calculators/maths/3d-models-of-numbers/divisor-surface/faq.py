# -*- coding: utf-8 -*-
from core.faqs import register_faqs

register_faqs("divisor-surface", [
    {"q": 'What does d(n) mean?', "a": 'd(n) is the count of whole numbers that divide n exactly. For 12 the divisors are 1,2,3,4,6,12, so d(12) = 6.'},
    {"q": 'Why do some columns spike?', "a": 'Highly composite numbers (like 12, 24, 60) have many divisors, so they stand tall; primes have only two and stay low.'},
    {"q": 'How is this linked to primes?', "a": "A number's divisor count is set by its prime factorisation, so this picture is the flip side of the prime spiral."},
    {"q": 'Where is divisor structure used?', "a": 'In cryptography, error-correcting codes, gear ratios and scheduling - anywhere factors and cycles matter.'},
    {"q": 'Why 60 seconds and 360 degrees?', "a": 'Both 60 and 360 are divisor-rich, so they split evenly many ways - handy for clocks, angles and calendars.'},
])
