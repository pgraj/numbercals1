from core.faqs import register_faqs
register_faqs("time-kinematic", [
    {"q": "What does this calculator find?",
     "a": "How long a journey takes, if you know the distance and your speed. The rule is "
          "time = distance \u00f7 speed (t = d/v)."},
    {"q": "Can you show an example?",
     "a": "You need to cover 100 metres at 20 metres per second. Time = 100 \u00f7 20 = 5 "
          "seconds. So it takes 5 seconds."},
    {"q": "How do I find distance or speed instead?",
     "a": "Rearrange the same formula: distance = speed \u00d7 time, and speed = distance "
          "\u00f7 time. Pick what you want in the 'Solve for' box."},
    {"q": "Why is it called 'time-kinematic'?",
     "a": "Just to tell it apart from the clock-and-calendar time tools. This one is about "
          "motion \u2014 finding travel time from speed and distance."},
    {"q": "What units should I use?",
     "a": "Distance in metres and speed in metres per second give time in seconds. "
          "Kilometres with km/h give hours. Keep both inputs in matching units."},
    {"q": "Where do I see this in real life?",
     "a": "Estimating how long a drive or a walk will take: take the distance, divide by "
          "your usual speed, and you have the time."},
])
