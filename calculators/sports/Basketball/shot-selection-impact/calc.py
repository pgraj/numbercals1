"""Shot Selection Impact — sports > Basketball.
Effective field goal % (a real metric): eFG% = (FGM + 0.5\u00d73PM) / FGA."""
from core.registry import register

@register(
    slug="shot-selection-impact",
    name="Shot Selection Impact Calculator",
    section="sports",
    sub="Basketball",
    tags=["basketball", "shot selection", "efg", "effective field goal", "threes", "impact"],
    formula="eFG% = (FGM + 0.5 \u00d7 3PM) / FGA \u00d7 100",
    summary="Effective field goal percentage, which credits the extra value of three-pointers \u2014 the standard way to judge shot selection quality.",
    viz_template="viz/shot-selection-impact.html",
)
def compute(field_goals_made: float = 9, three_pointers_made: float = 4, field_goals_attempted: float = 18):
    try:
        fgm = float(field_goals_made); tpm = float(three_pointers_made); fga = float(field_goals_attempted)
    except (TypeError, ValueError):
        return {"error": "Enter numbers only."}
    if fgm < 0 or tpm < 0 or fga < 0:
        return {"error": "Values cannot be negative."}
    if fga <= 0:
        return {"error": "Field goals attempted must be greater than zero."}
    if fgm > fga:
        return {"error": "Makes cannot exceed attempts."}
    if tpm > fgm:
        return {"error": "Three-pointers made cannot exceed total field goals made."}
    efg = (fgm + 0.5 * tpm) / fga * 100
    plain = fgm / fga * 100
    steps = [
        {"label": "Plain FG%", "math": r"\(" + ("%g" % fgm) + r" / " + ("%g" % fga) + r" = " + ("%.1f" % plain) + r"\%\)", "note": "Ignores the extra point from threes."},
        {"label": "Effective FG%", "math": r"\((" + ("%g" % fgm) + r" + 0.5 \times " + ("%g" % tpm) + r") / " + ("%g" % fga) + r" = " + ("%.1f" % efg) + r"\%\)", "note": "Credits threes as worth more."},
    ]
    return {
        "result": "Effective FG% = " + ("%.1f" % efg) + "%  (plain FG% " + ("%.1f" % plain) + "%)",
        "efg_percent": round(efg, 1), "fg_percent": round(plain, 1), "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
