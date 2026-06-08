"""Scholar: Svante Arrhenius, who related reaction rate to temperature."""
from core.registry import register_scholar

register_scholar(
    slug="arrhenius",
    name="Svante Arrhenius",
    era="1859–1927",
    field_of="Physical chemistry",
    blurb=("Svante Arrhenius was a Swedish scientist and a founder of physical "
           "chemistry, awarded the Nobel Prize in Chemistry in 1903 for his theory "
           "of electrolytic dissociation. He is also known for the Arrhenius "
           "equation, k = A e^(-Ea/RT), which describes how a reaction's rate "
           "constant rises steeply with temperature and falls with the activation "
           "energy Ea — the energy barrier reactant molecules must overcome. The "
           "equation explains why heating speeds reactions and underlies the study "
           "of reaction rates in this section. Arrhenius was also among the first "
           "to link atmospheric carbon dioxide to global temperature."),
    source_name="Wikipedia — Arrhenius equation",
    source_url="https://en.wikipedia.org/wiki/Arrhenius_equation",
)
