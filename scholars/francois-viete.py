"""Scholar: François Viète, who related a polynomial's coefficients to its roots."""
from core.registry import register_scholar

register_scholar(
    slug="francois-viete",
    name="François Viète",
    era="1540–1603",
    field_of="Algebra",
    blurb=("François Viète (Latinised as Franciscus Vieta) was a French "
           "mathematician and a founder of modern symbolic algebra, introducing "
           "the systematic use of letters for both knowns and unknowns. He is best "
           "known today for Vieta's formulas, which relate the coefficients of a "
           "polynomial to sums and products of its roots. For a quadratic, this is "
           "exactly the (x+a)(x+b) = x² + (a+b)x + ab relationship: the middle "
           "coefficient is the sum of the roots and the constant is their product — "
           "the principle behind the product identities in this section."),
    source_name="Wikipedia — Vieta's formulas",
    source_url="https://en.wikipedia.org/wiki/Vieta%27s_formulas",
)
