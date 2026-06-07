from core.faqs import register_faqs
register_faqs("distance", [
    {"q": "What does this calculator find?",
     "a": "How far you travel, if you know your speed and how long you travel for. The "
          "rule is distance = speed \u00d7 time (d = v\u00d7t)."},
    {"q": "Can you show an example?",
     "a": "A car drives at 20 metres per second for 5 seconds. Distance = 20 \u00d7 5 = 100 "
          "metres. Simple as that."},
    {"q": "How do I find speed or time instead?",
     "a": "Rearrange the same formula: speed = distance \u00f7 time, and time = distance "
          "\u00f7 speed. Pick what you want in the 'Solve for' box."},
    {"q": "Is this the same as the Speed calculator?",
     "a": "Yes \u2014 it is the same speed-distance-time relationship, just set up to find "
          "distance first. Use whichever calculator matches what your question asks for."},
    {"q": "What units should I use?",
     "a": "Speed in metres per second and time in seconds give distance in metres. Use "
          "km/h with hours for kilometres. Keep both inputs in matching units."},
    {"q": "Does this work if speed changes?",
     "a": "This assumes a steady speed. If the speed changes, you would use average speed, "
          "or the acceleration calculator for steadily changing speed."},
])
