"""Clothing Size Converter — static US / UK / EU / Asian lookup matrices.

Returns the equivalent sizes across regions for a chosen category and source
size. Visualisation: a styled HTML comparison table (not canvas).
"""
from core.registry import register

_DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or "
    "system errors. They are provided for general reference only — always "
    "verify results independently before relying on them for engineering, "
    "commercial, or professional decisions."
)

# category -> list of rows; each row is a dict of region -> size label.
# Rows are aligned so one row = one equivalent size across regions.
_TABLES = {
    "Women's Tops": [
        {"US": "0", "UK": "4", "EU": "32", "Asian": "S"},
        {"US": "2", "UK": "6", "EU": "34", "Asian": "S"},
        {"US": "4", "UK": "8", "EU": "36", "Asian": "M"},
        {"US": "6", "UK": "10", "EU": "38", "Asian": "M"},
        {"US": "8", "UK": "12", "EU": "40", "Asian": "L"},
        {"US": "10", "UK": "14", "EU": "42", "Asian": "L"},
        {"US": "12", "UK": "16", "EU": "44", "Asian": "XL"},
    ],
    "Men's Tops": [
        {"US": "XS", "UK": "XS", "EU": "44", "Asian": "S"},
        {"US": "S", "UK": "S", "EU": "46", "Asian": "M"},
        {"US": "M", "UK": "M", "EU": "48", "Asian": "L"},
        {"US": "L", "UK": "L", "EU": "50", "Asian": "XL"},
        {"US": "XL", "UK": "XL", "EU": "52", "Asian": "XXL"},
        {"US": "XXL", "UK": "XXL", "EU": "54", "Asian": "XXXL"},
    ],
    "Women's Shoes": [
        {"US": "5", "UK": "3", "EU": "35.5", "Asian": "22"},
        {"US": "6", "UK": "4", "EU": "36.5", "Asian": "23"},
        {"US": "7", "UK": "5", "EU": "37.5", "Asian": "24"},
        {"US": "8", "UK": "6", "EU": "38.5", "Asian": "25"},
        {"US": "9", "UK": "7", "EU": "40", "Asian": "26"},
        {"US": "10", "UK": "8", "EU": "41", "Asian": "27"},
    ],
    "Men's Shoes": [
        {"US": "7", "UK": "6", "EU": "40", "Asian": "25"},
        {"US": "8", "UK": "7", "EU": "41", "Asian": "26"},
        {"US": "9", "UK": "8", "EU": "42", "Asian": "27"},
        {"US": "10", "UK": "9", "EU": "44", "Asian": "28"},
        {"US": "11", "UK": "10", "EU": "45", "Asian": "29"},
        {"US": "12", "UK": "11", "EU": "46", "Asian": "30"},
    ],
    "Children's Tops": [
        {"US": "2T", "UK": "1.5-2y", "EU": "92", "Asian": "90"},
        {"US": "3T", "UK": "2-3y", "EU": "98", "Asian": "100"},
        {"US": "4T", "UK": "3-4y", "EU": "104", "Asian": "110"},
        {"US": "5", "UK": "4-5y", "EU": "110", "Asian": "120"},
        {"US": "6", "UK": "5-6y", "EU": "116", "Asian": "130"},
    ],
}

_REGIONS = ["US", "UK", "EU", "Asian"]


_EXPLANATION = [
    {"heading": "Why sizes don't match across regions",
     "body": "Clothing sizing grew up separately in each market: US numeric, UK numeric (offset from US), EU centimetre-based, and Asian systems often running smaller. There is no formula — only conventional alignment tables built from body measurements, which is what this converter looks up."},
    {"heading": "How to use the table",
     "body": "Pick the system you know and your size in it; the row that matches is highlighted across all four systems, with neighbouring rows visible so you can judge a borderline fit. Shoe sizes use length-based scales (EU sizes are roughly foot length in centimetres × 1.5)."},
    {"heading": "The big caveat",
     "body": "These are general alignments only. Real fit depends on brand, cut and 'vanity sizing', and fabrics stretch differently. Treat the result as a starting point and always check the maker's own size guide and garment measurements before buying."},
]


@register(
    slug="clothing-sizes",
    name="Clothing Size Converter",
    section="conversions",
    sub="3 · Thermal, Materials & Everyday",
    summary="Convert clothing and shoe sizes across US, UK, EU and Asian systems for men, women and children using standard size matrices.",
    formula="Lookup: match source size in region column, read across the row.",
    tags=["clothing", "size", "shoe", "apparel", "us", "uk", "eu", "converter"],
    viz_template="viz/clothing-sizes.html",
)
def compute(category=None, region=None, size=None, **_ignored):
    if category is None or region is None or size is None:
        return {"error": "Provide a category, a source region, and a size.", "steps": []}
    cat = str(category)
    reg = str(region)
    sz = str(size).strip()

    table = _TABLES.get(cat)
    if table is None:
        return {"error": "Unknown category: " + cat, "steps": []}
    if reg not in _REGIONS:
        return {"error": "Region must be one of: " + ", ".join(_REGIONS), "steps": []}

    match = None
    for row in table:
        if row.get(reg, "").lower() == sz.lower():
            match = row
            break
    if match is None:
        avail = ", ".join(r.get(reg, "") for r in table)
        return {"error": f"Size '{sz}' not found for {reg} in {cat}. Available: {avail}",
                "steps": []}

    result_text = " · ".join(f"{r}: {match[r]}" for r in _REGIONS)
    steps = [
        {"label": "Locate source size",
         "math": f"{reg} {sz} in {cat}"},
        {"label": "Equivalent sizes",
         "math": result_text},
    ]
    return {
        "result": result_text,
        "row": match,
        "regions": _REGIONS,
        "table": table,
        "category": cat,
        "matched_region": reg,
        "matched_size": match.get(reg),
        "steps": steps,
        "explanation": _EXPLANATION,
        "disclaimer": _DISCLAIMER,
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
