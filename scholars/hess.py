"""Scholar: Germain Hess, founder of thermochemistry."""
from core.registry import register_scholar

register_scholar(
    slug="hess",
    name="Germain Hess",
    era="1802–1850",
    field_of="Thermochemistry",
    blurb=("Germain Hess was a Swiss-born Russian chemist and physician whose "
           "studies of heat in chemical reactions founded thermochemistry. In 1840 "
           "he announced Hess's law of constant heat summation: the total enthalpy "
           "change of a reaction is the same regardless of the number of steps "
           "taken to get from reactants to products, because enthalpy is a state "
           "function. This lets chemists calculate heats of reaction that are hard "
           "to measure directly by adding up the steps of an alternative pathway. "
           "His work helped pave the way for the law of conservation of energy."),
    source_name="Wikipedia — Hess's law",
    source_url="https://en.wikipedia.org/wiki/Hess%27s_law",
)
