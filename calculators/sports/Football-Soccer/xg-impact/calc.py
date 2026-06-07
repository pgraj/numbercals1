"""Expected Goals (xG) Impact — sports > Football / Soccer.
Compares total xG for and against to a performance read. xG per shot is user-supplied
or summed; there is no single canonical xG model, so this aggregates user xG values."""
from core.registry import register

def _parse(nums):
    if isinstance(nums, (list, tuple)):
        return [float(v) for v in nums]
    raw = str(nums).replace(";", ",").replace(" ", ",")
    return [float(p) for p in raw.split(",") if p != ""]

@register(
    slug="xg-impact",
    name="Expected Goals (xG) Impact Calculator",
    section="sports",
    sub="Football / Soccer",
    tags=["football", "soccer", "xg", "expected goals", "chances", "impact"],
    formula="team xG = sum of each shot's xG ; xG difference = xG for \u2212 xG against",
    summary="Total a team's expected goals from each chance's xG and compare with goals actually scored to see over- or under-performance. xG values are user-supplied.",
    viz_template="viz/xg-impact.html",
)
def compute(shot_xgs: str = "0.12, 0.05, 0.33, 0.78, 0.09", goals_scored: float = 2,
            xg_against: float = 1.1):
    try:
        xs = _parse(shot_xgs)
        goals = float(goals_scored); xga = float(xg_against)
    except (TypeError, ValueError):
        return {"error": "Enter xG values (0-1) separated by commas, and numeric goals."}
    if not xs:
        return {"error": "Enter at least one shot xG value."}
    if any(x < 0 or x > 1 for x in xs):
        return {"error": "Each shot xG must be between 0 and 1."}
    if goals < 0 or xga < 0:
        return {"error": "Goals and xG against cannot be negative."}
    team_xg = sum(xs)
    perf = goals - team_xg  # + = clinical/over-performing, - = wasteful
    xg_diff = team_xg - xga
    steps = [
        {"label": "Total xG", "math": r"\(\sum xG = " + ("%.2f" % team_xg) + r"\)", "note": "Quality of chances created (" + str(len(xs)) + " shots)."},
        {"label": "vs goals", "math": r"\(" + ("%.0f" % goals) + r" - " + ("%.2f" % team_xg) + r" = " + ("%+.2f" % perf) + r"\)", "note": ("Clinical \u2014 scored above chance quality." if perf >= 0 else "Wasteful \u2014 scored below chance quality.")},
        {"label": "xG difference", "math": r"\(" + ("%.2f" % team_xg) + r" - " + ("%.2f" % xga) + r" = " + ("%+.2f" % xg_diff) + r"\)", "note": ("Created better chances than conceded." if xg_diff >= 0 else "Conceded better chances than created.")},
    ]
    return {
        "result": ("Team xG " + ("%.2f" % team_xg) + " from " + str(len(xs)) + " shots; "
                   + ("over" if perf >= 0 else "under") + "-performed by " + ("%.2f" % abs(perf))
                   + "; xG diff " + ("%+.2f" % xg_diff)),
        "team_xg": round(team_xg, 2), "performance": round(perf, 2), "xg_difference": round(xg_diff, 2),
        "shots": len(xs), "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
