"""Conversions section — units, measures, and constants across every domain.

Registers the section tile. No compute logic here; each converter lives in its
own folder under calculators/conversions/<sub>/<slug>/.
"""
from core.registry import register_section

register_section(
    id="conversions",
    name="Conversions",
    glyph="⇄",
    hue=195,
    blurb="Units, measures, and constants — every domain.",
    order=40,
)
