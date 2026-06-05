"""Percentage — maths › Arithmetic. Interactive pie of part vs whole."""
from core.registry import register


@register(
    slug="percentage",
    name="Percentage calculator",
    section="maths",
    topic="Arithmetic",
    sub="Arithmetic",
    tags=["percent", "percentage", "ratio", "change"],
    formula="part = (p/100)·whole ; p = (part/whole)·100",
    summary="Find a percentage of a number, what percent one number is of another, and percentage change.",
    viz_template="viz/percentage.html",
)
def compute(whole: float = 200, percent: float = 15):
    whole = float(whole); percent = float(percent)
    part = (percent / 100) * whole
    return {
        "part": round(part, 4),
        "rest": round(whole - part, 4),
        "series": [
            {"label": "part", "value": round(part, 4)},
            {"label": "rest", "value": round(whole - part, 4)},
        ],
    }
from core.faqs import load_sibling_faq
load_sibling_faq(__file__)