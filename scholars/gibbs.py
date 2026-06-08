"""Scholar: Josiah Willard Gibbs, founder of chemical thermodynamics."""
from core.registry import register_scholar

register_scholar(
    slug="gibbs",
    name="Josiah Willard Gibbs",
    era="1839–1903",
    field_of="Physical chemistry, thermodynamics",
    blurb=("Josiah Willard Gibbs was an American physicist, chemist, and "
           "mathematician who laid the foundations of chemical thermodynamics. "
           "From 1873 he developed the concept now called Gibbs free energy, "
           "\u0394G = \u0394H \u2212 T\u0394S, which combines a reaction's heat change and "
           "entropy change to predict whether it will happen spontaneously: a "
           "negative \u0394G means the process can proceed on its own. This single "
           "criterion governs chemical reactions, phase changes, and the link "
           "between energy and electrochemical cell voltage."),
    source_name="Wikipedia — Gibbs free energy",
    source_url="https://en.wikipedia.org/wiki/Gibbs_free_energy",
)
