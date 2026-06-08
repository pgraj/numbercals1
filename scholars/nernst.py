"""Scholar: Walther Nernst, who linked cell voltage to concentration."""
from core.registry import register_scholar

register_scholar(
    slug="nernst",
    name="Walther Nernst",
    era="1864–1941",
    field_of="Physical chemistry",
    blurb=("Walther Nernst was a German chemist and a founder of modern physical "
           "chemistry, awarded the Nobel Prize in Chemistry in 1920. In his 1889 "
           "work he established the Nernst equation, which connects the voltage of "
           "an electrochemical cell to the concentrations of the species in it, "
           "linking thermodynamics to electrochemistry. The equation predicts how "
           "a battery's voltage changes as it discharges and is fundamental to "
           "batteries, electroplating, and the electrical signals of nerve cells. "
           "Nernst is also known for the third law of thermodynamics."),
    source_name="Wikipedia — Nernst equation",
    source_url="https://en.wikipedia.org/wiki/Nernst_equation",
)
