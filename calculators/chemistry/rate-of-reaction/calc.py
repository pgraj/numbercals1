"""Rate of Reaction — chemistry > Chemical Kinetics > Reaction Rate. Calculate reaction rate = −Δ[R]/Δt: how fast a reactant is used up, with symbol legend and real-world examples."""
from core.registry import register


@register(
    slug='rate-of-reaction', name='Rate of Reaction', section="chemistry", topic='Chemical Kinetics', sub='Reaction Rate',
    order=1,
    tags=['rate', 'kinetics', 'reaction speed', 'chemistry'],
    formula='\\text{Rate} = \\frac{-Δ[R]}{Δ t}',
    summary='Calculate reaction rate = −Δ[R]/Δt: how fast a reactant is used up, with symbol legend and real-world examples.',
    viz_template="viz/rate-of-reaction.html",
)
def compute(dR=0.1, dt=10):
    try:
        dR = float(dR); dt = float(dt)
    except (TypeError, ValueError):
        return {"error": "Enter the concentration change and the time.", "steps": []}
    if dt == 0:
        return {"error": "Time interval cannot be zero.", "steps": []}
    rate = dR / dt
    def fmt(x): return ("%g" % round(x, 6))
    steps=[
        {"label":"Step 1 - Write the formula","math":r"\( \text{Rate} = \dfrac{-\Delta[R]}{\Delta t} \)","note":"Rate is how fast the reactant is used up over time. The minus sign keeps the answer positive."},
        {"label":"Step 2 - Put in your numbers","math":r"\( \text{Rate} = \dfrac{%s}{%s} \)" % (fmt(dR), fmt(dt)),"note":"\u0394[R] = %s mol/L was used up, over \u0394t = %s seconds." % (fmt(dR), fmt(dt))},
        {"label":"Step 3 - Divide","math":r"\( \text{Rate} = %s \text{ mol/L\u00b7s} \)" % fmt(rate),"note":"This is how many mol/L of reactant disappear each second."},
    ]
    explanation=[
        {"heading":"The formula in plain words","body":"Rate = how much reactant disappeared \u00f7 how long it took.  It measures the SPEED of a reaction - how fast the starting chemicals turn into products."},
        {"heading":"What each letter means","legend":[
            ["Rate","Speed of the reaction - mol/L used up per second (mol/L\u00b7s)."],
            ["\u0394[R]","Change in the reactant's concentration (how much got used up), in mol/L. (\u0394 means 'change in', [R] means 'concentration of reactant'.)"],
            ["\u0394t","The time interval over which that change happened, in seconds."],
            ["\u2212 (minus)","Makes the rate positive, since the reactant amount is going DOWN."],
        ]},
        {"heading":"Real life: how fast food goes off \U0001F34E","body":"Food spoiling is a chemical reaction with a rate. In a warm room it goes fast (food rots in a day); in the fridge the rate is much slower (food lasts a week). 'Use by' dates are really a reaction-rate calculation - which is why we keep things cold to slow the rate."},
        {"heading":"Real life: a glow stick \U0001FA84","body":"Snap a glow stick and it glows from a chemical reaction. Its rate sets how bright and how long it lasts. Warm it and the reaction speeds up - brighter but shorter. Chill it and the rate slows - dimmer but lasts longer. You are literally controlling reaction rate with temperature."},
    ]
    return {"result":"Rate of reaction = %s mol/L\u00b7s" % fmt(rate),
            "formula_plain":"Rate = \u2212\u0394[R] \u00f7 \u0394t  \u2192  how fast reactant is used up",
            "law":"Rate = \u2212\u0394[R] / \u0394t","law_label":"Rate of Reaction",
            "verified":True,"steps":steps,"explanation":explanation,"rate":rate}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
