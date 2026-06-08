"""B-Tree / B+ Tree - DSA explainer (auto-built to the pilot template).

Viz-first: the canvas teaches; compute() returns result, a stepped trace (each
frame carries a `line` into `algorithm` for the synced code highlight), the four
exam-fact cards plus a data-structure card, a definition line, and a disclaimer.
Never names a success field 'error'.
"""

from core.registry import register

_DISCLAIMER = 'Educational explainer. A small order-4 B-tree (up to 3 keys per node) is built from your values so the multiway structure is visible; real database B-trees pack hundreds of keys per node to match a disk page.'
_DEF = 'A B-tree is a balanced multiway search tree where each node holds many sorted keys and many children; because one node read decides which of many children to follow, it keeps the tree very shallow, minimising the number of slow disk accesses needed to find a key.'
_DEF_SRC_NAME = 'Wikipedia - B-tree'
_DEF_SRC_URL = 'https://en.wikipedia.org/wiki/B-tree'

_ALGO_PSEUDO = [
        'node = root',
        'while node is not a leaf:',
        '    find the key slot where target fits',
        '    if found here: return it',
        '    else descend into the matching child',
        'scan the leaf node for target',
]
_ALGO_PYTHON = [
        'node = root',
        'while node:',
        '    i = first index where target <= keys[i]',
        '    if i < len(keys) and keys[i]==target: return node',
        '    node = children[i] if children else None',
        'return None',
]

_EXPLANATION = [
    {"heading": 'Time complexity', "body": 'O(log n) - but with a very large branching factor, so the tree is extremely shallow and needs few node reads.'},
    {"heading": 'Space complexity', "body": 'O(n) - keys spread across nodes, each node sized to a disk page.'},
    {"heading": 'Best data type', "body": 'Enormous datasets stored on disk - the default index structure for databases and file systems.'},
    {"heading": 'Real-world example', "body": 'A library catalogue with broad index tabs, then sub-tabs, so you reach any book in just a few lookups.'},
    {"heading": 'The data structure', "body": "A B-tree is a balanced TREE whose nodes are themselves small sorted arrays of keys, each separating its children's key ranges. The fat nodes are the whole point: matching a node to a disk page means one read pulls in many keys at once, so the tree stays only a few levels deep even for billions of records."},
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
    slug='b-tree',
    name='B-Tree / B+ Tree',
    section="computers",
    topic='Data Structures and Algorithms (DSA)',
    sub='Tree-Based',
    order=3,
    summary="A 'fat' tree where each node holds many keys - built to minimise slow disk reads.",
    formula='each node holds up to m-1 keys and m children; one node read narrows to one child',
    tags=['b-tree', 'b+ tree', 'database index', 'disk', 'multiway', 'O(log n)'],
    viz_template="viz/b-tree.html",
    related=['binary-search-tree', 'avl-red-black-tree', 'lsm-tree', 'skip-list'],
)
def compute(values=None, target=23):
    raw = values if values else [10,20,30,40,50,60,70,80,23,35,15,45]
    try:
        vals=sorted(set(int(x) for x in raw)); tgt=int(target)
    except (TypeError,ValueError):
        return {"error":"Values and target must be whole numbers.","steps":[],"disclaimer":_DISCLAIMER}
    if not vals: return {"error":"Enter at least one value.","steps":[],"disclaimer":_DISCLAIMER}
    # Build a simple balanced order-4 B-tree-like structure (up to 3 keys/node) for display.
    # We approximate by a 2-level layout: leaves of <=3 keys, internal separators.
    MAXK=3
    leaves=[vals[i:i+MAXK] for i in range(0,len(vals),MAXK)]
    # root separators: last key of each leaf except last
    seps=[leaf[-1] for leaf in leaves[:-1]]
    root={"keys":seps,"leaf":False}
    frames=[]; steps=[]; found=False
    # search root
    ci=0
    while ci<len(seps) and tgt>seps[ci]: ci+=1
    frames.append({"level":"root","keys":list(seps),"leaves":[list(l) for l in leaves],"child":ci,"probe":-1,"line":1,
                   "msg":"At root: pick child "+str(ci)+" (the leaf whose range holds "+_f(tgt)+")"})
    steps.append({"label":"Read root","math":"choose child "+str(ci),"note":"One node read narrows "+str(len(vals))+" keys down to a single leaf of at most "+str(MAXK)+"."})
    leaf=leaves[ci] if ci<len(leaves) else []
    for pos,k in enumerate(leaf):
        hit=(k==tgt)
        frames.append({"level":"leaf","keys":list(seps),"leaves":[list(l) for l in leaves],"child":ci,"probe":pos,"line":5 if not hit else 3,
                       "msg":("found "+_f(tgt)+" in leaf "+str(ci)) if hit else ("scan leaf: "+_f(k)+(" = " if hit else " != ")+_f(tgt))})
        steps.append({"label":"Scan leaf","math":_f(k)+(" = " if hit else " != ")+_f(tgt),"note":("Found in leaf "+str(ci)+".") if hit else "Not this key; continue within the same leaf."})
        if hit: found=True; break
    if not found:
        frames.append({"level":"leaf","keys":list(seps),"leaves":[list(l) for l in leaves],"child":ci,"probe":-1,"line":6,
                       "msg":_f(tgt)+" not found in leaf "+str(ci)})
        steps.append({"label":"Not found","math":"leaf exhausted","note":_f(tgt)+" is not in the tree - only two levels were read."})
    result=("Found "+_f(tgt)+" with just 2 node reads (root then one leaf), out of "+str(len(vals))+" keys.") if found else (_f(tgt)+" is not present (2 node reads).")
    return {"result":result,"target":tgt,"seps":seps,"leaves":[list(l) for l in leaves],"found":found,
            "frames":frames,"steps":steps,"algorithm":{"pseudocode":_ALGO_PSEUDO,"python":_ALGO_PYTHON},
            "explanation":_EXPLANATION,"law_statement":_DEF,
            "law_source_name":_DEF_SRC_NAME,"law_source_url":_DEF_SRC_URL,"disclaimer":_DISCLAIMER}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
