"""SaaS Growth Forecast — business-simulation > Models.
Projects MRR forward N months with new MRR added each month and monthly churn applied.
Standard recursive MRR model: MRR_next = MRR\u00d7(1\u2212churn) + new MRR."""
from core.registry import register

@register(
    slug="saas-growth-forecast",
    name="SaaS Growth Forecast Calculator",
    section="business-simulation",
    sub="Models",
    tags=["saas", "mrr", "arr", "growth", "churn", "forecast", "simulation"],
    formula="MRR(next) = MRR \u00d7 (1 \u2212 monthly churn) + new MRR ; repeat for N months",
    summary="Forecast monthly recurring revenue over time as new MRR is added each month and churn erodes the base \u2014 the core SaaS growth recursion.",
    viz_template="viz/saas-growth-forecast.html",
)
def compute(starting_mrr: float = 50000, new_mrr_per_month: float = 8000,
            monthly_churn_percent: float = 3, months: float = 12):
    try:
        mrr = float(starting_mrr); new_mrr = float(new_mrr_per_month)
        churn = float(monthly_churn_percent); n = int(float(months))
    except (TypeError, ValueError):
        return {"error": "Enter numbers only."}
    if mrr < 0 or new_mrr < 0:
        return {"error": "MRR values cannot be negative."}
    if not (0 <= churn <= 100):
        return {"error": "Monthly churn must be between 0 and 100."}
    if not (1 <= n <= 120):
        return {"error": "Months must be between 1 and 120."}
    c = churn / 100.0
    start = mrr
    trail = [round(mrr, 0)]
    for _ in range(n):
        mrr = mrr * (1 - c) + new_mrr
        trail.append(round(mrr, 0))
    end_mrr = mrr
    arr = end_mrr * 12
    growth_pct = ((end_mrr / start - 1) * 100) if start > 0 else None
    steps = [
        {"label": "Monthly recursion", "math": r"\(\text{MRR}_{t+1} = \text{MRR}_t(1 - " + ("%.3g" % c) + r") + " + ("%.0f" % new_mrr) + r"\)", "note": "Churn shrinks the base, new sales rebuild it."},
        {"label": "After " + str(n) + " months", "math": r"\(\text{MRR} = " + ("%.0f" % end_mrr) + r"\)", "note": "Compounded over the horizon."},
        {"label": "Implied ARR", "math": r"\(" + ("%.0f" % end_mrr) + r" \times 12 = " + ("%.0f" % arr) + r"\)", "note": "Annualised run rate at the end."},
    ]
    return {
        "result": ("MRR " + ("%.0f" % start) + " \u2192 " + ("%.0f" % end_mrr) + " in " + str(n)
                   + " months  (ARR \u2248 " + ("%.0f" % arr) + ")"),
        "ending_mrr": round(end_mrr, 0), "ending_arr": round(arr, 0),
        "growth_percent": (round(growth_pct, 1) if growth_pct is not None else None),
        "trajectory": trail, "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
