# -*- coding: utf-8 -*-
"""Interactive Periodic Table — NumberCals calculator.

This is a reference/explorer tool rather than a single-formula calculator, so
compute() simply returns the full 118-element dataset that the viz renders into
an interactive grid + 3D atomic model. The data lives beside this file in
elements.json so the calculator folder stays fully plug-and-play.
"""
import json
import os

from core.registry import register
from core.faqs import load_sibling_faq

_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(_DIR, "elements.json"), encoding="utf-8") as _fh:
    _ELEMENTS = json.load(_fh)

load_sibling_faq(__file__)


@register(
    slug="periodic-table",
    name="Interactive Periodic Table",
    section="chemistry",
    topic="Periodic Table",
    sub="Elements Explorer",
    order=0,
    tags=["periodic table", "elements", "atomic structure", "chemistry",
          "atomic number", "electron shells", "organic", "inorganic"],
    formula="118 elements - click to explore",
    summary=("Explore all 118 elements: filter by organic or inorganic, then "
             "click any element for a rotatable 3D atomic model, its properties, "
             "where it is found and used, and how it helps in daily life."),
    viz_template="viz/periodic-table.html",
    scholar="dmitri-mendeleev",
)
def compute(**kwargs):
    """Return the element dataset. Ignores inputs; the viz drives interaction."""
    return {
        "result": "118 elements - click any element to explore it in 3D",
        "formula_plain": ("The periodic table arranges all known elements by "
                          "atomic number, so elements in the same column share "
                          "similar chemical behaviour."),
        "verified": True,
        "elements": _ELEMENTS,
        "count": len(_ELEMENTS),
        "steps": [],
        "explanation": [
            {"heading": "What the periodic table shows",
             "body": ("Every element is placed by its atomic number (the number "
                      "of protons). Reading left to right and top to bottom, the "
                      "elements' properties repeat in a regular, periodic pattern "
                      "- which is exactly what Mendeleev spotted in 1869.")},
            {"heading": "Organic vs inorganic (how this tool uses the words)",
             "body": ("Strictly, organic/inorganic describes compounds, not single "
                      "elements. Here 'Organic' highlights the elements central to "
                      "organic chemistry - H, C, N, O, P, S and the common organic "
                      "halogens F, Cl, Br, I - and everything else is 'Inorganic'.")},
            {"heading": "Real life: reading a label",
             "body": ("The 'Na' on a salt packet and the 'Fe' on a vitamin bottle "
                      "are element symbols straight from this table - sodium and iron.")},
            {"heading": "Real life: the air and water around you",
             "body": ("The air you breathe is mostly nitrogen (N) and oxygen (O), "
                      "and every drop of water is hydrogen (H) and oxygen (O) - four "
                      "boxes on this very table.")},
        ],
    }
