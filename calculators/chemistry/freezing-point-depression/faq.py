from core.faqs import register_faqs

register_faqs('freezing-point-depression', [
    {"q": 'Why does adding solute lower the freezing point?',
     "a": 'Dissolved particles get in the way of solvent molecules trying to line up into solid ice, so the solution must be cooled further before it can freeze. The more particles, the bigger the drop.'},
    {"q": 'Where is this used day to day?',
     "a": 'Salting icy roads and paths, antifreeze in car engines, keeping seawater liquid below 0°C, and making ice cream with a salt-ice bath. Anywhere you want a liquid to stay liquid in the cold.'},
    {"q": 'What is the freezing constant K_f?',
     "a": 'A property of the solvent - how many degrees the freezing point drops per unit of molality. For water it is 1.86, so a 1 molal solution freezes near -1.86°C.'},
    {"q": 'How does this find molecular weights?',
     "a": 'Dissolve a known mass, measure how far the freezing point drops, and work backwards to the moles and molar mass. This is called cryoscopy.'},
    {"q": "Why use molality and sometimes a van 't Hoff factor?",
     "a": "Molality is temperature-independent, which matters since freezing involves temperature. For salts that split into ions you multiply by the van 't Hoff factor - 1 molal salt makes about 2 molal in particles, doubling the drop."},
])
