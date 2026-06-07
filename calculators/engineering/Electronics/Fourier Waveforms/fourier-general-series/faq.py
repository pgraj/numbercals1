from core.faqs import register_faqs

register_faqs("fourier-general-series", [
    {"q": "What can I actually do on this page?", "a": "You set the Fourier coefficients yourself — a₀, a₁...a₅ and b₁...b₅ — and watch the wave they build. It is a sandbox: try to recreate a square or sawtooth from scratch, or invent a shape no standard wave makes. The presets load the recipes for the classic waves so you can reverse-engineer them."},
    {"q": "What is the difference between the a-n and b-n coefficients?", "a": "The a-n multiply cosines and the b-n multiply sines. Cosines are 'even' (symmetric about t=0) and sines are 'odd' (antisymmetric). A wave that is symmetric needs only cosines; an antisymmetric one needs only sines. Most real waves mix both."},
    {"q": "How would an engineer find these coefficients for a real signal?", "a": "By integration: aₙ and bₙ each come from multiplying the signal by the matching cosine or sine and averaging over one period (the integral formulas shown on the page). In practice this is done numerically with a Fast Fourier Transform — the same idea, computed in milliseconds."},
    {"q": "Why does a₀ get divided by two?", "a": "a₀/2 is the average value of the signal — its DC offset. The factor of two is a bookkeeping convention that makes the integral formula for a₀ look like all the others. Slide a₀ here and watch the whole wave shift up or down."},
    {"q": "What is this used for beyond the classroom?", "a": "This is the core of audio synthesis, vibration analysis, and signal compression. JPEG and MP3, for example, store sounds and images as Fourier-like coefficients and simply throw away the ones too small to notice — which is exactly the kind of intuition you build by sliding these bars."},
])
