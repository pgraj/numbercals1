"""Gibbs Free Energy (ΔG) — chemistry > Electrochemistry > Thermodynamics. Calculate ΔG = ΔH − TΔS to test if a reaction is spontaneous, with symbol legend and real-world examples."""
from core.registry import register


@register(
    slug='gibbs-free-energy', name='Gibbs Free Energy (ΔG)', section="chemistry", topic='Electrochemistry', sub='Thermodynamics',
    order=2,
    tags=['gibbs', 'free energy', 'spontaneity', 'chemistry'],
    formula='Δ G = Δ H - TΔ S',
    summary='Calculate ΔG = ΔH − TΔS to test if a reaction is spontaneous, with symbol legend and real-world examples.',
    viz_template="viz/gibbs-free-energy.html",
    scholar='gibbs',
)
def compute(dH=-100, T=298, dS=0.1):
    try:
        dH = float(dH); T = float(T); dS = float(dS)
    except (TypeError, ValueError):
        return {"error": "Enter \u0394H, T, and \u0394S.", "steps": []}
    dG = dH - T*dS
    def fmt(x): return ("%g" % round(x, 4))
    spont = "spontaneous - it can happen on its own (\u0394G < 0)" if dG<0 else ("non-spontaneous - it needs an energy push (\u0394G > 0)" if dG>0 else "exactly at equilibrium (\u0394G = 0)")
    steps=[
        {"label":"Step 1 - Write the formula","math":r"\( \Delta G = \Delta H - T\,\Delta S \)","note":"Balance the energy released against the increase in disorder."},
        {"label":"Step 2 - Put in your numbers","math":r"\( \Delta G = %s - (%s)(%s) \)" % (fmt(dH), fmt(T), fmt(dS)),"note":"\u0394H = %s, T = %s K, \u0394S = %s." % (fmt(dH), fmt(T), fmt(dS))},
        {"label":"Step 3 - Work it out","math":r"\( \Delta G = %s - %s = %s \)" % (fmt(dH), fmt(T*dS), fmt(dG)),"note":"Negative means it happens by itself; positive means it needs help."},
    ]
    explanation=[
        {"heading":"The formula in plain words","body":"Free energy change = energy released \u2212 (temperature \u00d7 increase in disorder).  If the answer is negative, the reaction happens on its own; if positive, you must push it with energy."},
        {"heading":"What each letter means","legend":[
            ["\u0394G","Gibbs free energy change. Negative = happens by itself; positive = needs energy. (\u0394 means 'change in'.)"],
            ["\u0394H","Heat released or absorbed (enthalpy change). Negative = gives out heat."],
            ["T","Temperature in kelvin (K)."],
            ["\u0394S","Change in disorder (entropy). Positive = more disordered/spread out."],
        ]},
        {"heading":"Real life: ice melting and cold packs \U0001F9CA","body":"Ice melting has positive \u0394G when cold (won't happen) but negative when warm (melts on its own) - the temperature term decides. Instant cold packs use a reaction that is spontaneous yet absorbs heat, so they go cold by themselves: \u0394G negative, \u0394H positive."},
        {"heading":"Real life: why batteries and fuels work \u26A1","body":"A reaction with negative \u0394G can do useful work - that is literally what a battery is (\u0394G = \u2212nFE links it to voltage). Burning fuel has a big negative \u0394G, releasing energy to move cars and generate power. \u0394G is the gatekeeper of which reactions can power things."},
    ]
    return {"result":"\u0394G = %s - %s" % (fmt(dG), spont),
            "formula_plain":"\u0394G = \u0394H \u2212 T\u0394S  \u2192  negative means the reaction happens on its own",
            "law":"\u0394G = \u0394H \u2212 T\u0394S  (also \u0394G = \u2212nFE)","law_label":"Gibbs Free Energy",
            "verified":True,"steps":steps,"explanation":explanation,"dG":dG,"spont":spont}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
