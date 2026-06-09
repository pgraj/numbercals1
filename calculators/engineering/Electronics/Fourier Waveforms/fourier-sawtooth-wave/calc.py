"""Sawtooth Wave Fourier Series â€” Engineering > Electronics > Fourier Waveforms.
Interactive Fourier visualiser. All rendering is client-side in the viz template;
compute() returns only static metadata (there is no server-side calculation)."""
from core.registry import register


@register(
    slug="fourier-sawtooth-wave",
    scholar="joseph-fourier",
    name="Sawtooth Wave Fourier Series",
    section="engineering",
    topic="Electronics",
    sub="Fourier Waveforms",
    tags=["fourier", "sawtooth", "harmonics", "signal"],
    formula="y(t)=frac{2A}{pi}sum_{n=1}^{N}frac{(-1)^{n+1}}{n}sin(nomega t)",
    summary="Assemble a sawtooth from all harmonics with alternating sign; watch the 1/n amplitude decay.",
    viz_template="viz/fourier-sawtooth-wave.html",
)
def compute():
    # Pure-visualisation tool: the interactive canvas lives in the viz template.
    return {
        "result": "Interactive Fourier visualiser â€” drag the sliders in the panel below.",
        "steps": [],
        "disclaimer": "Educational visualiser. Values/waveforms are drawn client-side and may be imperfect; cross-check against authoritative software.",
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
