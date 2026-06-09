# -*- coding: utf-8 -*-
from core.faqs import register_faqs

register_faqs("fourier-series", [
    {"q": 'What is a Fourier series?', "a": 'A way to build any repeating signal by adding simple sine (and cosine) waves of different frequencies and sizes.'},
    {"q": 'Why only odd harmonics for a square wave?', "a": "A square wave's symmetry cancels the even ones, leaving the 1st, 3rd, 5th... harmonics with amplitudes 4/(πk)."},
    {"q": 'Where is this used every day?', "a": 'MP3 audio, JPEG images, MRI scans and noise-cancelling headphones all rely on breaking signals into their frequencies.'},
    {"q": "Why doesn't it become a perfect square?", "a": 'With finite terms a small overshoot remains near the edges (the Gibbs phenomenon); infinitely many terms would be needed for a perfect square.'},
    {"q": 'What is a harmonic?', "a": 'A wave whose frequency is a whole-number multiple of the base frequency - the same idea as overtones in music.'},
])
