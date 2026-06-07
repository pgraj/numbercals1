from core.faqs import register_faqs

register_faqs("rw-tide-prediction", [
    {"q": 'How are tides modelled with trig?',
     "a": 'Tide height rises and falls roughly sinusoidally: h(t) = A·sin(2πt/T) + mean, where A is the tidal amplitude, T the period, and mean the average sea level.'},
    {"q": 'What is the tidal period?',
     "a": "A semi-diurnal tide repeats about every 12.42 hours — two highs and two lows a day — set by the Moon's motion."},
    {"q": 'Can you show a worked example?',
     "a": 'With A = 2 m, T = 12.42 h, mean 3 m, a quarter-period in (t ≈ 3.105 h) reaches high tide: h = mean + A = 5 m.'},
    {"q": 'What are the high and low marks?',
     "a": 'High tide = mean + A, low tide = mean − A. Here that is 5 m and 1 m.'},
    {"q": 'Is this exact?',
     "a": 'It is a single-harmonic estimate. Real tide tables combine many harmonic terms for the Moon, Sun and local effects, so use official tables for navigation.'},
])
