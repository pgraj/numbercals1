from core.faqs import register_faqs

register_faqs("boyles-law", [
    {"q": "What does Boyle's Law say, in simple words?",
     "a": "If you squeeze a trapped gas into a smaller space, its pressure goes up. Give "
          "it more room and the pressure drops. As long as the temperature stays the same, "
          "pressure and volume always trade off against each other."},
    {"q": "How do I use this calculator?",
     "a": "Pick what you want to find in the 'Solve for' box \u2014 P\u2081, V\u2081, "
          "P\u2082 or V\u2082 \u2014 then type in the other three values. The calculator "
          "works out the missing one using P\u2081V\u2081 = P\u2082V\u2082. The '1' is "
          "before and the '2' is after."},
    {"q": "Can you walk me through an example slowly?",
     "a": "Say a gas starts at pressure 100 and volume 2, and you squeeze it to volume 1. "
          "What is the new pressure? Pressure times volume stays equal: 100 \u00d7 2 = "
          "P\u2082 \u00d7 1, so 200 = P\u2082. The pressure doubled because the volume "
          "halved."},
    {"q": "What is the container option and the 'would burst' warning?",
     "a": "The gas law itself never stops \u2014 but a real container can. If you choose a "
          "balloon, syringe or steel cylinder, the calculator checks whether your final "
          "pressure goes past what that container can hold, and warns you if it would "
          "burst. Those burst values are rough, for illustration \u2014 not exact "
          "engineering numbers."},
    {"q": "What units should I use?",
     "a": "Any units you like \u2014 but keep them the same on both sides. If you measure "
          "pressure in pascals, use pascals for both pressures. If volume is in litres, "
          "use litres for both. Because it is a ratio, the units cancel out. (Note: the "
          "container burst check assumes the pressures are in pascals.)"},
    {"q": "Where do I see Boyle's Law in real life?",
     "a": "Squeeze a sealed packet of chips and it gets firmer \u2014 you shrank the volume "
          "so the pressure rose. Pump a bike tyre and the trapped air pushes back harder "
          "as it compresses. Scuba divers rely on it too, as the air in their gear changes "
          "volume with depth."},
])
