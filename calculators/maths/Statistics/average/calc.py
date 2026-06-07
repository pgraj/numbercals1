"""Average (mean) — maths > Statistics. Arithmetic mean of a list of numbers."""
from core.registry import register

def _parse(nums):
    if isinstance(nums, (list, tuple)):
        vals = list(nums)
    else:
        raw = str(nums).replace(";", ",").replace(" ", ",")
        vals = [p for p in raw.split(",") if p != ""]
    out = []
    for v in vals:
        out.append(float(v))
    return out

@register(
    slug="average",
    name="Average (Mean) Calculator",
    section="maths",
    sub="Statistics",
    tags=["average", "mean", "arithmetic mean", "statistics"],
    formula="mean = (sum of values) / (count of values)",
    summary="The arithmetic mean of a set of numbers \u2014 their sum divided by how many there are.",
    viz_template="viz/average.html",
)
def compute(numbers: str = "4, 8, 15, 16, 23, 42"):
    try:
        xs = _parse(numbers)
    except (TypeError, ValueError):
        return {"error": "Enter numbers separated by commas."}
    if not xs:
        return {"error": "Enter at least one number."}
    n = len(xs)
    total = sum(xs)
    mean = total / n
    steps = [
        {"label": "Add them up", "math": r"\(\sum x = " + ("%.4g" % total) + r"\)", "note": "Sum of all values."},
        {"label": "Divide by count", "math": r"\(\bar{x} = \dfrac{" + ("%.4g" % total) + r"}{" + str(n) + r"}\)", "note": str(n) + " values."},
        {"label": "Result", "math": r"\(\bar{x} = " + ("%.4g" % mean) + r"\)", "note": "The mean."},
    ]
    return {
        "result": "Mean = " + ("%.6g" % mean),
        "mean": round(mean, 6), "sum": round(total, 6), "count": n,
        "values": xs, "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
