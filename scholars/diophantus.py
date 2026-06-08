"""Scholar: Diophantus of Alexandria, an early pioneer of algebraic methods."""
from core.registry import register_scholar

register_scholar(
    slug="diophantus",
    name="Diophantus",
    era="c. 200–284 CE",
    field_of="Algebra, number theory",
    blurb=("Diophantus of Alexandria was a Greek mathematician often called one of "
           "the fathers of algebra. His work Arithmetica, a collection of problems "
           "solved with equations, introduced an early symbolic notation for an "
           "unknown and its powers, and is filled with the kind of identity "
           "manipulation and substitution used to expand and factor algebraic "
           "expressions. Equations requiring whole-number solutions are still "
           "called Diophantine equations in his honour, and Arithmetica directly "
           "influenced later algebraists including Viète and Fermat."),
    source_name="Wikipedia — Diophantus",
    source_url="https://en.wikipedia.org/wiki/Diophantus",
)
