"""Chemistry section — concentration, colligative properties, kinetics,
equilibrium, electrochemistry, and thermochemistry. Mirrors the physics.py pattern."""

from core.registry import register_section

register_section(
    id="chemistry",
    name="Chemistry",
    glyph="\u2697",          # U+2697 ALEMBIC (lab flask)
    hue=160,                  # teal-green, distinct from maths(150)/physics(210)/computers(265)
    blurb="Concentration, colligative properties, kinetics, equilibrium, and electrochemistry.",
    order=4,
)
