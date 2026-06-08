from core.faqs import register_faqs

register_faqs('osmotic-pressure', [
    {"q": 'What is osmotic pressure in plain terms?',
     "a": 'When pure solvent and a solution are separated by a membrane that only lets solvent through, solvent flows into the solution. Osmotic pressure is how hard you would have to push back to stop that flow. More concentrated solutions pull harder, so the pressure is higher.'},
    {"q": 'Where does it matter in real life?',
     "a": "In your cells (they must stay osmotically balanced or they swell or shrink), in IV drips (matched to blood), and in reverse-osmosis desalination that turns seawater into drinking water. It is one of biology and engineering's most important pressures."},
    {"q": 'Why is it useful for finding molecular weights?',
     "a": 'Because it depends only on the number of dissolved particles and is large even in dilute solutions. Dissolve a known mass, measure the osmotic pressure, and you can work out the moles and hence molar mass - great for big molecules like proteins.'},
    {"q": 'Why does the formula look like the gas law?',
     "a": "Because van 't Hoff found dissolved particles behave like a gas: π = CRT mirrors P = (n/V)RT. The particles spread out and 'push' just like gas molecules, which is why the same constant R appears."},
    {"q": 'How does the example reach about 2.46 atm?',
     "a": 'With C = 0.1, R = 0.0821, T = 300, the product is 0.1 × 0.0821 × 300 = 2.463 atm - about 2.5 times atmospheric pressure from a fairly dilute solution, showing how strong osmosis is.'},
])
