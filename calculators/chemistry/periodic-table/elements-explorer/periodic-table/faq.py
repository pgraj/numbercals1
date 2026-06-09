# -*- coding: utf-8 -*-
"""FAQs for the Interactive Periodic Table."""
from core.faqs import register_faqs

register_faqs("periodic-table", [
    {"q": "How do I use this periodic table?",
     "a": ("The full table is always shown. Use the Organic and Inorganic "
           "buttons to highlight those groups of elements, then click any "
           "element to open a popup with a rotatable 3D atomic model and its "
           "details. Drag the model to spin it and scroll to zoom.")},
    {"q": "Why is the 'chemical formula' for an element things like O2 or S8?",
     "a": ("A single element's 'chemical formula' is the form it naturally "
           "takes as a pure substance. Oxygen travels as O2 (two atoms), "
           "sulfur as S8 (eight-atom rings), while metals like iron are written "
           "simply as Fe. Noble gases such as helium are single atoms (He).")},
    {"q": "Are single elements really 'organic' or 'inorganic'?",
     "a": ("Strictly, those words describe compounds, not elements. This tool "
           "uses 'Organic' as a handy label for the elements at the heart of "
           "organic chemistry - hydrogen, carbon, nitrogen, oxygen, phosphorus, "
           "sulfur and the common organic halogens - and 'Inorganic' for the rest.")},
    {"q": "Is the 3D model a real photo of the atom?",
     "a": ("No - atoms are far too small to photograph, and modern physics "
           "describes electrons as fuzzy clouds, not neat orbits. The model is a "
           "Bohr-shell diagram: the electron-shell counts are accurate, but the "
           "circular orbits are an illustration to make the structure clear.")},
    {"q": "Why do some elements say they have no everyday use?",
     "a": ("Many heavy elements past uranium are made only in laboratories, a "
           "few atoms at a time, and survive for less than a second. They are "
           "real and important for science, but they genuinely have no use in "
           "daily life - so the tool says so honestly rather than inventing one.")},
])
