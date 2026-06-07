"""Median — maths > Statistics. Middle value of a sorted list (or mean of the two middle)."""
from core.registry import register

def _parse(nums):
    if isinstance(nums, (list, tuple)):
        return [float(v) for v in nums]
    raw = str(nums).replace(";", ",").replace(" ", ",")
    return [float(p) for p in raw.split(",") if p != ""]

@register(
    slug="median",
    name="Median Calculator",
    section="maths",
    sub="Statistics",
    tags=["median", "middle", "statistics", "percentile"],
    formula="median = middle value of the sorted list",
    summary="The middle value of a sorted list \u2014 or the mean of the two middle values when the count is even.",
    viz_template="viz/median.html",
)
def compute(numbers: str = "7, 3, 9, 1, 5"):
    try:
        xs = _parse(numbers)
    except (TypeError, ValueError):
        return {"error": "Enter numbers separated by commas."}
    if not xs:
        return {"error": "Enter at least one number."}
    s = sorted(xs)
    n = len(s)
    mid = n // 2
    if n % 2 == 1:
        med = s[mid]
        note = "Odd count: the single middle value."
    else:
        med = (s[mid - 1] + s[mid]) / 2
        note = "Even count: mean of the two middle values."
    steps = [
        {"label": "Sort", "math": r"\(" + ",\\ ".join("%.4g" % v for v in s) + r"\)", "note": "Values in order."},
        {"label": "Find middle", "math": r"\(n = " + str(n) + r"\)", "note": note},
        {"label": "Result", "math": r"\(\text{median} = " + ("%.4g" % med) + r"\)", "note": "Middle of the data."},
    ]
    return {
        "result": "Median = " + ("%.6g" % med),
        "median": round(med, 6), "count": n, "sorted": s, "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
