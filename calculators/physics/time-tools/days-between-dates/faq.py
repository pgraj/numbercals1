from core.faqs import register_faqs
register_faqs("days-between-dates", [
    {"q": "What does this calculator do?",
     "a": "It counts how many days are between two dates \u2014 and it gets leap years and "
          "different month lengths right automatically, so you do not have to count on a "
          "calendar."},
    {"q": "What is the difference between inclusive and exclusive?",
     "a": "Exclusive counts only the gap: from 1 March to 3 March is 2 days. Inclusive "
          "counts both end days as well, giving 3 days. Use inclusive when you are "
          "counting the length of an event (like 'how many days is my holiday')."},
    {"q": "Can you show an example?",
     "a": "From 1 January 2026 to 31 December 2026, exclusive, is 364 days. The year 2024 "
          "is a leap year, so the same span there is 365 days \u2014 the calculator counts "
          "the extra 29 February for you."},
    {"q": "How do I type the dates?",
     "a": "Use the format YYYY-MM-DD \u2014 for example 2026-03-01 for the 1st of March "
          "2026. Year first, then month, then day."},
    {"q": "Does the order of the dates matter?",
     "a": "No \u2014 if you put the later date first, the calculator still gives the size "
          "of the gap. It reports the number of days either way."},
    {"q": "Where would I use this?",
     "a": "Counting days until a deadline or holiday, working out someone's age in days, "
          "or measuring how long a project ran."},
])
