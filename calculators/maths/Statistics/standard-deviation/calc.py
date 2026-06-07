"""Standard deviation — maths > Statistics. Square root of the variance."""
from core.registry import register
import math

def _parse(nums):
    if isinstance(nums, (list, tuple)):
        return [float(v) for v in nums]
    raw = str(nums).replace(";", ",").replace(" ", ",")
    return [float(p) for p in raw.split(",") if p != ""]

@register(
    slug="standard-deviation",
    name="Standard Deviation Calculator",
    section="maths",
    sub="Statistics",
    tags=["standard deviation", "sigma", "spread", "statistics", "dispersion"],
    formula="\u03c3 = \u221a(\u03a3(x \u2212 mean)\u00b2 / N) ; sample s divides by N \u2212 1",
    summary="How far values typically sit from the mean \u2014 the square root of the variance, in the data's own units.",
    viz_template="viz/standard-deviation.html",
)
def compute(numbers: str = "4, 8, 15, 16, 23, 42", kind: str = "population"):
    try:
        xs = _parse(numbers)
    except (TypeError, ValueError):
        return {"error": "Enter numbers separated by commas."}
    if not xs:
        return {"error": "Enter at least one number."}
    n = len(xs)
    k = str(kind or "population").strip().lower()
    if k == "sample" and n < 2:
        return {"error": "Sample standard deviation needs at least two values."}
    mean = sum(xs) / n
    sq = sum((x - mean) ** 2 for x in xs)
    denom = (n - 1) if k == "sample" else n
    var = sq / denom
    sd = math.sqrt(var)
    steps = [
        {"label": "Mean", "math": r"\(\bar{x} = " + ("%.4g" % mean) + r"\)", "note": "Average of the values."},
        {"label": "Variance", "math": r"\(\dfrac{" + ("%.4g" % sq) + r"}{" + str(denom) + r"} = " + ("%.4g" % var) + r"\)",
         "note": ("Sample divides by n\u22121." if k == "sample" else "Population divides by N.")},
        {"label": "Square root", "math": r"\(\sigma = \sqrt{" + ("%.4g" % var) + r"} = " + ("%.4g" % sd) + r"\)", "note": "Back to the original units."},
    ]
    return {
        "result": ("Sample" if k == "sample" else "Population") + " SD = " + ("%.6g" % sd),
        "standard_deviation": round(sd, 6), "variance": round(var, 6), "mean": round(mean, 6),
        "count": n, "kind": k, "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
