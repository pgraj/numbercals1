"""Geometry section tile — area, length, and shape results that need no angle/trig."""
from core.registry import register_section

register_section(
    id="geometry",
    name="Geometry",
    glyph="\u25b3",   # triangle
    hue=150,
    blurb="Lengths, areas, and the classic theorems of shape and space.",
    order=20,
)
