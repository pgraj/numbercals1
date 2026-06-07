"""Scholar: Johannes Kepler, who discovered the three laws of planetary motion."""
from core.registry import register_scholar

register_scholar(
    slug="johannes-kepler",
    name="Johannes Kepler",
    era="1571\u20131630",
    field_of="Astronomy",
    blurb="Johannes Kepler was a German astronomer and mathematician who worked out how "
          "the planets actually move. Using the remarkably precise observations of Tycho "
          "Brahe, he found that planets travel in ellipses with the Sun at one focus "
          "(first law), sweep out equal areas in equal times so they move faster when "
          "closer to the Sun (second law), and obey a fixed relationship between orbital "
          "period and distance, the square of the period being proportional to the cube "
          "of the orbit's size (third law, published in 1619). These three laws replaced "
          "centuries of circular-orbit assumptions and later gave Newton the foundation "
          "for his law of universal gravitation.",
    source_name="Wikipedia \u2014 Johannes Kepler",
    source_url="https://en.wikipedia.org/wiki/Johannes_Kepler",
)
