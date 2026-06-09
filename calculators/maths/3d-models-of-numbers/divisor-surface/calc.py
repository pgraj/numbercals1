# -*- coding: utf-8 -*-
"""Divisor Surface - 3D number visualiser (NumberCals)."""
from core.registry import register
from core.faqs import load_sibling_faq

load_sibling_faq(__file__)


@register(
    slug="divisor-surface",
    name="Divisor Surface",
    section="maths",
    topic="3D Models of Numbers",
    sub="Sequences & Patterns",
    order=8,
    tags=["3d", "visualisation", "maths", "divisor surface"],
    formula='height = number of divisors d(n)',
    summary='A surface whose height is the number of divisors d(n), laid on a modular grid so the structure of factor-rich numbers shows.',
    viz_template="viz/m3d-viz.html",
)
def compute(**kwargs):
    return {
        "result": 'Divisor Surface - drag to rotate, explore in 3D',
        "formula_plain": 'height = number of divisors d(n)',
        "verified": True,
        "mode": "divisor-surface",
        "steps": [],
        "explanation": [
            {"heading": "Everyday hook", "body": 'Some numbers split neatly into many factors; others barely split at all - and that difference is powerful.'},
            {"heading": "Who uses it", "body": 'Cryptographers, computer scientists, engineers designing gears and schedules.'},
            {"heading": "What it is for", "body": 'Encryption, error-correcting codes, and anything with cycles or repetition.'},
            {"heading": "How it helps people", "body": 'Reliable data storage, secure communication, and the timing behind clocks, calendars and machines.'},
            {"heading": "Going deeper", "body": 'The number of divisors of n depends on its prime factorisation - linking back to the prime spiral. (Senior secondary and above)'},
        ],
    }
