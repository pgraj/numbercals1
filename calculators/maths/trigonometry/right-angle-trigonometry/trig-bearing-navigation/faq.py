from core.faqs import register_faqs

register_faqs("trig-bearing-navigation", [
    {"q": "What is a three-figure bearing?",
     "a": "A bearing is a direction given as an angle measured clockwise from "
          "north, always written with three digits from 000° to 360°. Due east "
          "is 090°, due south is 180°, and due west is 270°."},
    {"q": "Why always three digits?",
     "a": "Writing bearings as three figures (for example 045° rather than 45°) "
          "avoids confusion and keeps a consistent format on maps, charts, and in "
          "aviation and marine communication."},
    {"q": "Can you give a worked example?",
     "a": "Moving 10 units east and 10 units north gives a bearing of 045° "
          "(north-east) and a straight-line distance of √(10² + 10²) ≈ 14.14 "
          "units."},
    {"q": "How is the distance found?",
     "a": "The straight-line distance between the start and end points comes from "
          "Pythagoras applied to the east and north components: distance = √(east² "
          "+ north²)."},
    {"q": "Where is this used in real life?",
     "a": "Sailors and pilots plot courses, hikers and orienteers navigate with "
          "map and compass, search-and-rescue teams coordinate directions, and "
          "surveyors record the bearings of boundaries."},
])
