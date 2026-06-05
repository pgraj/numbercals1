"""Unit conversion helpers for the Health calculators.

Each physical calculator works internally in CANONICAL units:
    mass   -> kilograms (kg)
    length -> centimetres (cm)

The viz sends the user's chosen unit alongside the raw number; compute()
normalises to canonical units immediately, so every formula, step, and graph
downstream sees a single consistent unit. Display-side labelling is the
template's job; the maths never sees anything but kg and cm.
"""

# ---- mass -> kg ----------------------------------------------------------
_MASS_TO_KG = {
    "kg": 1.0,
    "lb": 0.45359237,
}

# ---- length -> cm --------------------------------------------------------
_LEN_TO_CM = {
    "cm": 1.0,
    "m": 100.0,
    "in": 2.54,
    "ft": 30.48,
}


def to_kg(value: float, unit: str) -> float:
    """Convert a mass in the given unit to kilograms."""
    return float(value) * _MASS_TO_KG.get((unit or "kg").lower(), 1.0)


def to_cm(value: float, unit: str) -> float:
    """Convert a single length in the given unit to centimetres."""
    return float(value) * _LEN_TO_CM.get((unit or "cm").lower(), 1.0)


def to_inches(value: float, unit: str) -> float:
    """Convert a single length in the given unit to inches (for inch-native formulas)."""
    return to_cm(value, unit) / 2.54


def height_to_inches(primary: float, unit: str, secondary: float = 0.0) -> float:
    """Height helper returning inches; ft uses primary=feet, secondary=inches."""
    unit = (unit or "in").lower()
    if unit == "ft":
        return float(primary) * 12.0 + float(secondary)
    return to_inches(primary, unit)


def height_to_cm(primary: float, unit: str, secondary: float = 0.0) -> float:
    """Height helper.

    For ft+in the form sends feet as `primary` and inches as `secondary`;
    for every other unit `secondary` is ignored.
    """
    unit = (unit or "cm").lower()
    if unit == "ft":
        return float(primary) * 30.48 + float(secondary) * 2.54
    return to_cm(primary, unit)


def mass_unit_label(unit: str) -> str:
    return {"kg": "kg", "lb": "lb"}.get((unit or "kg").lower(), "kg")


def length_unit_label(unit: str) -> str:
    return {"cm": "cm", "m": "m", "in": "in", "ft": "ft"}.get((unit or "cm").lower(), "cm")
