"""Calorie target — health › Diet & Nutrition.
Educational estimate built ON TOP of TDEE. Deliberately NOT a prescriptive
diet engine: goals are shown as informational ranges, a standard moderate
adjustment is used (not aggressive deficits), and a safe-calorie floor is
enforced with a visible note rather than silently returning a crash-diet number.
Macro split is shown as percentages with gram equivalents."""
from core.registry import register
from core.health_common import HEALTH_DISCLAIMER

# Standard, conservative adjustments. We intentionally do NOT offer large or
# custom deficits — this tool is for orientation, not for prescribing a diet.
GOALS = {
    "maintain": (0,    "Maintain weight"),
    "lose":     (-500, "Gradual loss (~0.45 kg/week)"),
    "gain":     (+400, "Gradual gain"),
}

# Widely cited minimum daily intakes below which eating should be medically
# supervised. We never present a target under these without flagging it.
FLOOR = {"male": 1500, "female": 1200, "other": 1350}

# Balanced reference macro split (% of calories). 4 kcal/g carb & protein, 9 kcal/g fat.
MACROS = {"Carbohydrate": 0.45, "Protein": 0.25, "Fat": 0.30}
KCAL_PER_G = {"Carbohydrate": 4, "Protein": 4, "Fat": 9}


@register(
    slug="calorie-target",
    name="Calorie Calculator",
    section="health",
    sub="Diet & Nutrition",
    tags=["calories", "calorie target", "macros", "maintenance", "nutrition"],
    formula=r"Target ≈ TDEE ± a moderate adjustment (shown as a range)",
    summary="An educational daily-calorie estimate from your TDEE, with a balanced macronutrient split. Not a diet plan.",
    viz_template="viz/calorie-target.html",
)
def compute(tdee: float, sex: str = "other", goal: str = "maintain"):
    sex = str(sex).strip().lower()
    if sex not in FLOOR:
        sex = "other"
    goal = str(goal).strip().lower()
    if goal not in GOALS:
        goal = "maintain"
    t = float(tdee)
    if t <= 0:
        return {"error": "Enter your TDEE (calories per day) — use the TDEE calculator first.",
                "steps": []}

    adj, goal_label = GOALS[goal]
    raw_target = t + adj

    floor = FLOOR[sex]
    floored = False
    target = raw_target
    if target < floor:
        target = floor
        floored = True

    # Present as an informational ±100 kcal range, not a single hard number.
    low = round(target - 100)
    high = round(target + 100)
    target_r = round(target)

    # Macro split in grams at the target.
    macros = []
    for name, frac in MACROS.items():
        kcal = target * frac
        grams = kcal / KCAL_PER_G[name]
        macros.append({"name": name, "pct": round(frac * 100),
                       "kcal": round(kcal), "grams": round(grams)})

    steps = [
        {"label": "Start from maintenance (TDEE)",
         "math": r"\( \text{TDEE} = %d \text{ kcal/day} \)" % round(t),
         "note": "This is roughly what holds your weight steady."},
        {"label": "Apply a moderate %s adjustment" % goal,
         "math": r"\( %d %s %d = %d \text{ kcal/day} \)"
                 % (round(t), "+" if adj >= 0 else "−", abs(adj), round(raw_target)),
         "note": goal_label + "."},
    ]
    if floored:
        steps.append({
            "label": "Apply the safe-calorie floor",
            "math": r"\( \text{raised to } %d \text{ kcal/day} \)" % floor,
            "note": "The estimate fell below a commonly cited safe minimum, so it has been "
                    "raised. Eating below this should only be done under medical supervision."})
    steps.append({
        "label": "Balanced macro split",
        "math": r"\( 45\%% \text{ carbs},\ 25\%% \text{ protein},\ 30\%% \text{ fat} \)",
        "note": "One common balanced ratio; individual needs vary."})

    return {
        "target": target_r,
        "range_low": low,
        "range_high": high,
        "goal": goal,
        "goal_label": goal_label,
        "floored": floored,
        "macros": macros,
        # A surfaced, machine-readable reminder the template renders prominently.
        "advisory": "This is a general educational estimate, not a diet plan or medical "
                    "advice. For a plan suited to you — especially when losing weight — "
                    "speak with a doctor or an accredited dietitian.",
        "disclaimer": HEALTH_DISCLAIMER,
        "steps": steps,
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
