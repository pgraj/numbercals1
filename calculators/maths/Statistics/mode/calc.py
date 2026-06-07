"""Mode — maths > Statistics. The most frequent value(s) in a list."""
from core.registry import register
from collections import Counter

def _parse(nums):
    if isinstance(nums, (list, tuple)):
        return [float(v) for v in nums]
    raw = str(nums).replace(";", ",").replace(" ", ",")
    return [float(p) for p in raw.split(",") if p != ""]

@register(
    slug="mode",
    name="Mode Calculator",
    section="maths",
    sub="Statistics",
    tags=["mode", "most frequent", "statistics"],
    formula="mode = the value(s) that appear most often",
    summary="The value or values that appear most frequently in a data set.",
    viz_template="viz/mode.html",
)
def compute(numbers: str = "2, 4, 4, 6, 6, 6, 9"):
    try:
        xs = _parse(numbers)
    except (TypeError, ValueError):
        return {"error": "Enter numbers separated by commas."}
    if not xs:
        return {"error": "Enter at least one number."}
    counts = Counter(xs)
    top = max(counts.values())
    modes = sorted(v for v, c in counts.items() if c == top)
    if top == 1:
        msg = "No repeats \u2014 every value appears once, so there is no mode."
        mode_str = "none"
    elif len(modes) == 1:
        msg = "Mode = " + ("%.6g" % modes[0]) + " (appears " + str(top) + " times)"
        mode_str = "%.6g" % modes[0]
    else:
        mode_str = ", ".join("%.6g" % m for m in modes)
        msg = "Modes = " + mode_str + " (each appears " + str(top) + " times)"
    steps = [
        {"label": "Count each", "math": r"\(\text{tally each value}\)", "note": "How often each number appears."},
        {"label": "Highest count", "math": r"\(" + str(top) + r"\)", "note": "The top frequency."},
        {"label": "Result", "math": r"\(\text{mode} = " + (mode_str if mode_str != "none" else r"\text{none}") + r"\)", "note": msg},
    ]
    return {
        "result": msg, "modes": modes, "max_count": top,
        "frequencies": {("%.6g" % k): c for k, c in sorted(counts.items())},
        "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
