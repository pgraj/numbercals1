from core.faqs import register_faqs

register_faqs("saas-growth-forecast", [
    {"q": "What is MRR?",
     "a": "Monthly Recurring Revenue, the predictable subscription income a SaaS business earns each month. ARR is simply MRR times twelve."},
    {"q": "How does the forecast work?",
     "a": "Each month it shrinks the existing MRR by the churn rate, then adds the new MRR you win, and repeats. That recursion is the heart of SaaS growth modelling."},
    {"q": "Why does churn matter so much?",
     "a": "Because it works against you every single month on a growing base. Even modest churn can cap growth, since you must replace lost revenue before adding any net new."},
    {"q": "What is the trajectory output?",
     "a": "The MRR at the end of each month, so you can see the growth curve, whether it accelerates, plateaus, or stalls as churn catches up with new sales."},
    {"q": "Is constant new MRR realistic?",
     "a": "It is a simplification. Real new MRR varies with seasons, marketing and market size. Try different values to bracket optimistic and cautious scenarios."},
])
