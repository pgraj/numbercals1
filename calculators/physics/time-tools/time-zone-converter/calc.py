"""Time Zone Converter: convert a wall-clock time from one zone to another using the
IANA database (zoneinfo), so daylight saving is handled automatically."""
from __future__ import annotations
from datetime import datetime
from core.registry import register

try:
    from zoneinfo import ZoneInfo
    _HAVE_TZ = True
except Exception:  # pragma: no cover
    _HAVE_TZ = False

_DISCLAIMER = ("These values are estimates and may contain computation, formula, "
    "or system errors. They are provided for general reference only \u2014 always verify "
    "results independently before relying on them for academic or professional "
    "decisions.")

_LAW_STATEMENT = ("Each time zone is an offset from UTC, and many zones shift by an hour for "
    "daylight saving at certain times of year. Converting means expressing the same moment "
    "in another zone's local clock.")
_LAW_SOURCE_NAME = "Wikipedia \u2014 Time zone"
_LAW_SOURCE_URL = "https://en.wikipedia.org/wiki/Time_zone"

# ~30 common cities -> IANA zone names. zoneinfo applies DST automatically.
_ZONES = {
    "Sydney": "Australia/Sydney", "Melbourne": "Australia/Melbourne",
    "Perth": "Australia/Perth", "Auckland": "Pacific/Auckland",
    "Tokyo": "Asia/Tokyo", "Singapore": "Asia/Singapore",
    "Hong Kong": "Asia/Hong_Kong", "Shanghai": "Asia/Shanghai",
    "Mumbai": "Asia/Kolkata", "Dubai": "Asia/Dubai",
    "Moscow": "Europe/Moscow", "Istanbul": "Europe/Istanbul",
    "London": "Europe/London", "Paris": "Europe/Paris",
    "Berlin": "Europe/Berlin", "Madrid": "Europe/Madrid",
    "Rome": "Europe/Rome", "Amsterdam": "Europe/Amsterdam",
    "Johannesburg": "Africa/Johannesburg", "Cairo": "Africa/Cairo",
    "Sao Paulo": "America/Sao_Paulo", "New York": "America/New_York",
    "Toronto": "America/Toronto", "Chicago": "America/Chicago",
    "Denver": "America/Denver", "Los Angeles": "America/Los_Angeles",
    "Mexico City": "America/Mexico_City", "Honolulu": "Pacific/Honolulu",
    "UTC": "UTC",
}

def _parse_dt(date_s, time_s):
    date_s = str(date_s).strip(); time_s = str(time_s).strip()
    if date_s == "" or time_s == "":
        return None
    ds = date_s.replace("/", "-").split("-")
    ts = time_s.split(":")
    try:
        y, mo, d = int(ds[0]), int(ds[1]), int(ds[2])
        h = int(ts[0]); mi = int(ts[1]) if len(ts) > 1 else 0
        return datetime(y, mo, d, h, mi)
    except (ValueError, IndexError, TypeError):
        return "format"

def _offset_str(dt_aware):
    off = dt_aware.utcoffset()
    if off is None:
        return "UTC"
    total = int(off.total_seconds() // 60)
    sign = "+" if total >= 0 else "-"
    total = abs(total)
    return "UTC%s%02d:%02d" % (sign, total // 60, total % 60)

_EXPLANATION = [
    {"heading": "What it does",
     "body": "You give a date and time in one city; the converter works out what the clock "
             "reads at that same moment in another city. Because zones differ by whole or "
             "half hours, the time \u2014 and sometimes the date \u2014 can change."},
    {"heading": "Daylight saving is automatic",
     "body": "Using the world time-zone database, the tool knows when each region is on "
             "summer (daylight saving) time, so the offset is correct for the exact date "
             "you enter \u2014 not just a fixed number."},
    {"heading": "Reading the result",
     "body": "The result shows the converted local time and that zone's offset from UTC. If "
             "the converted time rolls past midnight, the date shown will move to the next "
             "or previous day accordingly."},
]

@register(
    slug="time-zone-converter",
    name="Time Zone Converter",
    section="physics",
    topic="Time Tools",
    sub="Clock & Calendar",
    order=2,
    summary="Convert a date and time from one city's zone to another, with daylight saving handled automatically.",
    formula="same moment, different local clock",
    tags=["time zone", "timezone", "convert", "utc", "dst", "world clock"],
    viz_template="viz/time-zone-converter.html",
    related=["work-hours", "days-between-dates"],
)
def compute(from_zone="Sydney", to_zone="London",
            date="2026-06-01", time="09:00", **_ignored):
    if not _HAVE_TZ:
        return {"error": "Time zone database is unavailable in this environment.",
                "steps": [], "disclaimer": _DISCLAIMER}

    fz = str(from_zone or "").strip()
    tz = str(to_zone or "").strip()
    if fz not in _ZONES or tz not in _ZONES:
        return {"error": "Pick both cities from the list.", "steps": [], "disclaimer": _DISCLAIMER}

    naive = _parse_dt(date, time)
    if naive == "format":
        return {"error": "Use date YYYY-MM-DD and time HH:MM.", "steps": [], "disclaimer": _DISCLAIMER}
    if naive is None:
        return {"error": "Enter both a date and a time.", "steps": [], "disclaimer": _DISCLAIMER}

    try:
        src = naive.replace(tzinfo=ZoneInfo(_ZONES[fz]))
        dst = src.astimezone(ZoneInfo(_ZONES[tz]))
    except Exception:
        return {"error": "Could not convert between those zones.", "steps": [], "disclaimer": _DISCLAIMER}

    src_off = _offset_str(src)
    dst_off = _offset_str(dst)
    out_str = dst.strftime("%Y-%m-%d %H:%M")
    src_str = src.strftime("%Y-%m-%d %H:%M")

    steps = [
        {"label": "Source", "math": r"\(\text{" + fz + ": " + src_str + " (" + src_off + r")}\)",
         "note": "The time you entered, in the source zone."},
        {"label": "Same moment", "math": r"\(\text{convert to " + tz + r"}\)",
         "note": "Express that exact moment in the target zone (DST applied)."},
        {"label": "Result", "math": r"\(\text{" + tz + ": " + out_str + " (" + dst_off + r")}\)",
         "note": "Local time in the target city."},
    ]
    return {
        "result": tz + ": " + out_str + "  (" + dst_off + ")",
        "from_zone": fz, "to_zone": tz,
        "source_local": src_str, "source_offset": src_off,
        "target_local": out_str, "target_offset": dst_off,
        "steps": steps, "explanation": _EXPLANATION,
        "law_statement": _LAW_STATEMENT,
        "law_source_name": _LAW_SOURCE_NAME, "law_source_url": _LAW_SOURCE_URL,
        "disclaimer": _DISCLAIMER,
    }

from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
