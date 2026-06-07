"""Square Wave Fourier Series — Engineering > Electronics > Fourier Waveforms.
Interactive Fourier visualiser. All rendering is client-side in the viz template;
compute() returns only static metadata (there is no server-side calculation)."""
from core.registry import register


@register(
    slug="fourier-square-wave",
    name="Square Wave Fourier Series",
    section="engineering",
    topic="Electronics",
    sub="Fourier Waveforms",
    tags=["fourier", "square wave", "odd harmonics", "gibbs", "signal"],
    formula="y(t)=frac{4A}{pi}sum_{k=1,3,5,dots}^{N}frac{sin(komega t)}{k}",
    summary="Build a square wave from odd harmonics and watch the Gibbs overshoot as you add terms.",
    viz_template="viz/fourier-square-wave.html",
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
