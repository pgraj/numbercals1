"""A* (A-Star) Search - DSA explainer (auto-built to the pilot template).

Viz-first: the canvas teaches; compute() returns result, a stepped trace (each
frame carries a `line` into `algorithm` for the synced code highlight), the four
exam-fact cards plus a data-structure card, a definition line, and a disclaimer.
Never names a success field 'error'.
"""

from core.registry import register

_DISCLAIMER = 'Educational explainer. The heuristic h is the straight-line distance to the goal (admissible because a straight line is never longer than a real path). Edge numbers are costs.'
_DEF = 'A* search expands the node with the lowest f = g + h, where g is the known cost from the start and h is a heuristic estimate of the remaining cost to the goal; if h never overestimates (is admissible), A* finds an optimal path while exploring far fewer nodes than Dijkstra.'
_DEF_SRC_NAME = 'Wikipedia - A* search algorithm'
_DEF_SRC_URL = 'https://en.wikipedia.org/wiki/A*_search_algorithm'

_ALGO_PSEUDO = [
        'g[start] = 0; f[start] = h(start)',
        'while open set not empty:',
        '    u = node with smallest f = g + h',
        '    if u == goal: return path',
        '    for (v, w) in edges(u):',
        '        if g[u] + w < g[v]: g[v] = g[u]+w; f[v] = g[v] + h(v)',
]
_ALGO_PYTHON = [
        'import heapq',
        'g = {start: 0}; pq = [(h(start), start)]',
        'while pq:',
        '    f, u = heapq.heappop(pq)',
        '    if u == goal: break',
        '    for v, w in graph[u]:',
        '        if g[u]+w < g.get(v, inf):',
        '            g[v]=g[u]+w; heapq.heappush(pq, (g[v]+h(v), v))',
]

_EXPLANATION = [
    {"heading": 'Time complexity', "body": 'Depends on the heuristic; with a good admissible h it explores far fewer nodes than Dijkstra, often dramatically so.'},
    {"heading": 'Space complexity', "body": 'O(V) - it must remember all generated nodes in the open and closed sets.'},
    {"heading": 'Best data type', "body": 'Weighted graphs where you can estimate distance-to-goal - maps, game grids, robotics.'},
    {"heading": 'Real-world example', "body": 'Driving toward a city by generally heading in its compass direction, rather than exploring every side road equally.'},
    {"heading": 'The data structure', "body": "A* explores a WEIGHTED GRAPH with a PRIORITY QUEUE keyed by f = g + h. It is Dijkstra's structure with an extra ingredient - a heuristic estimate per node - so the priority queue favours nodes that are both cheap to reach AND look close to the goal, steering the search toward the target."},
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
    return round(math.hypot(ax - bx, ay - by) * 12, 1)   # scaled straight-line estimate



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
    slug='a-star-search',
    name='A* (A-Star) Search',
    section="computers",
    topic='Data Structures and Algorithms (DSA)',
    sub='Informed & Heuristic',
    order=2,
    summary='Dijkstra plus a heuristic guess of remaining distance, so it heads toward the goal.',
    formula='expand the node with smallest f = g (cost so far) + h (estimated cost to goal)',
    tags=['a star', 'a*', 'heuristic', 'pathfinding', 'f = g + h', 'admissible', 'games maps'],
    viz_template="viz/a-star-search.html",
    related=['dijkstra', 'greedy-best-first-search', 'ida-star'],
)
def compute(start="S", goal="G"):
    import heapq
    start=str(start).strip().upper(); goal=str(goal).strip().upper()
    if start not in _EDGES or goal not in _EDGES:
        return {"error":"Start and goal must be nodes S, A-E, or G.","steps":[],"disclaimer":_DISCLAIMER}
    INF=float("inf")
    hvals={n:_hdist(n,goal) for n in _POS}
    g={start:0}; prev={start:None}; pq=[(hvals[start],0,start)]; visited=[]; frames=[]; steps=[]; done=False
    while pq:
        f,gg,u=heapq.heappop(pq)
        if u in visited: continue
        visited.append(u)
        is_goal=(u==goal)
        frontier=[n for _,_,n in pq if n not in visited]
        frames.append({"visited":list(visited),"frontier":list(dict.fromkeys(frontier)),"cur":u,"dist":{k:v for k,v in g.items()},
                       "start":start,"line":3 if not is_goal else 4,
                       "msg":("reached goal "+goal+" at cost "+str(gg)) if is_goal else ("expand "+u+": f="+str(round(gg+hvals[u],1))+" (g="+str(gg)+" + h="+str(hvals[u])+")")})
        steps.append({"label":"Expand "+u,"math":"f = g+h = "+str(gg)+"+"+str(hvals[u])+" = "+str(round(gg+hvals[u],1)),"note":("Goal reached on an optimal path - the heuristic steered us here efficiently.") if is_goal else ("Choose the node with the smallest f. The heuristic h biases the search toward the goal.")})
        if is_goal: done=True; break
        for v,w in _EDGES[u]:
            nd=gg+w
            if nd<g.get(v,INF):
                g[v]=nd; prev[v]=u; heapq.heappush(pq,(nd+hvals[v],nd,v))
    path=[]
    if done:
        x=goal
        while x is not None: path.append(x); x=prev.get(x)
        path.reverse()
    result=("Optimal path "+start+" -> "+goal+": "+" -> ".join(path)+" (cost "+str(g.get(goal))+"). A* used the heuristic to reach the goal while exploring fewer nodes than Dijkstra would.") if done else (goal+" is not reachable from "+start+".")
    return {"result":result,"start":start,"goal":goal,"found":done,"path":path,"cost":g.get(goal),"hvals":hvals,
            "frames":frames,"steps":steps,"algorithm":{"pseudocode":_ALGO_PSEUDO,"python":_ALGO_PYTHON},
            "explanation":_EXPLANATION,"law_statement":_DEF,
            "law_source_name":_DEF_SRC_NAME,"law_source_url":_DEF_SRC_URL,"disclaimer":_DISCLAIMER}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
