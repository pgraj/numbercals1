"""Commission — business-finance > Core. Commission earned from sales and rate,
with optional base salary for total pay."""
from core.registry import register

@register(
    slug="commission",
    name="Commission Calculator",
    section="business-finance",
    sub="Core",
    tags=["commission", "sales", "rate", "earnings", "pay"],
    formula="commission = sales \u00d7 rate% ; total = base + commission",
    summary="Work out commission earned from a sales figure and rate, plus total pay including any base salary.",
    viz_template="viz/commission.html",
)
def compute(sales: float = 50000, commission_rate_percent: float = 5, base_pay: float = 0):
    try:
        S = float(sales); r = float(commission_rate_percent); base = float(base_pay)
    except (TypeError, ValueError):
        return {"error": "Enter numbers only."}
    if S < 0 or base < 0:
        return {"error": "Sales and base pay cannot be negative."}
    if r < 0:
        return {"error": "Commission rate cannot be negative."}
    comm = S * r / 100.0
    total = base + comm
    steps = [
        {"label": "Commission", "math": r"\(" + ("%.2f" % S) + r" \times " + ("%.4g" % r) + r"\% = " + ("%.2f" % comm) + r"\)", "note": "Sales times the rate."},
        {"label": "Total pay", "math": r"\(" + ("%.2f" % base) + r" + " + ("%.2f" % comm) + r" = " + ("%.2f" % total) + r"\)", "note": "Base plus commission."},
    ]
    return {
        "result": "Commission " + ("%.2f" % comm) + (("; total pay " + ("%.2f" % total)) if base > 0 else ""),
        "commission": round(comm, 2), "total_pay": round(total, 2), "base_pay": round(base, 2),
        "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
