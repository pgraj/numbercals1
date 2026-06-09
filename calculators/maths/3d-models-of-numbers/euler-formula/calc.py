# -*- coding: utf-8 -*-
"""Euler's Formula - 3D number visualiser (NumberCals)."""
from core.registry import register
from core.faqs import load_sibling_faq

load_sibling_faq(__file__)


@register(
    slug="euler-formula",
    name="Euler's Formula",
    section="maths",
    topic="3D Models of Numbers",
    sub="Famous Equations",
    order=3,
    tags=["3d", "visualisation", "maths", "eulers formula"],
    formula='e^(iθ) = cos θ + i sin θ',
    summary="Euler's formula drawn as a helix that lands exactly on -1 at θ = π - Euler's identity, e^(iπ) + 1 = 0.",
    viz_template="viz/m3d-viz.html",
    scholar='leonhard-euler',
)
def compute(**kwargs):
    return {
        "result": "Euler's Formula - drag to rotate, explore in 3D",
        "formula_plain": 'e^(iθ) = cos θ + i sin θ',
        "verified": True,
        "mode": "euler-formula",
        "steps": [],
        "explanation": [
            {"heading": "Everyday hook", "body": 'A spinning arrow can describe sound, light, and electricity.'},
            {"heading": "Who uses it", "body": 'Electrical, audio and telecommunications engineers; physicists.'},
            {"heading": "What it is for", "body": 'Turning waves and wobbles into neat spinning arrows that are easy to calculate with.'},
            {"heading": "How it helps people", "body": 'The electricity in your home, mobile signals, Wi-Fi and music streaming all rely on it.'},
            {"heading": "Going deeper", "body": 'e^(iθ) = cos θ + i sin θ links exponentials to circular motion; at θ = π it gives e^(iπ) + 1 = 0, often called the most beautiful equation in mathematics. (Senior secondary and above)'},
        ],
    }
