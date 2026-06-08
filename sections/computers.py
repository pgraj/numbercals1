"""Computers section — search algorithms, data structures, and the ideas
behind how machines find things. Mirrors the physics.py section pattern."""

from core.registry import register_section

register_section(
    id="computers",
    name="Computers",
    glyph="\u2328",          # U+2328 KEYBOARD
    hue=265,                  # violet, distinct from physics (210) / maths
    blurb="Search algorithms, data structures, and how machines find things.",
    order=3,
)
