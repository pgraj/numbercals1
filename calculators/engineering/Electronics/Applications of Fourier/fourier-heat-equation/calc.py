"""Heat Equation â€” Fourier's 1822 Problem â€” Engineering > Electronics > Applications of Fourier.
Interactive Fourier visualiser. All rendering is client-side in the viz template;
compute() returns only static metadata (there is no server-side calculation)."""
from core.registry import register


@register(
    slug="fourier-heat-equation",
    scholar="joseph-fourier",
    name="Heat Equation â€” Fourier's 1822 Problem",
    section="engineering",
    topic="Electronics",
    sub="Applications of Fourier",
    tags=["fourier", "heat equation", "pde", "diffusion", "physics"],
    formula="u(x,t)=sum_{n}b_nsin(npi x),e^{-alpha (npi)^2 t}",
    summary="The original problem Fourier solved: watch a heat profile relax over time as each harmonic decays.",
    viz_template="viz/fourier-heat-equation.html",
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
