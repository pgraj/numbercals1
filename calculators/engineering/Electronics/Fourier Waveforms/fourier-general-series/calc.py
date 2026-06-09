"""General Fourier Series (Your Coefficients) â€” Engineering > Electronics > Fourier Waveforms.
Interactive Fourier visualiser. All rendering is client-side in the viz template;
compute() returns only static metadata (there is no server-side calculation)."""
from core.registry import register


@register(
    slug="fourier-general-series",
    scholar="joseph-fourier",
    name="General Fourier Series (Your Coefficients)",
    section="engineering",
    topic="Electronics",
    sub="Fourier Waveforms",
    tags=["fourier", "coefficients", "trigonometric series", "synthesis"],
    formula="y(t)=frac{a_0}{2}+sum_{n=1}^{N}big[a_ncos(nomega t)+b_nsin(nomega t)big]",
    summary="Dial in your own a-n and b-n coefficients up to n=5 and synthesise any trigonometric Fourier series.",
    viz_template="viz/fourier-general-series.html",
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
