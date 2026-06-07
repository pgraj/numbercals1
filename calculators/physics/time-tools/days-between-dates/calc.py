"""Days Between Dates: calendar-accurate difference between two dates, with an
inclusive/exclusive option. Uses datetime."""
from __future__ import annotations
from datetime import date
from core.registry import register

_DISCLAIMER = ("These values are estimates and may contain computation, formula, "
    "or system errors. They are provided for general reference only \u2014 always verify "
    "results independently before relying on them for academic or professional "
    "decisions.")

_LAW_STATEMENT = ("The number of days between two dates is the calendar difference, counting "
    "leap years correctly. 'Inclusive' counts both the start and end day; 'exclusive' "
    "counts only the gap between them.")
_LAW_SOURCE_NAME = "Wikipedia \u2014 Leap year"
_LAW_SOURCE_URL = "https://en.wikipedia.org/wiki/Leap_year"

def _parse_date(s):
    s = str(s).strip()
    if s == "":
        return None
    parts = s.replace("/", "-").split("-")
    if len(parts) != 3:
        return "format"
    try:
        y, m, d = int(parts[0]), int(parts[1]), int(parts[2])
        return date(y, m, d)
    except (ValueError, TypeError):
        return "format"

_EXPLANATION = [
    {"heading": "How it counts",
     "body": "The calculator turns each date into a day number and subtracts them, so it "
             "automatically handles different month lengths and leap years (29 February). "
             "No manual counting needed."},
    {"heading": "Inclusive vs exclusive",
     "body": "Exclusive counts only the days in between \u2014 from 1 March to 3 March is 2 "
             "days. Inclusive counts both end days too, giving 3 days. Pick whichever your "
             "task needs (event lengths often use inclusive)."},
    {"heading": "Date format",
     "body": "Enter dates as YYYY-MM-DD (for example 2026-03-01). The end date can be "
             "earlier than the start \u2014 the calculator reports the size of the gap "
             "either way."},
]

@register(
    slug="days-between-dates",
    name="Days Between Dates",
    section="physics",
    topic="Time Tools",
    sub="Clock & Calendar",
    order=1,
    summary="Count the calendar-accurate number of days between two dates, with an inclusive or exclusive option.",
    formula="days = end \u2212 start",
    tags=["days between", "date difference", "calendar", "leap year", "time"],
    viz_template="viz/days-between-dates.html",
    related=["work-hours", "time-zone-converter"],
)
def compute(start_date="2026-01-01", end_date="2026-12-31", counting="exclusive", **_ignored):
    s = _parse_date(start_date)
    e = _parse_date(end_date)
    if s == "format" or e == "format":
        return {"error": "Use dates in YYYY-MM-DD format (for example 2026-03-01).", "steps": [], "disclaimer": _DISCLAIMER}
    if s is None or e is None:
        return {"error": "Enter both a start and an end date.", "steps": [], "disclaimer": _DISCLAIMER}

    mode = str(counting or "exclusive").strip().lower()
    raw = abs((e - s).days)
    days = raw + 1 if mode == "inclusive" else raw

    steps = [
        {"label": "Difference", "math": r"\(\lvert \text{end} - \text{start} \rvert\)",
         "note": "Calendar days between the two dates (leap years handled)."},
        {"label": "Counting", "math": (r"\(" + str(raw) + r" + 1\)" if mode == "inclusive" else r"\(" + str(raw) + r"\)"),
         "note": ("Inclusive: both end days counted." if mode == "inclusive" else "Exclusive: gap only.")},
        {"label": "Result", "math": r"\(" + str(days) + r"\ \text{days}\)", "note": "Total days."},
    ]
    weeks = days / 7.0
    return {
        "result": str(days) + " days  (" + ("%.1f" % weeks).rstrip("0").rstrip(".") + " weeks)",
        "days": days, "raw_days": raw, "counting": mode,
        "steps": steps, "explanation": _EXPLANATION,
        "law_statement": _LAW_STATEMENT,
        "law_source_name": _LAW_SOURCE_NAME, "law_source_url": _LAW_SOURCE_URL,
        "disclaimer": _DISCLAIMER,
    }

from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
