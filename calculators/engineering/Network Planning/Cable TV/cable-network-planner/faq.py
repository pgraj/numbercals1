from core.faqs import register_faqs

register_faqs("cable-network-planner", [
    {"q": "What does this tool actually do?",
     "a": "You drop a headend and consumer nodes on a map, and it sketches a first-pass cable-TV layout: it links them with a minimum-spanning-tree backbone, follows real roads (via OSRM), adjusts cable length for terrain (via Open-Elevation), models RG-11 RF loss to place amplifiers where they are physically needed, and prints a costed bill of materials. It is a learning and early-sketch aid, not a deployable design."},
    {"q": "Why does it place amplifiers where it does, instead of at fixed intervals?",
     "a": "It uses real RF physics. RG-11 hardline trunk loses about 6 dB per 100 m at the 750 MHz design frequency, so the tool walks each cable run accumulating loss and inserts an amplifier the moment cumulative loss exceeds the budget you set (default 30 dB). After each amplifier the budget resets. That is how amplifiers are actually spaced in a real HFC network."},
    {"q": "What is a Minimum Spanning Tree and why use one here?",
     "a": "An MST is the cheapest set of links that connects every node with no loops. For a cable backbone that means the least total trunk cable needed to reach every consumer from the headend. The tool builds it with Kruskal's algorithm, then refines each chosen link with road routing and terrain so the length estimate is realistic rather than straight-line."},
    {"q": "Why might the routes or terrain look wrong sometimes?",
     "a": "Road routing (OSRM) and elevation (Open-Elevation) are free public services that occasionally time out or rate-limit. When routing fails the tool falls back to a straight-line distance; when elevation fails it assumes flat ground. The segment table flags which data source was used for each link, so you can see where a fallback happened."},
    {"q": "Can I trust the cost estimates for a real budget?",
     "a": "No. The prices are order-of-magnitude figures in your chosen currency, useful only for the earliest back-of-envelope thinking. Real cable, amplifier, labour and permitting costs vary enormously by country, supplier, terrain and project scale. Always obtain current supplier quotes and a licensed engineer's design before committing money or building anything."},
])
