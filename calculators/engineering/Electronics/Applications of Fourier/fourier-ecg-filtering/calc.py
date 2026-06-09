"""ECG Noise Filtering â€” Engineering > Electronics > Applications of Fourier.
Interactive Fourier visualiser. All rendering is client-side in the viz template;
compute() returns only static metadata (there is no server-side calculation)."""
from core.registry import register


@register(
    slug="fourier-ecg-filtering",
    scholar="joseph-fourier",
    name="ECG Noise Filtering",
    section="engineering",
    topic="Electronics",
    sub="Applications of Fourier",
    tags=["fourier", "ecg", "filtering", "biomedical", "dft"],
    formula="y = mathcal{F}^{-1}big[,mathcal{F}(x)cdot H(f),big]",
    summary="Watch a noisy heartbeat trace get cleaned by transforming to the frequency domain, low-pass filtering, and transforming back.",
    viz_template="viz/fourier-ecg-filtering.html",
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
