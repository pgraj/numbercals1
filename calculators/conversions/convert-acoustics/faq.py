from core.faqs import register_faqs

register_faqs("convert-acoustics", [
    {"q": "What does the Acoustics & Signal Converter do?",
     "a": "It moves between logarithmic loudness and signal units — decibels, bels, nepers — "
          "and physical sound pressure in pascals, plus perceived loudness in sones. Everything "
          "is anchored on the decibel using the standard 20 µPa reference pressure."},
    {"q": "Why is the scale logarithmic?",
     "a": "Human hearing spans a vast range of pressures, so we measure sound on a log scale: "
          "every +20 dB is a tenfold increase in pressure. That is why 0 dB is not silence but "
          "the threshold of hearing."},
    {"q": "Can you show a worked example?",
     "a": "0.2 Pa to dB SPL: 20 × log10(0.2 / 20e-6) = 20 × log10(10000) = 80 dB SPL."},
    {"q": "How do I read the slider?",
     "a": "The logarithmic slider marks reference points — whisper (~30 dB), conversation "
          "(~60 dB), city traffic (~85 dB) and jet engine (~140 dB) — so your value lands in a "
          "recognisable everyday context."},
    {"q": "What are the limits?",
     "a": "Sound pressure and sone inputs must be positive (a log of zero or a negative is "
          "undefined). The sone↔dB mapping is an approximation at 1 kHz and is not a substitute "
          "for a calibrated loudness measurement."},
])
