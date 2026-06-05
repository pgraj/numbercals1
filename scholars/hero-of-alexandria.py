"""Scholar: Hero of Alexandria, credited with the formula for a triangle's area from its three sides."""
from core.registry import register_scholar

register_scholar(
    slug="hero-of-alexandria",
    name="Hero of Alexandria",
    era="c. 10 – c. 70 AD",
    field_of="Geometry, engineering",
    blurb="Hero (or Heron) of Alexandria was a Greek mathematician and engineer of the first "
          "century AD. The area formula that bears his name — giving a triangle's area from its "
          "three side lengths alone, with no angle or height required — is proved in his work "
          "Metrica, though the result was probably known earlier and the historian Thomas Heath "
          "suggested Archimedes knew it two centuries before. An equivalent formula was found "
          "independently by the Chinese mathematician Qin Jiushao in 1247. The formula can be "
          "proved geometrically, with trigonometry via the law of cosines, or algebraically using "
          "the Pythagorean theorem.",
    source_name="Wikipedia — Heron's formula",
    source_url="https://en.wikipedia.org/wiki/Heron%27s_formula",
)
