# -*- coding: utf-8 -*-
from core.faqs import register_faqs

register_faqs("prime-spiral", [
    {"q": 'Why plot primes on a spiral?', "a": 'A golden-angle spiral spreads the numbers evenly so patterns in where primes fall - bands and gaps - stand out far better than a straight line.'},
    {"q": 'What is a prime number?', "a": 'A whole number greater than 1 whose only factors are 1 and itself, like 2, 3, 5, 7, 11. Every other whole number is built by multiplying primes.'},
    {"q": 'Where are primes used in real life?', "a": 'They are the backbone of online security: RSA encryption relies on multiplying two large primes, which is easy, while factoring the result is practically impossible.'},
    {"q": 'Is there a largest prime?', "a": 'No - Euclid proved over 2000 years ago that primes never run out. The largest one found so far has tens of millions of digits.'},
    {"q": "Why do primes look random but aren't?", "a": 'Their exact positions are unpredictable, yet they thin out in a smooth, well-understood way described by the prime number theorem.'},
])
