from core.faqs import register_faqs

register_faqs("newtons-laws", [
    {"q": "What are Newton's three laws of motion?",
     "a": "The first law (inertia) says a body stays at rest or keeps moving at constant "
          "velocity unless a net force acts on it. The second law says the net force "
          "equals mass times acceleration, F = ma. The third law says every action has an "
          "equal and opposite reaction."},
    {"q": "How do I use F = ma?",
     "a": "Choose what you want to find. To get force, multiply mass by acceleration. To "
          "get mass, divide force by acceleration. To get acceleration, divide force by "
          "mass. For example, a 3 kg trolley pushed so it accelerates at 4 m/s\u00b2 needs "
          "a net force of 3 \u00d7 4 = 12 N."},
    {"q": "What units should I use?",
     "a": "Use SI units: mass in kilograms (kg), acceleration in metres per "
          "second-squared (m/s\u00b2) and force in newtons (N). One newton is the force "
          "that gives a 1 kg mass an acceleration of 1 m/s\u00b2."},
    {"q": "Why does the same force move a heavy object less?",
     "a": "Because acceleration is force divided by mass. For a fixed force, a larger mass "
          "gives a smaller acceleration, so heavier objects respond more sluggishly to "
          "the same push."},
    {"q": "If forces always come in pairs, why does anything move?",
     "a": "The action and reaction in the third law act on two different bodies, not the "
          "same one, so they do not cancel. When you push off the ground, the ground "
          "pushes back on you, and that reaction force is what moves you."},
])
