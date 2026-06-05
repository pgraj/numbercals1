from core.faqs import register_faqs

register_faqs("linear-equation", [
    {"q": "How do I solve ax + b = 0?",
     "a": "Move b to the other side and divide by a: x = −b / a. For 2x − 6 = 0, "
          "x = 6 / 2 = 3."},
    {"q": "What does the root mean on the graph?",
     "a": "The root is the x-value where the line crosses the horizontal axis — "
          "the single point where y equals zero."},
    {"q": "What does the slope tell me?",
     "a": "The slope a is how steep the line is: how far y changes for each step "
          "in x. A bigger a makes a steeper line; a negative a tilts it downward."},
    {"q": "Where is this used in real life?",
     "a": "Break-even points — if profit is 5x − 200, solving 5x − 200 = 0 shows "
          "you must sell 40 units to break even. Converting units — a linear rule "
          "links Celsius and Fahrenheit. Phone plans — a $20 base plus $0.10 a "
          "minute is a straight-line cost, and solving for a target bill tells "
          "you how many minutes you can use."},
    {"q": "When does a linear equation have no solution?",
     "a": "When a = 0 but b is not zero, the equation becomes b = 0, which is "
          "false, so there is no x that works. If a = 0 and b = 0, every x works."},
])
