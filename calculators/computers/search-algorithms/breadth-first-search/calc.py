"""Breadth-First Search (BFS) - DSA explainer (auto-built to the pilot template).

Viz-first: the canvas teaches; compute() returns result, a stepped trace (each
frame carries a `line` into `algorithm` for the synced code highlight), the four
exam-fact cards plus a data-structure card, a definition line, and a disclaimer.
Never names a success field 'error'.
"""

from core.registry import register

_DISCLAIMER = 'Educational explainer. A fixed 10-node graph is used so the layer-by-layer order is clear; BFS works on any graph of nodes and edges.'
_DEF = 'Breadth-first search explores a graph in layers using a FIFO queue: it visits the start, then all nodes one edge away, then all two edges away, and so on, so the first time it reaches a node is by a path with the fewest edges.'
_DEF_SRC_NAME = 'Wikipedia - Breadth-first search'
_DEF_SRC_URL = 'https://en.wikipedia.org/wiki/Breadth-first_search'

_ALGO_PSEUDO = [
        'queue = [start]; visited = {start}',
        'while queue not empty:',
        '    node = queue.pop_front()       # FIFO',
        '    if node == goal: return path',
        '    for nb in neighbours(node):',
        '        if nb not visited: visit, queue.push_back(nb)',
]
_ALGO_PYTHON = [
        'from collections import deque',
        'q = deque([start]); seen = {start}',
        'while q:',
        '    node = q.popleft()',
        '    if node == goal: return node',
        '    for nb in graph[node]:',
        '        if nb not in seen: seen.add(nb); q.append(nb)',
]

_EXPLANATION = [
    {"heading": 'Time complexity', "body": 'O(V + E) - every vertex and every edge is examined once.'},
    {"heading": 'Space complexity', "body": 'O(V) - the queue and visited set can hold up to all vertices.'},
    {"heading": 'Best data type', "body": 'Unweighted graphs where you want the fewest hops between two nodes.'},
    {"heading": 'Real-world example', "body": 'Finding the fewest handshakes between you and a celebrity - check friends, then friends-of-friends, ring by ring.'},
    {"heading": 'The data structure', "body": 'BFS explores a GRAPH (nodes joined by edges) using a QUEUE - a first-in, first-out line. The queue is what enforces the ring-by-ring order: nodes discovered earlier are expanded earlier, so the search fans out evenly in all directions from the start.'},
]

_GRAPH = {
    "A": ["B", "C"], "B": ["A", "D", "E"], "C": ["A", "F", "G"],
    "D": ["B", "H"], "E": ["B", "H", "I"], "F": ["C", "I"],
    "G": ["C", "J"], "H": ["D", "E", "J"], "I": ["E", "F", "J"], "J": ["G", "H", "I"],
}



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
    slug='breadth-first-search',
    name='Breadth-First Search (BFS)',
    section="computers",
    topic='Data Structures and Algorithms (DSA)',
    sub='Graph Traversal',
    order=1,
    summary='Explore all immediate neighbours first, then their neighbours - ring by ring.',
    formula='queue = [start]; pop front, visit, enqueue unvisited neighbours; repeat',
    tags=['bfs', 'breadth first', 'queue', 'shortest path', 'unweighted', 'O(V+E)'],
    viz_template="viz/breadth-first-search.html",
    related=['depth-first-search', 'bidirectional-search', 'dijkstra'],
)
def compute(start="A", goal="J"):
    from collections import deque
    start=str(start).strip().upper(); goal=str(goal).strip().upper()
    if start not in _GRAPH or goal not in _GRAPH:
        return {"error":"Start and goal must be nodes A-J.","steps":[],"disclaimer":_DISCLAIMER}
    q=deque([start]); seen={start}; visited=[]; frames=[]; steps=[]; found=False; parent={start:None}
    while q:
        node=q.popleft(); visited.append(node)
        frontier=list(q)
        is_goal=(node==goal)
        frames.append({"visited":list(visited),"frontier":list(frontier),"cur":node,"start":start,
                       "found":node if is_goal else None,"line":3 if not is_goal else 2,
                       "msg":("reached goal "+goal) if is_goal else ("visit "+node+"; queue: "+(", ".join(frontier) if frontier else "(empty)"))})
        steps.append({"label":"Visit "+node,"math":"dequeue "+node,"note":("Goal reached - BFS guarantees this is a fewest-edge path.") if is_goal else ("Expand "+node+"'s unvisited neighbours into the queue (they form the next ring).")})
        if is_goal: found=True; break
        for nb in _GRAPH[node]:
            if nb not in seen: seen.add(nb); q.append(nb); parent[nb]=node
    # reconstruct path
    path=[]
    if found:
        x=goal
        while x is not None: path.append(x); x=parent.get(x)
        path.reverse()
    result=("Reached "+goal+" from "+start+" in "+str(len(path)-1)+" edge"+("s" if len(path)-1!=1 else "")+" (path: "+" -> ".join(path)+"). BFS finds the fewest-edge path.") if found else (goal+" is not reachable from "+start+".")
    return {"result":result,"start":start,"goal":goal,"found":found,"path":path,"visited":visited,
            "frames":frames,"steps":steps,"algorithm":{"pseudocode":_ALGO_PSEUDO,"python":_ALGO_PYTHON},
            "explanation":_EXPLANATION,"law_statement":_DEF,
            "law_source_name":_DEF_SRC_NAME,"law_source_url":_DEF_SRC_URL,"disclaimer":_DISCLAIMER}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
