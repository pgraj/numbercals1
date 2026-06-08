"""Greedy Best-First Search - DSA explainer (auto-built to the pilot template).

Viz-first: the canvas teaches; compute() returns result, a stepped trace (each
frame carries a `line` into `algorithm` for the synced code highlight), the four
exam-fact cards plus a data-structure card, a definition line, and a disclaimer.
Never names a success field 'error'.
"""

from core.registry import register

_DISCLAIMER = 'Educational explainer. The heuristic h is straight-line distance to the goal. Because greedy search ignores cost-so-far, the path it returns may not be the cheapest, which the FAQ explains.'
_DEF = 'Greedy best-first search expands whichever frontier node has the smallest heuristic estimate to the goal, ignoring the cost already spent; this makes it very fast but not guaranteed to find the shortest path.'
_DEF_SRC_NAME = 'Wikipedia - Best-first search'
_DEF_SRC_URL = 'https://en.wikipedia.org/wiki/Best-first_search'

_ALGO_PSEUDO = [
        'frontier = {start}, ordered by h (estimate to goal)',
        'while frontier not empty:',
        '    u = node with smallest h',
        '    if u == goal: return path',
        '    add unvisited neighbours to frontier',
        '# note: cost-so-far g is never considered',
]
_ALGO_PYTHON = [
        'import heapq',
        'pq = [(h(start), start)]; seen={start}',
        'while pq:',
        '    _, u = heapq.heappop(pq)',
        '    if u == goal: break',
        '    for v, w in graph[u]:',
        '        if v not in seen: seen.add(v); heapq.heappush(pq,(h(v),v))',
]

_EXPLANATION = [
    {"heading": 'Time complexity', "body": 'Fast in practice - it beelines for the goal - but worst case can be poor if the heuristic misleads it.'},
    {"heading": 'Space complexity', "body": 'O(V) - frontier and visited set.'},
    {"heading": 'Best data type', "body": 'Weighted graphs where speed matters more than guaranteed optimality and the heuristic is reliable.'},
    {"heading": 'Real-world example', "body": 'Always walking toward the mountain you can see - quick, but you might hit a river and have to detour.'},
    {"heading": 'The data structure', "body": "Greedy best-first uses a WEIGHTED GRAPH and a PRIORITY QUEUE keyed by h alone (the estimate to the goal), ignoring g. By looking only at 'how close does this seem to the goal,' it rushes toward the target - fast, but blind to whether the route it is taking is actually cheap."},
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
    slug='greedy-best-first-search',
    name='Greedy Best-First Search',
    section="computers",
    topic='Data Structures and Algorithms (DSA)',
    sub='Informed & Heuristic',
    order=3,
    summary='Always move toward whatever LOOKS closest to the goal, ignoring the cost so far.',
    formula='expand the node with the smallest h (estimated distance to goal); ignore g',
    tags=['greedy best first', 'heuristic', 'fast', 'not optimal', 'pathfinding'],
    viz_template="viz/greedy-best-first-search.html",
    related=['a-star-search', 'dijkstra', 'ida-star'],
)
def compute(start="S", goal="G"):
    import heapq
    start=str(start).strip().upper(); goal=str(goal).strip().upper()
    if start not in _EDGES or goal not in _EDGES:
        return {"error":"Start and goal must be nodes S, A-E, or G.","steps":[],"disclaimer":_DISCLAIMER}
    hvals={n:_hdist(n,goal) for n in _POS}
    pq=[(hvals[start],start)]; seen={start}; prev={start:None}; gcost={start:0}; visited=[]; frames=[]; steps=[]; done=False
    while pq:
        hh,u=heapq.heappop(pq)
        visited.append(u)
        is_goal=(u==goal)
        frontier=[n for _,n in pq]
        frames.append({"visited":list(visited),"frontier":list(dict.fromkeys(frontier)),"cur":u,"dist":{k:v for k,v in gcost.items()},
                       "start":start,"line":3 if not is_goal else 2,
                       "msg":("reached goal "+goal) if is_goal else ("expand "+u+": h="+str(hvals[u])+" (closest-looking to goal)")})
        steps.append({"label":"Expand "+u,"math":"h = "+str(hvals[u]),"note":("Goal reached - quickly, though the path may not be cheapest.") if is_goal else ("Pick the node that LOOKS closest to the goal (smallest h). Cost so far is ignored.")})
        if is_goal: done=True; break
        for v,w in _EDGES[u]:
            if v not in seen:
                seen.add(v); prev[v]=u; gcost[v]=gcost[u]+w; heapq.heappush(pq,(hvals[v],v))
    path=[]
    if done:
        x=goal
        while x is not None: path.append(x); x=prev.get(x)
        path.reverse()
    total=gcost.get(goal)
    result=("Path "+start+" -> "+goal+": "+" -> ".join(path)+" (cost "+str(total)+"). Greedy reached the goal fast, but this path is not guaranteed to be the cheapest - compare with Dijkstra/A*.") if done else (goal+" is not reachable from "+start+".")
    return {"result":result,"start":start,"goal":goal,"found":done,"path":path,"cost":total,"hvals":hvals,
            "frames":frames,"steps":steps,"algorithm":{"pseudocode":_ALGO_PSEUDO,"python":_ALGO_PYTHON},
            "explanation":_EXPLANATION,"law_statement":_DEF,
            "law_source_name":_DEF_SRC_NAME,"law_source_url":_DEF_SRC_URL,"disclaimer":_DISCLAIMER}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
