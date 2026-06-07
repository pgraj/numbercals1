"""Tennis Match Momentum — sports > Other Sports.
ILLUSTRATIVE momentum index from recent games won, break points and service holds.
Transparent weighting; not an official metric."""
from core.registry import register

@register(
    slug="tennis-momentum",
    name="Tennis Match Momentum Calculator",
    section="sports",
    sub="Other Sports",
    tags=["tennis", "momentum", "break points", "service", "impact", "index"],
    formula="momentum = recent games won \u00d7 2 + breaks \u00d7 3 + holds \u2014 illustrative",
    summary="A transparent momentum index for a tennis match from recent games won, breaks of serve and service holds. Illustrative composite, not an official metric.",
    viz_template="viz/tennis-momentum.html",
)
def compute(recent_games_won: float = 4, recent_games_lost: float = 1,
            breaks_of_serve: float = 2, service_holds: float = 3):
    try:
        gw = float(recent_games_won); gl = float(recent_games_lost)
        br = float(breaks_of_serve); sh = float(service_holds)
    except (TypeError, ValueError):
        return {"error": "Enter numbers only."}
    if any(v < 0 for v in (gw, gl, br, sh)):
        return {"error": "Values cannot be negative."}
    score = gw * 2 + br * 3 + sh - gl * 2
    total = gw + gl
    win_share = (gw / total * 100) if total > 0 else 50.0
    if score >= 12:
        label = "strong momentum"
    elif score >= 5:
        label = "slight edge"
    else:
        label = "momentum against / even"
    steps = [
        {"label": "Weighted score", "math": r"\(" + ("2(%g)+3(%g)+%g-2(%g)" % (gw, br, sh, gl)) + r" = " + ("%.0f" % score) + r"\)", "note": "Breaks weighted highest \u2014 they swing sets."},
        {"label": "Recent games", "math": r"\(" + ("%.0f" % win_share) + r"\%\text{ won}\)", "note": "Share of recent games taken."},
    ]
    return {
        "result": ("Momentum index " + ("%.0f" % score) + " \u2014 " + label),
        "momentum_index": round(score, 0), "recent_win_share": round(win_share, 0),
        "model": "illustrative", "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
