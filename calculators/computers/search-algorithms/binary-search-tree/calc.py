"""Binary Search Tree (BST) - DSA explainer (auto-built to the pilot template).

Viz-first: the canvas teaches; compute() returns result, a stepped trace (each
frame carries a `line` into `algorithm` for the synced code highlight), the four
exam-fact cards plus a data-structure card, a definition line, and a disclaimer.
Never names a success field 'error'.
"""

from core.registry import register

_DISCLAIMER = 'Educational explainer. The tree is built by inserting your values in order; the shape (and therefore speed) depends on that insertion order, which the FAQ explains.'
_DEF = "A binary search tree stores keys so that every node's left subtree holds only smaller keys and its right subtree only larger keys; searching compares the target with each node and descends left or right, taking time proportional to the tree's height."
_DEF_SRC_NAME = 'Wikipedia - Binary search tree'
_DEF_SRC_URL = 'https://en.wikipedia.org/wiki/Binary_search_tree'

_ALGO_PSEUDO = [
        'node = root',
        'while node is not null:',
        '    if target == node.key: return node',
        '    elif target < node.key: node = node.left',
        '    else: node = node.right',
        'return NOT_FOUND',
]
_ALGO_PYTHON = [
        'node = root',
        'while node:',
        '    if target == node.key: return node',
        '    node = node.left if target < node.key else node.right',
        'return None',
]

_EXPLANATION = [
    {"heading": 'Time complexity', "body": 'O(log n) average when the tree is balanced; O(n) worst case if insertions arrive in sorted order and the tree degenerates into a straight line.'},
    {"heading": 'Space complexity', "body": 'O(n) - one node per key, plus child pointers.'},
    {"heading": 'Best data type', "body": 'Data that changes often and must stay searchable - frequent inserts, deletes, and lookups together.'},
    {"heading": 'Real-world example', "body": "A 'higher or lower' guessing game: each answer sends you down the left or right branch of possibilities."},
    {"heading": 'The data structure', "body": 'A BST is a linked TREE of nodes, each holding a key and pointers to a left and right child. The ordering invariant (left smaller, right larger) is what lets search discard half the remaining tree at each node - the dynamic, pointer-based cousin of the sorted array behind binary search.'},
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
    slug='binary-search-tree',
    name='Binary Search Tree (BST)',
    section="computers",
    topic='Data Structures and Algorithms (DSA)',
    sub='Tree-Based',
    order=1,
    summary='Each node keeps smaller values on its left, larger on its right - so search zig-zags down.',
    formula='at each node: go left if target < node, right if target > node, stop if equal',
    tags=['bst', 'binary search tree', 'ordered', 'insert', 'search', 'O(log n)'],
    viz_template="viz/binary-search-tree.html",
    related=['avl-red-black-tree', 'b-tree', 'skip-list', 'binary-search'],
)
def compute(values=None, target=23):
    raw = values if values else [50,30,70,20,40,60,80,23]
    try:
        vals=[int(x) for x in raw]; tgt=int(target)
    except (TypeError,ValueError):
        return {"error":"Values and target must be whole numbers.","steps":[],"disclaimer":_DISCLAIMER}
    if not vals: return {"error":"Enter at least one value.","steps":[],"disclaimer":_DISCLAIMER}
    # build BST as nodes list with positions for drawing
    nodes={}  # id -> {key,left,right,depth}
    root=None; nid=0
    def insert(root_id,key):
        nonlocal nid
        if root_id is None:
            nid+=1; nodes[nid]={"key":key,"left":None,"right":None}; return nid
        if key<nodes[root_id]["key"]:
            nodes[root_id]["left"]=insert(nodes[root_id]["left"],key)
        elif key>nodes[root_id]["key"]:
            nodes[root_id]["right"]=insert(nodes[root_id]["right"],key)
        return root_id
    for v in vals: root=insert(root,v)
    # assign x by inorder, y by depth (for layout)
    order=[]; 
    def inorder(i,d):
        if i is None: return
        inorder(nodes[i]["left"],d+1); nodes[i]["depth"]=d; order.append(i); inorder(nodes[i]["right"],d+1)
    inorder(root,0)
    for col,i in enumerate(order): nodes[i]["col"]=col
    # search trace
    frames=[]; steps=[]; cur=root; found=False; path=[]
    while cur is not None:
        path.append(cur); k=nodes[cur]["key"]
        if tgt==k:
            frames.append({"cur":cur,"path":list(path),"decided":"found","line":2})
            steps.append({"label":"Match","math":_f(tgt)+" = "+_f(k),"note":"Target found at this node."}); found=True; break
        elif tgt<k:
            frames.append({"cur":cur,"path":list(path),"decided":"left","line":3})
            steps.append({"label":"Go left","math":_f(tgt)+" < "+_f(k),"note":"Smaller than this node - the whole right subtree is skipped."}); cur=nodes[cur]["left"]
        else:
            frames.append({"cur":cur,"path":list(path),"decided":"right","line":4})
            steps.append({"label":"Go right","math":_f(tgt)+" > "+_f(k),"note":"Larger than this node - the whole left subtree is skipped."}); cur=nodes[cur]["right"]
    if not found:
        frames.append({"cur":None,"path":list(path),"decided":"absent","line":5})
        steps.append({"label":"Reached a leaf","math":"node is null","note":_f(tgt)+" is not in the tree."})
    height=max((nodes[i]["depth"] for i in nodes),default=0)+1
    result=("Found "+_f(tgt)+" after "+str(len(path))+" comparison"+("s" if len(path)!=1 else "")+" (tree height "+str(height)+").") if found else (_f(tgt)+" is not in the tree (after "+str(len(path))+" comparison"+("s" if len(path)!=1 else "")+").")
    return {"result":result,"target":tgt,"nodes":nodes,"root":root,"height":height,"found":found,
            "frames":frames,"steps":steps,"algorithm":{"pseudocode":_ALGO_PSEUDO,"python":_ALGO_PYTHON},
            "explanation":_EXPLANATION,"law_statement":_DEF,
            "law_source_name":_DEF_SRC_NAME,"law_source_url":_DEF_SRC_URL,"disclaimer":_DISCLAIMER}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
