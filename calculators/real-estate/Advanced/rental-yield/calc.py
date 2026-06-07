"""Rental Yield — real-estate > Advanced.
Gross and net rental yield: annual rent (less costs) over property value/price."""
from core.registry import register

@register(
    slug="rental-yield",
    name="Rental Yield Calculator",
    section="real-estate",
    sub="Advanced",
    tags=["real estate", "rental yield", "gross yield", "net yield", "property", "investment"],
    formula="gross yield = annual rent / price \u00d7 100 ; net yield subtracts annual costs",
    summary="Gross and net rental yield \u2014 the annual rent as a percentage of the property's price, before and after running costs.",
    viz_template="viz/rental-yield.html",
)
def compute(property_price: float = 600000, weekly_rent: float = 550, annual_costs: float = 6000):
    try:
        price = float(property_price); rent_w = float(weekly_rent); costs = float(annual_costs)
    except (TypeError, ValueError):
        return {"error": "Enter numbers only."}
    if price <= 0:
        return {"error": "Property price must be greater than zero."}
    if rent_w < 0 or costs < 0:
        return {"error": "Rent and costs cannot be negative."}
    annual_rent = rent_w * 52
    gross = annual_rent / price * 100
    net = (annual_rent - costs) / price * 100
    steps = [
        {"label": "Annual rent", "math": r"\(" + ("%g" % rent_w) + r" \times 52 = " + ("%.0f" % annual_rent) + r"\)", "note": "Weekly rent over a year."},
        {"label": "Gross yield", "math": r"\(" + ("%.0f" % annual_rent) + r" / " + ("%.0f" % price) + r" = " + ("%.2f" % gross) + r"\%\)", "note": "Before any costs."},
        {"label": "Net yield", "math": r"\((" + ("%.0f" % annual_rent) + r" - " + ("%.0f" % costs) + r") / " + ("%.0f" % price) + r" = " + ("%.2f" % net) + r"\%\)", "note": "After running costs \u2014 the truer figure."},
    ]
    return {
        "result": ("Gross yield " + ("%.2f" % gross) + "%, net yield " + ("%.2f" % net) + "%"),
        "gross_yield_percent": round(gross, 2), "net_yield_percent": round(net, 2),
        "annual_rent": round(annual_rent, 0), "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
