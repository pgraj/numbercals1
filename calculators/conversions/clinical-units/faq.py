from core.faqs import register_faqs

register_faqs("clinical-units", [
    {"q": "Why do lab values need molar mass to convert?",
     "a": "Conventional units (mg/dL) measure mass per volume, while SI units (mmol/L) measure "
          "moles per volume. Bridging them requires the analyte's molar mass: mmol/L = "
          "(mg/dL × 10) ÷ molar mass."},
    {"q": "Can you show a worked example?",
     "a": "Glucose 100 mg/dL with molar mass 180.16 g/mol: (100 × 10) ÷ 180.16 ≈ 5.55 mmol/L — "
          "the familiar normal fasting figure."},
    {"q": "Why is HbA1c handled differently?",
     "a": "HbA1c is reported as a percentage (DCCT/NGSP) or mmol/mol (IFCC), related by a linear "
          "formula rather than a molar mass: mmol/mol = (% − 2.15) × 10.929."},
    {"q": "Which analytes are supported?",
     "a": "Glucose, total cholesterol, LDL, HDL, creatinine, urea/BUN (all via molar mass) and "
          "HbA1c (via the IFCC formula). LDL and HDL share cholesterol's molar mass."},
    {"q": "Can I use this for medical decisions?",
     "a": "No. This is general information only, not medical advice. Reference ranges vary by "
          "laboratory and clinical context — always consult a qualified doctor or accredited "
          "practitioner before acting on any value."},
])
