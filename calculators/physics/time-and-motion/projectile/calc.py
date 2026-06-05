"""Projectile motion — physics › Time & Motion. Ships its own viz template."""
from math import sin, radians
from core.registry import register


@register(
    slug="projectile",
    name="Projectile motion",
    section="physics",
    sub="Time & Motion",
    tags=["kinematics", "trajectory", "range", "newton"],
    formula="R = v² · sin(2θ) / g",
    summary="Range, peak height, and flight time of a projectile.",
    viz_template="viz/projectile.html",
)
def compute(v: float, theta_deg: float, g: float = 9.81):
    v = float(v); g = float(g); th = radians(float(theta_deg))
    rng = v * v * sin(2 * th) / g
    hgt = v * v * sin(th) ** 2 / (2 * g)
    tim = 2 * v * sin(th) / g
    steps = [
        {"label": "List the known values",
         "math": r"\( v = %g\ \text{m/s},\quad \theta = %g^\circ,\quad g = %g\ \text{m/s}^2 \)"
                 % (v, float(theta_deg), g),
         "note": "Convert the angle to radians before using sine."},
        {"label": "Range — horizontal distance travelled",
         "math": r"\( R = \dfrac{v^2 \sin(2\theta)}{g} = \dfrac{%g^2 \sin(%g^\circ)}{%g} = %.4g\ \text{m} \)"
                 % (v, 2 * float(theta_deg), g, rng)},
        {"label": "Peak height — highest point reached",
         "math": r"\( H = \dfrac{v^2 \sin^2(\theta)}{2g} = %.4g\ \text{m} \)" % hgt},
        {"label": "Flight time — total time in the air",
         "math": r"\( T = \dfrac{2v \sin(\theta)}{g} = %.4g\ \text{s} \)" % tim},
    ]
    return {
        "range": rng,
        "height": hgt,
        "time": tim,
        "steps": steps,
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
