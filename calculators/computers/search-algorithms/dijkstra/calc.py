"""Dijkstra's Algorithm - DSA explainer (auto-built to the pilot template).

Viz-first: the canvas teaches; compute() returns result, a stepped trace (each
frame carries a `line` into `algorithm` for the synced code highlight), the four
exam-fact cards plus a data-structure card, a definition line, and a disclaimer.
Never names a success field 'error'.
"""

from core.registry import register

_DISCLAIMER = 'Educational explainer. A small weighted graph is used; edge numbers are costs. Dijkstra requires non-negative weights, explained in the FAQ.'
_DEF = "Dijkstra's algorithm finds the cheapest path in a graph with non-negative edge weights by always expanding the unvisited node with the smallest known distance from the start and relaxing its outgoing edges, settling each node's true shortest distance once."
_DEF_SRC_NAME = "Wikipedia - Dijkstra's algorithm"
_DEF_SRC_URL = 'https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm'

_ALGO_PSEUDO = [
        'dist[start] = 0; all others = infinity',
        'while unvisited nodes remain:',
        '    u = unvisited node with smallest dist',
        '    if u == goal: done',
        '    for (v, w) in edges(u):',
        '        if dist[u] + w < dist[v]: dist[v] = dist[u] + w',
]
_ALGO_PYTHON = [
        'import heapq',
        'dist = {start: 0}; pq = [(0, start)]',
        'while pq:',
        '    d, u = heapq.heappop(pq)',
        '    if u == goal: break',
        '    for v, w in graph[u]:',
        '        if d + w < dist.get(v, inf):',
        '            dist[v] = d + w; heapq.heappush(pq, (dist[v], v))',
]

_EXPLANATION = [
    {"heading": 'Time complexity', "body": 'O((V + E) log V) with a binary-heap priority queue - each node and edge processed, with log-time queue operations.'},
    {"heading": 'Space complexity', "body": 'O(V) - distances, the priority queue, and the previous-node map.'},
    {"heading": 'Best data type', "body": 'Weighted graphs with non-negative costs - road networks, network routing.'},
    {"heading": 'Real-world example', "body": 'Finding the cheapest combination of flights between two cities, always extending the cheapest route found so far.'},
    {"heading": 'The data structure', "body": "Dijkstra explores a WEIGHTED GRAPH using a PRIORITY QUEUE (min-heap) keyed by distance-from-start. The priority queue is the engine: it always hands back the closest unsettled node, which is what lets Dijkstra lock in each node's true shortest distance the first time it is removed."},
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
    slug='dijkstra',
    name="Dijkstra's Algorithm",
    section="computers",
    topic='Data Structures and Algorithms (DSA)',
    sub='Informed & Heuristic',
    order=1,
    summary='Find the cheapest path by always expanding the closest unvisited node so far.',
    formula='repeatedly pick the unvisited node with the smallest known distance; relax its edges',
    tags=['dijkstra', 'shortest path', 'weighted', 'priority queue', 'greedy', 'O((V+E)logV)'],
    viz_template="viz/dijkstra.html",
    related=['a-star-search', 'greedy-best-first-search', 'ida-star', 'breadth-first-search'],
)
def compute(start="S", goal="G"):
    import heapq
    start=str(start).strip().upper(); goal=str(goal).strip().upper()
    if start not in _EDGES or goal not in _EDGES:
        return {"error":"Start and goal must be nodes S, A-E, or G.","steps":[],"disclaimer":_DISCLAIMER}
    INF=float("inf"); dist={start:0}; prev={start:None}; pq=[(0,start)]; visited=[]; frames=[]; steps=[]; done=False
    while pq:
        d,u=heapq.heappop(pq)
        if u in visited: continue
        visited.append(u)
        is_goal=(u==goal)
        frontier=[n for _,n in pq if n not in visited]
        frames.append({"visited":list(visited),"frontier":list(dict.fromkeys(frontier)),"cur":u,"dist":{k:(v if v!=INF else None) for k,v in dist.items()},
                       "start":start,"line":3 if not is_goal else 4,
                       "msg":("settled goal "+goal+" at cost "+str(d)) if is_goal else ("settle "+u+" (cheapest known cost "+str(d)+")")})
        steps.append({"label":"Settle "+u,"math":"dist["+u+"] = "+str(d),"note":("Goal settled - its shortest cost is now final.") if is_goal else ("Pick the cheapest unsettled node ("+u+"), then relax its edges.")})
        if is_goal: done=True; break
        for v,w in _EDGES[u]:
            nd=d+w
            if nd<dist.get(v,INF):
                dist[v]=nd; prev[v]=u; heapq.heappush(pq,(nd,v))
    path=[]
    if done:
        x=goal
        while x is not None: path.append(x); x=prev.get(x)
        path.reverse()
    result=("Cheapest path "+start+" -> "+goal+": "+" -> ".join(path)+" (total cost "+str(dist.get(goal))+"). Dijkstra settled each node by lowest cost.") if done else (goal+" is not reachable from "+start+".")
    return {"result":result,"start":start,"goal":goal,"found":done,"path":path,"cost":dist.get(goal),
            "frames":frames,"steps":steps,"algorithm":{"pseudocode":_ALGO_PSEUDO,"python":_ALGO_PYTHON},
            "explanation":_EXPLANATION,"law_statement":_DEF,
            "law_source_name":_DEF_SRC_NAME,"law_source_url":_DEF_SRC_URL,"disclaimer":_DISCLAIMER}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
