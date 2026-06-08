"""Scholar: William Henry, who related dissolved gas to its partial pressure."""
from core.registry import register_scholar

register_scholar(
    slug="henry",
    name="William Henry",
    era="1774–1836",
    field_of="Chemistry",
    blurb=("William Henry was an English chemist who, in 1803, formulated Henry's "
           "law: at constant temperature, the amount of a gas that dissolves in a "
           "liquid is directly proportional to the partial pressure of that gas "
           "above the liquid (P = k_H x). It explains why a sealed fizzy drink "
           "holds its dissolved carbon dioxide under pressure and releases it as "
           "bubbles when opened, and why divers must manage dissolved gases in "
           "their blood. The law is a cornerstone of the chemistry of gases in "
           "solution."),
    source_name="Wikipedia — Henry's law",
    source_url="https://en.wikipedia.org/wiki/Henry%27s_law",
)
