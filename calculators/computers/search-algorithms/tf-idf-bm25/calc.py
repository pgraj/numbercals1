"""TF-IDF & BM25 (Relevance Ranking) - DSA explainer (auto-built to the pilot template).

Viz-first: the canvas teaches; compute() returns result, a stepped trace (each
frame carries a `line` into `algorithm` for the synced code highlight), the four
exam-fact cards plus a data-structure card, a definition line, and a disclaimer.
Never names a success field 'error'.
"""

from core.registry import register

_DISCLAIMER = "Educational explainer. TF-IDF scores are computed and documents ranked for the query; BM25's refinements (saturation, length normalisation) are described in the FAQ. Real engines tune several parameters."
_DEF = 'TF-IDF scores a term in a document as its term frequency times the inverse document frequency log(N / df), rewarding terms frequent in the document but rare across the corpus; BM25 extends this with term-frequency saturation and document-length normalisation for better ranking.'
_DEF_SRC_NAME = 'Wikipedia - tf-idf'
_DEF_SRC_URL = 'https://en.wikipedia.org/wiki/Tf%E2%80%93idf'

_ALGO_PSEUDO = [
        'for each query term t:',
        '    idf = log(N / docs_containing(t))',
        '    for each doc d containing t:',
        '        score[d] += tf(t, d) * idf',
        'rank documents by score (highest first)',
]
_ALGO_PYTHON = [
        'import math',
        'N = len(docs)',
        'for t in query:',
        '    df = sum(1 for d in docs if t in d)',
        '    idf = math.log(N / df) if df else 0',
        '    for d in docs_with(t): score[d] += tf(t,d) * idf',
]

_EXPLANATION = [
    {"heading": 'Time complexity', "body": 'Proportional to the postings lists of the query terms - score only the documents that actually contain the terms.'},
    {"heading": 'Space complexity', "body": 'O(corpus statistics) - term frequencies and document frequencies, typically stored with the index.'},
    {"heading": 'Best data type', "body": 'Ranking text documents by relevance to a keyword query - the scoring layer of search engines.'},
    {"heading": 'Real-world example', "body": "Ranking recipes for 'saffron': a recipe that says saffron often scores high, but only because saffron is rare across all recipes."},
    {"heading": 'The data structure', "body": 'TF-IDF and BM25 are SCORING FORMULAS applied on top of an inverted index - they operate on term frequencies (per document) and document frequencies (across the corpus). The data they need is just counts; the formulas turn those counts into a relevance number that orders the matching documents.'},
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
    slug='tf-idf-bm25',
    name='TF-IDF & BM25 (Relevance Ranking)',
    section="computers",
    topic='Data Structures and Algorithms (DSA)',
    sub='Information Retrieval',
    order=2,
    summary='Score how relevant each document is: reward query words that are frequent here but rare overall.',
    formula='tf-idf = term_frequency * log(N / docs_containing_term); BM25 refines this with saturation + length',
    tags=['tf-idf', 'bm25', 'ranking', 'relevance', 'search', 'term frequency', 'idf'],
    viz_template="viz/tf-idf-bm25.html",
    related=['inverted-index', 'pagerank'],
)
def compute(docs=None, query="cat"):

    import math
    docs = docs if docs else ["the cat sat on the mat","the dog chased the cat","a cat and a cat play","birds fly high"]
    try:
        D=[str(d).strip().lower() for d in docs if str(d).strip()]
        terms=[w.strip().lower() for w in str(query).split() if w.strip()]
    except (TypeError,ValueError):
        return {"error":"Provide documents and a query.","steps":[],"disclaimer":_DISCLAIMER}
    if not D: return {"error":"Add at least one document.","steps":[],"disclaimer":_DISCLAIMER}
    if not terms: return {"error":"Enter a query word.","steps":[],"disclaimer":_DISCLAIMER}
    N=len(D); tokens=[d.split() for d in D]
    frames=[]; steps=[]; scores=[0.0]*N
    for t in terms:
        df=sum(1 for tk in tokens if t in tk)
        idf=math.log(N/df) if df else 0.0
        steps.append({"label":"IDF of '"+t+"'","math":"log("+str(N)+"/"+str(df)+") = "+str(round(idf,3)),"note":("'"+t+"' appears in "+str(df)+" of "+str(N)+" docs; "+("rare -> high weight" if df<=N/2 else "common -> low weight")+".") if df else "'"+t+"' is not in any document."})
        for di,tk in enumerate(tokens):
            tf=tk.count(t)
            contrib=tf*idf
            scores[di]+=contrib
            if tf>0:
                frames.append({"term":t,"doc":di,"tf":tf,"idf":round(idf,3),"contrib":round(contrib,3),"scores":[round(s,3) for s in scores],"docs":D,"line":4,
                               "msg":"D"+str(di)+": tf('"+t+"')="+str(tf)+" x idf="+str(round(idf,3))+" = +"+str(round(contrib,3))})
                steps.append({"label":"Score D"+str(di)+" for '"+t+"'","math":str(tf)+" x "+str(round(idf,3))+" = "+str(round(contrib,3)),"note":"Add to D"+str(di)+"'s relevance score."})
    ranked=sorted(range(N), key=lambda i:-scores[i])
    frames.append({"term":None,"doc":None,"tf":0,"idf":0,"contrib":0,"scores":[round(s,3) for s in scores],"docs":D,"ranked":ranked,"line":5,
                   "msg":"final ranking: "+", ".join("D"+str(i)+"("+str(round(scores[i],2))+")" for i in ranked if scores[i]>0)})
    steps.append({"label":"Rank","math":"sort by score desc","note":"Documents ordered by relevance. Top: D"+str(ranked[0])+" if it scored highest."})
    top=[i for i in ranked if scores[i]>0]
    if top:
        result="Most relevant: D"+str(top[0])+" (\""+D[top[0]]+"\", score "+str(round(scores[top[0]],3))+"). Ranking rewards query words that are frequent here but rare across the corpus."
    else:
        result="No document contains the query terms, so all scores are zero."
    return {"result":result,"docs":D,"query_terms":terms,"scores":[round(s,3) for s in scores],"ranking":ranked,
            "frames":frames,"steps":steps,"algorithm":{"pseudocode":_ALGO_PSEUDO,"python":_ALGO_PYTHON},
            "explanation":_EXPLANATION,"law_statement":_DEF,
            "law_source_name":_DEF_SRC_NAME,"law_source_url":_DEF_SRC_URL,"disclaimer":_DISCLAIMER}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
