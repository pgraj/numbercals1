"""Health section — look & order for the home grid and sidebar.
Optional file; without it the section would auto-create with a '•' glyph.
"""
from core.registry import register_section

register_section(
    id="health",
    name="Health",
    glyph="♡",
    hue=4,                       # warm red — sits apart from the maths/accounting blues
    blurb="Body composition, energy, and fitness — every number shown with its working.",
    order=30,
)
