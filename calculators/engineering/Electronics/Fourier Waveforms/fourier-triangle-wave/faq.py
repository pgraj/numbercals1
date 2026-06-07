from core.faqs import register_faqs

register_faqs("fourier-triangle-wave", [
    {"q": "Why does the triangle wave converge so fast?", "a": "Because it is continuous — it has no instant jumps, only changes of slope. That smoothness makes its harmonics decay as 1/n² instead of 1/n, so just a handful of terms already looks almost perfect. Set N low here and you will see it is convincing with very few harmonics."},
    {"q": "Why does a triangle wave sound so soft?", "a": "Almost all of its energy sits in the fundamental and the next couple of odd harmonics, which drop off quickly. With little high-frequency content it sounds mellow and flute-like — the opposite of the bright, harsh sawtooth. It is a favourite for soft synth pads and sub-bass."},
    {"q": "Does the triangle wave show the Gibbs overshoot?", "a": "No — and that is the key lesson. Because it has no discontinuity, there is no overshoot to fight. Compare it with the square wave tab: the square never stops overshooting at its edges, while the triangle settles cleanly. Continuity is what kills Gibbs."},
    {"q": "Where are triangle waves used?", "a": "They generate smooth sweeps and modulation signals in electronics, drive some class-D amplifier and PWM schemes, and appear in audio as gentle LFO (low-frequency oscillator) shapes that sweep filters and volume up and down evenly."},
    {"q": "Why does the formula use (2k+1) and a 1/n² term?", "a": "The (2k+1) means only odd harmonics appear (like the square wave), but the 1/(2k+1)² makes them die away as the square of the harmonic number. Odd-only gives the symmetry; the squared decay gives the speed. Together they explain the triangle's clean, fast convergence."},
])
