"""IDA* (Iterative Deepening A*) - DSA explainer (auto-built to the pilot template).

Viz-first: the canvas teaches; compute() returns result, a stepped trace (each
frame carries a `line` into `algorithm` for the synced code highlight), the four
exam-fact cards plus a data-structure card, a definition line, and a disclaimer.
Never names a success field 'error'.
"""

from core.registry import register

_DISCLAIMER = "Educational explainer. Each round's f-threshold is shown; nodes whose f exceeds the current threshold are cut off, and the threshold rises each round until the goal is reached."
_DEF = 'IDA* performs repeated depth-first searches, each bounded by an f = g + h threshold; whenever a branch exceeds the threshold it is abandoned, and the threshold is raised to the smallest exceeded f for the next round, giving A*-optimal results with memory proportional only to the search depth.'
_DEF_SRC_NAME = 'Wikipedia - Iterative deepening A*'
_DEF_SRC_URL = 'https://en.wikipedia.org/wiki/Iterative_deepening_A*'

_ALGO_PSEUDO = [
        'threshold = h(start)',
        'repeat:',
        '    do a DFS, pruning any node with f = g+h > threshold',
        '    if goal reached within threshold: return path',
        '    threshold = smallest f that exceeded it',
]
_ALGO_PYTHON = [
        'threshold = h(start)',
        'while True:',
        '    found, next_t = dfs(start, 0, threshold)',
        '    if found: return path',
        '    if next_t == inf: return None   # no solution',
        '    threshold = next_t',
]

_EXPLANATION = [
    {"heading": 'Time complexity', "body": 'Comparable to A* in nodes expanded, but it re-expands nodes each round, so it does more repeated work in exchange for memory.'},
    {"heading": 'Space complexity', "body": "O(depth) - only the current path is stored, dramatically less than A*'s O(V) frontier."},
    {"heading": 'Best data type', "body": 'Optimal pathfinding when memory is tight - puzzle solvers, embedded systems.'},
    {"heading": 'Real-world example', "body": "Solving a Rubik's Cube or 15-puzzle, where the search tree is astronomically wide and A*'s memory would be impossible."},
    {"heading": 'The data structure', "body": 'IDA* explores a WEIGHTED GRAPH using a STACK (depth-first recursion) rather than a priority queue - that is the whole memory saving. It keeps only the current path in memory, not a huge frontier, repeating bounded DFS passes with a rising f = g + h cutoff until the goal is found.'},
]

_POS = {
    "S": (0.10, 0.50), "A": (0.32, 0.20), "B": (0.32, 0.78),
    "C": (0.55, 0.35), "D": (0.55, 0.68), "E": (0.78, 0.30), "G": (0.90, 0.55),
}
_EDGES = {
    "S": [("A", 2), ("B", 3)],
    "A": [("S", 2), ("C", 3), ("E", 6)],
    "B": [("S", 3), ("D", 4)],
    "C": [("A", 3), ("D", 2), ("E", 2)],
    "D": [("B", 4), ("C", 2), ("G", 5)],
    "E": [("A", 6), ("C", 2), ("G", 3)],
    "G": [("E", 3), ("D", 5)],
}
import math
def _hdist(a, b):
    ax, ay = _POS[a]; bx, by = _POS[b]
    return round(math.hypot(ax - bx, ay - by) * 12, 1)



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
    slug='ida-star',
    name='IDA* (Iterative Deepening A*)',
    section="computers",
    topic='Data Structures and Algorithms (DSA)',
    sub='Informed & Heuristic',
    order=4,
    summary='A* that uses far less memory by searching repeatedly with a growing cost limit.',
    formula='repeat: depth-first search bounded by f <= threshold; raise threshold to the smallest f that exceeded it',
    tags=['ida star', 'iterative deepening', 'memory efficient', 'heuristic', 'optimal', 'puzzles'],
    viz_template="viz/ida-star.html",
    related=['a-star-search', 'dijkstra', 'depth-first-search'],
)
def compute(start="S", goal="G"):
    start=str(start).strip().upper(); goal=str(goal).strip().upper()
    if start not in _EDGES or goal not in _EDGES:
        return {"error":"Start and goal must be nodes S, A-E, or G.","steps":[],"disclaimer":_DISCLAIMER}
    INF=float("inf")
    hvals={n:_hdist(n,goal) for n in _POS}
    frames=[]; steps=[]; done=False; final_path=[]
    threshold=hvals[start]; rnd=0
    while not done and rnd<8:
        rnd+=1
        visited_this=[]
        steps.append({"label":"Round "+str(rnd),"math":"threshold f <= "+str(round(threshold,1)),"note":"Run a depth-first search, abandoning any node whose f = g+h exceeds "+str(round(threshold,1))+"."})
        # iterative DFS with bound
        stack=[(start,0,[start])]; next_t=INF; reached=False; rpath=[]
        seen_order=[]
        while stack:
            node,g,path=stack.pop()
            f=g+hvals[node]
            if f>threshold:
                next_t=min(next_t,f)
                frames.append({"visited":list(seen_order),"frontier":[],"cur":node,"path":[],"dist":{},"start":start,"line":3,
                               "msg":"round "+str(rnd)+": cut "+node+" (f="+str(round(f,1))+" > "+str(round(threshold,1))+")"})
                continue
            seen_order.append(node)
            if node==goal:
                reached=True; rpath=path
                frames.append({"visited":list(seen_order),"frontier":[],"cur":node,"path":list(path),"dist":{},"start":start,"line":4,
                               "msg":"round "+str(rnd)+": reached goal within threshold!"})
                break
            frames.append({"visited":list(seen_order),"frontier":[],"cur":node,"path":list(path),"dist":{},"start":start,"line":2,
                           "msg":"round "+str(rnd)+": expand "+node+" (f="+str(round(f,1))+" <= "+str(round(threshold,1))+")"})
            for v,w in sorted(_EDGES[node], key=lambda e:-(hvals[e[0]])):
                if v not in path:
                    stack.append((v,g+w,path+[v]))
        if reached:
            done=True; final_path=rpath
            steps.append({"label":"Found","math":"goal within f <= "+str(round(threshold,1)),"note":"Optimal path found - and only the current path was ever held in memory."})
            break
        if next_t==INF:
            steps.append({"label":"No solution","math":"no f exceeded threshold","note":goal+" is unreachable."}); break
        steps.append({"label":"Raise threshold","math":str(round(threshold,1))+" -> "+str(round(next_t,1)),"note":"No goal within the limit; raise the threshold to the smallest f that was cut, and search again."})
        threshold=next_t
    result=("Optimal path "+start+" -> "+goal+": "+" -> ".join(final_path)+", found in "+str(rnd)+" deepening round"+("s" if rnd!=1 else "")+" using only path-depth memory.") if done else (goal+" is not reachable from "+start+".")
    return {"result":result,"start":start,"goal":goal,"found":done,"path":final_path,"hvals":hvals,
            "frames":frames,"steps":steps,"algorithm":{"pseudocode":_ALGO_PSEUDO,"python":_ALGO_PYTHON},
            "explanation":_EXPLANATION,"law_statement":_DEF,
            "law_source_name":_DEF_SRC_NAME,"law_source_url":_DEF_SRC_URL,"disclaimer":_DISCLAIMER}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
