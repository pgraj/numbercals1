# -*- coding: utf-8 -*-
"""Collatz Trajectories - 3D number visualiser (NumberCals)."""
from core.registry import register
from core.faqs import load_sibling_faq

load_sibling_faq(__file__)


@register(
    slug="collatz-trajectories",
    name="Collatz Trajectories",
    section="maths",
    topic="3D Models of Numbers",
    sub="Sequences & Patterns",
    order=7,
    tags=["3d", "visualisation", "maths", "collatz trajectories"],
    formula='the 3n+1 hailstone paths',
    summary='Hailstone paths for many starting numbers: even -> halve, odd -> triple and add one. They always reach 1 - but nobody has proved why.',
    viz_template="viz/m3d-viz.html",
    scholar='lothar-collatz',
)
def compute(**kwargs):
    return {
        "result": 'Collatz Trajectories - drag to rotate, explore in 3D',
        "formula_plain": 'the 3n+1 hailstone paths',
        "verified": True,
        "mode": "collatz-trajectories",
        "steps": [],
        "explanation": [
            {"heading": "Everyday hook", "body": 'Pick a number. Even? Halve it. Odd? Triple it and add one. You always reach 1... but nobody has proved why!'},
            {"heading": "Who uses it", "body": 'Mathematicians and computer scientists exploring patterns.'},
            {"heading": "What it is for", "body": 'Studying simple rules that produce surprisingly complex behaviour.'},
            {"heading": "How it helps people", "body": 'It teaches algorithmic thinking and shows that maths still has unsolved mysteries waiting to be cracked.'},
            {"heading": "Going deeper", "body": 'Despite a rule simple enough for a Year 5 student, the Collatz conjecture remains unproven. (Yr 9-12)'},
        ],
    }
