# -*- coding: utf-8 -*-
"""Prime Spiral - 3D number visualiser (NumberCals)."""
from core.registry import register
from core.faqs import load_sibling_faq

load_sibling_faq(__file__)


@register(
    slug="prime-spiral",
    name="Prime Spiral",
    section="maths",
    topic="3D Models of Numbers",
    sub="Sequences & Patterns",
    order=1,
    tags=["3d", "visualisation", "maths", "prime spiral"],
    formula='primes on a golden-angle spiral',
    summary='Prime numbers lifted onto a golden-angle spiral so the gaps and clusters become visible in 3D.',
    viz_template="viz/m3d-viz.html",
)
def compute(**kwargs):
    return {
        "result": 'Prime Spiral - drag to rotate, explore in 3D',
        "formula_plain": 'primes on a golden-angle spiral',
        "verified": True,
        "mode": "prime-spiral",
        "steps": [],
        "explanation": [
            {"heading": "Everyday hook", "body": 'Prime numbers are the secret-keepers of the internet.'},
            {"heading": "Who uses it", "body": 'Cryptographers, cybersecurity and software engineers, banks.'},
            {"heading": "What it is for", "body": 'Locking and unlocking the secret codes that protect information.'},
            {"heading": "How it helps people", "body": 'Every time you bank online, send a private message, or buy something, primes quietly keep it safe.'},
            {"heading": "Going deeper", "body": 'RSA encryption multiplies two huge primes together; its security comes from how hard it is to factor that product back. (Senior secondary and above)'},
        ],
    }
