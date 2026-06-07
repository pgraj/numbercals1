from core.faqs import register_faqs

register_faqs("fourier-heat-equation", [
    {"q": "Why is this called 'Fourier's original problem'?", "a": "Because it is literally why Fourier invented Fourier series. In 1822 he wanted to predict how heat spreads through a solid, and he discovered that breaking the temperature profile into sine waves made the problem solvable — each sine decays on its own. The whole field grew out of this one question."},
    {"q": "Why do the sharp features smooth out fastest?", "a": "Each harmonic decays at a rate proportional to the square of its frequency — the e^(-α n² t) term. High harmonics (the sharp, wiggly bits) die away far faster than low ones. That is why a hot spot blurs quickly into a smooth bump: the fine detail is in the fast-decaying harmonics."},
    {"q": "What does the diffusivity α represent?", "a": "How quickly a material conducts heat. Metals have high α (heat races through a copper pan handle); insulators like wood or foam have low α (the handle of a wooden spoon stays cool). Raise α here and watch the profile flatten faster."},
    {"q": "Does this same maths apply beyond heat?", "a": "Yes — the diffusion equation describes ink spreading in water, pollutants dispersing in air, and even the Black–Scholes model of option pricing in finance. Anywhere something spreads out to even itself over time, this Fourier solution applies."},
    {"q": "Why does the profile never quite reach a flat line?", "a": "Mathematically the harmonics decay exponentially but never hit exactly zero, so the temperature approaches uniform without truly arriving — just as a cooling cup of coffee gets ever closer to room temperature. Drag time forward and watch it asymptote toward flat."},
])
