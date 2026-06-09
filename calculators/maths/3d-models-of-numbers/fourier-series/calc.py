# -*- coding: utf-8 -*-
"""Fourier Series - 3D number visualiser (NumberCals)."""
from core.registry import register
from core.faqs import load_sibling_faq

load_sibling_faq(__file__)


@register(
    slug="fourier-series",
    name="Fourier Series",
    section="maths",
    topic="3D Models of Numbers",
    sub="Famous Equations",
    order=6,
    tags=["3d", "visualisation", "maths", "fourier series"],
    formula='building a square wave from sine waves',
    summary='A square wave built one harmonic at a time, showing how any signal can be made by stacking simple sine waves.',
    viz_template="viz/m3d-viz.html",
    scholar='joseph-fourier',
)
def compute(**kwargs):
    return {
        "result": 'Fourier Series - drag to rotate, explore in 3D',
        "formula_plain": 'building a square wave from sine waves',
        "verified": True,
        "mode": "fourier-series",
        "steps": [],
        "explanation": [
            {"heading": "Everyday hook", "body": "Any sound can be built by stacking simple 'pure' notes on top of each other."},
            {"heading": "Who uses it", "body": 'Audio engineers, medical-imaging specialists, phone and camera engineers.'},
            {"heading": "What it is for", "body": 'Breaking signals into simple waves so they can be cleaned up or compressed.'},
            {"heading": "How it helps people", "body": 'MP3 music, JPEG photos, MRI and ultrasound scans, and noise-cancelling headphones.'},
            {"heading": "Going deeper", "body": 'Adding more sine harmonics gets closer and closer to a square wave - the core idea behind signal processing. (Yr 11-12)'},
        ],
    }
