from core.faqs import register_faqs
register_faqs("work-hours", [
    {"q": "What does this calculator do?",
     "a": "It works out how many hours you actually worked, from your start time, your end "
          "time, and any unpaid break. Hours worked = (end \u2212 start) \u2212 break."},
    {"q": "Can you show an example?",
     "a": "Start at 09:00, finish at 17:00, with a 30-minute lunch break. That is 8 hours "
          "between start and end, minus 0.5 hours break = 7.5 hours worked."},
    {"q": "What about night shifts that cross midnight?",
     "a": "The calculator handles them. If you start at 22:00 and finish at 06:00, it sees "
          "that the end is 'earlier' on the clock, adds 24 hours, and correctly gives an "
          "8-hour shift."},
    {"q": "How do I enter the times?",
     "a": "Use 24-hour time as HH:MM \u2014 so 1:30 in the afternoon is 13:30, and "
          "half past nine in the morning is 09:30. Enter the break as a number of minutes."},
    {"q": "What if I have no break?",
     "a": "Just leave the break at 0. The full time between start and end is then counted "
          "as hours worked."},
    {"q": "Why does it say the break is longer than the shift?",
     "a": "That is a safety check \u2014 if the break you entered is bigger than the whole "
          "shift, something is wrong with the inputs, so the calculator asks you to check "
          "them rather than show a negative result."},
])
