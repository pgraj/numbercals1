"""Logarithm — maths › Algebra. Plots y = log_base(x). Napier (verified)."""
from math import log
from core.registry import register


@register(
    slug="logarithm", name="Logarithm calculator", section="maths", sub="Algebra", topic="Algebra",
    tags=["log", "logarithm", "ln", "log10", "base"],
    formula="log_b(x) = ln(x) / ln(b)",
    summary="Logarithm of a value to any base, with the log curve plotted.",
    viz_template="viz/logarithm.html", scholar="napier",
)
def compute(value: float = 8, base: float = 2):
    value = float(value); base = float(base)
    if value <= 0:
        return {"error": "value must be greater than 0", "series": [], "steps": []}
    if base <= 0 or base == 1:
        return {"error": "base must be > 0 and not equal to 1", "series": [], "steps": []}
    result = log(value) / log(base)
    xmax = max(value * 1.5, 10.0)
    steps = [
        {"label": "Write what the logarithm asks",
         "math": r"\( \log_{%g}(%g) = ?\ \Rightarrow\ %g^{?} = %g \)"
                 % (base, value, base, value)},
        {"label": "Apply the change-of-base rule",
         "math": r"\( \log_{%g}(%g) = \dfrac{\ln(%g)}{\ln(%g)} \)" % (base, value, value, base)},
        {"label": "Evaluate",
         "math": r"\( = \dfrac{%.6g}{%.6g} = %.6g \)" % (log(value), log(base), result)},
        {"label": "Check",
         "math": r"\( %g^{%.6g} = %g \)" % (base, result, value)},
    ]
    n = 60
    series = [{"x": round(xmax * i / n, 6),
               "y": round(log(xmax * i / n) / log(base), 6)} for i in range(1, n + 1)]
    return {"result": round(result, 6), "base": base, "value": value,
            "series": series, "steps": steps}


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
