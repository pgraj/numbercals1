from core.faqs import register_faqs

register_faqs("fourier-sawtooth-wave", [
    {"q": "Why is the sawtooth the 'brightest'-sounding basic wave?", "a": "It contains every harmonic — 1st, 2nd, 3rd, and so on — not just the odd ones. That full, dense set of overtones is why a sawtooth sounds rich and buzzy, and why it is the favourite starting waveform for analog synthesisers emulating strings and brass."},
    {"q": "Where do sawtooth waves appear in real devices?", "a": "The horizontal sweep in old CRT televisions and oscilloscopes is a sawtooth — the beam races across, then snaps back. They also drive the timing ramps in many analog circuits and the pitch sweeps in synthesisers. The slow rise and instant drop is the signature shape."},
    {"q": "Why do the harmonic amplitudes fall off as 1/n?", "a": "Because the sawtooth has a sharp jump once per cycle, just like the square wave. Any signal with a sudden discontinuity has harmonics that decay slowly, as 1/n. That slow decay is why both the sawtooth and square need many terms and both show the Gibbs overshoot at the jump."},
    {"q": "What does the alternating sign in the formula do?", "a": "The (-1)^(n+1) factor flips the sign of every other harmonic. That careful alternation is what tilts the wave into its ramp shape rather than a square. Toggle the spectrum on and increase N to see how each added harmonic nudges the line closer to a straight ramp."},
    {"q": "How is this different from the triangle wave?", "a": "Both can use all or many harmonics, but the sawtooth's amplitudes fall as 1/n while the triangle's fall as 1/n² — far faster. That is why the sawtooth sounds bright and edgy and the triangle sounds soft and flute-like. Open both tabs and compare their spectra side by side."},
])
