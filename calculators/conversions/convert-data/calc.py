"""Data Storage Converter — hub-and-spoke unit converter.

Architecture: every value is converted to the SI base unit (bit)
first, then from the base to the target. No peer-to-peer conversions.
"""
from core.registry import register

# label -> multiplier that takes 1 <unit> to the base (bit)
TO_BASE = {
    "bit": 1.0,
    "byte": 8.0,
    "KiB": 8192,
    "MiB": 8388608,
    "GiB": 8589934592,
    "TiB": 8796093022208,
    "KB": 8000.0,
    "MB": 8000000.0,
    "GB": 8000000000.0,
    "TB": 8000000000000.0,
    "PB": 8000000000000000.0,
    "bps": 1.0,
    "Kbps": 1000.0,
    "Mbps": 1000000.0,
    "Gbps": 1000000000.0,
    "Tbps": 1000000000000.0
}

_DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or "
    "system errors. They are provided for general reference only — always "
    "verify results independently before relying on them for engineering, "
    "commercial, or professional decisions."
)

_BENCHMARKS = [
    {"label": "Text page ~16 Kbit", "base": 16000.0},
    {"label": "MP3 song ~40 Mbit", "base": 40000000.0},
    {"label": "HD movie ~32 Gbit", "base": 32000000000.0}
]


_EXPLANATION = [
    {"heading": "Bits, bytes and the great prefix confusion",
     "body": "A bit is a single 0 or 1. Eight bits make a byte. The headache is the prefix: marketers use decimal (powers of 1000) while operating systems often use binary (powers of 1024). They are NOT the same, and the gap grows with size."},
    {"heading": "Decimal vs binary, side by side",
     "body": "Decimal (storage labels, drives): 1 KB = 1000 bytes, 1 MB = 1000 KB, 1 GB = 1000 MB, 1 TB = 1000 GB, 1 PB = 1000 TB. Binary (RAM, file sizes in many OSes): 1 KiB = 1024 bytes, 1 MiB = 1024 KiB, 1 GiB = 1024 MiB, 1 TiB = 1024 GiB. That is why a '1 TB' drive shows as about 931 GiB in your file manager — same bytes, different prefix."},
    {"heading": "Bandwidth uses bits, not bytes",
     "body": "Network speeds are quoted in bits per second (bps, Kbps, Mbps, Gbps), while file sizes are in bytes. Because 1 byte = 8 bits, a 100 Mbps connection downloads at best about 12.5 MB per second. Forgetting the ×8 is the single most common data-rate mistake."},
    {"heading": "Quick scale reference",
     "body": "KB/KiB ≈ a short email. MB/MiB ≈ a photo or a minute of music. GB/GiB ≈ a movie. TB/TiB ≈ a large drive or a film archive. PB ≈ a data-centre scale store (a thousand TB)."},
]


@register(
    slug="convert-data",
    name="Data Storage Converter",
    section="conversions",
    sub="1 · Basic Converters",
    summary="Convert digital data and bandwidth across binary (KiB/MiB/GiB) and decimal (KB/MB/GB) prefixes via the bit.",
    formula="result = value × (from→bit) ÷ (to→bit)",
    tags=['data', 'converter', 'conversion'],
    viz_template="viz/convert-data.html",
)
def compute(value=None, from_unit=None, to_unit=None, **_ignored):
    """Convert `value` from `from_unit` to `to_unit` via the bit."""
    if value is None or from_unit is None or to_unit is None:
        return {"error": "Provide a value, a source unit, and a target unit.", "steps": []}
    try:
        v = float(value)
    except (TypeError, ValueError):
        return {"error": "Value must be a number.", "steps": []}
    fu, tu = str(from_unit), str(to_unit)
    if fu not in TO_BASE:
        return {"error": "Unknown source unit: " + fu, "steps": []}
    if tu not in TO_BASE:
        return {"error": "Unknown target unit: " + tu, "steps": []}

    base = v * TO_BASE[fu]
    result = base / TO_BASE[tu]

    steps = [
        {"label": "To base unit (bit)",
          "math": f"{v:g} {fu} × {TO_BASE[fu]:g} = {base:g} bit"},
        {"label": "Base to target",
          "math": f"{base:g} ÷ {TO_BASE[tu]:g} = {result:g} {tu}"},
    ]
    return {
        "result": result,
        "result_unit": tu,
        "base_value": base,
        "base_unit": "bit",
        "benchmarks": _BENCHMARKS,
        "steps": steps,
        "explanation": _EXPLANATION,
        "disclaimer": _DISCLAIMER,
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
