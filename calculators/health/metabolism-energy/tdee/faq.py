from core.faqs import register_faqs

register_faqs("tdee", [
    {"q": "What is TDEE?",
     "a": "Total Daily Energy Expenditure is the full number of calories you burn in a typical "
          "day — your resting metabolism plus everything you do on top of it: walking, working, "
          "exercising, even digesting food. It is the figure that best represents how much energy "
          "you actually use day to day."},
    {"q": "How is it worked out?",
     "a": "Start with your BMR — the calories burned at complete rest — then multiply by an "
          "activity factor that reflects how much you move. The factor runs from 1.2 for a mostly "
          "sedentary life up to 1.9 for someone training hard most days or doing heavy physical "
          "work. A desk worker who walks a little might sit around 1.375."},
    {"q": "What do the activity levels mean?",
     "a": "Sedentary (1.2) is little or no exercise. Light (1.375) is light activity one to three "
          "days a week. Moderate (1.55) is three to five days. Active (1.725) is hard exercise most "
          "days. Extra active (1.9) is very intense training or a physically demanding job. Pick the "
          "one that honestly matches a normal week, not your best week."},
    {"q": "How do I read the chart?",
     "a": "The column is stacked in two parts. The lower block is your BMR — the energy you would "
          "burn doing nothing at all. The block on top is the extra energy your activity adds. "
          "Together they make your TDEE, so you can see how much of your daily burn is simply "
          "staying alive versus how much comes from moving."},
    {"q": "Where is this used in real life?",
     "a": "TDEE is the maintenance line — eat around it and weight tends to hold steady. It is the "
          "starting point planners use before deciding on any change. For example, a moderately "
          "active person with a 1,600 kcal BMR has a TDEE near 2,480 kcal. Remember it is an "
          "estimate from averages; real needs vary, so treat it as a guide and adjust to reality."},
])
