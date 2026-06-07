from core.faqs import register_faqs

register_faqs("batting-strike-rate-impact", [
    {"q": "What is strike rate?",
     "a": "Runs scored per 100 balls faced. A strike rate of 150 means 150 runs from every 100 balls, which is brisk scoring."},
    {"q": "Why does strike rate matter more in shorter formats?",
     "a": "Because balls are scarce in T20 and one-day cricket, so scoring fast is vital. In Test cricket, occupying the crease can matter more than tempo, so a lower strike rate is fine."},
    {"q": "Is a high strike rate always good?",
     "a": "Not on its own. Scoring fast but getting out cheaply can hurt the team. Strike rate is best read alongside the runs actually made and the match situation."},
    {"q": "How is it different from batting average?",
     "a": "Average is runs per dismissal (how many you make); strike rate is runs per 100 balls (how fast). A player can have a high average but a slow strike rate, or vice versa."},
    {"q": "Is this the standard formula?",
     "a": "Yes. Runs divided by balls faced times 100 is the universally used definition of batting strike rate."},
])
