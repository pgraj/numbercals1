"""Scholar: François-Marie Raoult, who related a solution's vapour pressure to composition."""
from core.registry import register_scholar

register_scholar(
    slug="raoult",
    name="François-Marie Raoult",
    era="1830–1901",
    field_of="Physical chemistry",
    blurb=("François-Marie Raoult was a French chemist who studied the physical "
           "properties of solutions. In 1887 he proposed Raoult's law: the vapour "
           "pressure of each component of an ideal solution equals the pure "
           "component's vapour pressure times its mole fraction. He showed that a "
           "dissolved solute lowers a solvent's vapour pressure in proportion to "
           "the amount dissolved, which gave a new way to measure molecular "
           "weights and underpins the colligative properties — vapour-pressure "
           "lowering, boiling-point elevation, and freezing-point depression — in "
           "this section. He was awarded the Davy Medal in 1892."),
    source_name="Wikipedia — Raoult's law",
    source_url="https://en.wikipedia.org/wiki/Raoult%27s_law",
)
