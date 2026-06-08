"""Trie (Prefix Tree) - DSA explainer (auto-built to the pilot template).

Viz-first: the canvas teaches; compute() returns result, a stepped trace (each
frame carries a `line` into `algorithm` for the synced code highlight), the four
exam-fact cards plus a data-structure card, a definition line, and a disclaimer.
Never names a success field 'error'.
"""

from core.registry import register

_DISCLAIMER = 'Educational explainer. The trie is drawn from your word list; matched nodes mark complete words. Memory grows with shared-prefix structure, noted in the FAQ.'
_DEF = 'A trie stores strings as a tree of characters, where each path from the root spells a prefix and shared prefixes share edges; looking up or prefix-matching a word of length m takes O(m) steps, independent of how many words the trie holds.'
_DEF_SRC_NAME = 'Wikipedia - Trie'
_DEF_SRC_URL = 'https://en.wikipedia.org/wiki/Trie'

_ALGO_PSEUDO = [
        'node = root',
        'for each character c in query:',
        '    if node has no child c: return NOT_FOUND',
        '    node = node.child[c]',
        'return node.is_word   # true if a complete word ends here',
]
_ALGO_PYTHON = [
        'node = root',
        'for c in query:',
        '    if c not in node.children: return False',
        '    node = node.children[c]',
        'return node.is_word',
]

_EXPLANATION = [
    {"heading": 'Time complexity', "body": 'O(m) where m is the length of the word or prefix - and completely independent of how many words the trie contains.'},
    {"heading": 'Space complexity', "body": 'O(total characters), and can be memory-heavy because each node may branch to many children.'},
    {"heading": 'Best data type', "body": 'Strings, especially large dictionaries with shared prefixes - autocomplete, spell-check, IP routing.'},
    {"heading": 'Real-world example', "body": "Typing 'ca...' and instantly seeing 'cat, car, cards' - the trie walks the shared 'ca' path then lists everything below it."},
    {"heading": 'The data structure', "body": 'A trie is a TREE whose edges are labelled with characters, so a node represents the prefix spelled along the path to it. Crucially, lookup time depends on the length of the word, not the number of words stored - a fundamentally different cost model from comparison-based trees.'},
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
    slug='trie',
    name='Trie (Prefix Tree)',
    section="computers",
    topic='Data Structures and Algorithms (DSA)',
    sub='Tree-Based',
    order=4,
    summary='A tree where each branch is a letter, so words sharing a prefix share a path.',
    formula='follow one edge per character; a word exists if the path ends at a marked node',
    tags=['trie', 'prefix tree', 'autocomplete', 'strings', 'O(m)', 'dictionary'],
    viz_template="viz/trie.html",
    related=['binary-search-tree', 'aho-corasick', 'suffix-tree-array'],
)
def compute(words=None, query="car"):
    raw = words if words else ["cat","car","card","cards","care","dog","do","dot"]
    try:
        ws=[str(w).strip().lower() for w in raw if str(w).strip()]
        q=str(query).strip().lower()
    except (TypeError,ValueError):
        return {"error":"Provide words and a query string.","steps":[],"disclaimer":_DISCLAIMER}
    if not ws: return {"error":"Add at least one word.","steps":[],"disclaimer":_DISCLAIMER}
    # build trie with node ids
    nodes={0:{"ch":"","children":{},"word":False,"depth":0,"parent":None}}; nid=0
    for w in ws:
        cur=0
        for c in w:
            ch=nodes[cur]["children"].get(c)
            if ch is None:
                nid+=1; nodes[nid]={"ch":c,"children":{},"word":False,"depth":nodes[cur]["depth"]+1,"parent":cur}
                nodes[cur]["children"][c]=nid; ch=nid
            cur=ch
        nodes[cur]["word"]=True
    # layout: assign columns by DFS order
    col=[0]
    def dfs(i):
        if not nodes[i]["children"]:
            nodes[i]["col"]=col[0]; col[0]+=1; return
        kids=[nodes[i]["children"][k] for k in sorted(nodes[i]["children"])]
        for k in kids: dfs(k)
        nodes[i]["col"]=sum(nodes[k]["col"] for k in kids)/len(kids)
    dfs(0)
    # search trace
    frames=[]; steps=[]; cur=0; ok=True; path=[0]
    for n,c in enumerate(q):
        ch=nodes[cur]["children"].get(c)
        if ch is None:
            frames.append({"path":list(path),"cur":cur,"miss":c,"decided":"miss","line":2,"msg":"no '"+c+"' edge -> '"+q+"' not present"})
            steps.append({"label":"Missing edge","math":"no child '"+c+"'","note":"The path breaks at '"+c+"', so no word with this prefix exists."}); ok=False; break
        path.append(ch); cur=ch
        frames.append({"path":list(path),"cur":cur,"miss":None,"decided":"walk","line":3,"msg":"follow '"+c+"' (prefix '"+q[:n+1]+"')"})
        steps.append({"label":"Follow '"+c+"'","math":"edge '"+c+"'","note":"Descend to the node for prefix '"+q[:n+1]+"'."})
    is_word = ok and nodes[cur]["word"]
    if ok:
        frames.append({"path":list(path),"cur":cur,"miss":None,"decided":"found" if is_word else "prefix","line":4,
                       "msg":("'"+q+"' is a complete word") if is_word else ("'"+q+"' is a valid prefix but not a stored word")})
        steps.append({"label":"End of query","math":"is_word = "+str(is_word),"note":("A complete word ends here." if is_word else "This is a prefix of stored words, but not itself a stored word.")})
    # collect completions
    comps=[]
    if ok:
        def collect(i,acc):
            if nodes[i]["word"]: comps.append(acc)
            for c in sorted(nodes[i]["children"]): collect(nodes[i]["children"][c],acc+c)
        collect(cur,q)
    if not ok:
        result="'"+q+"' is not present - the character path breaks, so no stored word has this prefix."
    elif is_word:
        result="'"+q+"' is a stored word. Words continuing this prefix: "+(", ".join(comps) if comps else q)+"."
    else:
        result="'"+q+"' is a valid prefix (not itself a word). Autocomplete suggestions: "+(", ".join(comps) if comps else "(none)")+"."
    return {"result":result,"query":q,"nodes":nodes,"found":is_word,"completions":comps,
            "frames":frames,"steps":steps,"algorithm":{"pseudocode":_ALGO_PSEUDO,"python":_ALGO_PYTHON},
            "explanation":_EXPLANATION,"law_statement":_DEF,
            "law_source_name":_DEF_SRC_NAME,"law_source_url":_DEF_SRC_URL,"disclaimer":_DISCLAIMER}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
