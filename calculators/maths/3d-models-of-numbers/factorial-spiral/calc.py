# -*- coding: utf-8 -*-
"""Factorial Spiral - 3D number visualiser (NumberCals)."""
from core.registry import register
from core.faqs import load_sibling_faq

load_sibling_faq(__file__)


@register(
    slug="factorial-spiral",
    name="Factorial Spiral",
    section="maths",
    topic="3D Models of Numbers",
    sub="Sequences & Patterns",
    order=2,
    tags=["3d", "visualisation", "maths", "factorial spiral"],
    formula='n! as a log-height spiral',
    summary='Factorial growth shown as a spiral whose height is log10(n!), so you can see how explosively n! grows.',
    viz_template="viz/m3d-viz.html",
)
def compute(**kwargs):
    return {
        "result": 'Factorial Spiral - drag to rotate, explore in 3D',
        "formula_plain": 'n! as a log-height spiral',
        "verified": True,
        "mode": "factorial-spiral",
        "steps": [],
        "explanation": [
            {"heading": "Everyday hook", "body": 'How many ways can you line up your friends for a photo? Factorials count that.'},
            {"heading": "Who uses it", "body": 'Statisticians, data scientists, delivery and logistics planners.'},
            {"heading": "What it is for", "body": 'Counting the number of possible arrangements and combinations.'},
            {"heading": "How it helps people", "body": 'Lottery odds, planning the shortest delivery routes, and apps that recommend videos or songs.'},
            {"heading": "Going deeper", "body": 'Factorials sit inside permutations, combinations and probability - the foundation of statistics and risk. (Senior secondary and above)'},
        ],
    }
