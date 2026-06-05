"""Fraction — maths › Arithmetic. Pie showing the resulting fraction."""
from fractions import Fraction
from core.registry import register


@register(
    slug="fraction",
    name="Fraction calculator",
    section="maths",
    sub="Arithmetic",
    tags=["fraction", "add", "subtract", "multiply", "divide"],
    formula="a/b op c/d  →  simplest form",
    summary="Add, subtract, multiply or divide two fractions and reduce to lowest terms.",
    viz_template="viz/fraction.html",
)
def compute(num1: float = 1, den1: float = 2, num2: float = 1, den2: float = 3,
            op: str = "add"):
    if int(den1) == 0 or int(den2) == 0:
        return {"error": "denominator cannot be zero", "series": []}
    a = Fraction(int(num1), int(den1))
    b = Fraction(int(num2), int(den2))
    ops = {"add": a + b, "subtract": a - b, "multiply": a * b,
           "divide": (a / b if b != 0 else None)}
    res = ops.get(op, a + b)
    if res is None:
        return {"error": "division by zero", "series": []}
    decimal = float(res)
    frac = decimal - int(decimal)  # fractional part for the pie
    return {
        "numerator": res.numerator,
        "denominator": res.denominator,
        "result": f"{res.numerator}/{res.denominator}",
        "decimal": round(decimal, 6),
        "series": [
            {"label": "filled", "value": round(abs(frac), 6)},
            {"label": "empty", "value": round(1 - abs(frac), 6)},
        ],
    }
from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
