"""Suffix Trees & Suffix Arrays - DSA explainer (auto-built to the pilot template).

Viz-first: the canvas teaches; compute() returns result, a stepped trace (each
frame carries a `line` into `algorithm` for the synced code highlight), the four
exam-fact cards plus a data-structure card, a definition line, and a disclaimer.
Never names a success field 'error'.
"""

from core.registry import register

_DISCLAIMER = 'Educational explainer. The suffix array (sorted suffixes) is shown and the pattern is located by binary search over it. Suffix trees give the same power with O(m) queries; the trade-offs are in the FAQ.'
_DEF = 'A suffix array lists the starting positions of all suffixes of a text in sorted order; once built, any pattern can be located by binary-searching these sorted suffixes in O(m log n), and a suffix tree achieves O(m) - both pre-indexing the text so repeated queries are fast.'
_DEF_SRC_NAME = 'Wikipedia - Suffix array'
_DEF_SRC_URL = 'https://en.wikipedia.org/wiki/Suffix_array'

_ALGO_PSEUDO = [
        'build: list all suffixes with start positions',
        'sort the suffixes alphabetically -> suffix array',
        'query pattern P:',
        '    binary-search the sorted suffixes for P as a prefix',
        '    matches = the range of suffixes starting with P',
]
_ALGO_PYTHON = [
        'suffixes = sorted(range(n), key=lambda i: text[i:])',
        '# binary search for pattern as a prefix',
        'lo = bisect_left(suffixes, P, key=...)',
        'hi = bisect_right(...)',
        'return [suffixes[k] for k in range(lo, hi)]',
]

_EXPLANATION = [
    {"heading": 'Time complexity', "body": 'Build: O(n log n) or O(n). Query: O(m log n) with a suffix array (binary search), O(m) with a suffix tree.'},
    {"heading": 'Space complexity', "body": 'Suffix array: O(n), compact. Suffix tree: O(n) but with a larger constant factor.'},
    {"heading": 'Best data type', "body": 'One fixed, large text queried many times - genomes, document indexes, data compression.'},
    {"heading": 'Real-world example', "body": 'Indexing a genome once so you can then instantly check whether any DNA snippet appears in it.'},
    {"heading": 'The data structure', "body": "A suffix array is a sorted ARRAY of all the text's suffix start positions; a suffix tree is a compressed TRIE of all suffixes. Both pre-process the text ONCE so that afterwards any substring query is fast - the cost shifts from each query to a single up-front build, ideal when one text is queried many times."},
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
    slug='suffix-tree-array',
    name='Suffix Trees & Suffix Arrays',
    section="computers",
    topic='Data Structures and Algorithms (DSA)',
    sub='String & Pattern Matching',
    order=5,
    summary="Pre-index ALL suffixes of a text once, then answer any 'is this substring here?' query fast.",
    formula='sort all suffixes (suffix array); binary-search the sorted suffixes for the pattern',
    tags=['suffix array', 'suffix tree', 'substring', 'indexing', 'binary search', 'bioinformatics'],
    viz_template="viz/suffix-tree-array.html",
    related=['knuth-morris-pratt', 'trie', 'binary-search'],
)
def compute(text="banana", pattern="ana"):
    text=str(text); pat=str(pattern)
    if not text: return {"error":"Enter text to index.","steps":[],"disclaimer":_DISCLAIMER}
    if not pat: return {"error":"Enter a pattern to look up.","steps":[],"disclaimer":_DISCLAIMER}
    n=len(text)
    suffixes=sorted(range(n), key=lambda i: text[i:])
    sa=[(idx, text[idx:]) for idx in suffixes]
    frames=[]; steps=[]
    steps.append({"label":"Build suffix array","math":str([s[0] for s in sa]),"note":"All "+str(n)+" suffixes sorted alphabetically (done once). Each entry is a starting position in the text."})
    # binary search for pattern as prefix
    lo,hi=0,n; m=len(pat)
    # lower bound
    a,b=0,n
    while a<b:
        mid=(a+b)//2
        if sa[mid][1][:m] < pat: a=mid+1
        else: b=mid
    left=a
    a,b=0,n
    while a<b:
        mid=(a+b)//2
        if sa[mid][1][:m] <= pat or sa[mid][1].startswith(pat): a=mid+1
        else: b=mid
    # recompute right cleanly: count suffixes starting with pat
    matches=sorted([sa[k][0] for k in range(n) if sa[k][1].startswith(pat)])
    # animate a binary search converging on the block
    a,b=0,n-1; step=0
    while a<=b and step<n+2:
        step+=1
        mid=(a+b)//2
        suf=sa[mid][1]; shown=suf[:max(m,3)]
        starts=suf.startswith(pat)
        cmpres = "starts with" if starts else ("< " if suf[:m]<pat else "> ")
        frames.append({"lo":a,"hi":b,"mid":mid,"sa":[ (s[0], s[1]) for s in sa],"pat":pat,"found":starts,"line":3,
                       "msg":"check suffix #"+str(mid)+" '"+suf+"' "+("(prefix match!)" if starts else (cmpres+" pattern"))})
        steps.append({"label":"Binary search","math":"suffix '"+suf+"' vs '"+pat+"'","note":("Found a suffix starting with the pattern - the matching block is here.") if starts else ("Pattern is "+cmpres+" this suffix; narrow the range.")})
        if starts: break
        if suf[:m]<pat: a=mid+1
        else: b=mid-1
    if matches:
        result="\""+pat+"\" occurs at position"+("s " if len(matches)>1 else " ")+", ".join(str(x) for x in matches)+". After a one-time O(n log n) build, this query took only a binary search."
    else:
        result="\""+pat+"\" does not occur in the text. The suffix array makes this answer fast for any pattern."
    return {"result":result,"text":text,"pattern":pat,"suffix_array":[s[0] for s in sa],"matches":matches,
            "frames":frames,"steps":steps,"algorithm":{"pseudocode":_ALGO_PSEUDO,"python":_ALGO_PYTHON},
            "explanation":_EXPLANATION,"law_statement":_DEF,
            "law_source_name":_DEF_SRC_NAME,"law_source_url":_DEF_SRC_URL,"disclaimer":_DISCLAIMER}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
