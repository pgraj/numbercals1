"""Scholar: Al-Khwarizmi, the Persian mathematician whose work gave algebra its name."""
from core.registry import register_scholar

register_scholar(
    slug="al-khwarizmi",
    name="Al-Khwarizmi",
    era="c. 780–850 CE",
    field_of="Algebra, arithmetic, astronomy",
    blurb=("Muhammad ibn Musa al-Khwarizmi was a Persian polymath at the House of "
           "Wisdom in Baghdad during the Islamic Golden Age. His treatise Al-Jabr "
           "(The Compendious Book on Calculation by Completion and Balancing), "
           "written between 813 and 833, gave the first systematic solution of "
           "linear and quadratic equations and is the source of the word "
           "'algebra' (from al-jabr). He solved quadratics by completing the "
           "square, with geometric justifications — the same square-and-rectangle "
           "reasoning behind the square identities such as (a+b)² in this section. "
           "The word 'algorithm' also derives from the Latinised form of his name."),
    source_name="Wikipedia — Muhammad ibn Musa al-Khwarizmi",
    source_url="https://en.wikipedia.org/wiki/Muhammad_ibn_Musa_al-Khwarizmi",
)
