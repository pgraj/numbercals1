"""AVL / Red-Black Trees (Self-Balancing) - DSA explainer (auto-built to the pilot template).

Viz-first: the canvas teaches; compute() returns result, a stepped trace (each
frame carries a `line` into `algorithm` for the synced code highlight), the four
exam-fact cards plus a data-structure card, a definition line, and a disclaimer.
Never names a success field 'error'.
"""

from core.registry import register

_DISCLAIMER = 'Educational explainer. The tree shown is kept balanced by simulated insertion so the height stays near log n; the search itself is identical to a plain BST but with a guaranteed-short path.'
_DEF = 'Self-balancing search trees (AVL, red-black) maintain the binary-search-tree ordering while enforcing a balance rule, performing rotations after inserts and deletes so the height stays proportional to log n - guaranteeing O(log n) search, insert and delete regardless of input order.'
_DEF_SRC_NAME = 'Wikipedia - Self-balancing binary search tree'
_DEF_SRC_URL = 'https://en.wikipedia.org/wiki/Self-balancing_binary_search_tree'

_ALGO_PSEUDO = [
        'search is the same as a BST:',
        'node = root',
        'while node: go left/right by comparison',
        '# the difference is on INSERT/DELETE:',
        'after updating, check balance and ROTATE',
        'so height stays about log n',
]
_ALGO_PYTHON = [
        '# search identical to BST',
        'node = root',
        'while node:',
        '    if target==node.key: return node',
        '    node = node.left if target<node.key else node.right',
        '# insert/delete call rotate() to rebalance',
]

_EXPLANATION = [
    {"heading": 'Time complexity', "body": 'O(log n) guaranteed for search, insert and delete - the balancing prevents the O(n) degeneration a plain BST can suffer.'},
    {"heading": 'Space complexity', "body": 'O(n) - one node per key plus a little balance metadata (a height or a colour bit).'},
    {"heading": 'Best data type', "body": 'Ordered data with constant changes where worst-case speed must be guaranteed, not just average.'},
    {"heading": 'Real-world example', "body": 'A library that constantly reshelves so no aisle ever gets too long to walk - lookups stay quick whatever order books arrive in.'},
    {"heading": 'The data structure', "body": 'This is still a binary-search TREE of linked nodes, but with extra balance bookkeeping (heights in AVL, colours in red-black) and rotation operations. The structure actively reshapes itself so its height never blows up - trading a little work per update for a guaranteed-fast search path.'},
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
    slug='avl-red-black-tree',
    name='AVL / Red-Black Trees (Self-Balancing)',
    section="computers",
    topic='Data Structures and Algorithms (DSA)',
    sub='Tree-Based',
    order=2,
    summary='BSTs that rebalance themselves on every change so they never degrade into a slow line.',
    formula='after each insert/delete, rotate subtrees to keep height ~ log n',
    tags=['avl tree', 'red-black tree', 'self-balancing', 'rotation', 'O(log n) guaranteed'],
    viz_template="viz/avl-red-black-tree.html",
    related=['binary-search-tree', 'b-tree', 'skip-list'],
)
def compute(values=None, target=23):
    raw = values if values else [50,30,70,20,40,60,80,23]
    try:
        vals=[int(x) for x in raw]; tgt=int(target)
    except (TypeError,ValueError):
        return {"error":"Values and target must be whole numbers.","steps":[],"disclaimer":_DISCLAIMER}
    if not vals: return {"error":"Enter at least one value.","steps":[],"disclaimer":_DISCLAIMER}
    # Build a balanced BST from the sorted unique values (simulating the result of self-balancing)
    uniq=sorted(set(vals))
    nodes={}; nid=0
    def build(lo,hi,depth):
        nonlocal nid
        if lo>hi: return None
        mid=(lo+hi)//2; nid+=1; me=nid
        nodes[me]={"key":uniq[mid],"left":None,"right":None,"depth":depth}
        nodes[me]["left"]=build(lo,mid-1,depth+1)
        nodes[me]["right"]=build(mid+1,hi,depth+1)
        return me
    root=build(0,len(uniq)-1,0)
    order=[]
    def inorder(i):
        if i is None: return
        inorder(nodes[i]["left"]); order.append(i); inorder(nodes[i]["right"])
    inorder(root)
    for col,i in enumerate(order): nodes[i]["col"]=col
    frames=[]; steps=[]; cur=root; found=False; path=[]
    while cur is not None:
        path.append(cur); k=nodes[cur]["key"]
        if tgt==k:
            frames.append({"cur":cur,"path":list(path),"decided":"found","line":3}); steps.append({"label":"Match","math":_f(tgt)+" = "+_f(k),"note":"Found - and the path was guaranteed short because the tree is balanced."}); found=True; break
        elif tgt<k:
            frames.append({"cur":cur,"path":list(path),"decided":"left","line":4}); steps.append({"label":"Go left","math":_f(tgt)+" < "+_f(k),"note":"Descend left; balance guarantees few such steps."}); cur=nodes[cur]["left"]
        else:
            frames.append({"cur":cur,"path":list(path),"decided":"right","line":4}); steps.append({"label":"Go right","math":_f(tgt)+" > "+_f(k),"note":"Descend right; balance guarantees few such steps."}); cur=nodes[cur]["right"]
    if not found:
        frames.append({"cur":None,"path":list(path),"decided":"absent","line":5}); steps.append({"label":"Reached a leaf","math":"node is null","note":_f(tgt)+" is not in the tree."})
    height=max((nodes[i]["depth"] for i in nodes),default=0)+1
    import math
    ideal=int(math.log2(len(uniq)))+1 if uniq else 0
    result=("Found "+_f(tgt)+" in "+str(len(path))+" step"+("s" if len(path)!=1 else "")+"; balanced height is "+str(height)+" (a plain BST could be far taller).") if found else (_f(tgt)+" is not in the tree (balanced height "+str(height)+").")
    return {"result":result,"target":tgt,"nodes":nodes,"root":root,"height":height,"found":found,
            "frames":frames,"steps":steps,"algorithm":{"pseudocode":_ALGO_PSEUDO,"python":_ALGO_PYTHON},
            "explanation":_EXPLANATION,"law_statement":_DEF,
            "law_source_name":_DEF_SRC_NAME,"law_source_url":_DEF_SRC_URL,"disclaimer":_DISCLAIMER}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
