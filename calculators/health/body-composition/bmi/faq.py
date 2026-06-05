from core.faqs import register_faqs

register_faqs("bmi", [
    {"q": "What is BMI?",
     "a": "Body Mass Index is a single number that compares your weight to your height. "
          "It divides your weight in kilograms by the square of your height in metres. It is "
          "a quick screening figure, not a diagnosis — it tells you roughly which weight band "
          "you sit in, which can be a starting point for a conversation with a doctor."},
    {"q": "What do the four bands mean?",
     "a": "The World Health Organization splits BMI into four ranges for adults: below 18.5 is "
          "underweight, 18.5 to just under 25 is the normal range, 25 to just under 30 is "
          "overweight, and 30 and above is obese. The cut-offs are the same for men and women."},
    {"q": "How do I read the gauge?",
     "a": "The bar is split into the four coloured bands in order, from underweight on the left "
          "to obese on the right. The needle drops onto the bar at your calculated score, so you "
          "can see at a glance which band you land in and how close you are to the next boundary."},
    {"q": "What are the limits of BMI?",
     "a": "BMI only knows your weight and height — it cannot tell muscle from fat. A very muscular "
          "athlete can read as overweight while carrying little fat, and BMI is less reliable for "
          "older adults, pregnant people, and children, who use age-and-sex percentile charts "
          "instead. Treat it as one rough signal among several, never the whole picture."},
    {"q": "Where is this used in real life?",
     "a": "BMI is used as a fast screening tool. A clinic might record it at a check-up: someone "
          "70 kg at 1.75 m has a BMI of about 22.9, squarely in the normal range. An insurer or a "
          "population health study might use it to flag groups for follow-up. In each case it is a "
          "first filter that points to whether a closer look is worth taking."},
])
