# -*- coding: utf-8 -*-
from core.faqs import register_faqs

register_faqs("lorenz-attractor", [
    {"q": 'What is the Lorenz attractor?', "a": 'The path traced by three linked equations Edward Lorenz used to model convection. It loops forever in a butterfly shape without ever repeating.'},
    {"q": 'What is the butterfly effect?', "a": 'Tiny differences in starting conditions grow into completely different outcomes - the reason long-range weather forecasts are uncertain.'},
    {"q": 'Is chaos the same as randomness?', "a": 'No. The system is fully deterministic - the same start gives the same path - but it is so sensitive that prediction quickly breaks down.'},
    {"q": 'Where does this matter?', "a": 'Weather and climate modelling, population biology, electronics and even heart-rhythm studies.'},
    {"q": 'Why does it look like a butterfly?', "a": 'The trajectory orbits two centres and swaps between them unpredictably, tracing two wing-like lobes.'},
])
