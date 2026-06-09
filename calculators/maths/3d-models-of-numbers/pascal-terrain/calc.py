# -*- coding: utf-8 -*-
"""Pascal Terrain - 3D number visualiser (NumberCals)."""
from core.registry import register
from core.faqs import load_sibling_faq

load_sibling_faq(__file__)


@register(
    slug="pascal-terrain",
    name="Pascal Terrain",
    section="maths",
    topic="3D Models of Numbers",
    sub="Surfaces & Shapes",
    order=9,
    tags=["3d", "visualisation", "maths", "pascal terrain", "pingala",
          "meru-prastara", "binomial"],
    formula='binomial coefficients as a 3D terrain',
    summary="Pascal's triangle as a 3D terrain, revealed row by row - each number the sum of the two above it.",
    viz_template="viz/m3d-viz.html",
    scholar='pingala',
)
def compute(**kwargs):
    return {
        "result": 'Pascal Terrain - drag to rotate, explore in 3D',
        "formula_plain": 'binomial coefficients as a 3D terrain',
        "verified": True,
        "mode": "pascal-terrain",
        "steps": [],
        "explanation": [
            {"heading": "Everyday hook", "body": 'A simple triangle where each number is the sum of the two above it secretly predicts coin-flip odds.'},
            {"heading": "Who discovered it (a long, shared history)", "body": (
                "Although the West calls it Pascal's triangle, the pattern was found "
                "independently across many centuries and cultures. In India, "
                "<a href=\"/scholar/pingala\">Pingala</a> (c. 3rd-2nd century BCE) "
                "studied the combinatorics in his work on poetic metre; the explicit "
                "triangular arrangement - the Meru-prastara, or 'staircase of Mount "
                "Meru' - was set out by the later commentator "
                "<a href=\"/scholar/halayudha\">Halayudha</a> (10th century CE). In "
                "Persia, <a href=\"/scholar/al-karaji\">al-Karaji</a> (c. 1000 CE) and "
                "then <a href=\"/scholar/omar-khayyam\">Omar Khayyam</a> (1048-1131) "
                "described it independently. In China, "
                "<a href=\"/scholar/jia-xian\">Jia Xian</a> (11th century) devised it "
                "and <a href=\"/scholar/yang-hui\">Yang Hui</a> (13th century) preserved "
                "it - still called 'Yang Hui's triangle' there. Finally "
                "<a href=\"/scholar/blaise-pascal\">Blaise Pascal</a> (France, 1654) "
                "tied it to probability theory, and the Western name stuck.")},
            {"heading": "Who uses it", "body": 'Statisticians, financial analysts, geneticists, engineers.'},
            {"heading": "What it is for", "body": 'The numbers that appear when you expand (a + b) to a power, used all through probability.'},
            {"heading": "How it helps people", "body": 'Insurance and risk models, finance, genetics predictions, and quality control in factories.'},
            {"heading": "Going deeper", "body": "The entries are the binomial coefficients 'n choose k' - the bridge between Pascal's triangle, factorials and probability. (Senior secondary and above)"},
        ],
    }
