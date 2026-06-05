from core.faqs import register_faqs

register_faqs("heart-rate-zones", [
    {"q": "What are heart rate training zones?",
     "a": "They are five bands of exercise intensity, each defined as a percentage range of your "
          "maximum heart rate. Lower zones feel easy and build endurance; higher zones are hard and "
          "build speed and power. Training in the right zone for your goal makes exercise more "
          "effective than just going as hard as possible every time."},
    {"q": "How is maximum heart rate estimated?",
     "a": "The simplest estimate is 220 minus your age — so a 40-year-old has an estimated max of "
          "about 180 beats per minute. It is only an average; real maximums vary by 10 to 20 beats "
          "between people of the same age, and the only exact way to know yours is a supervised "
          "maximal test."},
    {"q": "What is the Karvonen method?",
     "a": "Karvonen makes the zones more personal by using your heart-rate reserve — the gap between "
          "your maximum and your resting heart rate. Each zone percentage is applied to that reserve "
          "and your resting rate is added back. Because a fit person has a lower resting rate, this "
          "gives zone targets tailored to their fitness rather than to age alone. Add a resting heart "
          "rate and the calculator switches to this method automatically."},
    {"q": "How do I read the chart?",
     "a": "The bar is split into five coloured segments, from the easy warm-up zone on the left to the "
          "maximal red-line zone on the right. Each segment is labelled with its intensity range and "
          "the heart-rate window in beats per minute, so you can see exactly which pulse range each "
          "kind of training lives in."},
    {"q": "Where is this used in real life?",
     "a": "Runners, cyclists, and gym-goers use zones to steer training: easy aerobic base work in the "
          "lower zones, threshold and interval work higher up. Fitness watches show your live zone "
          "during a workout. If you have a heart condition or are new to intense exercise, check with "
          "a doctor before training in the higher zones."},
])
