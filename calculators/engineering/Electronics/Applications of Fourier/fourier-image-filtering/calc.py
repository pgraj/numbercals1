"""Image Filtering (1D Pixel Row) — Engineering > Electronics > Applications of Fourier.
Interactive Fourier visualiser. All rendering is client-side in the viz template;
compute() returns only static metadata (there is no server-side calculation)."""
from core.registry import register


@register(
    slug="fourier-image-filtering",
    scholar="joseph-fourier",
    name="Image Filtering (1D Pixel Row)",
    section="engineering",
    topic="Electronics",
    sub="Applications of Fourier",
    tags=["fourier", "image processing", "blur", "edge detection", "fft"],
    formula="text{low-pass / high-pass} = mathcal{F}^{-1}big[,mathcal{F}(x)cdot text{mask},big]",
    summary="Low-pass blurs and high-pass finds edges — the frequency-domain view of everyday image processing.",
    viz_template="viz/fourier-image-filtering.html",
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
