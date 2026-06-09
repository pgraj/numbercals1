"""OFDM — 5G Sub-Carriers — Engineering > Electronics > Applications of Fourier.
Interactive Fourier visualiser. All rendering is client-side in the viz template;
compute() returns only static metadata (there is no server-side calculation)."""
from core.registry import register


@register(
    slug="fourier-ofdm",
    scholar="joseph-fourier",
    name="OFDM — 5G Sub-Carriers",
    section="engineering",
    topic="Electronics",
    sub="Applications of Fourier",
    tags=["fourier", "ofdm", "5g", "orthogonality", "communications"],
    formula="s(t)=sum_{k} b_kcos(2pi k,Delta f,t)",
    summary="See how orthogonal sub-carriers pack data side by side, and how breaking their spacing causes crosstalk.",
    viz_template="viz/fourier-ofdm.html",
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
