from core.faqs import register_faqs

register_faqs("fourier-custom-harmonics", [
    {"q": "What is additive synthesis?", "a": "Building a sound by stacking pure sine waves — one per harmonic — each with its own amplitude and phase. It is the most direct way to apply Fourier's idea: instead of analysing a wave into harmonics, you compose one from harmonics. Add a few rows here and listen with your eyes."},
    {"q": "Where is additive synthesis actually used?", "a": "The Hammond organ is the classic example — its drawbars literally set the amplitude of nine harmonics, so a player builds tones by Fourier synthesis in real time. Pipe organs do the same acoustically, and modern software synths offer additive engines with hundreds of partials."},
    {"q": "Why does changing phase sometimes barely change what I see?", "a": "For a single tone your ear is fairly insensitive to the phase between harmonics — two waves that look very different can sound almost identical. But phase matters enormously for how waves combine in space (interference) and for transient, percussive sounds. The eye and the ear weigh it differently."},
    {"q": "How is this different from the General Series tab?", "a": "The General tab fixes you to harmonics 1–5 with cosine/sine pairs. This builder lets you add or remove any harmonic number you like, each as a single sine with amplitude and phase — closer to how a synthesiser drawbar or partial actually works."},
    {"q": "What is a good first experiment?", "a": "Start with the three seeded harmonics (a rough square wave) and try adding the 7th and 9th with the right 1/n amplitudes to sharpen it. Then delete all but the fundamental and the 2nd harmonic and watch a simple, vocal-like tone appear. Small changes, big differences."},
])
