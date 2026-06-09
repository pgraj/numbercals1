# -*- coding: utf-8 -*-
"""Lorenz Attractor - 3D number visualiser (NumberCals)."""
from core.registry import register
from core.faqs import load_sibling_faq

load_sibling_faq(__file__)


@register(
    slug="lorenz-attractor",
    name="Lorenz Attractor",
    section="maths",
    topic="3D Models of Numbers",
    sub="Chaos & Dynamics",
    order=5,
    tags=["3d", "visualisation", "maths", "lorenz attractor"],
    formula='the butterfly effect in 3D',
    summary="The Lorenz system traced in 3D - a never-repeating 'butterfly' that shows why tiny changes make weather hard to predict.",
    viz_template="viz/m3d-viz.html",
    scholar='edward-lorenz',
)
def compute(**kwargs):
    return {
        "result": 'Lorenz Attractor - drag to rotate, explore in 3D',
        "formula_plain": 'the butterfly effect in 3D',
        "verified": True,
        "mode": "lorenz-attractor",
        "steps": [],
        "explanation": [
            {"heading": "Everyday hook", "body": "A tiny change today can completely change the weather next week - that's why forecasts get fuzzy."},
            {"heading": "Who uses it", "body": 'Weather forecasters, climate scientists, engineers, biologists.'},
            {"heading": "What it is for", "body": 'Understanding systems that are sensitive and hard to predict.'},
            {"heading": "How it helps people", "body": 'Better weather and climate models, and tools for studying things like heart rhythms.'},
            {"heading": "Going deeper", "body": 'The Lorenz system is three linked equations whose solution never repeats - a famous example of deterministic chaos. (Senior secondary and above)'},
        ],
    }
