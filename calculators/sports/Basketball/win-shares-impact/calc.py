"""Win Shares Impact — sports > Basketball.
ILLUSTRATIVE simplified win-share estimate: marginal points over minutes converted
to wins via a league points-per-win figure. Real Win Shares (Basketball-Reference)
are far more complex; this is a transparent teaching approximation."""
from core.registry import register

@register(
    slug="win-shares-impact",
    name="Win Shares Impact Calculator",
    section="sports",
    sub="Basketball",
    tags=["basketball", "win shares", "wins", "contribution", "impact", "model"],
    formula="win shares \u2248 (player marginal points) / (points per win) \u2014 illustrative",
    summary="A simplified estimate of how many team wins a player's scoring contribution is worth. Illustrative approximation \u2014 official Win Shares use a much fuller model.",
    viz_template="viz/win-shares-impact.html",
)
def compute(points_per_game: float = 20, games: float = 70,
            points_per_win: float = 30, replacement_ppg: float = 8):
    try:
        ppg = float(points_per_game); g = float(games)
        ppw = float(points_per_win); rep = float(replacement_ppg)
    except (TypeError, ValueError):
        return {"error": "Enter numbers only."}
    if ppg < 0 or g < 0 or rep < 0:
        return {"error": "Values cannot be negative."}
    if ppw <= 0:
        return {"error": "Points per win must be greater than zero."}
    marginal_ppg = max(0.0, ppg - rep)
    season_points = marginal_ppg * g
    ws = season_points / ppw
    steps = [
        {"label": "Marginal scoring", "math": r"\(" + ("%g" % ppg) + r" - " + ("%g" % rep) + r" = " + ("%.1f" % marginal_ppg) + r"\text{ ppg}\)", "note": "Above a replacement-level player."},
        {"label": "Season points", "math": r"\(" + ("%.1f" % marginal_ppg) + r" \times " + ("%g" % g) + r" = " + ("%.0f" % season_points) + r"\)", "note": "Over the games played."},
        {"label": "Win shares", "math": r"\(" + ("%.0f" % season_points) + r" / " + ("%g" % ppw) + r" = " + ("%.1f" % ws) + r"\)", "note": "Marginal points converted to wins."},
    ]
    return {
        "result": "\u2248 " + ("%.1f" % ws) + " win shares (illustrative)",
        "win_shares": round(ws, 1), "marginal_ppg": round(marginal_ppg, 1),
        "model": "illustrative", "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
