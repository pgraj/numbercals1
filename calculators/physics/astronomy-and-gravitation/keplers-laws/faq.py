from core.faqs import register_faqs
register_faqs("keplers-laws", [
    {"q": "What are Kepler's three laws, in simple words?",
     "a": "First: planets travel in slightly squashed circles (ellipses) with the Sun "
          "off to one side. Second: a planet speeds up when it is near the Sun and slows "
          "down when far away. Third: planets farther from the Sun take much longer to go "
          "around \u2014 and there is an exact formula linking the two."},
    {"q": "What does T\u00b2 = 4\u03c0\u00b2a\u00b3 / (GM) mean?",
     "a": "T is how long one orbit takes, a is the size of the orbit (its semi-major "
          "axis), M is the mass of the thing being orbited (like the Sun), and G is a "
          "fixed constant of nature. Square the period and it is proportional to the cube "
          "of the distance \u2014 so going twice as far out makes the year far more than "
          "twice as long."},
    {"q": "Can you show an example?",
     "a": "Take Earth: its orbit is about 1.496 \u00d7 10\u00b9\u00b9 metres across and the "
          "Sun's mass is about 1.989 \u00d7 10\u00b3\u2070 kg. Put those into the third "
          "law and you get a period of about 31.5 million seconds \u2014 which is one year. "
          "The formula really works."},
    {"q": "Why does a planet speed up near the Sun?",
     "a": "Because of the second law: the line from the Sun to the planet always sweeps "
          "the same area in the same time. Near the Sun that line is short, so the planet "
          "has to move quickly to sweep the same area; far away the line is long, so it "
          "can move slowly."},
    {"q": "Why is this useful?",
     "a": "Astronomers use the third law to weigh the universe \u2014 if you watch how long "
          "something takes to orbit and how far out it is, you can work out the mass of "
          "the star or planet it goes around. It even helps find planets around other "
          "stars."},
    {"q": "Who was Kepler?",
     "a": "Johannes Kepler was a German astronomer in the early 1600s. Using very careful "
          "measurements, he replaced the old idea that orbits must be perfect circles with "
          "these three laws \u2014 work that later let Newton explain gravity itself."},
])
