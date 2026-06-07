"""Triangle Wave Fourier Series — Engineering > Electronics > Fourier Waveforms.
Interactive Fourier visualiser. All rendering is client-side in the viz template;
compute() returns only static metadata (there is no server-side calculation)."""
from core.registry import register


@register(
    slug="fourier-triangle-wave",
    name="Triangle Wave Fourier Series",
    section="engineering",
    topic="Electronics",
    sub="Fourier Waveforms",
    tags=["fourier", "triangle wave", "convergence", "signal"],
    formula="y(t)=frac{8A}{pi^{2}}sum_{k=0}^{N}frac{(-1)^{k}}{(2k+1)^{2}}sin!big((2k+1)omega tbig)",
    summary="See why a triangle wave converges so fast — its harmonics fall off as 1/n squared.",
    viz_template="viz/fourier-triangle-wave.html",
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
