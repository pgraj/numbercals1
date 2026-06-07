"""F1 Pit Stop Impact — sports > Other Sports.
Track-position arithmetic: time lost in the pit vs rivals' pace gives places lost/gained.
Mostly real arithmetic; the gap-to-position conversion is an estimate."""
from core.registry import register

@register(
    slug="f1-pit-stop-impact",
    name="F1 Pit Stop Impact Calculator",
    section="sports",
    sub="Other Sports",
    tags=["f1", "formula 1", "pit stop", "strategy", "time loss", "impact"],
    formula="net time = pit lane loss \u2212 (fresh-tyre gain per lap \u00d7 laps remaining)",
    summary="Estimate whether a pit stop pays off: the pit-lane time lost versus the lap-time gained on fresh tyres over the remaining laps.",
    viz_template="viz/f1-pit-stop-impact.html",
)
def compute(pit_lane_loss_s: float = 22, fresh_tyre_gain_per_lap_s: float = 1.2,
            laps_remaining: float = 15, avg_gap_between_cars_s: float = 1.5):
    try:
        loss = float(pit_lane_loss_s); gain = float(fresh_tyre_gain_per_lap_s)
        laps = float(laps_remaining); gap = float(avg_gap_between_cars_s)
    except (TypeError, ValueError):
        return {"error": "Enter numbers only."}
    if loss < 0 or laps < 0:
        return {"error": "Time loss and laps cannot be negative."}
    if gap <= 0:
        return {"error": "Average gap between cars must be greater than zero."}
    total_gain = gain * laps
    net = total_gain - loss  # + = pit stop pays off over the stint
    positions = net / gap
    steps = [
        {"label": "Tyre gain", "math": r"\(" + ("%g" % gain) + r" \times " + ("%g" % laps) + r" = " + ("%.1f" % total_gain) + r"\text{ s}\)", "note": "Fresh tyres are faster every lap."},
        {"label": "Net time", "math": r"\(" + ("%.1f" % total_gain) + r" - " + ("%g" % loss) + r" = " + ("%+.1f" % net) + r"\text{ s}\)", "note": ("Stop pays off over the stint." if net >= 0 else "Stop costs more than it gains over these laps.")},
        {"label": "Track position", "math": r"\(" + ("%+.1f" % net) + r" / " + ("%g" % gap) + r" \approx " + ("%+.1f" % positions) + r"\text{ places}\)", "note": "Net time converted to places, given the field's spacing."},
    ]
    return {
        "result": ("Net " + ("%+.1f" % net) + " s over the stint  (\u2248 " + ("%+.1f" % positions) + " places)"),
        "net_time_s": round(net, 1), "positions_delta": round(positions, 1),
        "tyre_gain_s": round(total_gain, 1), "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
