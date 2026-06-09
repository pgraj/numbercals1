"""Half-Wave Rectified Sine Series â€” Engineering > Electronics > Fourier Waveforms.
Interactive Fourier visualiser. All rendering is client-side in the viz template;
compute() returns only static metadata (there is no server-side calculation)."""
from core.registry import register


@register(
    slug="fourier-half-wave-rectified",
    scholar="joseph-fourier",
    name="Half-Wave Rectified Sine Series",
    section="engineering",
    topic="Electronics",
    sub="Fourier Waveforms",
    tags=["fourier", "rectifier", "half-wave", "ripple", "power electronics"],
    formula="y(t)=frac{A}{pi}+frac{A}{2}sin(omega t)-frac{2A}{pi}sum_{n=1}^{N}frac{cos(2nomega t)}{4n^{2}-1}",
    summary="The classic single-diode rectifier output: a DC term, the fundamental, and even-harmonic ripple.",
    viz_template="viz/fourier-half-wave-rectified.html",
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
