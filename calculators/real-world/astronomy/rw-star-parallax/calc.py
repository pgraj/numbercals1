"""Real-world worked example: a star's distance from its parallax angle, via the small-angle tangent (Astronomy)."""
import math

from core.registry import register

DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or system "
    "errors. They are provided for general reference only — always verify results "
    "independently before relying on them for academic or professional decisions."
)


@register(
    slug="rw-star-parallax",
    name="Distance to a star by parallax",
    section="real-world",
    sub="Astronomy",
    topic="Real-World Trigonometry",
    order=0,
    summary=(
        "A worked real-world example: as Earth orbits the Sun, a nearby star shifts "
        "against the background by a tiny parallax angle; the tangent of that "
        "angle over a one-AU baseline gives the star's distance in parsecs and "
        "light-years — shown on an animated orbit-and-star scene."
    ),
    formula="distance (pc) = 1 / parallax (arcsec)",
    tags=["real life trigonometry", "astronomy", "parallax", "parsec", "small angle", "stellar distance", "tangent", "worked example", "trigonometry", "A-Level", "ACARA Year 11"],
    viz_template="viz/rw-star-parallax.html",
    scholar="hipparchus",
    related=['trig-sin-cos-tan', 'trig-inverse'],
)
def compute(parallax_arcsec=None):
    try:
        def num(x, d=None):
            return d if (x is None or x == "") else float(x)
        # parallax angle in arcseconds; baseline = 1 AU (Earth-Sun). distance in parsecs/light-years.
        p_arcsec = num(parallax_arcsec, 0.7687)   # ~Alpha Centauri
        if p_arcsec <= 0:
            return _err("The parallax angle must be greater than zero.")
        # distance (parsecs) = 1 / parallax(arcsec); 1 pc = 3.26156 light-years
        d_pc = 1.0 / p_arcsec
        d_ly = d_pc * 3.26156
        # show the underlying small-angle tangent: d = baseline / tan(p)
        p_rad = math.radians(p_arcsec / 3600.0)
        steps = [
            {"label": "The parallax right triangle",
             "math": r"\(\tan p = \dfrac{\text{baseline (1 AU)}}{\text{distance}}\)",
             "note": "As Earth orbits, a nearby star shifts against the far background; half that shift is the parallax angle p, opposite a baseline of one astronomical unit."},
            {"label": "Small-angle shortcut",
             "math": r"\(\text{distance (pc)} = \dfrac{1}{p\,(\text{arcsec})} = \dfrac{1}{%s} = %s\ \text{pc}\)" % (_fmt(p_arcsec), _fmt(d_pc)),
             "note": "For tiny angles tan p ≈ p, which is exactly why the parsec is defined this way."},
            {"label": "Convert to light-years",
             "math": r"\(%s\ \text{pc} \times 3.26156 = %s\ \text{light-years}\)" % (_fmt(d_pc), _fmt(d_ly)),
             "note": "One parsec is about 3.26 light-years."},
        ]
        return {
            "result": _fmt(d_ly),
            "parallax_arcsec": p_arcsec,
            "distance_pc": round(d_pc, 4), "distance_ly": round(d_ly, 4),
            "steps": steps,
            "explanation": [
                {"heading": "The scenario",
                 "body": "Six months apart, astronomers photograph a nearby star from "
                         "opposite ends of Earth's orbit. Against the distant background it "
                         "appears to shift; half that shift is the parallax angle — here %s "
                         "arcseconds. From it, the star's distance follows." % _fmt(p_arcsec)},
                {"heading": "A very thin triangle",
                 "body": "The triangle has a one-AU baseline and a height of light-years, "
                         "so the parallax angle is minute. Tangent still applies, but "
                         "because the angle is so small, tan p ≈ p (in radians) — the basis "
                         "of the parsec ('parallax-second') unit."},
                {"heading": "Why it matters",
                 "body": "Parallax is the first rung of the cosmic distance ladder — the "
                         "only direct, geometry-based way to measure stellar distances, and "
                         "the calibration for every method used farther out."},
                {"heading": "Try it yourself",
                 "body": "Halve the parallax angle and the star doubles its distance — "
                         "smaller shifts mean far more distant stars, which is why only "
                         "nearby stars show a measurable parallax."},
            ],
            "disclaimer": DISCLAIMER,
        }
    except (TypeError, ValueError):
        return _err("Please enter a valid parallax angle in arcseconds.")


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
