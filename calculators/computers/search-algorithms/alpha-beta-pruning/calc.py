"""Alpha-Beta Pruning - DSA explainer (auto-built to the pilot template).

Viz-first: the canvas teaches; compute() returns result, a stepped trace (each
frame carries a `line` into `algorithm` for the synced code highlight), the four
exam-fact cards plus a data-structure card, a definition line, and a disclaimer.
Never names a success field 'error'.
"""

from core.registry import register

_DISCLAIMER = 'Educational explainer. The same fixed game tree as the minimax calculator is used so you can see which leaves alpha-beta skips (crossed out) while reaching the identical root value.'
_DEF = "Alpha-beta pruning runs minimax while tracking alpha (the best value MAX can already guarantee) and beta (the best MIN can guarantee); when a node's value can no longer affect the outcome (alpha >= beta), its remaining branches are pruned, yielding the identical result as minimax with far fewer evaluations."
_DEF_SRC_NAME = 'Wikipedia - Alpha-beta pruning'
_DEF_SRC_URL = 'https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning'

_ALGO_PSEUDO = [
        'function ab(node, alpha, beta, maximizing):',
        '    if leaf: return value',
        '    if maximizing: for each child:',
        '        alpha = max(alpha, ab(child, alpha, beta, False))',
        '        if alpha >= beta: break   # PRUNE',
        '    else: symmetric with beta and min',
]
_ALGO_PYTHON = [
        'def ab(node, a, b, maximizing):',
        '    if node.is_leaf: return node.value',
        '    if maximizing:',
        '        v = -inf',
        '        for c in node.children:',
        '            v = max(v, ab(c, a, b, False)); a = max(a, v)',
        '            if a >= b: break        # beta cutoff (prune)',
        '        return v',
        '    # MIN side is symmetric',
]

_EXPLANATION = [
    {"heading": 'Time complexity', "body": 'Down to O(b^(d/2)) with good move ordering - effectively doubling the search depth reachable for the same work compared to plain minimax.'},
    {"heading": 'Space complexity', "body": 'O(b*d) - same as minimax; alpha and beta are just two extra numbers per recursion level.'},
    {"heading": 'Best data type', "body": 'The same two-player perfect-information games as minimax, where deep search is needed - especially chess.'},
    {"heading": 'Real-world example', "body": 'Abandoning a plan the instant you realise it is already worse than another you have found - no need to explore it further.'},
    {"heading": 'The data structure', "body": 'Alpha-beta explores the same GAME TREE as minimax but carries two extra numbers down the recursion - alpha and beta - that bound what is still worth exploring. Those bounds are the data that let whole subtrees be discarded the moment they cannot influence the answer.'},
]

# Game tree leaves grouped by MIN node (3 MIN nodes, each with 3 leaves).
_LEAVES = [[3, 12, 8], [2, 4, 6], [14, 5, 2]]



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
    slug='alpha-beta-pruning',
    name='Alpha-Beta Pruning',
    section="computers",
    topic='Data Structures and Algorithms (DSA)',
    sub='Adversarial & Game-Tree',
    order=2,
    summary='Minimax that skips branches it can prove cannot change the result - same answer, far less work.',
    formula='track alpha (best for MAX) and beta (best for MIN); prune when alpha >= beta',
    tags=['alpha-beta', 'pruning', 'minimax', 'game tree', 'chess', 'O(b^(d/2))'],
    viz_template="viz/alpha-beta-pruning.html",
    related=['minimax', 'monte-carlo-tree-search'],
)
def compute(leaves=None):
    lv = leaves if leaves else _LEAVES
    try:
        L=[[int(x) for x in row] for row in lv]
    except (TypeError,ValueError):
        return {"error":"Leaf values must be whole numbers.","steps":[],"disclaimer":_DISCLAIMER}
    if not L or not all(L): return {"error":"Provide leaf values for each branch.","steps":[],"disclaimer":_DISCLAIMER}
    frames=[]; steps=[]; evaluated=[]; pruned=[]; minVals={}
    INF=float("inf"); alpha=-INF; beta=INF; root=-INF; pruned_count=0
    for i,row in enumerate(L):
        # MIN node i, with current alpha
        b_local=INF
        cut=False
        for j,val in enumerate(row):
            if cut:
                pruned.append([i,j]); pruned_count+=1
                frames.append({"evaluated":[e[:] for e in evaluated],"pruned":[p[:] for p in pruned],"minVals":dict(minVals),"rootVal":None,"cur":None,
                               "line":4,"msg":"prune leaf "+str(val)+" (branch "+str(i+1)+") - cannot change the result"})
                steps.append({"label":"Prune","math":"alpha "+str(alpha)+" >= beta "+str(b_local),"note":"MAX already has "+str(alpha)+" guaranteed; this MIN branch can only go lower, so the rest is skipped."})
                continue
            evaluated.append([i,j]); b_local=min(b_local,val)
            frames.append({"evaluated":[e[:] for e in evaluated],"pruned":[p[:] for p in pruned],"minVals":dict(minVals),"rootVal":None,"cur":[i,j],
                           "line":2,"msg":"evaluate leaf "+str(val)+"; branch-min so far "+str(b_local)})
            steps.append({"label":"Leaf "+str(val),"math":"branch min -> "+str(b_local),"note":"MIN keeps the lowest seen ("+str(b_local)+") in branch "+str(i+1)+"."})
            if b_local<=alpha:
                cut=True  # remaining leaves in this branch are pruned (alpha cutoff)
        minVals[i]=b_local
        frames.append({"evaluated":[e[:] for e in evaluated],"pruned":[p[:] for p in pruned],"minVals":dict(minVals),"rootVal":None,"cur":None,
                       "line":3,"msg":"MIN node "+str(i+1)+" = "+str(b_local)+"; update MAX guarantee"})
        root=max(root,b_local); alpha=max(alpha,root)
        steps.append({"label":"Branch "+str(i+1)+" done","math":"MIN = "+str(b_local)+", alpha -> "+str(alpha),"note":"MAX now guarantees at least "+str(alpha)+"."})
    rootVal=root; best=max(minVals,key=minVals.get)
    frames.append({"evaluated":[e[:] for e in evaluated],"pruned":[p[:] for p in pruned],"minVals":dict(minVals),"rootVal":rootVal,"cur":None,
                   "line":3,"msg":"root value = "+str(rootVal)+" ("+str(pruned_count)+" leaves pruned)"})
    steps.append({"label":"Root","math":"value = "+str(rootVal),"note":"Same answer as minimax, but "+str(pruned_count)+" leaf evaluation"+("s" if pruned_count!=1 else "")+" skipped."})
    result="Root value "+str(rootVal)+" (branch "+str(best+1)+") - identical to minimax, but "+str(pruned_count)+" leaf"+("s" if pruned_count!=1 else "")+" were pruned and never evaluated."
    return {"result":result,"leaves":L,"rootVal":rootVal,"best_branch":best,"pruned_count":pruned_count,
            "frames":frames,"steps":steps,"algorithm":{"pseudocode":_ALGO_PSEUDO,"python":_ALGO_PYTHON},
            "explanation":_EXPLANATION,"law_statement":_DEF,
            "law_source_name":_DEF_SRC_NAME,"law_source_url":_DEF_SRC_URL,"disclaimer":_DISCLAIMER}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
