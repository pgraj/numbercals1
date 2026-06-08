"""Inverted Index - DSA explainer (auto-built to the pilot template).

Viz-first: the canvas teaches; compute() returns result, a stepped trace (each
frame carries a `line` into `algorithm` for the synced code highlight), the four
exam-fact cards plus a data-structure card, a definition line, and a disclaimer.
Never names a success field 'error'.
"""

from core.registry import register

_DISCLAIMER = 'Educational explainer. A handful of short documents are indexed; the postings lists and the intersection for a multi-word query are shown. Real engines add positions, frequencies, and compression.'
_DEF = "An inverted index maps each term to the list of documents that contain it (its postings list); a query is answered by looking up each term's list and combining them, so the engine retrieves matching documents without scanning any document text at query time."
_DEF_SRC_NAME = 'Wikipedia - Inverted index'
_DEF_SRC_URL = 'https://en.wikipedia.org/wiki/Inverted_index'

_ALGO_PSEUDO = [
        'build: for each document d, for each word w:',
        '    index[w].add(d)',
        'query(words):',
        '    lists = [index[w] for w in words]',
        '    return intersection(lists)   # docs with ALL words',
]
_ALGO_PYTHON = [
        'index = defaultdict(set)',
        'for d, text in enumerate(docs):',
        '    for w in text.split(): index[w].add(d)',
        'result = set.intersection(*(index[w] for w in query.split()))',
]

_EXPLANATION = [
    {"heading": 'Time complexity', "body": 'Term lookup is O(1) (hash) or O(log V); answering a query is proportional to the sizes of the postings lists involved, not the whole corpus.'},
    {"heading": 'Space complexity', "body": 'O(total terms across documents) - one posting per (term, document) occurrence.'},
    {"heading": 'Best data type', "body": 'Full-text search over large document collections - the core of every search engine.'},
    {"heading": 'Real-world example', "body": "A book's index at the back: look up a word and jump straight to the pages it appears on."},
    {"heading": 'The data structure', "body": "An inverted index is a HASH MAP (or sorted dictionary) from each term to a POSTINGS LIST - the documents containing it. It inverts the natural document->words layout into words->documents, which is exactly the direction a search needs, turning 'which docs have this word?' into a direct lookup."},
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
    slug='inverted-index',
    name='Inverted Index',
    section="computers",
    topic='Data Structures and Algorithms (DSA)',
    sub='Information Retrieval',
    order=1,
    summary='Flip documents into a word->documents map, so a search jumps straight to matching docs.',
    formula='for each word, store the list of documents containing it; query = intersect those lists',
    tags=['inverted index', 'search engine', 'postings list', 'full text search', 'O(1) term lookup'],
    viz_template="viz/inverted-index.html",
    related=['tf-idf-bm25', 'pagerank', 'hash-table-lookup'],
)
def compute(docs=None, query="cat dog"):

    docs = docs if docs else ["the cat sat","the dog ran","cat and dog play","a bird sang"]
    try:
        D=[str(d).strip() for d in docs if str(d).strip()]
        terms=[w.strip().lower() for w in str(query).split() if w.strip()]
    except (TypeError,ValueError):
        return {"error":"Provide documents and a query.","steps":[],"disclaimer":_DISCLAIMER}
    if not D: return {"error":"Add at least one document.","steps":[],"disclaimer":_DISCLAIMER}
    if not terms: return {"error":"Enter one or more query words.","steps":[],"disclaimer":_DISCLAIMER}
    index={}
    for di,text in enumerate(D):
        for w in text.lower().split():
            index.setdefault(w,set()).add(di)
    index={w:sorted(s) for w,s in index.items()}
    frames=[]; steps=[]
    steps.append({"label":"Build the index","math":str(len(index))+" unique terms","note":"Each term now points to the list of documents that contain it (its postings list)."})
    # show each query term's postings, then intersect
    postings=[]
    for t in terms:
        plist=index.get(t,[])
        postings.append(set(plist))
        frames.append({"phase":"lookup","term":t,"plist":plist,"result":[],"index":index,"terms":terms,"line":4,
                       "msg":"look up '"+t+"' -> docs "+(str(plist) if plist else "(none)")})
        steps.append({"label":"Look up '"+t+"'","math":"postings = "+str(plist),"note":("Documents containing '"+t+"': "+", ".join("D"+str(x) for x in plist)+".") if plist else "No document contains '"+t+"'."})
    result_docs=sorted(set.intersection(*postings)) if postings and all(postings) else []
    frames.append({"phase":"intersect","term":None,"plist":[],"result":result_docs,"index":index,"terms":terms,"line":5,
                   "msg":"intersect all lists -> "+(str(result_docs) if result_docs else "(no doc has all terms)")})
    steps.append({"label":"Intersect","math":"docs with ALL query words = "+str(result_docs),"note":("Documents matching every query word: "+", ".join("D"+str(x) for x in result_docs)+".") if result_docs else "No single document contains all the query words."})
    if result_docs:
        result="Query "+str(terms)+" matches document"+("s " if len(result_docs)>1 else " ")+", ".join("D"+str(x)+" (\""+D[x]+"\")" for x in result_docs)+" - found by list intersection, no document scanned."
    else:
        result="No document contains all of "+str(terms)+". The index answered instantly by intersecting postings lists."
    return {"result":result,"docs":D,"query_terms":terms,"index":index,"matches":result_docs,
            "frames":frames,"steps":steps,"algorithm":{"pseudocode":_ALGO_PSEUDO,"python":_ALGO_PYTHON},
            "explanation":_EXPLANATION,"law_statement":_DEF,
            "law_source_name":_DEF_SRC_NAME,"law_source_url":_DEF_SRC_URL,"disclaimer":_DISCLAIMER}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
