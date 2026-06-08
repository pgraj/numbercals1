"""Aho-Corasick - DSA explainer (auto-built to the pilot template).

Viz-first: the canvas teaches; compute() returns result, a stepped trace (each
frame carries a `line` into `algorithm` for the synced code highlight), the four
exam-fact cards plus a data-structure card, a definition line, and a disclaimer.
Never names a success field 'error'.
"""

from core.registry import register

_DISCLAIMER = "Educational explainer. The text is scanned once; at each character the automaton's current trie node is shown, and any patterns ending there are reported. Failure links (the multi-pattern generalisation of KMP) are described in the FAQ."
_DEF = "Aho-Corasick builds a trie of all search patterns augmented with failure links (like KMP's failure function generalised to many patterns), then scans the text once: it follows trie edges on matches and failure links on mismatches, reporting every occurrence of every pattern in O(n + m + z) time."
_DEF_SRC_NAME = 'Wikipedia - Aho-Corasick algorithm'
_DEF_SRC_URL = 'https://en.wikipedia.org/wiki/Aho%E2%80%93Corasick_algorithm'

_ALGO_PSEUDO = [
        'build a trie of all patterns',
        'add failure links (BFS over the trie)',
        'node = root',
        'for each character c in text:',
        '    follow goto/failure links to the next node',
        '    report every pattern ending at this node',
]
_ALGO_PYTHON = [
        'trie = build_trie(patterns)',
        'add_failure_links(trie)   # BFS',
        'node = root',
        'for c in text:',
        '    while no edge c from node and node != root: node = node.fail',
        '    node = node.go(c)',
        '    output += node.matches',
]

_EXPLANATION = [
    {"heading": 'Time complexity', "body": 'O(n + m + z) - n to scan the text, m to build the automaton from all patterns of total length m, z occurrences reported. Independent of how many patterns.'},
    {"heading": 'Space complexity', "body": 'O(m) - the trie of all patterns plus failure links.'},
    {"heading": 'Best data type', "body": 'Scanning text for any of a large dictionary of words at once - filters, intrusion detection, search.'},
    {"heading": 'Real-world example', "body": 'A spam or profanity filter checking every message against thousands of banned phrases in one pass.'},
    {"heading": 'The data structure', "body": "Aho-Corasick builds a TRIE of all the patterns and adds FAILURE LINKS between trie nodes - pointers that say 'if the current character does not extend this path, jump here instead.' The trie shares common prefixes across patterns, and the failure links let a single text scan track all patterns at once."},
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
    slug='aho-corasick',
    name='Aho-Corasick',
    section="computers",
    topic='Data Structures and Algorithms (DSA)',
    sub='String & Pattern Matching',
    order=4,
    summary='Search for MANY patterns at once in a single pass, using a trie with failure links.',
    formula='build a trie of all patterns + failure links; scan the text once, following links on mismatch',
    tags=['aho-corasick', 'multi-pattern', 'trie', 'failure links', 'dictionary matching', 'O(n+m+z)'],
    viz_template="viz/aho-corasick.html",
    related=['knuth-morris-pratt', 'trie', 'rabin-karp'],
)
def compute(text="she sells seashells", patterns="she,he,sea,sells"):

    text=str(text)
    pats = patterns if isinstance(patterns,list) else [p.strip() for p in str(patterns).split(",")]
    pats=[p for p in pats if p]
    if not pats: return {"error":"Enter one or more comma-separated patterns.","steps":[],"disclaimer":_DISCLAIMER}
    if not text: return {"error":"Enter text to search.","steps":[],"disclaimer":_DISCLAIMER}
    # Build trie
    goto=[{}]; out=[set()]; fail=[0]
    for pi,p in enumerate(pats):
        cur=0
        for ch in p:
            if ch not in goto[cur]:
                goto.append({}); out.append(set()); fail.append(0); goto[cur][ch]=len(goto)-1
            cur=goto[cur][ch]
        out[cur].add(p)
    # BFS failure links
    from collections import deque
    q=deque()
    for ch,nx in goto[0].items(): fail[nx]=0; q.append(nx)
    while q:
        u=q.popleft()
        for ch,v in goto[u].items():
            q.append(v)
            f=fail[u]
            while f and ch not in goto[f]: f=fail[f]
            fail[v]=goto[f].get(ch,0) if goto[f].get(ch,0)!=v else 0
            out[v]|=out[fail[v]]
    # scan
    frames=[]; steps=[]; found=[]
    node=0
    for i,ch in enumerate(text):
        while node and ch not in goto[node]: node=fail[node]
        node=goto[node].get(ch,0)
        hits=sorted(out[node])
        if hits:
            for h in hits: found.append((h,i-len(h)+1))
        frames.append({"i":i,"ch":ch,"node":node,"hits":hits,"text":text,"line":4,
                       "msg":"read '"+ch+"' (pos "+str(i)+")"+(" -> match: "+", ".join(hits) if hits else "")})
        steps.append({"label":"Read '"+ch+"' (pos "+str(i)+")","math":"automaton node "+str(node),"note":("Patterns ending here: "+", ".join(hits)+".") if hits else "Advance the automaton; no pattern ends here yet."})
    uniq=sorted(set(p for p,_ in found))
    if found:
        detail="; ".join(p+"@"+str(pos) for p,pos in found[:8])
        result="Found "+str(len(found))+" occurrence"+("s" if len(found)!=1 else "")+" of "+str(len(uniq))+" pattern"+("s" if len(uniq)!=1 else "")+" in ONE pass: "+detail+("..." if len(found)>8 else "")+"."
    else:
        result="None of the "+str(len(pats))+" patterns occur in the text (single pass)."
    return {"result":result,"text":text,"patterns":pats,"matches":[[p,pos] for p,pos in found],
            "frames":frames,"steps":steps,"algorithm":{"pseudocode":_ALGO_PSEUDO,"python":_ALGO_PYTHON},
            "explanation":_EXPLANATION,"law_statement":_DEF,
            "law_source_name":_DEF_SRC_NAME,"law_source_url":_DEF_SRC_URL,"disclaimer":_DISCLAIMER}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
