from core.faqs import register_faqs

register_faqs("bmr", [
    {"q": "What is BMR?",
     "a": "Basal Metabolic Rate is the number of calories your body burns just to keep you "
          "alive at complete rest — breathing, circulating blood, keeping your organs running, "
          "holding body temperature. It is the energy you would use lying still all day, before "
          "any movement, eating, or exercise is added on top."},
    {"q": "What is the Mifflin-St Jeor equation?",
     "a": "It is the modern standard formula for estimating BMR from weight in kilograms, height "
          "in centimetres, and age in years. Men add 5 to the result and women subtract 161, "
          "reflecting average differences in body composition. It tends to be more accurate for "
          "today's populations than the older Harris-Benedict equation it largely replaced."},
    {"q": "Why is there an 'Other' option for sex?",
     "a": "The equation was derived with two variants, defined on biological sex, that differ only "
          "by a constant (+5 versus -161). 'Other' simply takes the midpoint of the two, giving a "
          "reasonable central estimate when neither variant clearly applies. For the most accurate "
          "figure, a clinician can measure resting metabolism directly."},
    {"q": "How do I read the chart?",
     "a": "The first bar is your estimated BMR in calories per day. The bars beside it are everyday "
          "energy references at the same scale — for instance how much energy you burn over a "
          "night's sleep — so the abstract calorie number has something familiar to sit against."},
    {"q": "Where is this used in real life?",
     "a": "BMR is the foundation for working out daily calorie needs. A 30-year-old man, 80 kg and "
          "180 cm, has a BMR near 1,780 kcal; a 30-year-old woman, 65 kg and 165 cm, near 1,370 kcal. "
          "Multiply BMR by an activity factor and you get total daily energy expenditure, which "
          "nutrition and fitness planning then builds on. It is an estimate, not a prescription."},
])
