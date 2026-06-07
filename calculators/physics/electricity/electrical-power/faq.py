from core.faqs import register_faqs
register_faqs("electrical-power", [
    {"q": "What is electrical power, in simple words?",
     "a": "Power is how fast a device uses electrical energy. A 100-watt bulb uses energy "
          "ten times faster than a 10-watt one. The basic rule is power = voltage \u00d7 "
          "current (P = V \u00d7 I)."},
    {"q": "Why are there three formulas?",
     "a": "Because of Ohm's Law (V = IR) you can swap things in. If you know voltage and "
          "current, use P = V\u00d7I. Know current and resistance? Use P = I\u00b2\u00d7R. "
          "Know voltage and resistance? Use P = V\u00b2\u00f7R. All three give the same "
          "power \u2014 just pick the one matching what you know."},
    {"q": "Can you show an example?",
     "a": "A device runs at 12 volts and draws 2 amps. Power = 12 \u00d7 2 = 24 watts. If "
          "instead you knew it had 6 ohms of resistance at 2 amps: P = 2\u00b2 \u00d7 6 = "
          "24 watts too. Same answer."},
    {"q": "What is a watt?",
     "a": "A watt is one unit of energy (a joule) used every second. So a 60-watt bulb uses "
          "60 joules of energy each second it is on."},
    {"q": "Is this the same as the mechanical power calculator?",
     "a": "No \u2014 they are different. Mechanical power is about work and motion (P = "
          "W/t = F\u00d7v), while electrical power is about circuits (P = V\u00d7I). Same "
          "idea of 'energy per second', but different quantities, so they are separate "
          "calculators."},
    {"q": "Why does this matter for my electricity bill?",
     "a": "Your bill is based on energy used, which is power \u00d7 time (kilowatt-hours). "
          "A high-power appliance left on for a long time uses the most energy \u2014 which "
          "is why heaters and dryers cost more to run than a phone charger."},
])
