"""Retail Packaging Converter — Pallet → Case → Pack → Unit hierarchy.

Multiplies a quantity at any level down to base units (or rolls up), using
configurable units-per-level inputs. Visualisation: breakdown donut.
"""
from core.registry import register

_DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or "
    "system errors. They are provided for general reference only — always "
    "verify results independently before relying on them for engineering, "
    "commercial, or professional decisions."
)

_LEVELS = ["Pallet", "Case", "Pack", "Unit"]


_EXPLANATION = [
    {"heading": "It is a nested multiplication",
     "body": "A retail supply chain stacks quantities: many units make a pack, many packs make a case, many cases make a pallet. Converting between levels is just multiplying or dividing by how many of the smaller thing fit in the larger one. There is no fixed standard — you tell the tool your product's pack/case/pallet ratios."},
    {"heading": "How the maths chains together",
     "body": "Units in one pallet = (cases per pallet) × (packs per case) × (units per pack). So with 40 cases/pallet, 12 packs/case and 24 units/pack: one pallet = 40 × 12 × 24 = 11,520 units. To find total units, multiply your quantity by the units contained in whatever level you entered."},
    {"heading": "Worked example",
     "body": "2 pallets, using the ratios above: 2 × 11,520 = 23,040 units. The same 23,040 units is also 23,040 ÷ 288 = 80 cases (since one case = 12 × 24 = 288 units), or 960 packs. Rolling 'up' can give fractional pallets — that just means a partial load, not an error."},
]


@register(
    slug="packaging-units",
    name="Retail Packaging Converter",
    section="conversions",
    sub="2 · Advanced Converters",
    summary="Convert quantities across a retail packaging hierarchy — pallets, cases, packs and units — with configurable units-per-level.",
    formula="units = qty × (cases/pallet × packs/case × units/pack), scaled from the chosen level",
    tags=["packaging", "retail", "pallet", "case", "pack", "logistics", "converter"],
    viz_template="viz/packaging-units.html",
)
def compute(quantity=None, level=None,
            cases_per_pallet=None, packs_per_case=None, units_per_pack=None,
            **_ignored):
    if quantity is None or level is None:
        return {"error": "Provide a quantity and the level it is counted in.", "steps": []}
    try:
        qty = float(quantity)
        cpp = float(cases_per_pallet if cases_per_pallet is not None else 0)
        ppc = float(packs_per_case if packs_per_case is not None else 0)
        upp = float(units_per_pack if units_per_pack is not None else 0)
    except (TypeError, ValueError):
        return {"error": "All quantities must be numbers.", "steps": []}
    lvl = str(level)
    if lvl not in _LEVELS:
        return {"error": "Level must be one of: " + ", ".join(_LEVELS), "steps": []}
    if min(cpp, ppc, upp) <= 0:
        return {"error": "Cases/pallet, packs/case and units/pack must all be positive.", "steps": []}

    # units contained in one of each level
    units_in = {
        "Pallet": cpp * ppc * upp,
        "Case": ppc * upp,
        "Pack": upp,
        "Unit": 1.0,
    }
    total_units = qty * units_in[lvl]

    breakdown = {
        "Pallet": total_units / units_in["Pallet"],
        "Case": total_units / units_in["Case"],
        "Pack": total_units / units_in["Pack"],
        "Unit": total_units,
    }
    steps = [
        {"label": "Units per chosen level",
         "math": f"1 {lvl} = {units_in[lvl]:g} units"},
        {"label": "Total base units",
         "math": f"{qty:g} {lvl} × {units_in[lvl]:g} = {total_units:g} units"},
    ]
    return {
        "result": total_units,
        "result_unit": "units",
        "breakdown": breakdown,
        "levels": _LEVELS,
        "steps": steps,
        "explanation": _EXPLANATION,
        "disclaimer": _DISCLAIMER,
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
