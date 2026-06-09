"""Custom Harmonics â€” Additive Synthesis â€” Engineering > Electronics > Fourier Waveforms.
Interactive Fourier visualiser. All rendering is client-side in the viz template;
compute() returns only static metadata (there is no server-side calculation)."""
from core.registry import register


@register(
    slug="fourier-custom-harmonics",
    scholar="joseph-fourier",
    name="Custom Harmonics â€” Additive Synthesis",
    section="engineering",
    topic="Electronics",
    sub="Fourier Waveforms",
    tags=["fourier", "additive synthesis", "harmonics", "audio"],
    formula="y(t)=sum_i A_isin(n_iomega t+varphi_i)",
    summary="Add and remove arbitrary harmonics to build a tone from scratch â€” the additive synthesis behind pipe and drawbar organs.",
    viz_template="viz/fourier-custom-harmonics.html",
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
