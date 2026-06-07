from core.faqs import register_faqs

register_faqs("density", [
    {"q": "What is density, in simple words?",
     "a": "Density is how heavy something is for its size. Imagine two boxes the same "
          "size: one full of cotton, one full of iron. The iron box is far heavier \u2014 it "
          "is denser, because much more stuff (mass) is packed into the same space."},
    {"q": "Why does the same size give a different mass for cotton, water or metal?",
     "a": "Because each material has its own density. Fill the same cup with cotton, "
          "water, or gold and you get wildly different masses \u2014 the gold is about 19 "
          "times heavier than the water, and the water far heavier than the cotton. Pick a "
          "material in the calculator and it fills in that material's density for you."},
    {"q": "Why does it say some objects are too heavy to lift?",
     "a": "Because mass is what your back actually has to lift. Safety experts (NIOSH) "
          "say about 23 kg is the most a single person should lift in good conditions. A "
          "small block of iron or gold can already pass that, while a big bundle of cotton "
          "stays light \u2014 the calculator shows the weight and whether it is in the safe "
          "range."},
    {"q": "Can you walk me through an example slowly?",
     "a": "Sure. Take a block of iron (density 7860 kg/m\u00b3) that is 0.001 cubic metres "
          "in size. Mass = density \u00d7 volume = 7860 \u00d7 0.001 = 7.86 kg. Its weight "
          "is about 7.86 \u00d7 9.81 = 77 newtons \u2014 heavy, but still safely liftable. "
          "Make it ten times bigger and it would be 78.6 kg, far too heavy to lift alone."},
    {"q": "Why do some things float and others sink?",
     "a": "It comes down to density compared with water (about 1000 kg/m\u00b3). Anything "
          "less dense floats; anything denser sinks. Cotton and wood float; iron and gold "
          "sink. The calculator notes which side of water your material is on."},
    {"q": "How do I find mass or volume instead of density?",
     "a": "Use the 'Solve for' box to pick mass or volume. Mass = density \u00d7 volume, "
          "and volume = mass \u00f7 density. If you pick a material, its density is filled "
          "in automatically, so you just need the other value."},
])
