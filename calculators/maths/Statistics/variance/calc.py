"""Variance — maths > Statistics. Population or sample variance of a list."""
from core.registry import register

def _parse(nums):
    if isinstance(nums, (list, tuple)):
        return [float(v) for v in nums]
    raw = str(nums).replace(";", ",").replace(" ", ",")
    return [float(p) for p in raw.split(",") if p != ""]

@register(
    slug="variance",
    name="Variance Calculator",
    section="maths",
    sub="Statistics",
    tags=["variance", "spread", "statistics", "dispersion"],
    formula="population \u03c3\u00b2 = \u03a3(x \u2212 mean)\u00b2 / N ; sample s\u00b2 divides by N \u2212 1",
    summary="How spread out the data is \u2014 the average of the squared distances from the mean.",
    viz_template="viz/variance.html",
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
        return {"error": "Sample variance needs at least two values."}
    mean = sum(xs) / n
    sq = sum((x - mean) ** 2 for x in xs)
    denom = (n - 1) if k == "sample" else n
    var = sq / denom
    steps = [
        {"label": "Mean", "math": r"\(\bar{x} = " + ("%.4g" % mean) + r"\)", "note": "Average of the values."},
        {"label": "Squared distances", "math": r"\(\sum (x-\bar{x})^2 = " + ("%.4g" % sq) + r"\)", "note": "Add up each gap from the mean, squared."},
        {"label": "Divide", "math": r"\(\dfrac{" + ("%.4g" % sq) + r"}{" + str(denom) + r"} = " + ("%.4g" % var) + r"\)",
         "note": ("Sample divides by n\u22121." if k == "sample" else "Population divides by N.")},
    ]
    return {
        "result": ("Sample" if k == "sample" else "Population") + " variance = " + ("%.6g" % var),
        "variance": round(var, 6), "mean": round(mean, 6), "count": n, "kind": k, "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
