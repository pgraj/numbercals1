"""Monte Carlo Tree Search (MCTS) - DSA explainer (auto-built to the pilot template).

Viz-first: the canvas teaches; compute() returns result, a stepped trace (each
frame carries a `line` into `algorithm` for the synced code highlight), the four
exam-fact cards plus a data-structure card, a definition line, and a disclaimer.
Never names a success field 'error'.
"""

from core.registry import register

_DISCLAIMER = 'Educational explainer. A few candidate first moves each have a hidden underlying win probability; the demo runs random simulations and shows the win-rate estimates converging. Results vary run to run, which is the nature of a randomised method.'
_DEF = 'Monte Carlo Tree Search builds a search tree incrementally through four repeated steps - selection (using UCB1 to balance exploration and exploitation), expansion, random simulation (rollout) to a result, and backpropagation of that result - converging on the move with the best win rate as simulations increase.'
_DEF_SRC_NAME = 'Wikipedia - Monte Carlo tree search'
_DEF_SRC_URL = 'https://en.wikipedia.org/wiki/Monte_Carlo_tree_search'

_ALGO_PSEUDO = [
        'repeat many times:',
        '    SELECT: descend using UCB1 (balance win-rate vs exploration)',
        '    EXPAND: add a new child node',
        '    SIMULATE: play out a random game to the end',
        '    BACKPROPAGATE: add the result to every node on the path',
        'finally: pick the move with the most visits / best win rate',
]
_ALGO_PYTHON = [
        'for _ in range(simulations):',
        '    leaf = select(root)          # UCB1 down the tree',
        '    child = expand(leaf)',
        '    result = rollout(child)      # random play-out',
        '    backpropagate(child, result) # update wins/visits',
        'return max(root.children, key=lambda c: c.visits)',
]

_EXPLANATION = [
    {"heading": 'Time complexity', "body": 'Tunable - more simulations give stronger, more reliable estimates. You trade compute time for quality; there is no fixed cost.'},
    {"heading": 'Space complexity', "body": 'Grows with the tree - it only stores the nodes it actually visits, expanding gradually.'},
    {"heading": 'Best data type', "body": 'Huge decision spaces where full calculation is impossible and outcomes can be simulated - Go, complex board games.'},
    {"heading": 'Real-world example', "body": "Trying many 'what if I played this?' scenarios in your head and going with the move that usually works out best."},
    {"heading": 'The data structure', "body": 'MCTS grows a GAME TREE annotated with STATISTICS - each node stores how many times it was visited and how many of those simulations led to a win. Unlike minimax, which needs an evaluation of every position, MCTS learns which moves are good purely from the win/visit counts it accumulates.'},
]



def _f(x):
    if isinstance(x, float) and x.is_integer():
        return str(int(x))
    return str(x)


def _bubble_sort(arr):
    """Ascending bubble sort, recording each comparison/swap for the sort animation."""
    a = list(arr)
    moves = []
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            do_swap = a[j] > a[j + 1]
            moves.append({"i": j, "j": j + 1, "swap": bool(do_swap), "snapshot": list(a), "line": -1})
            if do_swap:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    moves.append({"i": -1, "j": -1, "swap": False, "snapshot": list(a), "line": -1})
    return a, moves


def _finish(arr, tgt, found, frames, steps, sort_moves=None, input_array=None):
    if found >= 0:
        result = "Found " + _f(tgt) + " at index " + str(found) + " in " + str(len(frames)) + " probe" + ("s" if len(frames) != 1 else "") + "."
    else:
        result = _f(tgt) + " is not in the list (after " + str(len(frames)) + " probe" + ("s" if len(frames) != 1 else "") + ")."
    out = {"result": result, "target": tgt, "array": arr, "found_index": found,
            "frames": frames, "steps": steps,
            "algorithm": {"pseudocode": _ALGO_PSEUDO, "python": _ALGO_PYTHON},
            "explanation": _EXPLANATION, "law_statement": _DEF,
            "law_source_name": _DEF_SRC_NAME, "law_source_url": _DEF_SRC_URL,
            "disclaimer": _DISCLAIMER}
    if sort_moves is not None:
        out["sort_moves"] = sort_moves
        out["input_array"] = input_array if input_array is not None else arr
    return out


@register(
    slug='monte-carlo-tree-search',
    name='Monte Carlo Tree Search (MCTS)',
    section="computers",
    topic='Data Structures and Algorithms (DSA)',
    sub='Adversarial & Game-Tree',
    order=3,
    summary='Play many random simulated games and favour the moves that win most often.',
    formula='repeat: Select (UCB1) -> Expand -> Simulate (random rollout) -> Backpropagate wins',
    tags=['mcts', 'monte carlo', 'ucb1', 'rollout', 'alphago', 'simulation'],
    viz_template="viz/monte-carlo-tree-search.html",
    related=['minimax', 'alpha-beta-pruning', 'beam-search'],
)
def compute(moves=None, simulations=30):
    import random, math
    mv = moves if moves else ["A","B","C"]
    try:
        names=[str(m).strip() for m in mv if str(m).strip()][:4]
        sims=max(4,min(80,int(simulations)))
    except (TypeError,ValueError):
        return {"error":"Provide candidate moves and a simulation count.","steps":[],"disclaimer":_DISCLAIMER}
    if not names: return {"error":"Add at least two candidate moves.","steps":[],"disclaimer":_DISCLAIMER}
    if len(names)<2: names=names+["B"]
    # hidden true win-probabilities (deterministic per position by name hash, for reproducibility)
    def truep(nm):
        h=sum(ord(c) for c in nm)
        return 0.35 + (h % 50)/100.0   # 0.35 .. 0.84
    truth={nm:truep(nm) for nm in names}
    rng=random.Random(42)
    wins={nm:0 for nm in names}; visits={nm:0 for nm in names}
    frames=[]; steps=[]
    order=[]
    for t in range(sims):
        # SELECT via UCB1
        total=sum(visits.values())+1
        def ucb(nm):
            if visits[nm]==0: return float("inf")
            return wins[nm]/visits[nm] + 1.4*math.sqrt(math.log(total)/visits[nm])
        choice=max(names,key=ucb)
        # SIMULATE rollout
        win = 1 if rng.random()<truth[choice] else 0
        visits[choice]+=1; wins[choice]+=win
        rate={nm:(round(wins[nm]/visits[nm],2) if visits[nm] else 0.0) for nm in names}
        # only record a frame every few sims to keep animation digestible
        if t<6 or t%max(1,sims//12)==0 or t==sims-1:
            frames.append({"choice":choice,"win":win,"visits":dict(visits),"wins":dict(wins),"rate":rate,"sim":t+1,"line":2,
                           "msg":"sim "+str(t+1)+": try "+choice+" -> "+("WIN" if win else "loss")})
        if t<6:
            steps.append({"label":"Sim "+str(t+1),"math":"play "+choice+" -> "+("win" if win else "loss"),"note":"UCB1 chose "+choice+" (balancing its win-rate against how little it has been tried); a random rollout gave a "+("win" if win else "loss")+", updating its stats."})
    best=max(names,key=lambda nm: (visits[nm], wins[nm]/visits[nm] if visits[nm] else 0))
    final_rate={nm:(round(wins[nm]/visits[nm],2) if visits[nm] else 0.0) for nm in names}
    steps.append({"label":"Decision","math":"most-visited / best win-rate move","note":"After "+str(sims)+" simulations, move "+best+" has the strongest record ("+str(wins[best])+"/"+str(visits[best])+" wins). MCTS picks it."})
    result="After "+str(sims)+" simulations, MCTS favours move "+best+" (win rate "+str(final_rate[best])+", visited "+str(visits[best])+" times). More simulations sharpen the estimate."
    return {"result":result,"names":names,"final_rate":final_rate,"visits":visits,"wins":wins,"best":best,
            "frames":frames,"steps":steps,"algorithm":{"pseudocode":_ALGO_PSEUDO,"python":_ALGO_PYTHON},
            "explanation":_EXPLANATION,"law_statement":_DEF,
            "law_source_name":_DEF_SRC_NAME,"law_source_url":_DEF_SRC_URL,"disclaimer":_DISCLAIMER}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
