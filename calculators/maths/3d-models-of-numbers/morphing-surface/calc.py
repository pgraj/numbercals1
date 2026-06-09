# -*- coding: utf-8 -*-
"""Morphing Surface - 3D number visualiser (NumberCals)."""
from core.registry import register
from core.faqs import load_sibling_faq

load_sibling_faq(__file__)


@register(
    slug="morphing-surface",
    name="Morphing Surface",
    section="maths",
    topic="3D Models of Numbers",
    sub="Surfaces & Shapes",
    order=4,
    tags=["3d", "visualisation", "maths", "morphing surface"],
    formula='z = f(x, y) animated over time',
    summary='A 3D surface z = f(x, y) that ripples and morphs over time, showing how a formula with two inputs makes a shape.',
    viz_template="viz/m3d-viz.html",
)
def compute(**kwargs):
    return {
        "result": 'Morphing Surface - drag to rotate, explore in 3D',
        "formula_plain": 'z = f(x, y) animated over time',
        "verified": True,
        "mode": "morphing-surface",
        "steps": [],
        "explanation": [
            {"heading": "Everyday hook", "body": "Hills, valleys and a stadium's curved roof are all surfaces you can write as a formula."},
            {"heading": "Who uses it", "body": 'Architects, engineers, 3D animators, mapmakers.'},
            {"heading": "What it is for", "body": 'Designing shapes and modelling how things bend, stretch or flow.'},
            {"heading": "How it helps people", "body": 'Safer bridges and buildings, accurate maps and weather models, and the worlds you see in films and games.'},
            {"heading": "Going deeper", "body": 'z = f(x, y) lets two inputs control a height - how 3D modelling and multivariable thinking begin. (Yr 10-12)'},
        ],
    }
