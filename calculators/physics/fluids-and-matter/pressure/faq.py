from core.faqs import register_faqs

register_faqs("pressure", [
    {"q": "What is pressure, in simple words?",
     "a": "Pressure is how concentrated a push is \u2014 how much force is squeezed onto "
          "each bit of area. Press your finger gently on a table: low pressure. Press the "
          "same finger on a sharp pin with the same force: huge pressure on that tiny "
          "point, which is why it hurts."},
    {"q": "Why does a sharp knife cut better than a blunt one?",
     "a": "Because a sharp edge is very thin, so it puts your pushing force onto a tiny "
          "area. Small area with the same force means very high pressure, enough to cut. A "
          "blunt knife spreads the force over a wider edge, so the pressure is too low to "
          "slice."},
    {"q": "Can you walk me through an example slowly?",
     "a": "Yes. Push with a force of 20 N onto an area of 0.5 square metres. Pressure = "
          "force \u00f7 area = 20 \u00f7 0.5 = 40. So the pressure is 40 pascals (Pa). A "
          "pascal just means one newton pushing on one square metre."},
    {"q": "How do I find force or area instead?",
     "a": "Rearrange the same formula. Force = pressure \u00d7 area, and area = force "
          "\u00f7 pressure. Choose what you want in the 'Solve for' box and it works it "
          "out for you."},
    {"q": "Where do I see pressure in real life?",
     "a": "Snowshoes spread your weight over a big area so the pressure is low and you do "
          "not sink into snow. Camels have wide feet for the same reason in sand. High "
          "heels do the opposite \u2014 all the weight on a tiny tip makes a big dent."},
])
