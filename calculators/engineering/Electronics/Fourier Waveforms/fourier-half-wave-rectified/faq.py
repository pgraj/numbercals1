from core.faqs import register_faqs

register_faqs("fourier-half-wave-rectified", [
    {"q": "What is half-wave rectification, in plain terms?", "a": "It is what a single diode does: it lets the positive half of an AC wave through and chops off the negative half. The result is a bumpy, one-sided signal — the first step inside many simple power supplies that turn AC from the wall into DC for electronics."},
    {"q": "Why does the output have a DC component?", "a": "Because you removed the negative halves, the signal no longer averages to zero — it now has a positive average, the A/π term in the formula. That non-zero average is the DC you are trying to extract. The rest of the harmonics are the unwanted 'ripple' a smoothing capacitor has to remove."},
    {"q": "Why are there strong even harmonics and 2f ripple?", "a": "Chopping off half the wave breaks its symmetry and injects energy at twice the original frequency and its multiples. That is why a half-wave rectifier produces prominent ripple at 2f — and why power-supply designers prefer full-wave rectifiers, which push the ripple even higher and make it easier to filter out."},
    {"q": "Where would I find this circuit?", "a": "Inside cheap DC adapters, battery chargers, AM radio signal detectors (the diode 'demodulates' the audio), and many sensor front-ends. Anywhere a single diode turns alternating current into a one-directional signal, this is the waveform you get."},
    {"q": "How does a smoothing capacitor relate to this spectrum?", "a": "A capacitor is a low-pass filter: it keeps the DC term and attenuates the higher ripple harmonics. The taller the ripple bars in this spectrum, the more filtering you need. Reading the harmonic amplitudes here is literally the first step in designing that filter."},
])
