from core.faqs import register_faqs

register_faqs("calorie-target", [
    {"q": "What does this calculator do?",
     "a": "It takes your TDEE — the calories that keep your weight steady — and shows an "
          "educational estimate of a daily intake for maintaining, gently losing, or gently gaining "
          "weight, along with a balanced split of carbohydrate, protein, and fat. It is a starting "
          "point for understanding the numbers, not a diet plan and not medical advice."},
    {"q": "Why is the result shown as a range, and why won't it go very low?",
     "a": "Daily energy needs vary from day to day and person to person, so a single exact number "
          "would be falsely precise — a small range is more honest. The tool also uses only a "
          "moderate adjustment and will not show a target below a commonly cited safe minimum "
          "(around 1,500 kcal for men and 1,200 for women). Eating below that should only happen "
          "under medical supervision, so the calculator raises the figure and says so."},
    {"q": "What is a macronutrient split?",
     "a": "Your calories come from three macronutrients: carbohydrates and protein at about 4 "
          "calories per gram, and fat at about 9. A split says what share of your calories comes "
          "from each. This tool uses one common balanced ratio — roughly 45% carbs, 25% protein, "
          "30% fat — and converts it into grams. There is no single correct split; it depends on "
          "your body, activity, and goals."},
    {"q": "How do I read the chart?",
     "a": "The pie shows how your target calories divide across the three macronutrients by "
          "percentage, and the labels give the gram amount for each. It is a picture of proportions, "
          "to make an abstract split easy to grasp at a glance."},
    {"q": "Is this safe to follow on its own?",
     "a": "Treat it as general information, not a prescription. Calorie needs are individual, and "
          "rapid or very low-calorie dieting can be harmful. If you are planning a meaningful change "
          "to how you eat — particularly weight loss, or if you have any history of disordered "
          "eating — please talk with a doctor or an accredited practising dietitian first. They can "
          "give advice that fits your health, which a generic formula cannot."},
])
