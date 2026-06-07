"""Real-world worked example: ocean depth from an angled sonar beam's slant range and angle, via sine (Marine Biology)."""
import math

from core.registry import register

DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or system "
    "errors. They are provided for general reference only — always verify results "
    "independently before relying on them for academic or professional decisions."
)


@register(
    slug="rw-ocean-depth",
    name="Ocean depth from angled sonar",
    section="maths",
    sub="Marine Biology",
    topic="Real-World Trigonometry",
    order=0,
    summary=(
        "A worked real-world example: a research vessel's angled sonar beam returns "
        "a slant range at a known beam angle; sine gives the straight-down depth "
        "and cosine the horizontal offset — the geometry of seabed mapping — "
        "shown on an animated underwater scene you can adjust."
    ),
    formula="depth = slant range × sin θ",
    tags=["real life trigonometry", "marine biology", "sonar", "ocean depth", "echo sounding", "sine", "triangulation", "worked example", "trigonometry", "GCSE", "ACARA Year 10"],
    viz_template="viz/rw-ocean-depth.html",
    scholar="hipparchus",
    related=['trig-sin-cos-tan', 'trig-3d-problems'],
)
def compute(slant_range=None, angle_deg=None):
    try:
        def num(x, d=None):
            return d if (x is None or x == "") else float(x)
        slant = num(slant_range, 600.0)   # measured slant distance of the sonar beam, metres
        ang = num(angle_deg, 35.0)        # beam angle below the horizontal
        if slant <= 0:
            return _err("The slant range must be greater than zero.")
        if not (0 < ang < 90):
            return _err("The beam angle must be between 0° and 90°.")
        depth = slant * math.sin(math.radians(ang))
        horiz = slant * math.cos(math.radians(ang))
        steps = [
            {"label": "Set up the beam triangle",
             "math": r"\(\sin\theta = \dfrac{\text{depth}}{\text{slant range}}\)",
             "note": "The angled sonar beam is the hypotenuse; the depth straight down is the opposite side."},
            {"label": "Solve for depth",
             "math": r"\(\text{depth} = %s \times \sin %s^\circ = %s\ \text{m}\)" % (_fmt(slant), _fmt(ang), _fmt(depth)),
             "note": "Vertical depth of the seabed (or shoal) beneath the survey point."},
            {"label": "Horizontal offset",
             "math": r"\(\text{offset} = %s \times \cos %s^\circ = %s\ \text{m}\)" % (_fmt(slant), _fmt(ang), _fmt(horiz)),
             "note": "How far ahead of the vessel the beam hit — useful for mapping."},
        ]
        return {
            "result": _fmt(depth),
            "slant_range": slant, "angle_deg": ang,
            "depth": round(depth, 3), "offset": round(horiz, 3),
            "steps": steps,
            "explanation": [
                {"heading": "The scenario",
                 "body": "A research vessel sends an angled sonar ping that returns after "
                         "travelling %s m, aimed %s° below the horizontal. The straight-down "
                         "depth is recovered from that slant range and angle." % (_fmt(slant), _fmt(ang))},
                {"heading": "Sine for depth, cosine for offset",
                 "body": "The beam is the hypotenuse. Sine (opposite over hypotenuse) gives "
                         "the vertical depth; cosine (adjacent over hypotenuse) gives how far "
                         "ahead of the vessel the seabed point lies."},
                {"heading": "Why it matters",
                 "body": "Marine biologists and hydrographers map seabeds, locate reefs and "
                         "fish shoals, and chart safe channels with angled-beam sonar — the "
                         "same triangle whether the beam points straight down or off to one side."},
                {"heading": "Try it yourself",
                 "body": "Steepen the beam toward 90° and the depth approaches the full "
                         "slant range; flatten it and most of the distance becomes horizontal "
                         "offset instead of depth."},
            ],
            "disclaimer": DISCLAIMER,
        }
    except (TypeError, ValueError):
        return _err("Please enter valid numbers for the slant range and beam angle.")


def _err(msg):
    return {"error": msg, "steps": [], "disclaimer": DISCLAIMER}


def _fmt(x):
    if x is None:
        return ""
    if abs(x - round(x)) < 1e-9:
        return str(int(round(x)))
    return ("%.4f" % x).rstrip("0").rstrip(".")


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
