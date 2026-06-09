# -*- coding: utf-8 -*-
from core.faqs import register_faqs

register_faqs("factorial-spiral", [
    {"q": 'What does n! mean?', "a": 'n! (n factorial) multiplies all whole numbers from 1 up to n. So 5! = 5x4x3x2x1 = 120.'},
    {"q": 'Why does the height use log10(n!)?', "a": 'Factorials grow so fast that 40! already has 48 digits. Plotting the number of digits (log10) keeps the whole spiral on screen.'},
    {"q": 'Where do factorials show up?', "a": 'Anywhere you count arrangements: seating plans, passwords, card shuffles, and the permutations and combinations behind probability.'},
    {"q": 'How many ways can 10 people line up?', "a": '10! = 3,628,800 different orders - from just ten people.'},
    {"q": 'What is 0!?', "a": '0! = 1, by definition. There is exactly one way to arrange nothing - the empty arrangement.'},
])
