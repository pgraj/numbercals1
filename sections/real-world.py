"""Real-World Trigonometry section — interactive worked examples that put the
trig ratios to work on tangible problems (heights, navigation, construction,
astronomy, forensics, marine depth). Each page is a scenario: pre-set defaults,
a domain-specific diagram, a story animation, and a couple of live inputs so the
reader can explore "what if". Pages link back to the calculators they exercise,
and those calculators link forward to these examples from their FAQ.
"""
from core.registry import register_section

register_section(
    id="real-world",
    name="Real-World Trigonometry",
    glyph="\U0001F30D",   # globe
    hue=205,
    blurb="See trigonometry solve tangible problems — measuring heights, "
          "navigating, building, and reaching the stars.",
    order=25,
)
