"""LSH (Locality-Sensitive Hashing) - DSA explainer (auto-built to the pilot template).

Viz-first: the canvas teaches; compute() returns result, a stepped trace (each
frame carries a `line` into `algorithm` for the synced code highlight), the four
exam-fact cards plus a data-structure card, a definition line, and a disclaimer.
Never names a success field 'error'.
"""

from core.registry import register

_DISCLAIMER = "Educational explainer. A simple bit-sampling hash over short binary vectors is used so 'similar items collide' is visible; production LSH uses families like MinHash or SimHash tuned to a chosen similarity measure."
_DEF = "Locality-sensitive hashing uses hash functions for which the probability that two items collide rises with their similarity, so similar items fall into the same bucket; candidate matches are then drawn only from the query's bucket instead of comparing against everything."
_DEF_SRC_NAME = 'Wikipedia - Locality-sensitive hashing'
_DEF_SRC_URL = 'https://en.wikipedia.org/wiki/Locality-sensitive_hashing'

_ALGO_PSEUDO = [
        'pick a locality-sensitive hash family',
        'for each item: bucket = lsh_hash(item)',
        '    store item in table[bucket]',
        'to query q: b = lsh_hash(q)',
        'compare q only with items in table[b]   # candidates',
        'return the closest candidate(s)',
]
_ALGO_PYTHON = [
        'def lsh_hash(v): return tuple(v[i] for i in sampled_positions)',
        'for item in items:',
        '    table[lsh_hash(item)].append(item)',
        'cand = table[lsh_hash(query)]',
        'return min(cand, key=lambda c: distance(c, query))',
]

_EXPLANATION = [
    {"heading": 'Time complexity', "body": "Sub-linear - you compare the query only against its bucket's contents, not all n items, so it beats the O(n*n) cost of checking every pair."},
    {"heading": 'Space complexity', "body": 'O(n) - items are stored across buckets, often with several hash tables for accuracy.'},
    {"heading": 'Best data type', "body": "High-dimensional data where 'similar' matters more than 'identical' - images, text embeddings, documents."},
    {"heading": 'Real-world example', "body": 'Sorting photos into rough piles by colour so visually similar ones sit together, then only comparing within a pile.'},
    {"heading": 'The data structure', "body": 'LSH stores items in a HASH TABLE of buckets, but the hash is deliberately NOT collision-avoiding - it is collision-SEEKING for similar inputs. Where an ordinary hash table scatters similar keys apart, LSH pulls them together, so a bucket becomes a pool of likely-similar candidates. It is the bridge between hashing and nearest-neighbour search.'},
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
    slug='lsh',
    name='LSH (Locality-Sensitive Hashing)',
    section="computers",
    topic='Data Structures and Algorithms (DSA)',
    sub='Hash-Based',
    order=3,
    summary="A hash designed so that SIMILAR items land in the same bucket - find 'alike', not identical.",
    formula='choose hashes where Pr[h(a)=h(b)] grows with similarity(a,b); group items by bucket',
    tags=['lsh', 'locality sensitive hashing', 'similarity', 'near duplicate', 'buckets', 'approximate'],
    viz_template="viz/lsh.html",
    related=['hash-table-lookup', 'bloom-filter', 'hnsw', 'faiss'],
)
def compute(items=None, query="1,1,0,1,0", bands=2):
    import itertools
    raw = items if items else ["1,1,0,1,0","1,1,1,1,0","0,0,1,0,1","1,0,0,1,0","0,1,1,0,1"]
    def parse(s):
        return [1 if str(t).strip() in ("1","true","True") else 0 for t in str(s).split(",") if str(t).strip()!=""]
    try:
        vecs=[parse(x) for x in raw if parse(x)]
        q=parse(query); nb=max(1,min(4,int(bands)))
    except (TypeError,ValueError):
        return {"error":"Provide binary vectors (comma-separated 0/1) and a query vector.","steps":[],"disclaimer":_DISCLAIMER}
    if not vecs or not q: return {"error":"Add at least one item vector and a query vector.","steps":[],"disclaimer":_DISCLAIMER}
    dim=min(len(q), min(len(v) for v in vecs))
    vecs=[v[:dim] for v in vecs]; q=q[:dim]
    # LSH = sample the first nb bit positions as the bucket signature
    sampled=list(range(min(nb,dim)))
    def sig(v): return tuple(v[i] for i in sampled)
    buckets={}
    for idx,v in enumerate(vecs):
        buckets.setdefault(sig(v),[]).append(idx)
    qsig=sig(q)
    def ham(a,b): return sum(1 for x,y in zip(a,b) if x!=y)
    frames=[]; steps=[]
    frames.append({"phase":"hash","qsig":list(qsig),"cand":[],"probe":-1,"line":3,
                   "buckets":{str(list(k)):v for k,v in buckets.items()},"vecs":[list(v) for v in vecs],
                   "msg":"LSH signature of query = "+str(list(qsig))})
    steps.append({"label":"Hash the query","math":"signature = "+str(list(qsig)),
                  "note":"The query's signature (its first "+str(len(sampled))+" bits) picks the bucket of likely-similar candidates."})
    cand=buckets.get(qsig,[])
    frames.append({"phase":"bucket","qsig":list(qsig),"cand":list(cand),"probe":-1,"line":4,
                   "buckets":{str(list(k)):v for k,v in buckets.items()},"vecs":[list(v) for v in vecs],
                   "msg":("candidates in bucket: "+", ".join("#"+str(c+1) for c in cand)) if cand else "no candidates share the query's bucket"})
    steps.append({"label":"Gather candidates","math":"table["+str(list(qsig))+"]",
                  "note":("Only "+str(len(cand))+" of "+str(len(vecs))+" items share the bucket - we compare just those, not everything.") if cand else "No item shares the bucket; with more hash tables LSH would still find near matches."})
    best=-1; bestd=10**9
    for c in cand:
        d=ham(q,vecs[c])
        frames.append({"phase":"probe","qsig":list(qsig),"cand":list(cand),"probe":c,"line":5,
                       "buckets":{str(list(k)):v for k,v in buckets.items()},"vecs":[list(v) for v in vecs],
                       "msg":"compare #"+str(c+1)+" -> distance "+str(d)})
        steps.append({"label":"Compare candidate #"+str(c+1),"math":"Hamming distance = "+str(d),
                      "note":"Differs from the query in "+str(d)+" bit"+("s" if d!=1 else "")+"."})
        if d<bestd: bestd=d; best=c
    if best>=0:
        result="Closest similar item: #"+str(best+1)+" "+str(vecs[best])+" (distance "+str(bestd)+"), found by comparing only the query's bucket."
        frames.append({"phase":"done","qsig":list(qsig),"cand":list(cand),"probe":best,"line":5,
                       "buckets":{str(list(k)):v for k,v in buckets.items()},"vecs":[list(v) for v in vecs],
                       "msg":"closest: #"+str(best+1)+" (distance "+str(bestd)+")"})
        steps.append({"label":"Result","math":"min distance = "+str(bestd),"note":"The nearest item in the bucket is returned as the approximate match."})
    else:
        result="No candidate shared the query's bucket. In practice LSH uses several hash tables so near-matches are still caught."
    return {"result":result,"query":q,"vecs":[list(v) for v in vecs],"buckets":{str(list(k)):v for k,v in buckets.items()},
            "qsig":list(qsig),"best":best,"frames":frames,"steps":steps,
            "algorithm":{"pseudocode":_ALGO_PSEUDO,"python":_ALGO_PYTHON},
            "explanation":_EXPLANATION,"law_statement":_DEF,
            "law_source_name":_DEF_SRC_NAME,"law_source_url":_DEF_SRC_URL,"disclaimer":_DISCLAIMER}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
