"""
NumberCals — PER-CALCULATOR tests (APPEND-ONLY).

This is the ONLY test file that grows as the site grows. Each calculator gets
one small block here checking its known values and that its page renders.

HOW TO ADD A BLOCK (you do this; I'll hand you the block to paste):
  * Copy one of the examples below.
  * Change the slug, the inputs, and the expected numbers.
  * Paste it at the bottom of this file. Never edit the blocks above.
  * Run:  pytest -q

You never re-upload this file. When I deliver a new calculator I give you a
~6-line block to append here, not a replacement file.
"""

# === EXAMPLE BLOCKS (the three starter calculators) =======================

def test_projectile(reg):
    out = reg.resolve("projectile").compute(v=20, theta_deg=45, g=9.81)
    assert round(out["range"], 2) == 40.77
    assert round(out["time"], 3) == 2.883


def test_projectile_page_renders(client):
    assert client.get("/calc/projectile").status_code == 200


def test_quadratic(reg):
    real = reg.resolve("quadratic").compute(a=1, b=-3, c=2)
    assert sorted([real["root1"], real["root2"]]) == [1.0, 2.0]
    comp = reg.resolve("quadratic").compute(a=1, b=0, c=1)
    assert "i" in str(comp["root1"])


def test_quadratic_has_no_unverified_scholar(client):
    # We removed the speculative Aryabhata link: no scholar attribution unless verified.
    assert "/scholar/" not in client.get("/calc/quadratic").text


def test_quadratic_has_parabola_chart(client):
    page = client.get("/calc/quadratic").text
    assert 'id="quad-chart"' in page
    assert "/api/compute/quadratic" in page


def test_quadratic_nature_classification(reg):
    q = reg.resolve("quadratic")
    assert q.compute(a=1, b=-3, c=2)["nature"] == "two distinct real roots"
    assert q.compute(a=1, b=2, c=1)["nature"] == "one repeated real root"
    assert q.compute(a=1, b=0, c=1)["nature"] == "no real roots (complex)"


def test_compound_interest(reg):
    out = reg.resolve("compound-interest").compute(
        principal=1000, rate_pct=5, years=10, n=12)
    assert out["future_value"] == 1647.01
    assert "series" in out and len(out["series"]) >= 2  # data for the chart


def test_compound_interest_has_interactive_chart(client):
    page = client.get("/calc/compound-interest").text
    assert 'id="ci-chart"' in page          # canvas present
    assert "/api/compute/compound-interest" in page  # wired to compute API


def test_compound_interest_has_no_unverified_scholar(client):
    assert "/scholar/" not in client.get("/calc/compound-interest").text


# === APPEND NEW CALCULATOR BLOCKS BELOW THIS LINE =========================
# (paste blocks I give you here — e.g. Kepler's third law next time)
# === Maths › Arithmetic ====================================================
# APPEND THIS BLOCK to the bottom of tests/test_calculators.py.
# Do NOT replace the file — paste only the lines below.

def test_percentage(reg):
    out = reg.resolve("percentage").compute(whole=200, percent=15)
    assert out["part"] == 30.0
    assert out["rest"] == 170.0
    assert "series" in out and len(out["series"]) == 2


def test_percentage_page_renders(client):
    assert client.get("/calc/percentage").status_code == 200


def test_fraction(reg):
    assert reg.resolve("fraction").compute(num1=1, den1=2, num2=1, den2=3,
                                           op="add")["result"] == "5/6"
    assert reg.resolve("fraction").compute(num1=2, den1=3, num2=3, den2=4,
                                           op="multiply")["result"] == "1/2"


def test_fraction_page_renders(client):
    assert client.get("/calc/fraction").status_code == 200


def test_ratio(reg):
    assert reg.resolve("ratio").compute(a=12, b=18)["simplified"] == "2:3"


def test_ratio_page_renders(client):
    assert client.get("/calc/ratio").status_code == 200


def test_lcm(reg):
    assert reg.resolve("lcm").compute(a=4, b=6)["lcm"] == 12
    assert reg.resolve("lcm").compute(a=21, b=6)["lcm"] == 42


def test_lcm_page_renders(client):
    assert client.get("/calc/lcm").status_code == 200


def test_gcd(reg):
    assert reg.resolve("gcd").compute(a=48, b=36)["gcd"] == 12
    assert reg.resolve("gcd").compute(a=17, b=5)["gcd"] == 1


def test_gcd_page_renders(client):
    assert client.get("/calc/gcd").status_code == 200


def test_arithmetic_scholar_attribution(client):
    # Euclid is verified (Elements Book VII) -> allowed on gcd and lcm.
    assert "/scholar/euclid" in client.get("/calc/gcd").text
    assert "/scholar/euclid" in client.get("/calc/lcm").text
    # No verified scholar for these three -> must carry no attribution.
    for s in ["percentage", "fraction", "ratio"]:
        assert "/scholar/" not in client.get("/calc/" + s).text

# === FAQs for the 3 existing calculators ===================================
# APPEND to the bottom of tests/test_calculators.py. Paste only these lines.
from core import faqs as _faqs


def test_existing_calculators_have_faqs(reg):
    for s in ["projectile", "quadratic", "compound-interest"]:
        assert len(_faqs.faqs_for(s)) >= 3, f"{s} is missing FAQs"


def test_existing_faqs_render_on_page(client):
    # requires the /calc/<slug> route to pass faqs into the template context
    assert "Frequently asked questions" in client.get("/calc/quadratic").text
    
# === Step-by-step working added to 5 calculators ==========================
# APPEND to the bottom of tests/test_calculators.py. Paste only these lines.
# These confirm known values are unchanged AND that steps are now present.

def test_steps_present_and_values_intact(reg):
    o = reg.resolve("compound-interest").compute(principal=1000, rate_pct=5, years=10, n=12)
    assert o["future_value"] == 1647.01 and len(o["series"]) >= 2 and len(o["steps"]) >= 3

    o = reg.resolve("projectile").compute(v=20, theta_deg=45, g=9.81)
    assert round(o["range"], 2) == 40.77 and len(o["steps"]) >= 3

    o = reg.resolve("linear-equation").compute(a=2, b=-6)
    assert o["root"] == 3.0 and len(o["steps"]) >= 3

    o = reg.resolve("logarithm").compute(value=8, base=2)
    assert o["result"] == 3.0 and len(o["steps"]) >= 3

    o = reg.resolve("exponential").compute(a=2, base=3, x=4)
    assert o["result"] == 162.0 and len(o["steps"]) >= 3


def test_steps_empty_on_error(reg):
    # error paths must not crash and should carry an empty steps list
    assert reg.resolve("linear-equation").compute(a=0, b=5)["steps"] == []
    assert reg.resolve("logarithm").compute(value=8, base=1)["steps"] == []
    
# === Accounting (14 calculators) ==========================================
# APPEND to the bottom of tests/test_calculators.py. Paste ONLY these lines.
# Do NOT replace the file. Run:  pytest -q
from core import faqs as _faqs_acct


# --- known compute values --------------------------------------------------

def test_simple_interest(reg):
    o = reg.resolve("simple-interest").compute(principal=1000, rate_pct=5, years=3)
    assert o["interest"] == 150.0
    assert o["amount"] == 1150.0
    assert len(o["steps"]) >= 3


def test_loan_emi(reg):
    o = reg.resolve("loan-emi").compute(principal=100000, rate_pct=12, years=1)
    assert round(o["emi"], 2) == 8884.88
    assert len(o["steps"]) >= 3


def test_mortgage(reg):
    o = reg.resolve("mortgage").compute(home_price=500000, down_payment=100000,
                                        years=30, rate_pct=6,
                                        annual_tax=3000, annual_insurance=1200)
    assert round(o["principal_interest"], 2) == 2398.20
    assert round(o["monthly_tax"], 2) == 250.0
    assert round(o["monthly_insurance"], 2) == 100.0
    assert len(o["steps"]) >= 3


def test_roi(reg):
    o = reg.resolve("roi").compute(cost=1000, current_value=1250)
    assert o["roi_pct"] == 25.0
    assert o["net_return"] == 250.0


def test_cagr(reg):
    o = reg.resolve("cagr").compute(begin_value=10000, end_value=16000, years=4)
    assert round(o["cagr_pct"], 2) == 12.47
    assert len(o["steps"]) >= 3


def test_break_even(reg):
    o = reg.resolve("break-even").compute(fixed_costs=10000, variable_cost=5, price=20)
    assert o["contribution_margin"] == 15.0
    assert round(o["break_even_units"], 2) == 666.67
    assert round(o["break_even_revenue"], 2) == 13333.33
    assert len(o["steps"]) >= 3
    # price must exceed variable cost -> graceful error, empty steps
    err = reg.resolve("break-even").compute(fixed_costs=10000, variable_cost=20, price=5)
    assert "error" in err and err["steps"] == []


def test_profit_margin(reg):
    o = reg.resolve("profit-margin").compute(revenue=100000, cogs=60000,
                                             operating_expenses=20000)
    assert o["gross_margin_pct"] == 40.0
    assert o["net_margin_pct"] == 20.0
    assert o["gross_profit"] == 40000.0


def test_discount(reg):
    o = reg.resolve("discount").compute(original_price=200, discount_pct=25, tax_pct=10)
    assert o["savings"] == 50.0
    assert o["final_price"] == 165.0


def test_investment_growth(reg):
    o = reg.resolve("investment-growth").compute(principal=10000, annual_contribution=10000,
                                                 rate_pct=7, years=18)
    assert o["total_contributions"] == 180000.0
    assert "series" in o and len(o["series"]) >= 2
    assert len(o["steps"]) >= 3


def test_future_value(reg):
    o = reg.resolve("future-value").compute(present_value=5000, rate_pct=6, periods=10)
    assert round(o["future_value"], 2) == 8954.24


def test_dividend(reg):
    o = reg.resolve("dividend").compute(stock_price=50, shares=100, yield_pct=4,
                                        years=5, reinvest="No")
    assert o["annual_income"] == 400.0
    drip = reg.resolve("dividend").compute(stock_price=50, shares=100, yield_pct=4,
                                           years=5, reinvest="Yes")
    assert drip["final_value"] > o["final_value"]


def test_sip(reg):
    o = reg.resolve("sip").compute(monthly_investment=100, rate_pct=12, years=5)
    assert o["total_invested"] == 6000.0
    assert o["future_value"] > o["total_invested"]
    assert len(o["steps"]) >= 3


def test_amortization(reg):
    o = reg.resolve("amortization").compute(amount=300000, rate_pct=6, years=30)
    assert round(o["emi"], 2) == 1798.65
    assert len(o["series"]) == 30
    assert len(o["steps"]) >= 3


def test_interest_rate(reg):
    o = reg.resolve("interest-rate").compute(principal=1000, maturity_amount=1500, years=5)
    assert round(o["rate_pct"], 2) == 8.45
    assert len(o["steps"]) >= 3


def test_property_value_simple(reg):
    o = reg.resolve("property-value").compute(price=600000, appreciation_pct=5,
                                              years=10, inflation_pct=3, mode="simple")
    assert round(o["nominal_value"]) == round(600000 * 1.05 ** 10)
    assert round(o["real_value"]) == round(600000 * 1.05 ** 10 / 1.03 ** 10)
    assert o["real_value"] < o["nominal_value"]
    assert len(o["series"]) == 11 and o["series"][0]["nominal"] == 600000
    assert len(o["steps"]) >= 3


def test_property_value_scenarios(reg):
    o = reg.resolve("property-value").compute(price=600000, appreciation_pct=5,
                                              years=10, mode="scenarios")
    b = o["scenarios"]
    assert b["low"]["rate_pct"] == 3.0
    assert b["avg"]["rate_pct"] == 5.0
    assert b["high"]["rate_pct"] == 7.0
    assert b["high"]["nominal_value"] > b["avg"]["nominal_value"] > b["low"]["nominal_value"]


def test_property_value_mortgage(reg):
    o = reg.resolve("property-value").compute(price=600000, appreciation_pct=5,
                                              years=10, inflation_pct=3, mode="mortgage",
                                              deposit=120000, loan_rate_pct=6, loan_years=30)
    assert o["loan"] == 480000.0
    assert 2870 < o["monthly_repayment"] < 2886
    assert 0 < o["loan_balance"] < 480000
    assert o["equity"] == round(o["nominal_value"] - o["loan_balance"], 2)
    assert o["roi_on_deposit_pct"] is not None
    assert len(o["steps"]) >= 4
    # zero deposit -> ROI undefined, not a crash
    z = reg.resolve("property-value").compute(price=500000, appreciation_pct=4,
                                              years=5, mode="mortgage", deposit=0)
    assert z["roi_on_deposit_pct"] is None


def test_property_value_bad_mode_falls_back(reg):
    o = reg.resolve("property-value").compute(price=500000, appreciation_pct=4,
                                              years=5, mode="garbage")
    assert o["mode"] == "simple"


# --- pages render ----------------------------------------------------------

def test_accounting_pages_render(client):
    for s in ["simple-interest", "loan-emi", "mortgage", "roi", "cagr",
              "break-even", "profit-margin", "discount", "investment-growth",
              "future-value", "dividend", "sip", "amortization", "interest-rate", "property-value"]:
        assert client.get("/calc/" + s).status_code == 200, s


# --- each calculator carries FAQs -----------------------------------------

def test_accounting_calculators_have_faqs(reg):
    for s in ["simple-interest", "loan-emi", "mortgage", "roi", "cagr",
              "break-even", "profit-margin", "discount", "investment-growth",
              "future-value", "dividend", "sip", "amortization", "interest-rate", "property-value"]:
        assert len(_faqs_acct.faqs_for(s)) >= 3, f"{s} is missing FAQs"


# --- no unverified scholar attribution on any of the 14 -------------------

def test_accounting_have_no_unverified_scholar(client):
    for s in ["simple-interest", "loan-emi", "mortgage", "roi", "cagr",
              "break-even", "profit-margin", "discount", "investment-growth",
              "future-value", "dividend", "sip", "amortization", "interest-rate", "property-value"]:
        assert "/scholar/" not in client.get("/calc/" + s).text, s

# === Health (8 calculators) ===============================================
# APPEND to the bottom of tests/test_calculators.py. Paste ONLY these lines.
# Do NOT replace the file. Fixtures reg + client come from conftest.
# Run:  pytest -q
# === Health (8 calculators) ===============================================
# APPEND to the bottom of tests/test_calculators.py. Paste ONLY these lines.
# Do NOT replace the file. Fixtures reg + client come from conftest.
# Run:  pytest -q
from core import faqs as _faqs_health


# --- known compute values --------------------------------------------------

def test_bmi(reg):
    o = reg.resolve("bmi").compute(weight_kg=70, height_cm=175)
    assert o["bmi"] == 22.9
    assert o["status"] == "Normal"
    assert len(o["bands"]) == 4 and len(o["steps"]) >= 3
    # band edges line up with WHO cut-offs
    assert reg.resolve("bmi").compute(weight_kg=50, height_cm=175)["status"] == "Underweight"
    assert reg.resolve("bmi").compute(weight_kg=85, height_cm=175)["status"] == "Overweight"
    assert reg.resolve("bmi").compute(weight_kg=100, height_cm=175)["status"] == "Obese"


def test_bmi_bad_input(reg):
    assert reg.resolve("bmi").compute(weight_kg=0, height_cm=175)["steps"] == []


def test_bmr_mifflin(reg):
    # male: 10*80 + 6.25*180 - 5*30 + 5 = 1780
    assert reg.resolve("bmr").compute(sex="male", age=30, weight_kg=80, height_cm=180)["bmr"] == 1780
    # female: same minus 161 = 1614
    assert reg.resolve("bmr").compute(sex="female", age=30, weight_kg=80, height_cm=180)["bmr"] == 1614
    # other: midpoint = 1697
    assert reg.resolve("bmr").compute(sex="other", age=30, weight_kg=80, height_cm=180)["bmr"] == 1697


def test_tdee(reg):
    o = reg.resolve("tdee").compute(sex="male", age=30, weight_kg=80, height_cm=180, activity="moderate")
    assert o["bmr"] == 1780
    assert o["tdee"] == 2759          # 1780 * 1.55
    assert o["active"] == 979
    assert len(o["steps"]) >= 3
    # unknown activity falls back to sedentary, never crashes
    assert reg.resolve("tdee").compute(sex="male", age=30, weight_kg=80,
                                       height_cm=180, activity="garbage")["factor"] == 1.2


def test_body_fat_navy(reg):
    # male: 86.010*log10(34-15) - 70.041*log10(70) + 36.76 ≈ 17.5
    o = reg.resolve("body-fat").compute(sex="male", weight_kg=80, height_in=70,
                                        waist_in=34, neck_in=15)
    assert o["body_fat_pct"] == 17.5
    assert round(o["fat_mass_kg"] + o["lean_mass_kg"], 1) == 80.0
    assert len(o["steps"]) >= 3
    # female needs hip -> graceful error
    err = reg.resolve("body-fat").compute(sex="female", weight_kg=70, height_in=66,
                                          waist_in=32, neck_in=14)
    assert "error" in err and err["steps"] == []
    # impossible geometry -> graceful error, not a math crash
    bad = reg.resolve("body-fat").compute(sex="male", weight_kg=70, height_in=70,
                                          waist_in=15, neck_in=15)
    assert "error" in bad and bad["steps"] == []


def test_ideal_weight_devine(reg):
    # male 5ft10in: 50 + 2.3*10 = 73.0
    o = reg.resolve("ideal-weight").compute(sex="male", height_ft=5, height_in=10,
                                            current_weight_kg=78)
    assert o["ideal_kg"] == 73.0
    assert o["low_kg"] < o["ideal_kg"] < o["high_kg"]
    assert o["relation"] in ("below", "within", "above")
    # female base is lower
    assert reg.resolve("ideal-weight").compute(sex="female", height_ft=5,
                                               height_in=10)["ideal_kg"] == 68.5


def test_calorie_target_guardrails(reg):
    # maintain: target == tdee, shown as a range, not floored
    o = reg.resolve("calorie-target").compute(tdee=2400, sex="male", goal="maintain")
    assert o["target"] == 2400
    assert o["range_low"] == 2300 and o["range_high"] == 2500
    assert o["floored"] is False
    assert sum(m["kcal"] for m in o["macros"]) == 2400
    assert o["advisory"]            # advisory text is always present
    # safe floor enforced (female): 1600 - 500 = 1100 -> raised to 1200, flagged
    f = reg.resolve("calorie-target").compute(tdee=1600, sex="female", goal="lose")
    assert f["target"] == 1200 and f["floored"] is True
    # safe floor enforced (male): 1800 - 500 = 1300 -> raised to 1500
    m = reg.resolve("calorie-target").compute(tdee=1800, sex="male", goal="lose")
    assert m["target"] == 1500 and m["floored"] is True
    # no tdee -> graceful error
    assert reg.resolve("calorie-target").compute(tdee=0)["steps"] == []


def test_water_intake(reg):
    # 70kg, 30min, spring: 70*0.033 + (30/30)*0.35 = 2.66 (spring multiplier 1.0)
    o = reg.resolve("water-intake").compute(weight_kg=70, exercise_min=30, climate="spring")
    assert o["litres"] == 2.66
    assert o["ounces"] == 90        # 2.66 * 33.814 ≈ 90
    assert len(o["steps"]) >= 3
    # summer scales up
    summer = reg.resolve("water-intake").compute(weight_kg=70, exercise_min=30, climate="summer")
    assert summer["litres"] > o["litres"]
    assert reg.resolve("water-intake").compute(weight_kg=0, exercise_min=30)["steps"] == []


def test_heart_rate_zones(reg):
    # age 35 -> max 185, simple % of max when no resting HR
    o = reg.resolve("heart-rate-zones").compute(age=35, resting_hr=0)
    assert o["max_hr"] == 185
    assert o["method"] == "Percentage of max"
    assert len(o["zones"]) == 5
    assert o["zones"][0]["label"] == "Warm up" and o["zones"][-1]["label"] == "Red line"
    # Karvonen: HRR = 185-60 = 125; aerobic low 70% -> 125*0.7 + 60 = 147.5 -> 148
    k = reg.resolve("heart-rate-zones").compute(age=35, resting_hr=60)
    assert k["method"] == "Karvonen"
    aerobic = [z for z in k["zones"] if z["label"] == "Aerobic"][0]
    assert aerobic["low_bpm"] == 148
    assert reg.resolve("heart-rate-zones").compute(age=200)["steps"] == []


# --- pages render ----------------------------------------------------------

def test_health_pages_render(client):
    for s in ["bmi", "bmr", "tdee", "body-fat", "ideal-weight",
              "calorie-target", "water-intake", "heart-rate-zones"]:
        assert client.get("/calc/" + s).status_code == 200, s


# --- each carries FAQs -----------------------------------------------------

def test_health_calculators_have_faqs(reg):
    for s in ["bmi", "bmr", "tdee", "body-fat", "ideal-weight",
              "calorie-target", "water-intake", "heart-rate-zones"]:
        assert len(_faqs_health.faqs_for(s)) >= 3, f"{s} is missing FAQs"


# --- scholar attribution: only the two with a verified scholar link --------

def test_health_scholar_attribution(client, reg):
    # BMR -> Mifflin-St Jeor, HR -> Karvonen; both pages link out.
    assert "/scholar/mifflin-st-jeor" in client.get("/calc/bmr").text
    assert "/scholar/karvonen" in client.get("/calc/heart-rate-zones").text
    # the remaining six must NOT invent a scholar link.
    for s in ["bmi", "tdee", "body-fat", "ideal-weight",
              "calorie-target", "water-intake"]:
        assert "/scholar/" not in client.get("/calc/" + s).text, s


# === Health batch — v2 additions (units, status, seasons, scholars) ========
# APPEND these to the same file. They cover the second-round changes.

def test_units_weight_and_height(reg):
    # BMI: 154 lb + 5ft9in should match ~70kg / 175cm result closely
    metric = reg.resolve("bmi").compute(weight_kg=70, height_cm=175)["bmi"]
    imperial = reg.resolve("bmi").compute(
        weight_kg=154, weight_unit="lb",
        height_cm=5, height_unit="ft", height_in2=9)["bmi"]
    assert abs(metric - imperial) < 0.5
    # metres path
    assert reg.resolve("bmi").compute(weight_kg=70, height_cm=1.75, height_unit="m")["bmi"] == 22.9
    # BMR accepts units too and matches the canonical kg/cm answer
    a = reg.resolve("bmr").compute(sex="male", age=30, weight_kg=80, height_cm=180)["bmr"]
    b = reg.resolve("bmr").compute(sex="male", age=30,
                                   weight_kg=176.37, weight_unit="lb",
                                   height_cm=180, height_unit="cm")["bmr"]
    assert abs(a - b) <= 1


def test_body_fat_unit_conversions(reg):
    # inches-native vs cm-entered should land within rounding of each other
    inch = reg.resolve("body-fat").compute(sex="male", weight_kg=80, height_in=70,
                                           waist_in=34, neck_in=15)["body_fat_pct"]
    cm = reg.resolve("body-fat").compute(sex="male", weight_kg=80,
                                         height_in=177.8, height_unit="cm",
                                         waist_in=86.36, neck_in=38.1,
                                         length_unit="cm")["body_fat_pct"]
    assert abs(inch - cm) < 0.6


def test_ideal_weight_status_verdict(reg):
    # within healthy band -> Normal
    o = reg.resolve("ideal-weight").compute(sex="male", height_ft=5, height_in=10,
                                            current_weight_kg=73)
    assert o["status"] == "Normal"
    assert o["bmi"] is not None
    # very high weight -> Obese verdict
    hi = reg.resolve("ideal-weight").compute(sex="male", height_ft=5, height_in=10,
                                             current_weight_kg=110)
    assert hi["status"] == "Obese"
    # no current weight -> no status, still returns ideal
    none = reg.resolve("ideal-weight").compute(sex="male", height_ft=5, height_in=10)
    assert none["status"] is None and none["ideal_kg"] == 73.0
    # current weight accepts lb
    lb = reg.resolve("ideal-weight").compute(sex="male", height_ft=5, height_in=10,
                                             current_weight_kg=161, weight_unit="lb")
    assert lb["current_kg"] == 73.0


def test_water_seasons(reg):
    base = reg.resolve("water-intake").compute(weight_kg=70, exercise_min=30, climate="spring")["litres"]
    summer = reg.resolve("water-intake").compute(weight_kg=70, exercise_min=30, climate="summer")["litres"]
    winter = reg.resolve("water-intake").compute(weight_kg=70, exercise_min=30, climate="winter")["litres"]
    hot = reg.resolve("water-intake").compute(weight_kg=70, exercise_min=30, climate="hot_humid")["litres"]
    assert winter < base < summer < hot
    # weight unit works
    lb = reg.resolve("water-intake").compute(weight_kg=154, weight_unit="lb",
                                             exercise_min=30, climate="spring")["litres"]
    assert abs(lb - base) < 0.05
    # unknown climate falls back to spring, never crashes
    assert reg.resolve("water-intake").compute(weight_kg=70, climate="zzz")["litres"] > 0


def test_disclaimer_on_every_health_calc(reg):
    cases = {
        "bmi": dict(weight_kg=70, height_cm=175),
        "bmr": dict(sex="male", age=30, weight_kg=80, height_cm=180),
        "tdee": dict(sex="male", age=30, weight_kg=80, height_cm=180, activity="moderate"),
        "body-fat": dict(sex="male", weight_kg=80, height_in=70, waist_in=34, neck_in=15),
        "ideal-weight": dict(sex="male", height_ft=5, height_in=10, current_weight_kg=78),
        "calorie-target": dict(tdee=2400, sex="male", goal="maintain"),
        "water-intake": dict(weight_kg=70, exercise_min=30, climate="spring"),
        "heart-rate-zones": dict(age=35, resting_hr=60),
    }
    for slug, kw in cases.items():
        out = reg.resolve(slug).compute(**kw)
        assert out.get("disclaimer"), f"{slug} missing disclaimer"
        assert "professional" in out["disclaimer"].lower()


def test_scholars_registered_and_linked(reg):
    slugs = {s.slug for s in reg.all_scholars()}
    assert "mifflin-st-jeor" in slugs
    assert "karvonen" in slugs
    assert reg.resolve("bmr").scholar == "mifflin-st-jeor"
    assert reg.resolve("heart-rate-zones").scholar == "karvonen"

# ============================================================================
# TRIGONOMETRY — STAGE 1 (Foundations + Right-Angle Trig)  [append-only block]
# Added by the Stage 1 build. Known-value checks + contract checks. These import
# each calc module directly and exercise compute(); they do not require a server.
# Safe to append to the existing tests/test_calculators.py.
# ============================================================================
import importlib.util as _ilu
import pathlib as _pl
import math as _math

_TRIG_BASE = _pl.Path(__file__).resolve().parent.parent / "calculators" / "maths" / "trigonometry"

_TRIG_CALCS = {
    "trig-angles": "foundations/trig-angles",
    "trig-pythagoras": "foundations/trig-pythagoras",
    "trig-similar-triangles": "foundations/trig-similar-triangles",
    "trig-intro-ratios": "foundations/trig-intro-ratios",
    "trig-sin-cos-tan": "right-angle-trigonometry/trig-sin-cos-tan",
    "trig-inverse": "right-angle-trigonometry/trig-inverse",
    "trig-elevation-depression": "right-angle-trigonometry/trig-elevation-depression",
    "trig-bearing-navigation": "right-angle-trigonometry/trig-bearing-navigation",
    "trig-area-triangle": "right-angle-trigonometry/trig-area-triangle",
    "trig-3d-problems": "right-angle-trigonometry/trig-3d-problems",
}


def _load_trig(slug):
    path = _TRIG_BASE / _TRIG_CALCS[slug] / "calc.py"
    spec = _ilu.spec_from_file_location("trig_" + slug.replace("-", "_"), path)
    mod = _ilu.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _approx(a, b, tol=1e-2):
    return a is not None and abs(a - b) < tol


# ---- known-value checks (the hand-worked examples from the build) ----------

def test_trig_pythagoras_known():
    m = _load_trig("trig-pythagoras")
    assert _approx(m.compute(a=3, b=4, solve_for="c")["result"], 5)
    assert _approx(m.compute(b=4, c=5, solve_for="a")["result"], 3)
    assert _approx(m.compute(a=5, c=13, solve_for="b")["result"], 12)


def test_trig_angles_known():
    m = _load_trig("trig-angles")
    assert m.compute(angle_deg=135)["kind"] == "obtuse"
    assert m.compute(angle_deg=90)["kind"] == "right"
    assert m.compute(angle_deg=270)["kind"] == "reflex"
    assert _approx(m.compute(angle_deg=30)["complement"], 60)


def test_trig_similar_known():
    m = _load_trig("trig-similar-triangles")
    assert _approx(m.compute(a1=3, a2=6, b1=4)["b2"], 8)


def test_trig_intro_ratios_known():
    m = _load_trig("trig-intro-ratios")
    r = m.compute(opp=3, adj=4, hyp=5)
    assert _approx(r["sin"], 0.6) and _approx(r["cos"], 0.8) and _approx(r["tan"], 0.75)
    assert _approx(m.compute(opp=3, adj=4)["hyp"], 5)  # derives hypotenuse


def test_trig_sin_cos_tan_known():
    m = _load_trig("trig-sin-cos-tan")
    assert _approx(m.compute(angle_deg=30, known_type="hyp", known_val=10, want_type="opp")["value"], 5)
    assert _approx(m.compute(angle_deg=45, known_type="adj", known_val=10, want_type="opp")["value"], 10)


def test_trig_inverse_known():
    m = _load_trig("trig-inverse")
    assert _approx(m.compute(side1=5, side1_type="opp", side2=10, side2_type="hyp")["angle"], 30)
    assert _approx(m.compute(side1=5, side1_type="opp", side2=5, side2_type="adj")["angle"], 45)


def test_trig_elevation_known():
    m = _load_trig("trig-elevation-depression")
    assert _approx(m.compute(angle_deg=40, distance=50, find="height")["height"], 41.955, 1e-2)
    assert _approx(m.compute(height=41.955, distance=50, find="angle")["angle"], 40, 1e-2)


def test_trig_bearing_known():
    m = _load_trig("trig-bearing-navigation")
    r = m.compute(east=10, north=10)
    assert _approx(r["bearing"], 45) and r["result"] == "045\u00b0"
    assert _approx(r["distance"], 14.1421, 1e-3)
    assert _approx(m.compute(east=0, north=-5)["bearing"], 180)


def test_trig_area_known():
    m = _load_trig("trig-area-triangle")
    assert _approx(m.compute(a=6, b=8, angle_C=30)["area"], 12)


def test_trig_3d_known():
    m = _load_trig("trig-3d-problems")
    r = m.compute(length=3, width=4, height=12)
    assert _approx(r["space_diag"], 13) and _approx(r["base_diag"], 5)
    assert _approx(r["angle"], 67.38, 1e-2)


# ---- contract checks (success carries disclaimer+steps; errors never raise) -

def test_trig_compute_contract():
    good_args = {
        "trig-angles": dict(angle_deg=45),
        "trig-pythagoras": dict(a=3, b=4, solve_for="c"),
        "trig-similar-triangles": dict(a1=3, a2=6, b1=4),
        "trig-intro-ratios": dict(opp=3, adj=4, hyp=5),
        "trig-sin-cos-tan": dict(angle_deg=30, known_type="hyp", known_val=10, want_type="opp"),
        "trig-inverse": dict(side1=5, side1_type="opp", side2=10, side2_type="hyp"),
        "trig-elevation-depression": dict(angle_deg=40, distance=50, find="height"),
        "trig-bearing-navigation": dict(east=10, north=10),
        "trig-area-triangle": dict(a=6, b=8, angle_C=30),
        "trig-3d-problems": dict(length=3, width=4, height=12),
    }
    for slug in _TRIG_CALCS:
        m = _load_trig(slug)
        r = m.compute(**good_args[slug])
        assert "disclaimer" in r and r["disclaimer"]
        assert isinstance(r.get("steps"), list) and len(r["steps"]) >= 1
        for st in r["steps"]:
            assert {"label", "math", "note"} <= set(st)
        # error path: empty call must not raise and must return the error shape
        e = m.compute()
        assert "error" in e and e.get("steps") == [] and "disclaimer" in e

# ============================================================================
# TRIGONOMETRY — STAGE 2 (Functions & Graphs + Non-Right-Angle Trig)
# [append-only block]
# Added by the Stage 2 build. Known-value checks + contract checks. These import
# each calc module directly and exercise compute(); they do not require a server.
# Safe to append to the existing tests/test_calculators.py.
# ============================================================================
import importlib.util as _ilu2
import pathlib as _pl2
import math as _math2

_TRIG2_BASE = _pl2.Path(__file__).resolve().parent.parent / "calculators" / "maths" / "trigonometry"

_TRIG2_CALCS = {
    # Trigonometric Functions & Graphs
    "trig-unit-circle": "trigonometric-functions-and-graphs/trig-unit-circle",
    "trig-radians": "trigonometric-functions-and-graphs/trig-radians",
    "trig-sine-graph": "trigonometric-functions-and-graphs/trig-sine-graph",
    "trig-cosine-graph": "trigonometric-functions-and-graphs/trig-cosine-graph",
    "trig-tangent-graph": "trigonometric-functions-and-graphs/trig-tangent-graph",
    "trig-transformations": "trigonometric-functions-and-graphs/trig-transformations",
    "trig-period-amplitude": "trigonometric-functions-and-graphs/trig-period-amplitude",
    # Non-Right-Angle Trigonometry
    "trig-sine-rule": "non-right-angle-trigonometry/trig-sine-rule",
    "trig-cosine-rule": "non-right-angle-trigonometry/trig-cosine-rule",
    "trig-ambiguous-case": "non-right-angle-trigonometry/trig-ambiguous-case",
    "trig-sine-rule-area": "non-right-angle-trigonometry/trig-sine-rule-area",
    "trig-heron": "non-right-angle-trigonometry/trig-heron",
}


def _load_trig2(slug):
    path = _TRIG2_BASE / _TRIG2_CALCS[slug] / "calc.py"
    spec = _ilu2.spec_from_file_location("trig2_" + slug.replace("-", "_"), path)
    mod = _ilu2.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _approx2(a, b, tol=1e-2):
    return a is not None and abs(a - b) < tol


_DISCLAIMER2 = "These values are estimates"


# ---- known-value checks (the hand-worked examples from the build) ----------

def test_trig2_unit_circle_60():
    r = _load_trig2("trig-unit-circle").compute(angle_deg=60)
    assert _approx2(r["cos"], 0.5)
    assert _approx2(r["sin"], 0.866025)
    assert "Quadrant I" in r["quadrant"]


def test_trig2_unit_circle_tan_undefined_at_90():
    r = _load_trig2("trig-unit-circle").compute(angle_deg=90)
    assert r["tan"] is None


def test_trig2_radians_180_is_pi():
    r = _load_trig2("trig-radians").compute(value=180, direction="deg2rad")
    assert _approx2(r["radians"], _math2.pi)
    assert "pi" in r["result"]


def test_trig2_radians_reverse():
    r = _load_trig2("trig-radians").compute(value=_math2.pi, direction="rad2deg")
    assert _approx2(r["degrees"], 180)


def test_trig2_sine_graph_30():
    r = _load_trig2("trig-sine-graph").compute(angle_deg=30)
    assert _approx2(r["y"], 0.5)
    assert r["amplitude"] == 1 and r["period_deg"] == 360


def test_trig2_cosine_graph_60():
    r = _load_trig2("trig-cosine-graph").compute(angle_deg=60)
    assert _approx2(r["y"], 0.5)


def test_trig2_cosine_graph_starts_at_one():
    r = _load_trig2("trig-cosine-graph").compute(angle_deg=0)
    assert _approx2(r["y"], 1.0)


def test_trig2_tangent_graph_45():
    r = _load_trig2("trig-tangent-graph").compute(angle_deg=45)
    assert _approx2(r["y"], 1.0)


def test_trig2_tangent_graph_undefined_at_90():
    r = _load_trig2("trig-tangent-graph").compute(angle_deg=90)
    assert r.get("undefined") is True
    assert r["y"] is None


def test_trig2_transformations_eval():
    r = _load_trig2("trig-transformations").compute(A=2, B=1, C=0, D=0, x_deg=90)
    assert _approx2(r["y"], 2.0)
    assert _approx2(r["amplitude"], 2) and _approx2(r["period_deg"], 360)


def test_trig2_transformations_period_from_B():
    r = _load_trig2("trig-transformations").compute(A=3, B=2, C=0, D=0, x_deg=45)
    assert _approx2(r["period_deg"], 180)


def test_trig2_period_amplitude():
    r = _load_trig2("trig-period-amplitude").compute(A=3, B=2)
    assert _approx2(r["amplitude"], 3)
    assert _approx2(r["period_deg"], 180)


def test_trig2_sine_rule_find_side():
    r = _load_trig2("trig-sine-rule").compute(
        mode="side", known_side=7, known_angle=30, other_angle=45)
    assert _approx2(r["value"], 9.8995, 1e-2)


def test_trig2_sine_rule_find_angle():
    r = _load_trig2("trig-sine-rule").compute(
        mode="angle", known_side=7, known_angle=30, other_side=5)
    assert _approx2(r["value"], 20.92, 1e-1)


def test_trig2_cosine_rule_find_side():
    r = _load_trig2("trig-cosine-rule").compute(mode="side", a=5, b=7, angle_C=60)
    assert _approx2(r["value"], 6.245, 1e-2)


def test_trig2_cosine_rule_sss_right_angle():
    r = _load_trig2("trig-cosine-rule").compute(mode="angle", a=3, b=4, c=5)
    assert _approx2(r["value"], 90.0)


def test_trig2_ambiguous_two_triangles():
    r = _load_trig2("trig-ambiguous-case").compute(a=6, b=8, A=30)
    assert r["count"] == 2


def test_trig2_ambiguous_one_triangle():
    r = _load_trig2("trig-ambiguous-case").compute(a=10, b=8, A=30)
    assert r["count"] == 1


def test_trig2_ambiguous_no_triangle():
    r = _load_trig2("trig-ambiguous-case").compute(a=2, b=8, A=80)
    assert r["count"] == 0


def test_trig2_sine_rule_area():
    r = _load_trig2("trig-sine-rule-area").compute(a=8, b=11, angle_C=37)
    assert _approx2(r["area"], 26.48, 1e-1)


def test_trig2_heron_345():
    r = _load_trig2("trig-heron").compute(a=3, b=4, c=5)
    assert _approx2(r["area"], 6.0)
    assert _approx2(r["s"], 6.0)


# ---- contract checks (apply to every Stage 2 calculator) -------------------

_TRIG2_VALID_ARGS = {
    "trig-unit-circle": dict(angle_deg=60),
    "trig-radians": dict(value=180, direction="deg2rad"),
    "trig-sine-graph": dict(angle_deg=30),
    "trig-cosine-graph": dict(angle_deg=60),
    "trig-tangent-graph": dict(angle_deg=45),
    "trig-transformations": dict(A=2, B=1, C=0, D=0, x_deg=90),
    "trig-period-amplitude": dict(A=3, B=2),
    "trig-sine-rule": dict(mode="side", known_side=7, known_angle=30, other_angle=45),
    "trig-cosine-rule": dict(mode="side", a=5, b=7, angle_C=60),
    "trig-ambiguous-case": dict(a=6, b=8, A=30),
    "trig-sine-rule-area": dict(a=8, b=11, angle_C=37),
    "trig-heron": dict(a=3, b=4, c=5),
}


def test_trig2_all_success_contract():
    for slug, args in _TRIG2_VALID_ARGS.items():
        r = _load_trig2(slug).compute(**args)
        assert "error" not in r, slug
        assert isinstance(r.get("steps"), list) and r["steps"], slug
        for s in r["steps"]:
            assert {"label", "math", "note"} <= set(s), slug
        assert r.get("disclaimer", "").startswith(_DISCLAIMER2), slug


def test_trig2_all_error_contract():
    # Calling with no/invalid arguments should return a clean error, never raise.
    # A few calcs have valid defaults for every parameter, so they are given
    # explicitly invalid input instead of an empty call.
    _bad_args = {
        "trig-transformations": dict(B=0),       # zero B -> infinite period
        "trig-period-amplitude": dict(B=0),      # zero B -> infinite period
    }
    for slug in _TRIG2_CALCS:
        r = _load_trig2(slug).compute(**_bad_args.get(slug, {}))
        assert "error" in r, slug
        assert r.get("steps") == [], slug
        assert r.get("disclaimer", "").startswith(_DISCLAIMER2), slug


def test_trig2_all_json_safe():
    import json as _json2
    for slug, args in _TRIG2_VALID_ARGS.items():
        r = _load_trig2(slug).compute(**args)
        _json2.dumps(r)  # must not raise
# ============================================================================
# TRIGONOMETRY — STAGE 1 (Foundations + Right-Angle Trig)  [append-only block]
# Added by the Stage 1 build. Known-value checks + contract checks. These import
# each calc module directly and exercise compute(); they do not require a server.
# Safe to append to the existing tests/test_calculators.py.
# ============================================================================
import importlib.util as _ilu
import pathlib as _pl
import math as _math

_TRIG_BASE = _pl.Path(__file__).resolve().parent.parent / "calculators" / "maths" / "trigonometry"

_TRIG_CALCS = {
    "trig-angles": "foundations/trig-angles",
    "trig-pythagorean-identity": "foundations/trig-pythagorean-identity",
    "trig-similar-triangles": "foundations/trig-similar-triangles",
    "trig-intro-ratios": "foundations/trig-intro-ratios",
    "trig-sin-cos-tan": "right-angle-trigonometry/trig-sin-cos-tan",
    "trig-inverse": "right-angle-trigonometry/trig-inverse",
    "trig-elevation-depression": "right-angle-trigonometry/trig-elevation-depression",
    "trig-bearing-navigation": "right-angle-trigonometry/trig-bearing-navigation",
    "trig-area-triangle": "right-angle-trigonometry/trig-area-triangle",
    "trig-3d-problems": "right-angle-trigonometry/trig-3d-problems",
}


def _load_trig(slug):
    path = _TRIG_BASE / _TRIG_CALCS[slug] / "calc.py"
    spec = _ilu.spec_from_file_location("trig_" + slug.replace("-", "_"), path)
    mod = _ilu.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _approx(a, b, tol=1e-2):
    return a is not None and abs(a - b) < tol


# ---- known-value checks (the hand-worked examples from the build) ----------

def test_trig_pythagorean_identity_known():
    # Pythagoras' theorem moved to the Geometry section (slug geo-pythagoras,
    # covered in the Stage 3 tests). Foundations now hosts the Pythagorean
    # identity sin^2 + cos^2 = 1 instead.
    m = _load_trig("trig-pythagorean-identity")
    assert _approx(m.compute(mode="verify", angle_deg=37)["sum"], 1.0)
    assert _approx(m.compute(mode="find", ratio="sin", value=0.6, quadrant="1")["found_value"], 0.8)


def test_trig_angles_known():
    m = _load_trig("trig-angles")
    assert m.compute(angle_deg=135)["kind"] == "obtuse"
    assert m.compute(angle_deg=90)["kind"] == "right"
    assert m.compute(angle_deg=270)["kind"] == "reflex"
    assert _approx(m.compute(angle_deg=30)["complement"], 60)


def test_trig_similar_known():
    m = _load_trig("trig-similar-triangles")
    assert _approx(m.compute(a1=3, a2=6, b1=4)["b2"], 8)


def test_trig_intro_ratios_known():
    m = _load_trig("trig-intro-ratios")
    r = m.compute(opp=3, adj=4, hyp=5)
    assert _approx(r["sin"], 0.6) and _approx(r["cos"], 0.8) and _approx(r["tan"], 0.75)
    assert _approx(m.compute(opp=3, adj=4)["hyp"], 5)  # derives hypotenuse


def test_trig_sin_cos_tan_known():
    m = _load_trig("trig-sin-cos-tan")
    assert _approx(m.compute(angle_deg=30, known_type="hyp", known_val=10, want_type="opp")["value"], 5)
    assert _approx(m.compute(angle_deg=45, known_type="adj", known_val=10, want_type="opp")["value"], 10)


def test_trig_inverse_known():
    m = _load_trig("trig-inverse")
    assert _approx(m.compute(side1=5, side1_type="opp", side2=10, side2_type="hyp")["angle"], 30)
    assert _approx(m.compute(side1=5, side1_type="opp", side2=5, side2_type="adj")["angle"], 45)


def test_trig_elevation_known():
    m = _load_trig("trig-elevation-depression")
    assert _approx(m.compute(angle_deg=40, distance=50, find="height")["height"], 41.955, 1e-2)
    assert _approx(m.compute(height=41.955, distance=50, find="angle")["angle"], 40, 1e-2)


def test_trig_bearing_known():
    m = _load_trig("trig-bearing-navigation")
    r = m.compute(east=10, north=10)
    assert _approx(r["bearing"], 45) and r["result"] == "045\u00b0"
    assert _approx(r["distance"], 14.1421, 1e-3)
    assert _approx(m.compute(east=0, north=-5)["bearing"], 180)


def test_trig_area_known():
    m = _load_trig("trig-area-triangle")
    assert _approx(m.compute(a=6, b=8, angle_C=30)["area"], 12)


def test_trig_3d_known():
    m = _load_trig("trig-3d-problems")
    r = m.compute(length=3, width=4, height=12)
    assert _approx(r["space_diag"], 13) and _approx(r["base_diag"], 5)
    assert _approx(r["angle"], 67.38, 1e-2)


# ---- contract checks (success carries disclaimer+steps; errors never raise) -

def test_trig_compute_contract():
    good_args = {
        "trig-angles": dict(angle_deg=45),
        "trig-pythagorean-identity": dict(mode="verify", angle_deg=37),
        "trig-similar-triangles": dict(a1=3, a2=6, b1=4),
        "trig-intro-ratios": dict(opp=3, adj=4, hyp=5),
        "trig-sin-cos-tan": dict(angle_deg=30, known_type="hyp", known_val=10, want_type="opp"),
        "trig-inverse": dict(side1=5, side1_type="opp", side2=10, side2_type="hyp"),
        "trig-elevation-depression": dict(angle_deg=40, distance=50, find="height"),
        "trig-bearing-navigation": dict(east=10, north=10),
        "trig-area-triangle": dict(a=6, b=8, angle_C=30),
        "trig-3d-problems": dict(length=3, width=4, height=12),
    }
    for slug in _TRIG_CALCS:
        m = _load_trig(slug)
        r = m.compute(**good_args[slug])
        assert "disclaimer" in r and r["disclaimer"]
        assert isinstance(r.get("steps"), list) and len(r["steps"]) >= 1
        for st in r["steps"]:
            assert {"label", "math", "note"} <= set(st)
        # error path: empty call must not raise and must return the error shape
        e = m.compute()
        assert "error" in e and e.get("steps") == [] and "disclaimer" in e
# ============================================================================
# TRIGONOMETRY — STAGE 2 (Functions & Graphs + Non-Right-Angle Trig)
# [append-only block]
# Added by the Stage 2 build. Known-value checks + contract checks. These import
# each calc module directly and exercise compute(); they do not require a server.
# Safe to append to the existing tests/test_calculators.py.
# ============================================================================
import importlib.util as _ilu2
import pathlib as _pl2
import math as _math2

_TRIG2_BASE = _pl2.Path(__file__).resolve().parent.parent / "calculators" / "maths" / "trigonometry"

_TRIG2_CALCS = {
    # Trigonometric Functions & Graphs
    "trig-unit-circle": "trigonometric-functions-and-graphs/trig-unit-circle",
    "trig-radians": "trigonometric-functions-and-graphs/trig-radians",
    "trig-sine-graph": "trigonometric-functions-and-graphs/trig-sine-graph",
    "trig-cosine-graph": "trigonometric-functions-and-graphs/trig-cosine-graph",
    "trig-tangent-graph": "trigonometric-functions-and-graphs/trig-tangent-graph",
    "trig-transformations": "trigonometric-functions-and-graphs/trig-transformations",
    "trig-period-amplitude": "trigonometric-functions-and-graphs/trig-period-amplitude",
    # Non-Right-Angle Trigonometry
    "trig-sine-rule": "non-right-angle-trigonometry/trig-sine-rule",
    "trig-cosine-rule": "non-right-angle-trigonometry/trig-cosine-rule",
    "trig-ambiguous-case": "non-right-angle-trigonometry/trig-ambiguous-case",
    "trig-sine-rule-area": "non-right-angle-trigonometry/trig-sine-rule-area",
}


def _load_trig2(slug):
    path = _TRIG2_BASE / _TRIG2_CALCS[slug] / "calc.py"
    spec = _ilu2.spec_from_file_location("trig2_" + slug.replace("-", "_"), path)
    mod = _ilu2.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _approx2(a, b, tol=1e-2):
    return a is not None and abs(a - b) < tol


_DISCLAIMER2 = "These values are estimates"


# ---- known-value checks (the hand-worked examples from the build) ----------

def test_trig2_unit_circle_60():
    r = _load_trig2("trig-unit-circle").compute(angle_deg=60)
    assert _approx2(r["cos"], 0.5)
    assert _approx2(r["sin"], 0.866025)
    assert "Quadrant I" in r["quadrant"]


def test_trig2_unit_circle_tan_undefined_at_90():
    r = _load_trig2("trig-unit-circle").compute(angle_deg=90)
    assert r["tan"] is None


def test_trig2_radians_180_is_pi():
    r = _load_trig2("trig-radians").compute(value=180, direction="deg2rad")
    assert _approx2(r["radians"], _math2.pi)
    assert "pi" in r["result"]


def test_trig2_radians_reverse():
    r = _load_trig2("trig-radians").compute(value=_math2.pi, direction="rad2deg")
    assert _approx2(r["degrees"], 180)


def test_trig2_sine_graph_30():
    r = _load_trig2("trig-sine-graph").compute(angle_deg=30)
    assert _approx2(r["y"], 0.5)
    assert r["amplitude"] == 1 and r["period_deg"] == 360


def test_trig2_cosine_graph_60():
    r = _load_trig2("trig-cosine-graph").compute(angle_deg=60)
    assert _approx2(r["y"], 0.5)


def test_trig2_cosine_graph_starts_at_one():
    r = _load_trig2("trig-cosine-graph").compute(angle_deg=0)
    assert _approx2(r["y"], 1.0)


def test_trig2_tangent_graph_45():
    r = _load_trig2("trig-tangent-graph").compute(angle_deg=45)
    assert _approx2(r["y"], 1.0)


def test_trig2_tangent_graph_undefined_at_90():
    r = _load_trig2("trig-tangent-graph").compute(angle_deg=90)
    assert r.get("undefined") is True
    assert r["y"] is None


def test_trig2_transformations_eval():
    r = _load_trig2("trig-transformations").compute(A=2, B=1, C=0, D=0, x_deg=90)
    assert _approx2(r["y"], 2.0)
    assert _approx2(r["amplitude"], 2) and _approx2(r["period_deg"], 360)


def test_trig2_transformations_period_from_B():
    r = _load_trig2("trig-transformations").compute(A=3, B=2, C=0, D=0, x_deg=45)
    assert _approx2(r["period_deg"], 180)


def test_trig2_period_amplitude():
    r = _load_trig2("trig-period-amplitude").compute(A=3, B=2)
    assert _approx2(r["amplitude"], 3)
    assert _approx2(r["period_deg"], 180)


def test_trig2_sine_rule_find_side():
    r = _load_trig2("trig-sine-rule").compute(
        mode="side", known_side=7, known_angle=30, other_angle=45)
    assert _approx2(r["value"], 9.8995, 1e-2)


def test_trig2_sine_rule_find_angle():
    r = _load_trig2("trig-sine-rule").compute(
        mode="angle", known_side=7, known_angle=30, other_side=5)
    assert _approx2(r["value"], 20.92, 1e-1)


def test_trig2_cosine_rule_find_side():
    r = _load_trig2("trig-cosine-rule").compute(mode="side", a=5, b=7, angle_C=60)
    assert _approx2(r["value"], 6.245, 1e-2)


def test_trig2_cosine_rule_sss_right_angle():
    r = _load_trig2("trig-cosine-rule").compute(mode="angle", a=3, b=4, c=5)
    assert _approx2(r["value"], 90.0)


def test_trig2_ambiguous_two_triangles():
    r = _load_trig2("trig-ambiguous-case").compute(a=6, b=8, A=30)
    assert r["count"] == 2


def test_trig2_ambiguous_one_triangle():
    r = _load_trig2("trig-ambiguous-case").compute(a=10, b=8, A=30)
    assert r["count"] == 1


def test_trig2_ambiguous_no_triangle():
    r = _load_trig2("trig-ambiguous-case").compute(a=2, b=8, A=80)
    assert r["count"] == 0


def test_trig2_sine_rule_area():
    r = _load_trig2("trig-sine-rule-area").compute(a=8, b=11, angle_C=37)
    assert _approx2(r["area"], 26.48, 1e-1)


# ---- contract checks (apply to every Stage 2 calculator) -------------------

_TRIG2_VALID_ARGS = {
    "trig-unit-circle": dict(angle_deg=60),
    "trig-radians": dict(value=180, direction="deg2rad"),
    "trig-sine-graph": dict(angle_deg=30),
    "trig-cosine-graph": dict(angle_deg=60),
    "trig-tangent-graph": dict(angle_deg=45),
    "trig-transformations": dict(A=2, B=1, C=0, D=0, x_deg=90),
    "trig-period-amplitude": dict(A=3, B=2),
    "trig-sine-rule": dict(mode="side", known_side=7, known_angle=30, other_angle=45),
    "trig-cosine-rule": dict(mode="side", a=5, b=7, angle_C=60),
    "trig-ambiguous-case": dict(a=6, b=8, A=30),
    "trig-sine-rule-area": dict(a=8, b=11, angle_C=37),
}


def test_trig2_all_success_contract():
    for slug, args in _TRIG2_VALID_ARGS.items():
        r = _load_trig2(slug).compute(**args)
        assert "error" not in r, slug
        assert isinstance(r.get("steps"), list) and r["steps"], slug
        for s in r["steps"]:
            assert {"label", "math", "note"} <= set(s), slug
        assert r.get("disclaimer", "").startswith(_DISCLAIMER2), slug


def test_trig2_all_error_contract():
    # Calling with no/invalid arguments should return a clean error, never raise.
    # A few calcs have valid defaults for every parameter, so they are given
    # explicitly invalid input instead of an empty call.
    _bad_args = {
        "trig-transformations": dict(B=0),       # zero B -> infinite period
        "trig-period-amplitude": dict(B=0),      # zero B -> infinite period
    }
    for slug in _TRIG2_CALCS:
        r = _load_trig2(slug).compute(**_bad_args.get(slug, {}))
        assert "error" in r, slug
        assert r.get("steps") == [], slug
        assert r.get("disclaimer", "").startswith(_DISCLAIMER2), slug


def test_trig2_all_json_safe():
    import json as _json2
    for slug, args in _TRIG2_VALID_ARGS.items():
        r = _load_trig2(slug).compute(**args)
        _json2.dumps(r)  # must not raise
# ============================================================================
# TRIGONOMETRY / GEOMETRY — STAGE 3 (Pythagoras → Geometry, Heron + 2 proofs)
# [append-only block]
# Added by the Stage 3 build. Covers the calculators that were moved to the new
# Geometry section and the two Heron proof companions. Same self-contained
# pattern as the Stage 1/2 appends: each test imports a calc module directly and
# exercises compute(); no server required. Safe to append to the existing
# tests/test_calculators.py.
# ============================================================================
import importlib.util as _ilu3
import pathlib as _pl3
import math as _math3

_ROOT3 = _pl3.Path(__file__).resolve().parent.parent / "calculators"

# slug -> calc.py path relative to the calculators/ root
_TRIG3_CALCS = {
    "geo-pythagoras": "geometry/triangles/pythagoras-theorem",
    "geo-heron": "geometry/triangles/heron-formula",
    "trig-pythagorean-identity": "maths/trigonometry/foundations/trig-pythagorean-identity",
    "trig-heron-proof": "maths/trigonometry/non-right-angle-trigonometry/trig-heron-proof",
    "heron-algebraic": "maths/algebra/heron-algebraic",
}


def _load_trig3(slug):
    path = _ROOT3 / _TRIG3_CALCS[slug] / "calc.py"
    spec = _ilu3.spec_from_file_location("trig3_" + slug.replace("-", "_"), path)
    mod = _ilu3.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _approx3(a, b, tol=1e-3):
    return a is not None and abs(float(a) - b) < tol


_DISCLAIMER3 = "These values are estimates"


# ---- known-value checks ----------------------------------------------------

def test_trig3_pythagoras_hypotenuse_345():
    r = _load_trig3("geo-pythagoras").compute(a=3, b=4, solve_for="c")
    assert _approx3(r["result"], 5.0)
    assert r["result_label"] == "Hypotenuse c"
    assert r["solved"] == "c"


def test_trig3_pythagoras_leg_from_hyp():
    # 5-12-13: given c=13 and one leg 5, the other leg is 12.
    r = _load_trig3("geo-pythagoras").compute(c=13, b=5, solve_for="a")
    assert _approx3(r["result"], 12.0)
    assert r["result_label"] == "Leg a"


def test_trig3_pythagoras_rejects_short_hypotenuse():
    # hypotenuse must exceed the known leg
    r = _load_trig3("geo-pythagoras").compute(c=3, b=5, solve_for="a")
    assert "error" in r


def test_trig3_pythagoras_rejects_negative():
    r = _load_trig3("geo-pythagoras").compute(a=-3, b=4, solve_for="c")
    assert "error" in r


def test_trig3_geo_heron_345():
    r = _load_trig3("geo-heron").compute(a=3, b=4, c=5)
    assert _approx3(r["area"], 6.0)
    assert _approx3(r["s"], 6.0)


def test_trig3_geo_heron_rejects_degenerate():
    # 1, 2, 3 violates the triangle inequality
    r = _load_trig3("geo-heron").compute(a=1, b=2, c=3)
    assert "error" in r


def test_trig3_identity_verify_sums_to_one():
    for ang in (0, 37, 90, 210, 359.5):
        r = _load_trig3("trig-pythagorean-identity").compute(mode="verify", angle_deg=ang)
        assert "error" not in r, ang
        assert _approx3(r["sum"], 1.0), ang


def test_trig3_identity_find_cos_from_sin_q1():
    # sin = 0.6, Q1 -> cos = +0.8
    r = _load_trig3("trig-pythagorean-identity").compute(
        mode="find", ratio="sin", value=0.6, quadrant="1")
    assert r["found"] == "cos"
    assert _approx3(r["found_value"], 0.8)


def test_trig3_identity_find_cos_sign_in_q2():
    # sin = 0.6, Q2 -> cos = -0.8
    r = _load_trig3("trig-pythagorean-identity").compute(
        mode="find", ratio="sin", value=0.6, quadrant="2")
    assert _approx3(r["found_value"], -0.8)


def test_trig3_identity_rejects_out_of_range():
    r = _load_trig3("trig-pythagorean-identity").compute(
        mode="find", ratio="sin", value=1.5, quadrant="1")
    assert "error" in r


def test_trig3_heron_proof_matches_heron_345():
    r = _load_trig3("trig-heron-proof").compute(a=3, b=4, c=5)
    assert _approx3(r["angle_C"], 90.0)        # right angle opposite c=5
    assert _approx3(r["area_trig"], 6.0)
    assert _approx3(r["area_heron"], 6.0)
    assert r["match"] is True


def test_trig3_heron_proof_matches_heron_678():
    r = _load_trig3("trig-heron-proof").compute(a=6, b=7, c=8)
    assert _approx3(r["area_trig"], r["area_heron"])
    assert r["match"] is True


def test_trig3_heron_proof_rejects_degenerate():
    r = _load_trig3("trig-heron-proof").compute(a=1, b=2, c=3)
    assert "error" in r


def test_trig3_heron_algebraic_matches_heron_345():
    r = _load_trig3("heron-algebraic").compute(a=3, b=4, c=5)
    assert _approx3(r["height"], 2.4)          # altitude onto the base c=5
    assert _approx3(r["foot_d"], 3.2)
    assert _approx3(r["area_alg"], 6.0)
    assert r["match"] is True


def test_trig3_heron_algebraic_matches_heron_obtuse():
    # 13, 4, 15 is a valid (obtuse) triangle, area 24
    r = _load_trig3("heron-algebraic").compute(a=13, b=4, c=15)
    assert _approx3(r["area_alg"], 24.0)
    assert _approx3(r["area_alg"], r["area_heron"])
    assert r["match"] is True


def test_trig3_heron_algebraic_rejects_degenerate():
    r = _load_trig3("heron-algebraic").compute(a=1, b=2, c=3)
    assert "error" in r


# ---- contract checks (success + error, every Stage 3 calc) -----------------

_TRIG3_VALID_ARGS = {
    "geo-pythagoras": dict(a=3, b=4, solve_for="c"),
    "geo-heron": dict(a=3, b=4, c=5),
    "trig-pythagorean-identity": dict(mode="verify", angle_deg=37),
    "trig-heron-proof": dict(a=6, b=7, c=8),
    "heron-algebraic": dict(a=6, b=7, c=8),
}


def test_trig3_all_success_contract():
    for slug, args in _TRIG3_VALID_ARGS.items():
        r = _load_trig3(slug).compute(**args)
        assert "error" not in r, slug
        assert isinstance(r.get("steps"), list) and r["steps"], slug
        for s in r["steps"]:
            assert {"label", "math", "note"} <= set(s), slug
        assert "result" in r, slug
        assert r.get("disclaimer", "").startswith(_DISCLAIMER3), slug


def test_trig3_all_error_contract():
    # Degenerate triangle / invalid input -> clean error dict, never an exception.
    _bad = {
        "geo-pythagoras": dict(a=-1, b=4, solve_for="c"),
        "geo-heron": dict(a=1, b=2, c=3),
        "trig-pythagorean-identity": dict(mode="find", ratio="sin", value=5, quadrant="1"),
        "trig-heron-proof": dict(a=1, b=2, c=3),
        "heron-algebraic": dict(a=1, b=2, c=3),
    }
    for slug, args in _bad.items():
        r = _load_trig3(slug).compute(**args)
        assert "error" in r and isinstance(r["error"], str), slug
        assert r.get("steps") == [], slug
        assert r.get("disclaimer", "").startswith(_DISCLAIMER3), slug


def test_trig3_viz_templates_registered():
    # Each calc should declare its own viz template (no stale cross-links).
    # Only runs where the registry exposes the metadata on the function;
    # skipped on registries that don't attach it.
    import pytest
    expected = {
        "geo-pythagoras": "viz/geo-pythagoras.html",
        "geo-heron": "viz/geo-heron.html",
        "trig-pythagorean-identity": "viz/trig-pythagorean-identity.html",
        "trig-heron-proof": "viz/trig-heron-proof.html",
        "heron-algebraic": "viz/heron-algebraic.html",
    }
    fn = _load_trig3("geo-pythagoras").compute
    if not hasattr(fn, "_nc_meta"):
        pytest.skip("registry does not expose _nc_meta on compute")
    for slug, vt in expected.items():
        meta = _load_trig3(slug).compute._nc_meta
        assert meta.get("viz_template") == vt, (slug, meta.get("viz_template"))
        
# ============================================================================
# REAL-WORLD TRIGONOMETRY — worked examples + applications auto-linking
# [append-only block]
# Covers the six interactive worked-example calculators in the real-world
# section, plus the bidirectional applications linking layer. Self-contained:
# imports each calc module directly and exercises compute(); the linking tests
# drive a small in-test registry stub so they run without the server.
# ============================================================================
import importlib.util as _ilu_rw
import pathlib as _pl_rw
import math as _math_rw

_RW_ROOT = _pl_rw.Path(__file__).resolve().parent.parent / "calculators" / "real-world"

# slug -> path (relative to the real-world root)
_RW_CALCS = {
    "rw-tree-height": "heights-and-distances/rw-tree-height",
    "rw-plane-altitude": "navigation/rw-plane-altitude",
    "rw-roof-pitch": "construction/rw-roof-pitch",
    "rw-star-parallax": "astronomy/rw-star-parallax",
    "rw-bullet-trajectory": "forensics/rw-bullet-trajectory",
    "rw-ocean-depth": "marine/rw-ocean-depth",
}


def _load_rw(slug):
    path = _RW_ROOT / _RW_CALCS[slug] / "calc.py"
    spec = _ilu_rw.spec_from_file_location("rw_" + slug.replace("-", "_"), path)
    mod = _ilu_rw.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _approx_rw(a, b, tol=1e-2):
    return a is not None and abs(float(a) - b) < tol


_DISCLAIMER_RW = "These values are estimates"


# ---- known-value checks (each scenario's headline maths) -------------------

def test_rw_tree_height_known():
    # 50 m away, 40 deg, eye 1.6 m -> 50*tan40 + 1.6
    r = _load_rw("rw-tree-height").compute(distance=50, angle_deg=40, eye_height=1.6)
    assert _approx_rw(r["above_eye"], 50 * _math_rw.tan(_math_rw.radians(40)))
    assert _approx_rw(r["total_height"], 50 * _math_rw.tan(_math_rw.radians(40)) + 1.6)


def test_rw_tree_height_rejects_bad_angle():
    assert "error" in _load_rw("rw-tree-height").compute(distance=10, angle_deg=90)
    assert "error" in _load_rw("rw-tree-height").compute(distance=0, angle_deg=30)


def test_rw_plane_altitude_known():
    r = _load_rw("rw-plane-altitude").compute(distance=12000, angle_deg=7)
    assert _approx_rw(r["altitude"], 12000 * _math_rw.tan(_math_rw.radians(7)), tol=1)
    assert _approx_rw(r["slant"], 12000 / _math_rw.cos(_math_rw.radians(7)), tol=1)


def test_rw_roof_pitch_known():
    # rise 2.5 over run 4 -> atan(2.5/4); rafter = hypot(4,2.5)
    r = _load_rw("rw-roof-pitch").compute(run_width=4, rise=2.5)
    assert _approx_rw(r["pitch_deg"], _math_rw.degrees(_math_rw.atan2(2.5, 4)))
    assert _approx_rw(r["rafter"], _math_rw.hypot(4, 2.5))


def test_rw_star_parallax_alpha_centauri():
    # 0.7687 arcsec -> ~1.3009 pc -> ~4.24 ly (the real Alpha Centauri value)
    r = _load_rw("rw-star-parallax").compute(parallax_arcsec=0.7687)
    assert _approx_rw(r["distance_pc"], 1.0 / 0.7687, tol=1e-3)
    assert _approx_rw(r["distance_ly"], (1.0 / 0.7687) * 3.26156, tol=1e-2)


def test_rw_star_parallax_rejects_zero():
    assert "error" in _load_rw("rw-star-parallax").compute(parallax_arcsec=0)


def test_rw_bullet_trajectory_known():
    # drop 1.2 over travel 3 -> atan(1.2/3)
    r = _load_rw("rw-bullet-trajectory").compute(horizontal=3, vertical_drop=1.2)
    assert _approx_rw(r["impact_angle"], _math_rw.degrees(_math_rw.atan2(1.2, 3)))
    assert _approx_rw(r["path_length"], _math_rw.hypot(3, 1.2))


def test_rw_ocean_depth_known():
    # slant 600 at 35 deg -> depth = 600 sin35; offset = 600 cos35
    r = _load_rw("rw-ocean-depth").compute(slant_range=600, angle_deg=35)
    assert _approx_rw(r["depth"], 600 * _math_rw.sin(_math_rw.radians(35)), tol=1e-1)
    assert _approx_rw(r["offset"], 600 * _math_rw.cos(_math_rw.radians(35)), tol=1e-1)


def test_rw_ocean_depth_rejects_bad_angle():
    assert "error" in _load_rw("rw-ocean-depth").compute(slant_range=600, angle_deg=0)


# ---- contract checks (success + error, every worked example) ---------------

_RW_VALID_ARGS = {
    "rw-tree-height": dict(distance=25, angle_deg=32, eye_height=1.6),
    "rw-plane-altitude": dict(distance=12000, angle_deg=7),
    "rw-roof-pitch": dict(run_width=4, rise=2.5),
    "rw-star-parallax": dict(parallax_arcsec=0.7687),
    "rw-bullet-trajectory": dict(horizontal=3, vertical_drop=1.2),
    "rw-ocean-depth": dict(slant_range=600, angle_deg=35),
}


def test_rw_all_success_contract():
    for slug, args in _RW_VALID_ARGS.items():
        r = _load_rw(slug).compute(**args)
        assert "error" not in r, slug
        assert "result" in r, slug
        assert isinstance(r.get("steps"), list) and r["steps"], slug
        for s in r["steps"]:
            assert {"label", "math", "note"} <= set(s), slug
        assert isinstance(r.get("explanation"), list) and r["explanation"], slug
        assert r.get("disclaimer", "").startswith(_DISCLAIMER_RW), slug



# ---- registry-level membership + relatedness (uses the real registry) ------
# These load the whole app via core.registry.load_all so they exercise the
# actual Calc objects and core.related, not a stub. Skipped automatically if
# the project layout isn't importable from the test's working directory.

def _load_registry():
    import importlib, pathlib, sys
    root = pathlib.Path(__file__).resolve().parent.parent
    if str(root) not in sys.path:
        sys.path.insert(0, str(root))
    try:
        from core import registry, related  # noqa
    except Exception:
        return None, None
    importlib.reload(registry)
    registry.load_all(str(root))
    from core import related
    return registry, related


def test_rw_all_in_real_world_section():
    registry, _ = _load_registry()
    if registry is None:
        import pytest; pytest.skip("core.registry not importable here")
    for slug in _RW_CALCS:
        c = registry.resolve(slug)
        assert c is not None, slug
        assert c.section == "real-world", slug
        assert c.topic == "Real-World Trigonometry", slug
        assert c.viz_template == "viz/%s.html" % slug, slug


def test_rw_curated_related_present_and_first():
    """Each worked example's curated `related` slugs lead the related rail."""
    registry, related = _load_registry()
    if registry is None:
        import pytest; pytest.skip("core.registry not importable here")
    expected = {
        "rw-tree-height": ["trig-elevation-depression", "trig-sin-cos-tan"],
        "rw-ocean-depth": ["trig-sin-cos-tan", "trig-3d-problems"],
        "rw-roof-pitch": ["trig-sin-cos-tan", "trig-inverse"],
    }
    for slug, want in expected.items():
        rail = related.related_calcs(slug, limit=6)
        top = [r["slug"] for r in rail][:len(want)]
        assert top == want, (slug, top, want)
        # curated entries are flagged curated=True
        assert all(r["curated"] for r in rail[:len(want)]), slug


def test_related_auto_fill_and_no_anchor_self():
    registry, related = _load_registry()
    if registry is None:
        import pytest; pytest.skip("core.registry not importable here")
    rail = related.related_calcs("rw-tree-height", limit=6)
    slugs = [r["slug"] for r in rail]
    assert "rw-tree-height" not in slugs            # never links to itself
    assert len(rail) == len(set(slugs))             # no duplicates
    assert any(not r["curated"] for r in rail)      # auto-fill kicked in


def test_related_unknown_slug_empty():
    registry, related = _load_registry()
    if registry is None:
        import pytest; pytest.skip("core.registry not importable here")
    assert related.related_calcs("does-not-exist") == []


def test_related_curated_dead_slug_skipped():
    """A curated slug that isn't registered must not appear (no dead link)."""
    registry, related = _load_registry()
    if registry is None:
        import pytest; pytest.skip("core.registry not importable here")
    c = registry.resolve("rw-tree-height")
    original = list(c.related)
    try:
        c.related = original + ["totally-missing-calc"]
        rail = [r["slug"] for r in related.related_calcs("rw-tree-height", limit=8)]
        assert "totally-missing-calc" not in rail
    finally:
        c.related = original


def test_health_summary_clean():
    """The shipped package should have no hard errors in the health check."""
    registry, _ = _load_registry()
    if registry is None:
        import pytest; pytest.skip("core.registry not importable here")
    try:
        from core import health
    except Exception:
        import pytest; pytest.skip("core.health not importable here")
    s = health.summary()
    assert s["checks"]["missing_viz_templates"] == [], s["checks"]["missing_viz_templates"]
    assert s["checks"]["dead_related_links"] == [], s["checks"]["dead_related_links"]
