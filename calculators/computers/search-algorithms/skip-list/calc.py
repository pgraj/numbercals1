"""Skip List - DSA explainer (auto-built to the pilot template).

Viz-first: the canvas teaches; compute() returns result, a stepped trace (each
frame carries a `line` into `algorithm` for the synced code highlight), the four
exam-fact cards plus a data-structure card, a definition line, and a disclaimer.
Never names a success field 'error'.
"""

from core.registry import register

_DISCLAIMER = 'Educational explainer. Node levels here are assigned by a fixed pattern for a clear picture; real skip lists assign levels randomly (coin flips), which gives the O(log n) expectation discussed in the FAQ.'
_DEF = 'A skip list layers express lanes over a sorted linked list: higher levels link fewer, more widely spaced nodes; searching moves right on a level until the next node would overshoot, then drops a level, achieving O(log n) expected time using randomness instead of tree rotations.'
_DEF_SRC_NAME = 'Wikipedia - Skip list'
_DEF_SRC_URL = 'https://en.wikipedia.org/wiki/Skip_list'

_ALGO_PSEUDO = [
        'node = top-left (head of highest level)',
        'for level from highest down to 0:',
        '    while next node on this level <= target:',
        '        move right',
        '    drop down one level',
        'check the node reached at the bottom',
]
_ALGO_PYTHON = [
        'node = head; level = top',
        'while level >= 0:',
        '    while node.next[level] and node.next[level].key <= target:',
        '        node = node.next[level]',
        '    level -= 1',
        'return node if node.key == target else None',
]

_EXPLANATION = [
    {"heading": 'Time complexity', "body": 'O(log n) expected - the express lanes let a search skip large gaps, like a balanced tree, but the guarantee is probabilistic rather than absolute.'},
    {"heading": 'Space complexity', "body": 'O(n) expected - most nodes sit only on the bottom level; the higher lanes hold geometrically fewer nodes.'},
    {"heading": 'Best data type', "body": 'Ordered in-memory data needing fast search and update, where a simpler alternative to balanced trees is welcome.'},
    {"heading": 'Real-world example', "body": 'Express and local subway lines: ride the express to get near your stop, then switch to the local for the last bit.'},
    {"heading": 'The data structure', "body": 'A skip list is a tower of linked LISTS: the bottom level holds every key in order, and each higher level is a sparse express lane. The structure uses randomness rather than the rotations of a balanced tree to stay fast - simpler to implement, with the same O(log n) expected search.'},
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
    slug='skip-list',
    name='Skip List',
    section="computers",
    topic='Data Structures and Algorithms (DSA)',
    sub='Tree-Based',
    order=5,
    summary="A linked list with extra 'express lane' layers that let you skip ahead quickly.",
    formula='start top-left; move right while next <= target, else drop down a level; repeat',
    tags=['skip list', 'express lanes', 'randomized', 'linked list', 'O(log n)', 'redis'],
    viz_template="viz/skip-list.html",
    related=['binary-search-tree', 'avl-red-black-tree', 'b-tree'],
)
def compute(values=None, target=23):
    import math
    raw = values if values else [3,8,12,16,23,27,33,42,55,61,70,88]
    try:
        vals=sorted(set(int(x) for x in raw)); tgt=int(target)
    except (TypeError,ValueError):
        return {"error":"Values and target must be whole numbers.","steps":[],"disclaimer":_DISCLAIMER}
    if not vals: return {"error":"Enter at least one value.","steps":[],"disclaimer":_DISCLAIMER}
    n=len(vals)
    # deterministic levels for a clean picture: level = number of times index divisible by 2
    def lvl(i):
        L=0; x=i+1
        while x%2==0 and L<3: x//=2; L+=1
        return L
    levels=max(lvl(i) for i in range(n))
    # node[i] present on levels 0..lvl(i)
    present=[[True]+[ (lvl(i)>=L) for L in range(1,levels+1)] for i in range(n)]
    frames=[]; steps=[]; found=False
    pos=-1  # virtual head before index 0
    L=levels
    while L>=0:
        # move right on level L while next present node <= tgt
        while True:
            nxt=None
            for j in range(pos+1,n):
                if present[j][L]:
                    nxt=j; break
            if nxt is not None and vals[nxt]<=tgt:
                pos=nxt
                hit=(vals[nxt]==tgt)
                frames.append({"pos":pos,"level":L,"levels":levels,"vals":vals,"present":present,"decided":"found" if hit else "right","line":2,
                               "msg":("found "+_f(tgt)+" on express level "+str(L)) if hit else ("level "+str(L)+": move right to "+_f(vals[nxt]))})
                steps.append({"label":"Level "+str(L)+" right","math":_f(vals[nxt])+(" = " if hit else " <= ")+_f(tgt),"note":("Found on level "+str(L)+" - express lanes skipped many nodes.") if hit else "Still within range; advance along this express lane."})
                if hit: found=True; break
            else:
                break
        if found: break
        frames.append({"pos":pos,"level":L,"levels":levels,"vals":vals,"present":present,"decided":"down","line":4,
                       "msg":"drop from level "+str(L)+" to "+str(L-1) if L>0 else "at bottom level"})
        steps.append({"label":"Drop level","math":"level "+str(L)+" -> "+str(L-1),"note":"Next express node overshoots; drop to a finer level."})
        L-=1
    if not found:
        # final check at bottom
        check = pos+1 if pos+1<n else -1
        ok = check>=0 and vals[check]==tgt
        if ok:
            found=True; pos=check
            frames.append({"pos":pos,"level":0,"levels":levels,"vals":vals,"present":present,"decided":"found","line":5,"msg":"found "+_f(tgt)+" at the bottom level"})
            steps.append({"label":"Bottom check","math":_f(tgt)+" present","note":"Found on the full bottom level."})
        else:
            frames.append({"pos":pos,"level":0,"levels":levels,"vals":vals,"present":present,"decided":"absent","line":5,"msg":_f(tgt)+" not present"})
            steps.append({"label":"Not found","math":"bottom level passed target","note":_f(tgt)+" is not in the skip list."})
    result=("Found "+_f(tgt)+" using the express lanes (level "+str(frames[-1]['level'])+").") if found else (_f(tgt)+" is not present.")
    return {"result":result,"target":tgt,"vals":vals,"present":present,"levels":levels,"found":found,
            "frames":frames,"steps":steps,"algorithm":{"pseudocode":_ALGO_PSEUDO,"python":_ALGO_PYTHON},
            "explanation":_EXPLANATION,"law_statement":_DEF,
            "law_source_name":_DEF_SRC_NAME,"law_source_url":_DEF_SRC_URL,"disclaimer":_DISCLAIMER}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
