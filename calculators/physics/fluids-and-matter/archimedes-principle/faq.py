from core.faqs import register_faqs

register_faqs("archimedes-principle", [
    {"q": "What does Archimedes' Principle say, in simple words?",
     "a": "When you put something in water, it pushes some water out of the way. The water "
          "pushes back up on the object with a force equal to the weight of the water that "
          "got shoved aside. That upward push is called buoyancy \u2014 it is what makes "
          "things feel lighter in water."},
    {"q": "Why does a huge steel ship float but a steel nail sinks?",
     "a": "It is all about how much water you push aside. A ship is hollow and wide, so it "
          "shoves aside a massive amount of water \u2014 enough that the upward push equals "
          "the ship's weight, so it floats. Squash that steel into a nail and it pushes "
          "aside almost no water, so it sinks."},
    {"q": "Can you walk me through an example slowly?",
     "a": "Say an object pushes aside 0.001 cubic metres of water (density 1000 kg/m\u00b3), "
          "with gravity g = 9.81. Buoyant force = density \u00d7 volume \u00d7 g = 1000 "
          "\u00d7 0.001 \u00d7 9.81 = 9.81. So the water pushes up with 9.81 newtons."},
    {"q": "What is 'displaced volume'?",
     "a": "It is just the amount of fluid the object pushes out of the way. If the object "
          "is fully underwater, the displaced volume equals the object's own volume. If it "
          "floats, only the underwater part counts."},
    {"q": "Why do I feel lighter in a swimming pool?",
     "a": "Because the water is pushing up on you with a buoyant force, holding up a lot of "
          "your weight. You still weigh the same, but the upward push from the water means "
          "your legs have to support much less, so you feel light and can even float."},
    {"q": "Does the fluid have to be water?",
     "a": "No. It works in any fluid \u2014 including air and other liquids. A helium "
          "balloon rises because the air around it pushes up with more force than the "
          "balloon's weight. Denser fluids give a bigger upward push, which is why it is "
          "easier to float in very salty sea water."},
])
