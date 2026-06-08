"""Scholar: Michael Faraday, whose laws govern electrolysis."""
from core.registry import register_scholar

register_scholar(
    slug="faraday",
    name="Michael Faraday",
    era="1791–1867",
    field_of="Physics, chemistry",
    blurb=("Michael Faraday was an English scientist whose discoveries shaped both "
           "electromagnetism and electrochemistry. His laws of electrolysis (1834) "
           "state that the mass of a substance deposited or dissolved at an "
           "electrode is proportional to the quantity of electric charge passed. "
           "This is the basis of electroplating, metal refining, and the "
           "electrolytic production of elements. The Faraday constant (about "
           "96,500 coulombs per mole of electrons) and the unit of capacitance, "
           "the farad, are both named in his honour."),
    source_name="Wikipedia — Faraday's laws of electrolysis",
    source_url="https://en.wikipedia.org/wiki/Faraday%27s_laws_of_electrolysis",
)
