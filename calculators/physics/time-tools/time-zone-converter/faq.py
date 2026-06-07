from core.faqs import register_faqs
register_faqs("time-zone-converter", [
    {"q": "What does this calculator do?",
     "a": "It takes a date and time in one city and tells you what the clock reads at that "
          "same moment in another city \u2014 useful for booking calls or flights across "
          "the world."},
    {"q": "Does it handle daylight saving time?",
     "a": "Yes, automatically. It uses the world time-zone database, which knows when each "
          "place switches to summer time, so the conversion is correct for the exact date "
          "you pick \u2014 not just a fixed offset."},
    {"q": "Can you show an example?",
     "a": "9:00 in the morning in Sydney on 1 June 2026 is just after midnight in London "
          "that same day (London is on summer time then, UTC+1). The tool shows the "
          "converted time and the offset from UTC."},
    {"q": "Why does the date sometimes change?",
     "a": "Because zones can be many hours apart. If converting pushes the time past "
          "midnight, the calendar date shifts to the day before or after \u2014 which is "
          "why a call can land 'tomorrow' for the other person."},
    {"q": "How do I enter the time?",
     "a": "Pick the two cities from the list, then type the date as YYYY-MM-DD and the "
          "time as HH:MM in 24-hour form (for example 14:30 for half past two in the "
          "afternoon)."},
    {"q": "What does UTC mean?",
     "a": "UTC is the world's reference time (roughly the time in London in winter). Every "
          "zone is described as an offset from UTC \u2014 for example UTC+10 is ten hours "
          "ahead. The result shows the target city's offset so you can see the difference."},
])
