"""Discount — accounting › Sales & Retail Accounting.
Waterfall: original price -> minus savings -> plus tax -> final price.
Direct arithmetic; no step-by-step."""
from core.registry import register


@register(
    slug="discount",
    name="Discount Calculator",
    section="accounting",
    sub="Sales & Retail Accounting",
    tags=["discount", "sale", "tax", "savings", "price"],
    formula="Final = (Price − Price·d) × (1 + tax)",
    summary="Final price and total savings after a percentage discount and an optional tax.",
    viz_template="viz/discount.html",
)
def compute(original_price: float, discount_pct: float, tax_pct: float = 0):
    P = float(original_price)
    d = float(discount_pct) / 100
    tax = float(tax_pct) / 100
    if P < 0 or d < 0 or d > 1 or tax < 0:
        return {"error": "Check inputs: discount must be between 0 and 100%."}

    savings = P * d
    discounted = P - savings
    tax_amount = discounted * tax
    final = discounted + tax_amount
    return {
        "final_price": round(final, 2),
        "savings": round(savings, 2),
        "discounted": round(discounted, 2),
        "tax_amount": round(tax_amount, 2),
        "original_price": round(P, 2),
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
