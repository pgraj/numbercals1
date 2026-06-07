"""Kepler's Laws of planetary motion. Mode selector:
  1st (elliptical orbits), 2nd (equal areas in equal times),
  3rd (T^2 = 4 pi^2 a^3 / (G M)) — the computational mode, solve T, a or M."""
from __future__ import annotations
import math
from core.registry import register

_DISCLAIMER = ("These values are estimates and may contain computation, formula, "
    "or system errors. They are provided for general reference only \u2014 always verify "
    "results independently before relying on them for academic or professional "
    "decisions.")

_G = 6.6743e-11  # N m^2 / kg^2 (CODATA)

_LAW_SOURCE_NAME = "Wikipedia \u2014 Kepler's laws of planetary motion"
_LAW_SOURCE_URL = "https://en.wikipedia.org/wiki/Kepler%27s_laws_of_planetary_motion"

_LAW1 = ("Kepler's first law: every planet moves in an ellipse with the Sun at one of the "
    "two foci \u2014 orbits are slightly squashed circles, not perfect circles.")
_LAW2 = ("Kepler's second law: a line from the Sun to the planet sweeps out equal areas in "
    "equal times, so a planet moves faster when it is closer to the Sun and slower when "
    "farther away.")
_LAW3 = ("Kepler's third law: the square of a planet's orbital period is proportional to the "
    "cube of its orbit's size, T\u00b2 = 4\u03c0\u00b2a\u00b3 / (G M). Planets farther out "
    "take much longer to go around.")

def _f(x):
    if x is None: return ""
    if isinstance(x,(int,float)) and abs(x) >= 1e6 or (x!=0 and abs(x) < 1e-3):
        return ("%.4g" % x)
    if abs(x - round(x)) < 1e-9: return str(int(round(x)))
    return ("%.4f" % x).rstrip("0").rstrip(".")

_EXPLANATION_1 = [
    {"heading": "What an ellipse orbit means",
     "body": "Planets do not go around in perfect circles. They follow an ellipse \u2014 a "
             "gently stretched circle \u2014 and the Sun sits at one focus, slightly off "
             "centre. For most planets the stretch is small, so the orbit looks nearly "
             "circular, but it is never exact."},
    {"heading": "Why it mattered",
     "body": "For centuries people assumed orbits had to be perfect circles. Kepler showed "
             "the real shape is an ellipse, which finally matched the careful "
             "observations \u2014 a huge step toward modern astronomy."},
]
_EXPLANATION_2 = [
    {"heading": "Equal areas in equal times",
     "body": "Imagine a line joining the Sun to a planet. In any fixed amount of time that "
             "line sweeps out the same area, wherever the planet is. To cover the same "
             "area when it is close to the Sun, the planet must move faster; when far "
             "away, it moves slower."},
    {"heading": "Where you see it",
     "body": "Earth moves fastest in early January, when it is closest to the Sun, and "
             "slowest in July, when it is farthest \u2014 exactly what the second law "
             "predicts."},
]
_EXPLANATION_3 = [
    {"heading": "Period and distance are linked",
     "body": "The third law ties how long a planet takes to orbit (its period T) to how big "
             "its orbit is (the semi-major axis a). Square the period and it is "
             "proportional to the cube of the distance \u2014 so doubling the orbit size "
             "makes the year far more than twice as long."},
    {"heading": "What the constant means",
     "body": "The full form is T\u00b2 = 4\u03c0\u00b2a\u00b3 / (G M), where G is the "
             "gravitational constant and M is the mass of the central body (e.g. the Sun). "
             "Because that constant is fixed for one central body, every planet around the "
             "Sun follows the same T\u00b2-to-a\u00b3 relationship."},
    {"heading": "Units",
     "body": "Here a is in metres, M in kilograms and T comes out in seconds (G = 6.6743 "
             "\u00d7 10\u207b\u00b9\u00b9). The Sun's mass is about 1.989 \u00d7 "
             "10\u00b3\u2070 kg; Earth's orbit has a \u2248 1.496 \u00d7 10\u00b9\u00b9 m."},
]

@register(
    slug="keplers-laws",
    name="Kepler's Laws",
    section="physics",
    topic="Astronomy & Gravitation",
    sub="Orbits",
    order=0,
    summary="Explore Kepler's three laws of planetary motion; the third law solves for orbital period, distance or central mass.",
    formula="T\u00b2 = 4\u03c0\u00b2a\u00b3 / (G M)",
    tags=["kepler", "orbit", "planet", "astronomy", "gravitation", "period", "ellipse"],
    viz_template="viz/keplers-laws.html",
    scholar="johannes-kepler",
    related=["newtons-second-law", "potential-energy"],
)
def compute(mode="third", solve_for="period",
            period=None, axis=1.496e11, mass=1.989e30, **_ignored):
    try:
        md = str(mode or "third").strip().lower()
    except Exception:
        md = "third"

    # Modes 1 and 2 are explanatory (no numeric solve)
    if md in ("first", "1", "1st"):
        return {
            "result": "Kepler's First Law \u2014 elliptical orbits",
            "mode": "first",
            "steps": [
                {"label": "First law", "math": r"\(\text{orbit = ellipse, Sun at one focus}\)",
                 "note": "Orbits are ellipses, not perfect circles."},
            ],
            "explanation": _EXPLANATION_1,
            "law_statement": _LAW1,
            "law_source_name": _LAW_SOURCE_NAME, "law_source_url": _LAW_SOURCE_URL,
            "disclaimer": _DISCLAIMER,
        }
    if md in ("second", "2", "2nd"):
        return {
            "result": "Kepler's Second Law \u2014 equal areas in equal times",
            "mode": "second",
            "steps": [
                {"label": "Second law",
                 "math": r"\(\dfrac{dA}{dt} = \text{constant}\)",
                 "note": "The Sun-planet line sweeps equal areas in equal times."},
            ],
            "explanation": _EXPLANATION_2,
            "law_statement": _LAW2,
            "law_source_name": _LAW_SOURCE_NAME, "law_source_url": _LAW_SOURCE_URL,
            "disclaimer": _DISCLAIMER,
        }

    # Third law — computational
    try:
        sf = str(solve_for or "period").strip().lower()
    except Exception:
        sf = "period"

    def num(v):
        if v is None or v == "":
            return None
        return float(v)

    try:
        T = num(period)
        a = num(axis)
        M = num(mass)
    except (TypeError, ValueError):
        return {"error": "Please enter numbers only.", "steps": [], "disclaimer": _DISCLAIMER}

    out_T, out_a, out_M = T, a, M
    steps = [
        {"label": "Third law", "math": r"\(T^2 = \dfrac{4\pi^2 a^3}{G M}\)",
         "note": "G = 6.6743e-11 N m^2/kg^2."},
    ]
    result = ""

    if sf == "period":
        if a is None or M is None:
            return {"error": "Enter the orbit size (a) and central mass (M) to find the period.",
                    "steps": [], "disclaimer": _DISCLAIMER}
        if a < 0 or M <= 0:
            return {"error": "Orbit size must be positive and mass must be greater than zero.",
                    "steps": [], "disclaimer": _DISCLAIMER}
        out_T = math.sqrt((4 * math.pi**2 * a**3) / (_G * M))
        steps.append({"label": "Substitute",
            "math": r"\(T = \sqrt{\dfrac{4\pi^2 (" + _f(a) + r")^3}{G\,(" + _f(M) + r")}}\)",
            "note": "a in metres, M in kg."})
        steps.append({"label": "Result", "math": r"\(T = " + _f(out_T) + r"\ \text{s}\)",
            "note": "Orbital period in seconds (" + _f(out_T/86400.0) + " days)."})
        result = "Orbital period T = " + _f(out_T) + " s  (" + _f(out_T/86400.0) + " days)"

    elif sf == "axis" or sf == "distance":
        if T is None or M is None:
            return {"error": "Enter the period (T) and central mass (M) to find the orbit size.",
                    "steps": [], "disclaimer": _DISCLAIMER}
        if T < 0 or M <= 0:
            return {"error": "Period must be positive and mass must be greater than zero.",
                    "steps": [], "disclaimer": _DISCLAIMER}
        out_a = ((_G * M * T**2) / (4 * math.pi**2)) ** (1.0/3.0)
        steps.append({"label": "Rearrange", "math": r"\(a = \sqrt[3]{\dfrac{G M T^2}{4\pi^2}}\)",
            "note": "Solve the third law for a."})
        steps.append({"label": "Result", "math": r"\(a = " + _f(out_a) + r"\ \text{m}\)",
            "note": "Semi-major axis (orbit size) in metres."})
        result = "Orbit size a = " + _f(out_a) + " m"

    elif sf == "mass":
        if T is None or a is None:
            return {"error": "Enter the period (T) and orbit size (a) to find the central mass.",
                    "steps": [], "disclaimer": _DISCLAIMER}
        if T <= 0 or a < 0:
            return {"error": "Period must be greater than zero and orbit size must be positive.",
                    "steps": [], "disclaimer": _DISCLAIMER}
        out_M = (4 * math.pi**2 * a**3) / (_G * T**2)
        steps.append({"label": "Rearrange", "math": r"\(M = \dfrac{4\pi^2 a^3}{G T^2}\)",
            "note": "Solve the third law for the central mass."})
        steps.append({"label": "Result", "math": r"\(M = " + _f(out_M) + r"\ \text{kg}\)",
            "note": "Mass of the central body in kilograms."})
        result = "Central mass M = " + _f(out_M) + " kg"

    else:
        return {"error": "Choose what to solve for: period, axis or mass.",
                "steps": [], "disclaimer": _DISCLAIMER}

    return {
        "result": result,
        "mode": "third",
        "solve_for": sf,
        "period": out_T, "axis": out_a, "mass": out_M,
        "G": _G,
        "steps": steps,
        "explanation": _EXPLANATION_3,
        "law_statement": _LAW3,
        "law_source_name": _LAW_SOURCE_NAME,
        "law_source_url": _LAW_SOURCE_URL,
        "disclaimer": _DISCLAIMER,
    }

from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
