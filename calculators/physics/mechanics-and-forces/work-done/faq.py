from core.faqs import register_faqs

register_faqs("work-done", [
    {"q": "What does 'work' mean in physics?",
     "a": "In physics, you do work when you push or pull something and it actually moves. "
          "Push a box across the floor \u2014 that is work. The bigger the push and the "
          "farther it moves, the more work you do. If nothing moves, you did zero work, no "
          "matter how hard you strained."},
    {"q": "Why is there an angle in the formula?",
     "a": "Because the direction you push matters. Only the part of your push that goes the "
          "same way the object moves actually helps. If you pull a sled with a rope at an "
          "angle, some of your pull lifts the rope upward and is wasted; only the part "
          "pulling forward does the work. The 'cos' in the formula measures how much of "
          "your push points the right way."},
    {"q": "What happens at 0, 60 and 90 degrees?",
     "a": "At 0 degrees you push straight along the movement \u2014 all your force counts. "
          "At 60 degrees, only half of it counts. At 90 degrees (pushing sideways to the "
          "movement) none of it counts, so you do zero work. That is why carrying a heavy "
          "bag flat across a room does no work against gravity \u2014 you lift it straight "
          "up, but you walk sideways."},
    {"q": "Can you walk me through an example slowly?",
     "a": "Yes. Push a box with 10 N of force, straight along the floor (angle = 0), and "
          "it moves 5 m. The formula is Work = force \u00d7 distance \u00d7 cos(angle). At "
          "0 degrees, cos is 1, so it is just 10 \u00d7 5 \u00d7 1 = 50. You did 50 joules "
          "of work. (A newton, N, is a unit of push; a joule, J, is the unit of work and "
          "energy.)"},
    {"q": "Can work be negative?",
     "a": "Yes, and it is a neat idea. If a force pushes against the movement \u2014 like "
          "friction dragging on a sliding box, or brakes slowing a car \u2014 it does "
          "negative work, meaning it takes energy away instead of adding it. That is how "
          "brakes stop you."},
    {"q": "Does it matter if I use degrees or radians for the angle?",
     "a": "No. Degrees and radians are just two ways of writing the same angle, like "
          "writing a date as '1 Jan' or '01/01'. Use the toggle to switch. The same angle "
          "gives the same answer either way \u2014 60 degrees and pi/3 radians are the same "
          "turn, so they give identical work."},
])
