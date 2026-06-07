"""Work Hours: hours worked from start/end times minus a break. Handles overnight shifts."""
from __future__ import annotations
from core.registry import register

_DISCLAIMER = ("These values are estimates and may contain computation, formula, "
    "or system errors. They are provided for general reference only \u2014 always verify "
    "results independently before relying on them for academic or professional "
    "decisions.")

_LAW_STATEMENT = ("Hours worked = (end time \u2212 start time) \u2212 break. If the end time "
    "is earlier than the start, the shift runs past midnight, so a day is added.")
_LAW_SOURCE_NAME = "Wikipedia \u2014 Working time"
_LAW_SOURCE_URL = "https://en.wikipedia.org/wiki/Working_time"

def _f(x):
    if x is None: return ""
    if abs(x - round(x)) < 1e-9: return str(int(round(x)))
    return ("%.2f" % x).rstrip("0").rstrip(".")

def _parse_hhmm(s):
    # Accept "HH:MM" or "H:MM" or a plain hour number.
    s = str(s).strip()
    if s == "":
        return None
    if ":" in s:
        parts = s.split(":")
        h = int(parts[0]); m = int(parts[1])
    else:
        h = int(float(s)); m = 0
    if h < 0 or h > 23 or m < 0 or m > 59:
        return "range"
    return h * 60 + m

_EXPLANATION = [
    {"heading": "How it is worked out",
     "body": "The calculator turns your start and end times into minutes, subtracts the "
             "start from the end, then takes off your break. Divide by 60 and you get the "
             "hours worked."},
    {"heading": "Overnight shifts",
     "body": "If your shift ends earlier on the clock than it starts (say 22:00 to 06:00), "
             "it must have crossed midnight, so the calculator adds 24 hours before "
             "subtracting. That gives the correct 8-hour overnight shift."},
    {"heading": "Breaks",
     "body": "Unpaid breaks are taken off the total. Enter the break in minutes; leave it "
             "at 0 if there is no break to deduct."},
]

@register(
    slug="work-hours",
    name="Work Hours Calculator",
    section="physics",
    topic="Time Tools",
    sub="Clock & Calendar",
    order=0,
    summary="Work out hours worked from a start and end time, minus an optional break; handles overnight shifts.",
    formula="hours = (end \u2212 start) \u2212 break",
    tags=["work hours", "timesheet", "shift", "overnight", "time", "payroll"],
    viz_template="viz/work-hours.html",
    related=["days-between-dates", "time-zone-converter"],
)
def compute(start="09:00", end="17:00", break_minutes=30, **_ignored):
    s = _parse_hhmm(start)
    e = _parse_hhmm(end)
    if s == "range" or e == "range":
        return {"error": "Use 24-hour times between 00:00 and 23:59.", "steps": [], "disclaimer": _DISCLAIMER}
    if s is None or e is None:
        return {"error": "Enter both a start and an end time as HH:MM.", "steps": [], "disclaimer": _DISCLAIMER}
    try:
        brk = float(break_minutes) if break_minutes not in (None, "") else 0.0
    except (TypeError, ValueError):
        return {"error": "Break must be a number of minutes.", "steps": [], "disclaimer": _DISCLAIMER}
    if brk < 0:
        return {"error": "Break cannot be negative.", "steps": [], "disclaimer": _DISCLAIMER}

    overnight = e <= s
    span = (e - s) + (1440 if overnight else 0)  # minutes
    worked = span - brk
    if worked < 0:
        return {"error": "The break is longer than the shift \u2014 check your inputs.", "steps": [], "disclaimer": _DISCLAIMER}
    hours = worked / 60.0

    steps = [
        {"label": "Shift length",
         "math": r"\(\text{end} - \text{start}" + (r" + 24\text{h}" if overnight else "") + r"\)",
         "note": ("Shift crosses midnight, so 24 hours are added." if overnight
                  else "End minus start.")},
        {"label": "Minus break", "math": r"\(" + _f(span) + r"\,\text{min} - " + _f(brk) + r"\,\text{min}\)",
         "note": "Take off the unpaid break."},
        {"label": "Result", "math": r"\(" + _f(worked) + r"\,\text{min} = " + _f(hours) + r"\,\text{h}\)",
         "note": "Worked minutes converted to hours."},
    ]
    return {
        "result": "Hours worked = " + _f(hours) + " h  (" + _f(worked) + " min)",
        "hours": hours, "worked_minutes": worked, "overnight": overnight,
        "steps": steps, "explanation": _EXPLANATION,
        "law_statement": _LAW_STATEMENT,
        "law_source_name": _LAW_SOURCE_NAME, "law_source_url": _LAW_SOURCE_URL,
        "disclaimer": _DISCLAIMER,
    }

from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
