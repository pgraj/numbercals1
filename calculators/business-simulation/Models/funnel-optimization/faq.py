from core.faqs import register_faqs

register_faqs("funnel-optimization", [
    {"q": "What is a conversion funnel?",
     "a": "The series of steps a visitor passes through to convert, like visit, sign-up, then purchase. Each step has its own conversion rate, and they multiply together."},
    {"q": "Why do the stages multiply?",
     "a": "Because you only reach a later stage if you passed the earlier ones. Three stages of 40%, 50% and 30% give an overall rate of just 6%, since each leak compounds."},
    {"q": "Which stage should I fix first?",
     "a": "Often the worst-performing or highest-traffic one, since improving it flows through to everything downstream. The calculator lets you test improving any single stage."},
    {"q": "Why is fixing one stage so powerful?",
     "a": "Because the gain multiplies through the rest of the funnel and applies to all your traffic. A few points on one weak step can lift total conversions noticeably."},
    {"q": "What does this miss?",
     "a": "It assumes stages are independent and rates are stable. In reality, changing one step can affect others, so test real changes rather than trusting the model alone."},
])
