"""Property value estimator — accounting › Real Estate / Property.

Projects what a property bought today is worth after n years of appreciation,
in both nominal and inflation-adjusted (real) terms. Three depths via `mode`:

  simple    : price + appreciation + inflation -> nominal vs real value curves.
  scenarios : same, but low / average / high appreciation bands around the rate.
  mortgage  : adds deposit + loan so it reports equity, and real ROI on the
              cash actually put in (the deposit).

Step-by-step working is returned because the real-value and equity figures
involve a chain the reader benefits from seeing.
"""
from core.registry import register


def _real(nominal, infl, years):
    """Deflate a nominal figure to today's money."""
    return nominal / ((1 + infl) ** years) if infl > -1 else nominal


@register(
    slug="property-value",
    name="Property Value Estimator",
    section="accounting",
    sub="Real Estate / Property",
    tags=["property", "real estate", "house price", "appreciation",
          "inflation", "equity", "home value"],
    formula="Value = Price·(1 + g)^n ; Real value = Value / (1 + i)^n",
    summary="Projects a property's future value from an appreciation rate, shows "
            "the real (inflation-adjusted) value, and — in mortgage mode — the "
            "equity and the real return on your deposit.",
    viz_template="viz/property-value.html",
)
def compute(price: float,
            appreciation_pct: float,
            years: float,
            inflation_pct: float = 3.0,
            mode: str = "simple",
            deposit: float = 0.0,
            loan_rate_pct: float = 6.0,
            loan_years: float = 30.0):
    P = float(price)
    g = float(appreciation_pct) / 100
    i = float(inflation_pct) / 100
    n = int(float(years))
    m = str(mode).strip().lower()
    if m not in ("simple", "scenarios", "mortgage"):
        m = "simple"

    if P < 0 or n < 0:
        return {"error": "Price and years must be zero or positive.", "steps": []}
    if n == 0:
        n = 0  # degenerate but valid: value == price

    # --- core projection (used by every mode) ----------------------------
    def proj(rate):
        out = []
        for yr in range(0, n + 1):
            nominal = P * (1 + rate) ** yr
            out.append({
                "year": yr,
                "nominal": round(nominal, 2),
                "real": round(_real(nominal, i, yr), 2),
            })
        return out

    series = proj(g)
    final = series[-1]
    nominal_value = final["nominal"]
    real_value = final["real"]
    total_gain = round(nominal_value - P, 2)
    real_gain = round(real_value - P, 2)

    result = {
        "mode": m,
        "price": round(P, 2),
        "years": n,
        "appreciation_pct": round(float(appreciation_pct), 4),
        "inflation_pct": round(float(inflation_pct), 4),
        "nominal_value": nominal_value,
        "real_value": real_value,
        "total_gain": total_gain,
        "real_gain": real_gain,
        "series": series,
    }

    steps = [
        {"label": "Project the nominal value",
         "math": r"\( V = P\,(1+g)^n = %s\,(1+%.4f)^{%d} = %s \)"
                 % (f"{P:,.0f}", g, n, f"{nominal_value:,.2f}"),
         "note": "Compound the purchase price by the appreciation rate for each year."},
        {"label": "Strip out inflation to get today's money",
         "math": r"\( V_{real} = \dfrac{V}{(1+i)^n} = \dfrac{%s}{(1+%.4f)^{%d}} = %s \)"
                 % (f"{nominal_value:,.2f}", i, n, f"{real_value:,.2f}"),
         "note": "The real value is what the future price is worth in today's dollars."},
        {"label": "Gain in real terms",
         "math": r"\( %s - %s = %s \)"
                 % (f"{real_value:,.2f}", f"{P:,.0f}", f"{real_gain:,.2f}"),
         "note": "A positive figure means the property outpaced inflation; "
                 "negative means it lost ground in real terms."},
    ]

    # --- scenarios: low / average / high appreciation bands --------------
    if m == "scenarios":
        low_rate = max(g - 0.02, -0.99)
        high_rate = g + 0.02
        result["scenarios"] = {
            "low":  {"rate_pct": round(low_rate * 100, 2),
                     "series": proj(low_rate),
                     "nominal_value": round(P * (1 + low_rate) ** n, 2)},
            "avg":  {"rate_pct": round(g * 100, 2),
                     "series": series,
                     "nominal_value": nominal_value},
            "high": {"rate_pct": round(high_rate * 100, 2),
                     "series": proj(high_rate),
                     "nominal_value": round(P * (1 + high_rate) ** n, 2)},
        }
        steps.append({
            "label": "Bracket the uncertainty",
            "math": r"\( g_{low}=%.2f\%%,\ g_{avg}=%.2f\%%,\ g_{high}=%.2f\%% \)"
                    % (low_rate * 100, g * 100, high_rate * 100),
            "note": "Markets are not a single number. The low and high bands sit "
                    "two percentage points either side of your estimate."})

    # --- mortgage: equity + real ROI on the deposit ----------------------
    if m == "mortgage":
        D = max(float(deposit), 0.0)
        loan = max(P - D, 0.0)
        lr = float(loan_rate_pct) / 100 / 12
        lm = int(float(loan_years) * 12)
        # monthly repayment
        if loan > 0 and lr > 0 and lm > 0:
            emi = loan * lr * (1 + lr) ** lm / ((1 + lr) ** lm - 1)
        elif loan > 0 and lm > 0:
            emi = loan / lm
        else:
            emi = 0.0
        # outstanding balance after n years of repayments (capped at term)
        months_paid = min(n * 12, lm)
        if lr > 0 and lm > 0:
            balance = loan * (1 + lr) ** months_paid \
                - emi * (((1 + lr) ** months_paid - 1) / lr)
        else:
            balance = max(loan - emi * months_paid, 0.0)
        balance = max(round(balance, 2), 0.0)

        equity = round(nominal_value - balance, 2)
        real_equity = round(_real(equity, i, n), 2)
        # ROI measured against the cash actually committed: the deposit
        roi_on_deposit = round(((real_equity - D) / D) * 100, 2) if D > 0 else None

        result.update({
            "deposit": round(D, 2),
            "loan": round(loan, 2),
            "monthly_repayment": round(emi, 2),
            "loan_balance": balance,
            "equity": equity,
            "real_equity": real_equity,
            "roi_on_deposit_pct": roi_on_deposit,
        })
        steps.append({
            "label": "Equity = value − what you still owe",
            "math": r"\( E = %s - %s = %s \)"
                    % (f"{nominal_value:,.2f}", f"{balance:,.2f}", f"{equity:,.2f}"),
            "note": "Equity is the slice of the property you actually own once the "
                    "outstanding loan is subtracted."})
        if roi_on_deposit is not None:
            steps.append({
                "label": "Real return on your deposit",
                "math": r"\( ROI = \dfrac{E_{real} - D}{D}\times100 = "
                        r"\dfrac{%s - %s}{%s}\times100 = %.2f\%% \)"
                        % (f"{real_equity:,.2f}", f"{D:,.0f}", f"{D:,.0f}",
                           roi_on_deposit),
                "note": "The deposit is the cash you put in. This is what that cash "
                        "grew to in real terms, expressed as a percentage."})

    result["steps"] = steps
    return result


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
