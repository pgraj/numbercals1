"""Transfer Value Impact — sports > Football / Soccer.
ILLUSTRATIVE: adjusts a base value by age, contract years left, form and output.
A transparent toy model of how factors push a fee up or down \u2014 not a market valuation."""
from core.registry import register

@register(
    slug="transfer-value-impact",
    name="Transfer Value Impact Calculator",
    section="sports",
    sub="Football / Soccer",
    tags=["football", "soccer", "transfer", "value", "fee", "impact", "model"],
    formula="value = base \u00d7 age factor \u00d7 contract factor \u00d7 form factor \u2014 illustrative",
    summary="See how age, remaining contract and recent form push a player's transfer value up or down, using a transparent illustrative model. Not a real market valuation.",
    viz_template="viz/transfer-value-impact.html",
)
def compute(base_value_m: float = 30, age: float = 24, contract_years_left: float = 3,
            form_index: float = 1.0):
    try:
        base = float(base_value_m); a = float(age); cy = float(contract_years_left); form = float(form_index)
    except (TypeError, ValueError):
        return {"error": "Enter numbers only."}
    if base < 0:
        return {"error": "Base value cannot be negative."}
    if not (15 <= a <= 45):
        return {"error": "Age should be between 15 and 45."}
    if cy < 0:
        return {"error": "Contract years cannot be negative."}
    if form <= 0:
        return {"error": "Form index must be greater than zero (1.0 = average)."}
    # age factor: peaks ~24-27, declines after
    if a <= 27:
        age_factor = 1.0 + max(0.0, (27 - abs(a - 25.5)) - 25.5) * 0  # keep near 1 in prime
        age_factor = 1.05 if 23 <= a <= 27 else 0.95 if a < 23 else 1.0
    else:
        age_factor = max(0.4, 1.0 - (a - 27) * 0.08)
    # contract factor: <1 year left slashes value; long deals add a little
    if cy < 1:
        contract_factor = 0.5
    elif cy < 2:
        contract_factor = 0.8
    else:
        contract_factor = min(1.15, 1.0 + (cy - 2) * 0.05)
    value = base * age_factor * contract_factor * form
    steps = [
        {"label": "Age factor", "math": r"\(\times " + ("%.2f" % age_factor) + r"\)", "note": ("Prime years hold value." if a <= 27 else "Value tapers after the late 20s.")},
        {"label": "Contract factor", "math": r"\(\times " + ("%.2f" % contract_factor) + r"\)", "note": ("Short contract slashes the fee \u2014 leverage gone." if cy < 2 else "A long deal protects the fee.")},
        {"label": "Form", "math": r"\(\times " + ("%.2f" % form) + r"\)", "note": "1.0 = average; above 1 = hot streak."},
    ]
    return {
        "result": ("Illustrative value \u2248 " + ("%.1f" % value) + "M  (from a " + ("%.0f" % base) + "M base)"),
        "estimated_value_m": round(value, 2), "age_factor": round(age_factor, 2),
        "contract_factor": round(contract_factor, 2), "model": "illustrative", "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
