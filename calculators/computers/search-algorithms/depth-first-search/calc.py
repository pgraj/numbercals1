"""Depth-First Search (DFS) - DSA explainer (auto-built to the pilot template).

Viz-first: the canvas teaches; compute() returns result, a stepped trace (each
frame carries a `line` into `algorithm` for the synced code highlight), the four
exam-fact cards plus a data-structure card, a definition line, and a disclaimer.
Never names a success field 'error'.
"""

from core.registry import register

_DISCLAIMER = "Educational explainer. The same fixed 10-node graph as BFS is used so you can directly compare the deep-first order against BFS's ring-by-ring order."
_DEF = 'Depth-first search explores a graph by going as deep as possible along each branch before backtracking, using a stack (or recursion); it visits every vertex and edge once and is the basis for cycle detection, topological sorting and connectivity tests.'
_DEF_SRC_NAME = 'Wikipedia - Depth-first search'
_DEF_SRC_URL = 'https://en.wikipedia.org/wiki/Depth-first_search'

_ALGO_PSEUDO = [
        'stack = [start]; visited = {}',
        'while stack not empty:',
        '    node = stack.pop()             # LIFO',
        '    if node == goal: return path',
        '    if node not visited: visit it',
        '    push unvisited neighbours onto stack',
]
_ALGO_PYTHON = [
        'stack = [start]; seen = set()',
        'while stack:',
        '    node = stack.pop()',
        '    if node == goal: return node',
        '    if node in seen: continue',
        '    seen.add(node)',
        '    for nb in graph[node]: stack.append(nb)',
]

_EXPLANATION = [
    {"heading": 'Time complexity', "body": 'O(V + E) - like BFS, every vertex and edge is examined once.'},
    {"heading": 'Space complexity', "body": "O(V) - the stack (or recursion depth) can hold a whole path; often less than BFS's wide frontier."},
    {"heading": 'Best data type', "body": 'Any graph where you need to explore fully, detect cycles, or order dependencies - not for shortest paths.'},
    {"heading": 'Real-world example', "body": 'Exploring a maze by always going forward until you hit a dead end, then backtracking to the last junction.'},
    {"heading": 'The data structure', "body": 'DFS explores a GRAPH using a STACK - last in, first out (often the call stack via recursion). The stack is what drives it deep: the most recently discovered node is expanded next, so the search plunges down one branch before ever returning to explore alternatives.'},
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
    slug='depth-first-search',
    name='Depth-First Search (DFS)',
    section="computers",
    topic='Data Structures and Algorithms (DSA)',
    sub='Graph Traversal',
    order=2,
    summary='Follow one path as far as it goes, then back up and try another - using a stack.',
    formula='stack = [start]; pop top, visit, push unvisited neighbours; repeat',
    tags=['dfs', 'depth first', 'stack', 'recursion', 'backtracking', 'O(V+E)'],
    viz_template="viz/depth-first-search.html",
    related=['breadth-first-search', 'bidirectional-search'],
)
def compute(start="A", goal="J"):
    start=str(start).strip().upper(); goal=str(goal).strip().upper()
    if start not in _GRAPH or goal not in _GRAPH:
        return {"error":"Start and goal must be nodes A-J.","steps":[],"disclaimer":_DISCLAIMER}
    stack=[start]; seen=set(); visited=[]; frames=[]; steps=[]; found=False; parent={start:None}
    while stack:
        node=stack.pop()
        if node in seen: continue
        seen.add(node); visited.append(node)
        is_goal=(node==goal)
        frames.append({"visited":list(visited),"frontier":list(dict.fromkeys([s for s in reversed(stack) if s not in seen])),"cur":node,"start":start,
                       "found":node if is_goal else None,"line":3 if not is_goal else 2,
                       "msg":("reached goal "+goal) if is_goal else ("visit "+node+"; stack top next")})
        steps.append({"label":"Visit "+node,"math":"pop "+node,"note":("Goal reached by diving deep (not necessarily the shortest path).") if is_goal else ("Push "+node+"'s unvisited neighbours; the most recent one is explored next - so we go deep.")})
        if is_goal: found=True; break
        for nb in _GRAPH[node]:
            if nb not in seen:
                stack.append(nb)
                if nb not in parent: parent[nb]=node
    path=[]
    if found:
        x=goal
        while x is not None: path.append(x); x=parent.get(x)
        path.reverse()
    result=("Reached "+goal+" from "+start+" via "+" -> ".join(path)+" ("+str(len(visited))+" nodes visited). DFS dives deep; this path may not be the shortest.") if found else (goal+" is not reachable from "+start+".")
    return {"result":result,"start":start,"goal":goal,"found":found,"path":path,"visited":visited,
            "frames":frames,"steps":steps,"algorithm":{"pseudocode":_ALGO_PSEUDO,"python":_ALGO_PYTHON},
            "explanation":_EXPLANATION,"law_statement":_DEF,
            "law_source_name":_DEF_SRC_NAME,"law_source_url":_DEF_SRC_URL,"disclaimer":_DISCLAIMER}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
