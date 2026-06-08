"""Bidirectional Search - DSA explainer (auto-built to the pilot template).

Viz-first: the canvas teaches; compute() returns result, a stepped trace (each
frame carries a `line` into `algorithm` for the synced code highlight), the four
exam-fact cards plus a data-structure card, a definition line, and a disclaimer.
Never names a success field 'error'.
"""

from core.registry import register

_DISCLAIMER = 'Educational explainer. Both frontiers expand one ring per step on the shared fixed graph; the meeting node is highlighted when the two searches touch.'
_DEF = 'Bidirectional search runs two simultaneous breadth-first searches, one forward from the start and one backward from the goal, and stops when their frontiers meet; because each side only explores about half the depth, it can examine far fewer nodes than a single search.'
_DEF_SRC_NAME = 'Wikipedia - Bidirectional search'
_DEF_SRC_URL = 'https://en.wikipedia.org/wiki/Bidirectional_search'

_ALGO_PSEUDO = [
        'frontierF = {start}; frontierB = {goal}',
        'while both frontiers non-empty:',
        '    expand frontierF one ring (forward)',
        '    expand frontierB one ring (backward)',
        '    if frontiers share a node: MEET - join paths',
        'return joined path',
]
_ALGO_PYTHON = [
        'seenF={start}; seenB={goal}; fF=[start]; fB=[goal]',
        'while fF and fB:',
        '    fF = expand(fF, seenF)   # one BFS ring forward',
        '    fB = expand(fB, seenB)   # one BFS ring backward',
        '    meet = seenF & seenB',
        '    if meet: return join(meet)',
]

_EXPLANATION = [
    {"heading": 'Time complexity', "body": "Roughly the square root of a single search's cost - two searches of half the depth each, so about 2 * b^(d/2) instead of b^d."},
    {"heading": 'Space complexity', "body": 'O(b^(d/2)) - it must store both frontiers, which is the main cost.'},
    {"heading": 'Best data type', "body": 'Large graphs with a known start and goal, and edges that can be followed backward (route planning, networks).'},
    {"heading": 'Real-world example', "body": 'Two people walking toward each other from opposite ends of a tunnel - they meet in roughly half the time of one person walking the whole way.'},
    {"heading": 'The data structure', "body": 'Bidirectional search runs two GRAPH searches at once, each with its own QUEUE and visited set - one growing forward from the start, one backward from the goal. The structure is two BFS frontiers; the trick is detecting the moment a node appears in both visited sets, which stitches the two half-paths into one.'},
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
    slug='bidirectional-search',
    name='Bidirectional Search',
    section="computers",
    topic='Data Structures and Algorithms (DSA)',
    sub='Graph Traversal',
    order=3,
    summary='Search from the start AND the goal at the same time, meeting in the middle.',
    formula='run two BFS frontiers (from start, from goal); stop when they intersect',
    tags=['bidirectional', 'two-way', 'meet in the middle', 'BFS', 'route planning'],
    viz_template="viz/bidirectional-search.html",
    related=['breadth-first-search', 'depth-first-search', 'dijkstra', 'a-star-search'],
)
def compute(start="A", goal="J"):
    start=str(start).strip().upper(); goal=str(goal).strip().upper()
    if start not in _GRAPH or goal not in _GRAPH:
        return {"error":"Start and goal must be nodes A-J.","steps":[],"disclaimer":_DISCLAIMER}
    if start==goal:
        return {"error":"Pick different start and goal nodes.","steps":[],"disclaimer":_DISCLAIMER}
    seenF={start}; seenB={goal}; frontF=[start]; frontB=[goal]
    visF=[start]; visB=[goal]; frames=[]; steps=[]; meet=None
    parF={start:None}; parB={goal:None}
    frames.append({"visited":list(visF),"visited2":list(visB),"frontier":list(frontF),"frontier2":list(frontB),"meet":None,"start":start,"line":0,
                   "msg":"start forward from "+start+", backward from "+goal})
    steps.append({"label":"Initialise","math":"two frontiers","note":"One search grows forward from "+start+", another backward from "+goal+"."})
    step=0
    while frontF and frontB and meet is None and step<12:
        step+=1
        # expand forward one ring
        nF=[]
        for node in frontF:
            for nb in _GRAPH[node]:
                if nb not in seenF: seenF.add(nb); parF[nb]=node; nF.append(nb); visF.append(nb)
        frontF=nF
        meet = next((x for x in seenF if x in seenB), None)
        frames.append({"visited":list(visF),"visited2":list(visB),"frontier":list(frontF),"frontier2":list(frontB),"meet":meet,"start":start,"line":2,
                       "msg":("forward ring: "+(", ".join(nF) if nF else "(none)"))+(" | MEET at "+meet if meet else "")})
        steps.append({"label":"Forward ring "+str(step),"math":"expand from "+start,"note":("Frontiers meet at "+meet+"!") if meet else "Grow the forward frontier one more ring."})
        if meet: break
        # expand backward one ring
        nB=[]
        for node in frontB:
            for nb in _GRAPH[node]:
                if nb not in seenB: seenB.add(nb); parB[nb]=node; nB.append(nb); visB.append(nb)
        frontB=nB
        meet = next((x for x in seenF if x in seenB), None)
        frames.append({"visited":list(visF),"visited2":list(visB),"frontier":list(frontF),"frontier2":list(frontB),"meet":meet,"start":start,"line":3,
                       "msg":("backward ring: "+(", ".join(nB) if nB else "(none)"))+(" | MEET at "+meet if meet else "")})
        steps.append({"label":"Backward ring "+str(step),"math":"expand from "+goal,"note":("Frontiers meet at "+meet+"!") if meet else "Grow the backward frontier one more ring."})
        if meet: break
    if meet:
        # build path: start..meet (parF) + meet..goal (parB)
        left=[]; x=meet
        while x is not None: left.append(x); x=parF.get(x)
        left.reverse()
        right=[]; x=parB.get(meet)
        while x is not None: right.append(x); x=parB.get(x)
        path=left+right
        result="Frontiers met at "+meet+". Path: "+" -> ".join(path)+". Each side searched only about half the distance, so far fewer nodes were explored than a single search."
    else:
        result=goal+" is not reachable from "+start+"."
    return {"result":result,"start":start,"goal":goal,"found":meet is not None,"meet":meet,
            "frames":frames,"steps":steps,"algorithm":{"pseudocode":_ALGO_PSEUDO,"python":_ALGO_PYTHON},
            "explanation":_EXPLANATION,"law_statement":_DEF,
            "law_source_name":_DEF_SRC_NAME,"law_source_url":_DEF_SRC_URL,"disclaimer":_DISCLAIMER}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
