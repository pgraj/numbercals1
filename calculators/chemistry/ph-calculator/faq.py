from core.faqs import register_faqs

register_faqs('ph-calculator', [
    {"q": 'What does pH measure?',
     "a": 'How acidic or basic a solution is, from the hydrogen-ion concentration, on a 0-14 scale. Low pH = acidic, 7 = neutral, high = basic.'},
    {"q": 'Why is the scale logarithmic?',
     "a": 'Because hydrogen-ion concentrations span a huge range. Each whole pH unit is a tenfold change - pH 4 is ten times more acidic than pH 5.'},
    {"q": 'Where does pH matter day to day?',
     "a": 'Blood (must stay near 7.4), stomach acid, soil for plants, pools, shampoo, food and brewing. It is one of the most-measured quantities anywhere.'},
    {"q": 'How does the example give pH 3?',
     "a": '[H⁺] = 10⁻³, and −log(10⁻³) = 3. A thousandth of a mole of H⁺ per litre is acidic, like orange juice.'},
    {"q": 'How do pH and pOH relate?',
     "a": 'In water, pH + pOH = 14. So pH 3 means pOH 11. That is why neutral is pH 7 - exactly half of 14, where H⁺ and OH⁻ are equal.'},
])
