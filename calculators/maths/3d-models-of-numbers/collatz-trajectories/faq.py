# -*- coding: utf-8 -*-
from core.faqs import register_faqs

register_faqs("collatz-trajectories", [
    {"q": 'What is the Collatz rule?', "a": "Start with any positive whole number. If it's even, halve it; if it's odd, triple it and add one. Repeat."},
    {"q": 'Why is it famous?', "a": 'Every number tested - billions of them - eventually reaches 1, yet no one has proved it must always happen. It is a famous unsolved problem.'},
    {"q": "What are 'hailstone' numbers?", "a": 'The values bounce up and down like hailstones in a cloud before finally falling to 1, which is why the sequences got the nickname.'},
    {"q": 'Has anyone solved it?', "a": 'Not yet. It has been checked by computer to astronomically large numbers, but a general proof remains open.'},
    {"q": 'Why show it to students?', "a": 'It proves that maths still has simple-sounding mysteries, and it is a great introduction to algorithms and sequences.'},
])
