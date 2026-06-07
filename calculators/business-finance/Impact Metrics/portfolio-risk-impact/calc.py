"""Portfolio Risk Impact — business-finance > Impact Metrics.
Two-asset portfolio volatility from weights, individual volatilities and correlation \u2014
shows the diversification effect. Standard portfolio-variance formula."""
from core.registry import register
import math

@register(
    slug="portfolio-risk-impact",
    name="Portfolio Risk Impact Calculator",
    section="business-finance",
    sub="Impact Metrics",
    tags=["portfolio", "risk", "volatility", "diversification", "correlation", "impact"],
    formula="\u03c3p = \u221a(w1\u00b2\u03c31\u00b2 + w2\u00b2\u03c32\u00b2 + 2 w1 w2 \u03c11\u2082 \u03c31 \u03c32)",
    summary="Estimate a two-asset portfolio's volatility from each asset's weight and risk and their correlation \u2014 showing how diversification lowers total risk.",
    viz_template="viz/portfolio-risk-impact.html",
)
def compute(weight_a_percent: float = 60, volatility_a_percent: float = 18,
            volatility_b_percent: float = 8, correlation: float = 0.2):
    try:
        wa = float(weight_a_percent) / 100.0
        sa = float(volatility_a_percent) / 100.0
        sb = float(volatility_b_percent) / 100.0
        rho = float(correlation)
    except (TypeError, ValueError):
        return {"error": "Enter numbers only."}
    if not (0 <= wa <= 1):
        return {"error": "Weight of asset A must be between 0 and 100."}
    if sa < 0 or sb < 0:
        return {"error": "Volatility cannot be negative."}
    if not (-1 <= rho <= 1):
        return {"error": "Correlation must be between -1 and 1."}
    wb = 1 - wa
    var = (wa**2) * (sa**2) + (wb**2) * (sb**2) + 2 * wa * wb * rho * sa * sb
    sigma = math.sqrt(var) if var > 0 else 0.0
    weighted_avg = wa * sa + wb * sb  # the no-diversification benchmark
    benefit = weighted_avg - sigma
    steps = [
        {"label": "Weights", "math": r"\(w_A = " + ("%.2f" % wa) + r",\ w_B = " + ("%.2f" % wb) + r"\)", "note": "They sum to 1."},
        {"label": "Portfolio variance", "math": r"\(\sigma_p^2 = w_A^2\sigma_A^2 + w_B^2\sigma_B^2 + 2w_Aw_B\rho\sigma_A\sigma_B\)", "note": "Correlation \u03c1 = " + ("%.2g" % rho) + "."},
        {"label": "Volatility", "math": r"\(\sigma_p = " + ("%.4f" % sigma) + r" = " + ("%.2f" % (sigma*100)) + r"\%\)", "note": "Below the " + ("%.2f" % (weighted_avg*100)) + "% weighted average \u2014 that gap is the diversification benefit."},
    ]
    return {
        "result": ("Portfolio volatility \u2248 " + ("%.2f" % (sigma*100)) + "%  (vs "
                   + ("%.2f" % (weighted_avg*100)) + "% weighted average \u2014 diversification saves "
                   + ("%.2f" % (benefit*100)) + " pts)"),
        "portfolio_volatility_percent": round(sigma * 100, 3),
        "weighted_average_percent": round(weighted_avg * 100, 3),
        "diversification_benefit_percent": round(benefit * 100, 3), "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
