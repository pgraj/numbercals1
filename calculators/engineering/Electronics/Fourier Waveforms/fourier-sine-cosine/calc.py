"""Sine & Cosine Building Blocks — Engineering > Electronics > Fourier Waveforms.
Interactive Fourier visualiser. All rendering is client-side in the viz template;
compute() returns only static metadata (there is no server-side calculation)."""
from core.registry import register


@register(
    slug="fourier-sine-cosine",
    scholar="joseph-fourier",
    name="Sine & Cosine Building Blocks",
    section="engineering",
    topic="Electronics",
    sub="Fourier Waveforms",
    tags=["fourier", "sine", "cosine", "signal", "harmonic"],
    formula="y(t) = Asin(2pi f t + varphi) text{and} Acos(2pi f t + varphi)",
    summary="See how amplitude, frequency and phase shape the pure sine and cosine that every Fourier series is built from.",
    viz_template="viz/fourier-sine-cosine.html",
)
def compute():
    # Pure-visualisation tool: the interactive canvas lives in the viz template.
    return {
        "result": "Interactive Fourier visualiser — drag the sliders in the panel below.",
        "steps": [],
        "disclaimer": "Educational visualiser. Values/waveforms are drawn client-side and may be imperfect; cross-check against authoritative software.",
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
