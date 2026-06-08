"""FAISS (IVF + Product Quantization) - DSA explainer (auto-built to the pilot template).

Viz-first: the canvas teaches; compute() returns result, a stepped trace (each
frame carries a `line` into `algorithm` for the synced code highlight), the four
exam-fact cards plus a data-structure card, a definition line, and a disclaimer.
Never names a success field 'error'.
"""

from core.registry import register

_DISCLAIMER = 'Educational explainer. 2D points stand in for high-dimensional embeddings so clustering and cell-search are visible. IVF (search nearest cells) is animated; product quantization (compression) is explained in the FAQ. This is approximate - it can miss the true nearest neighbour, by design.'
_DEF = 'FAISS speeds up vector similarity search with an inverted file index (IVF): vectors are clustered around centroids, and a query searches only the nprobe nearest clusters rather than all vectors; product quantization (PQ) additionally compresses vectors into compact codes so billions fit in memory, trading a little accuracy for large speed and space gains.'
_DEF_SRC_NAME = 'FAISS wiki - Guidelines'
_DEF_SRC_URL = 'https://github.com/facebookresearch/faiss/wiki'

_ALGO_PSEUDO = [
        'build: cluster all vectors into cells (k centroids)',
        '      (optional) compress vectors with product quantization',
        'query q:',
        '    find the nprobe centroids nearest to q',
        '    compare q only with vectors in those cells',
        '    return the closest found',
]
_ALGO_PYTHON = [
        'centroids = kmeans(vectors, k)',
        'cells = assign_to_nearest(vectors, centroids)',
        '# query:',
        'near = nprobe_nearest(centroids, q)',
        'cands = [v for c in near for v in cells[c]]',
        'return min(cands, key=lambda v: dist(v, q))',
]

_EXPLANATION = [
    {"heading": 'Time complexity', "body": 'Sub-linear - search only nprobe of many clusters instead of all vectors. Tuning nprobe trades speed against recall.'},
    {"heading": 'Space complexity', "body": 'Greatly reduced with product quantization - each vector becomes a few bytes instead of full floats.'},
    {"heading": 'Best data type', "body": 'Massive collections of high-dimensional embeddings - semantic search, recommendations, RAG retrieval.'},
    {"heading": 'Real-world example', "body": 'Finding similar images among a billion: sort them into bins by rough appearance, then only compare within the few most relevant bins.'},
    {"heading": 'The data structure', "body": 'FAISS organises VECTORS into clusters around CENTROIDS (an inverted file: centroid -> list of its vectors), optionally storing each vector as a compressed PQ CODE rather than full coordinates. Searching only a few nearby clusters, over compressed codes, is what lets it handle billions of vectors fast - the structure trades exhaustive accuracy for scale.'},
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
    slug='faiss',
    name='FAISS (IVF + Product Quantization)',
    section="computers",
    topic='Data Structures and Algorithms (DSA)',
    sub='Approximate Nearest Neighbour (ANN)',
    order=2,
    summary='Cluster vectors into cells, search only the nearest cells, and compress vectors to save memory.',
    formula='IVF: assign vectors to nearest centroid; search only the closest few cells. PQ: compress each vector into small codes.',
    tags=['faiss', 'ivf', 'product quantization', 'vector search', 'ann', 'embeddings', 'clustering'],
    viz_template="viz/faiss.html",
    related=['hnsw', 'lsh', 'hash-table-lookup'],
)
def compute(vectors=None, query="5,5", nprobe=2):

    import math
    raw = vectors if vectors else ["1,2","2,1","8,8","9,7","2,9","1,8","8,2","9,3","5,5"]
    def parse(s):
        try: return tuple(float(x) for x in str(s).split(",") if str(x).strip()!="")
        except ValueError: return None
    pts=[parse(v) for v in raw]; pts=[p for p in pts if p and len(p)==2]
    q=parse(query)
    try: nprobe=max(1,int(nprobe))
    except (TypeError,ValueError): nprobe=2
    if not pts or not q or len(q)!=2:
        return {"error":"Provide 2D vectors like 1,2 and a 2D query like 5,5.","steps":[],"disclaimer":_DISCLAIMER}
    n=len(pts)
    # simple fixed 4-centroid clustering by quadrant of the data range
    xs=[p[0] for p in pts]; ys=[p[1] for p in pts]
    mx=(min(xs)+max(xs))/2; my=(min(ys)+max(ys))/2
    cents=[(min(xs),min(ys)),(max(xs),min(ys)),(min(xs),max(ys)),(max(xs),max(ys))]
    def d(a,b): return math.hypot(a[0]-b[0],a[1]-b[1])
    # assign each point to nearest centroid
    assign=[min(range(4),key=lambda c:d(pts[i],cents[c])) for i in range(n)]
    cells={c:[i for i in range(n) if assign[i]==c] for c in range(4)}
    frames=[]; steps=[]
    steps.append({"label":"Cluster vectors","math":str(n)+" vectors into 4 cells","note":"Vectors are grouped around centroids (an inverted file). The query will only search the nearest cells."})
    # rank centroids by distance to q
    cent_order=sorted(range(4),key=lambda c:d(q,cents[c]))
    probed=cent_order[:nprobe]
    frames.append({"phase":"centroids","cents":cents,"pts":pts,"assign":assign,"probed":[],"cand":[],"best":None,"q":list(q),"line":3,
                   "msg":"query "+str(list(q))+": find the "+str(nprobe)+" nearest cell(s)"})
    steps.append({"label":"Pick nearest cells","math":"nprobe = "+str(nprobe),"note":"Centroids ranked by distance to the query; only the nearest "+str(nprobe)+" cell(s) will be searched."})
    frames.append({"phase":"probe","cents":cents,"pts":pts,"assign":assign,"probed":list(probed),"cand":[],"best":None,"q":list(q),"line":4,
                   "msg":"search cells "+str(probed)+" only (skip the rest)"})
    cands=[i for c in probed for i in cells[c]]
    steps.append({"label":"Gather candidates","math":str(len(cands))+" of "+str(n)+" vectors","note":"Only vectors in the probed cells are compared - the rest are skipped, which is the speed-up (and the source of approximation)."})
    best=None; bestd=1e9
    for i in cands:
        dd=d(q,pts[i])
        frames.append({"phase":"compare","cents":cents,"pts":pts,"assign":assign,"probed":list(probed),"cand":list(cands),"best":i,"q":list(q),"line":5,
                       "msg":"compare vector "+str(i)+" "+str(pts[i])+" -> dist "+str(round(dd,2))})
        if dd<bestd: bestd=dd; best=i
        steps.append({"label":"Check vector "+str(i),"math":"dist = "+str(round(dd,2)),"note":"Distance from the query to this candidate."})
    # true nearest (for honesty about approximation)
    true_best=min(range(n),key=lambda i:d(q,pts[i]))
    approx_ok = (best==true_best)
    frames.append({"phase":"done","cents":cents,"pts":pts,"assign":assign,"probed":list(probed),"cand":list(cands),"best":best,"q":list(q),"line":6,
                   "msg":"nearest in probed cells: vector "+str(best)+" "+str(pts[best])})
    steps.append({"label":"Result","math":"approx nearest = vector "+str(best),"note":("This matches the true nearest neighbour." if approx_ok else "Note: the TRUE nearest is vector "+str(true_best)+", in an unprobed cell - increasing nprobe would find it. This is the accuracy/speed trade-off.")})
    result="Approximate nearest to "+str(list(q))+": vector "+str(best)+" "+str(pts[best])+" (distance "+str(round(bestd,2))+"), found by searching only "+str(nprobe)+" of 4 cells." + ("" if approx_ok else " Raising nprobe would recover the exact nearest.")
    return {"result":result,"pts":[list(p) for p in pts],"query":list(q),"best":best,"true_best":true_best,"nprobe":nprobe,
            "frames":frames,"steps":steps,"algorithm":{"pseudocode":_ALGO_PSEUDO,"python":_ALGO_PYTHON},
            "explanation":_EXPLANATION,"law_statement":_DEF,
            "law_source_name":_DEF_SRC_NAME,"law_source_url":_DEF_SRC_URL,"disclaimer":_DISCLAIMER}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
