from core.faqs import register_faqs
register_faqs("ohms-law", [
    {"q": "What is Ohm's Law, in simple words?",
     "a": "It links three things in a circuit: voltage (the electrical push), current (how "
          "much electricity flows), and resistance (how much the circuit fights the flow). "
          "The rule is voltage = current \u00d7 resistance, or V = I \u00d7 R."},
    {"q": "Can you use a everyday picture?",
     "a": "Think of water in a pipe. Voltage is how hard you push the water, current is how "
          "much water flows, and resistance is how narrow the pipe is. Push harder and more "
          "flows; use a narrower pipe and less flows. Electricity behaves the same way."},
    {"q": "Can you walk through an example?",
     "a": "Say a circuit has a current of 2 amperes through a 5-ohm resistor. Voltage = "
          "current \u00d7 resistance = 2 \u00d7 5 = 10 volts. So there are 10 volts across "
          "that resistor."},
    {"q": "How do I find current or resistance instead?",
     "a": "Rearrange the same formula. Current = voltage \u00f7 resistance, and resistance "
          "= voltage \u00f7 current. Pick what you want in the 'Solve for' box and the "
          "calculator does the rearranging."},
    {"q": "What are the units?",
     "a": "Voltage is measured in volts (V), current in amperes or 'amps' (A), and "
          "resistance in ohms (the \u03a9 symbol). One volt pushing across one ohm makes "
          "one amp flow."},
    {"q": "Where do I see Ohm's Law in real life?",
     "a": "Everywhere electricity is used \u2014 it sets how bright a bulb is, how fast a "
          "phone charges, and why thin wires get hot. Engineers use it constantly to "
          "choose the right resistor or wire for a job."},
])
