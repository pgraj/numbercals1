from core.faqs import register_faqs

register_faqs("newtons-second-law", [
    {"q": "What does Newton's second law say, in plain words?",
     "a": "If you push something, it speeds up. The harder you push, the faster it speeds "
          "up. And the heavier the thing is, the less it speeds up for the same push. In "
          "short: force = mass \u00d7 acceleration, written F = m a."},
    {"q": "What is acceleration?",
     "a": "Acceleration just means how quickly the speed is changing. A car going from "
          "still to fast very quickly has high acceleration. It is not the speed itself \u2014 "
          "it is how fast the speed is building up (or dropping)."},
    {"q": "Can you walk me through an example slowly?",
     "a": "Yes. Push a 3 kg toy car so it accelerates at 4 m/s2 (its speed grows by 4 "
          "metres per second, every second). Force = mass \u00d7 acceleration = 3 \u00d7 4 "
          "= 12. So you needed 12 newtons of push. A newton (N) is just the unit for "
          "force."},
    {"q": "How do I find mass or acceleration instead of force?",
     "a": "Just rearrange the same formula. To get mass, divide force by acceleration. To "
          "get acceleration, divide force by mass. Pick what you want in the 'Solve for' "
          "box and the calculator does the rearranging for you."},
    {"q": "Why does the same push move a heavy thing less?",
     "a": "Because the push has to share itself out over more mass. Kick a football and it "
          "flies; kick a bowling ball the same way and it barely moves and your foot hurts. "
          "Same force, much more mass, so much less acceleration."},
    {"q": "How is this connected to the first law?",
     "a": "The second law contains the first one. If the force is zero, then acceleration "
          "is zero too \u2014 meaning the speed does not change. That is exactly what the "
          "first law says: no force, no change in motion."},
])
