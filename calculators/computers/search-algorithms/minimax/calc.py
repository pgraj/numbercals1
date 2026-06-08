"""Minimax - DSA explainer (auto-built to the pilot template).

Viz-first: the canvas teaches; compute() returns result, a stepped trace (each
frame carries a `line` into `algorithm` for the synced code highlight), the four
exam-fact cards plus a data-structure card, a definition line, and a disclaimer.
Never names a success field 'error'.
"""

from core.registry import register

_DISCLAIMER = 'Educational explainer. A small fixed game tree (you = MAX at the root and leaves, opponent = MIN in between) is evaluated; leaf numbers are outcome scores from your point of view.'
_DEF = "Minimax evaluates a game tree by assuming both players play optimally: at the maximising player's nodes it takes the maximum of the children's values, at the minimising player's nodes the minimum, propagating values from the leaves up to choose the root move with the best guaranteed outcome."
_DEF_SRC_NAME = 'Wikipedia - Minimax'
_DEF_SRC_URL = 'https://en.wikipedia.org/wiki/Minimax'

_ALGO_PSEUDO = [
        'function minimax(node, maximizing):',
        '    if node is a leaf: return its value',
        '    if maximizing:',
        '        return max(minimax(child, False) for child)',
        '    else:',
        '        return min(minimax(child, True) for child)',
]
_ALGO_PYTHON = [
        'def minimax(node, maximizing):',
        '    if node.is_leaf: return node.value',
        '    vals = [minimax(c, not maximizing) for c in node.children]',
        '    return max(vals) if maximizing else min(vals)',
]

_EXPLANATION = [
    {"heading": 'Time complexity', "body": 'O(b^d) - b moves per turn, d turns deep. The tree explodes exponentially, which is why pruning (next calculator) matters.'},
    {"heading": 'Space complexity', "body": 'O(b*d) - the depth-first recursion only holds one path plus siblings at each level.'},
    {"heading": 'Best data type', "body": 'Two-player, perfect-information, turn-based games - chess, checkers, tic-tac-toe, Connect Four.'},
    {"heading": 'Real-world example', "body": 'Planning your move while assuming your rival will make the best possible counter-move at every turn.'},
    {"heading": 'The data structure', "body": "Minimax explores a GAME TREE - nodes are game states, edges are moves, alternating between your turn (MAX) and the opponent's (MIN). It is a depth-first traversal that returns a value from every node; the tree structure and the alternating max/min rule together encode 'assume the opponent plays their best.'"},
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
    slug='minimax',
    name='Minimax',
    section="computers",
    topic='Data Structures and Algorithms (DSA)',
    sub='Adversarial & Game-Tree',
    order=1,
    summary='Assume the opponent plays perfectly; pick the move maximising your worst-case outcome.',
    formula='MAX nodes take the max of children; MIN nodes take the min; values propagate to the root',
    tags=['minimax', 'game tree', 'adversarial', 'max min', 'optimal play', 'O(b^d)'],
    viz_template="viz/minimax.html",
    related=['alpha-beta-pruning', 'monte-carlo-tree-search'],
)
def compute(leaves=None):
    lv = leaves if leaves else _LEAVES
    try:
        L=[[int(x) for x in row] for row in lv]
    except (TypeError,ValueError):
        return {"error":"Leaf values must be whole numbers.","steps":[],"disclaimer":_DISCLAIMER}
    if not L or not all(L): return {"error":"Provide leaf values for each branch.","steps":[],"disclaimer":_DISCLAIMER}
    frames=[]; steps=[]; evaluated=[]; minVals={}
    # MIN nodes take min of their leaves (MAX would pick a leaf, but here leaves are terminal so MIN minimises)
    for i,row in enumerate(L):
        for j,val in enumerate(row):
            evaluated.append([i,j])
            frames.append({"evaluated":[e[:] for e in evaluated],"pruned":[],"minVals":dict(minVals),"rootVal":None,"cur":[i,j],
                           "line":1,"msg":"evaluate leaf "+str(val)+" (branch "+str(i+1)+")"})
            steps.append({"label":"Leaf "+str(val),"math":"value = "+str(val),"note":"A terminal outcome score for branch "+str(i+1)+", from your (MAX) point of view."})
        mv=min(row); minVals[i]=mv
        frames.append({"evaluated":[e[:] for e in evaluated],"pruned":[],"minVals":dict(minVals),"rootVal":None,"cur":None,
                       "line":5,"msg":"MIN node "+str(i+1)+" = min"+str(row)+" = "+str(mv)})
        steps.append({"label":"MIN of branch "+str(i+1),"math":"min"+str(row)+" = "+str(mv),"note":"The opponent will pick the worst-for-you outcome here, so this branch is worth "+str(mv)+" to you."})
    rootVal=max(minVals.values()); best=max(minVals,key=minVals.get)
    frames.append({"evaluated":[e[:] for e in evaluated],"pruned":[],"minVals":dict(minVals),"rootVal":rootVal,"cur":None,
                   "line":3,"msg":"MAX (root) = max of MIN values = "+str(rootVal)})
    steps.append({"label":"MAX at root","math":"max"+str(list(minVals.values()))+" = "+str(rootVal),"note":"You pick the branch with the best guaranteed value: branch "+str(best+1)+", worth "+str(rootVal)+"."})
    result="Best guaranteed outcome is "+str(rootVal)+" by choosing branch "+str(best+1)+". Minimax assumes the opponent always replies optimally."
    return {"result":result,"leaves":L,"rootVal":rootVal,"best_branch":best,
            "frames":frames,"steps":steps,"algorithm":{"pseudocode":_ALGO_PSEUDO,"python":_ALGO_PYTHON},
            "explanation":_EXPLANATION,"law_statement":_DEF,
            "law_source_name":_DEF_SRC_NAME,"law_source_url":_DEF_SRC_URL,"disclaimer":_DISCLAIMER}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
