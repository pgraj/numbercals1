"""Vowel Synthesis from Formants â€” Engineering > Electronics > Applications of Fourier.
Interactive Fourier visualiser. All rendering is client-side in the viz template;
compute() returns only static metadata (there is no server-side calculation)."""
from core.registry import register


@register(
    slug="fourier-vowel-formants",
    scholar="joseph-fourier",
    name="Vowel Synthesis from Formants",
    section="engineering",
    topic="Electronics",
    sub="Applications of Fourier",
    tags=["fourier", "formants", "speech", "vowel", "audio"],
    formula="text{speech} = text{glottal source} ast text{vocal-tract filter}",
    summary="See how three resonant formant frequencies shape a glottal buzz into recognisable vowels.",
    viz_template="viz/fourier-vowel-formants.html",
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
