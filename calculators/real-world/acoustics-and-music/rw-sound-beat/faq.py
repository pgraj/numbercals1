from core.faqs import register_faqs

register_faqs("rw-sound-beat", [
    {"q": 'What causes beats?',
     "a": 'Two tones of nearly equal frequency add to a sound that pulses in loudness. The pulse rate is the beat frequency, f_beat = |f₁ − f₂|.'},
    {"q": 'What is the trig behind it?',
     "a": 'sin(2πf₁t) + sin(2πf₂t) factors into a fast tone at the average frequency multiplied by a slow envelope at half the difference — that envelope is the throb you hear.'},
    {"q": 'Can you show a worked example?',
     "a": '440 Hz and 444 Hz give f_beat = |440 − 444| = 4 Hz — four loudness pulses every second.'},
    {"q": 'How do musicians use beats?',
     "a": 'When tuning, two strings near the same pitch beat slowly; as they approach unison the beats slow and vanish. No beats means the pitches match.'},
    {"q": 'Why no angle toggle here?',
     "a": 'This calculator works with frequencies and time, not an angle, so there is no degrees/radians choice to make.'},
])
