"""HNSW (Hierarchical Navigable Small World) — 3D interactive explainer.

The student enters 1-5 short documents (<=30 chars each) and a search word.
compute() ranks the documents by LEXICAL similarity to the query (word/character
overlap - NOT true embeddings; that needs a server-side embeddings route, see
README), and returns a layered greedy-descent trace the 3D viz animates: the
query enters a sparse top layer and hops down toward the closest document.

Honesty: this is lexical similarity standing in for semantic similarity so the
GRAPH MECHANIC is teachable offline. The disclaimer and an FAQ say so plainly.
"""

from core.registry import register

_DISCLAIMER = (
    "Educational explainer. Similarity here is LEXICAL (shared words and "
    "characters), used as a stand-in so the HNSW graph-walk can be shown offline. "
    "Real HNSW compares meaning via embedding vectors and returns APPROXIMATE "
    "nearest neighbours - trading a little accuracy for large speed gains. See the "
    "FAQ on lexical vs semantic similarity."
)

_DEF = (
    "HNSW arranges items as a multi-layer graph of 'navigable small world' links: "
    "a sparse top layer for long-range hops and dense lower layers for fine search. "
    "A query enters at the top, greedily walks to the closest neighbour, then drops "
    "a layer and repeats - reaching the nearest match in roughly logarithmic hops."
)
_DEF_SRC_NAME = "Malkov & Yashunin (2016), 'Efficient and robust ANN search using HNSW'"
_DEF_SRC_URL = "https://arxiv.org/abs/1603.09320"

_DEFAULT_DOCS = [
    "the dog chased the cat",
    "fresh pasta with tomato sauce",
    "electric cars charge overnight",
]

_EXPLANATION = [
    {"heading": "Time complexity",
     "body": "Roughly O(log n) per query. Sparse upper layers cover huge distances "
             "in a few hops before refining at the dense bottom layer."},
    {"heading": "Space complexity",
     "body": "O(n) and memory-heavy: every item stores neighbour links across "
             "layers, so a large index usually lives in RAM."},
    {"heading": "Best data type",
     "body": "High-dimensional vectors - text or image embeddings. It is the "
             "backbone of vector databases (Pinecone, Weaviate, ChromaDB, Milvus) "
             "and so of RAG / AI retrieval."},
    {"heading": "Real-world example",
     "body": "An AI assistant searching your notes by meaning, or 'documents like "
             "this one' - exactly the document-search you just ran, but over "
             "millions of items."},
    {"heading": "The greedy hop",
     "body": "Within any layer the search only ever moves to the neighbour that's "
             "closer to the query, never backward. It stops the moment no neighbour "
             "improves."},
    {"heading": "The descent",
     "body": "When a layer offers no closer step, the search drops to the same node "
             "on the layer below and resumes. The top layer's long links cover huge "
             "distance in one hop; each layer down refines within a smaller "
             "neighbourhood."},
    {"heading": "The economy",
     "body": "Notice how few nodes the marker ever touches. That's the whole "
             "payoff: logarithmic-ish search instead of scanning all ten (or, in a "
             "real index, all million) nodes."},
    {"heading": "The data structure",
     "body": "HNSW runs on a GRAPH - nodes (one per item) joined by edges to their "
             "neighbours, stored as an adjacency list so each node just keeps a "
             "short list of who it links to. The layered twist puts the same nodes "
             "on stacked levels, sparse on top and dense below, so one structure "
             "supports both long jumps and fine local search. Contrast binary "
             "search's sorted array - each algorithm is really defined by the data "
             "structure beneath it."},
]


_ALGO_PSEUDO = [
    "entry = top layer's entry point",                       # 0
    "for layer from top down to 0:",                         # 1
    "    while a neighbour is closer to query than current:",# 2
    "        current = that closer neighbour   # greedy hop",# 3
    "    drop down one layer, keep current as entry",        # 4
    "return current   # approximate nearest neighbour",      # 5
]
_ALGO_PYTHON = [
    "current = entry_point(top_layer)",                      # 0
    "for layer in range(top, -1, -1):",                      # 1
    "    while True:",                                       # 2
    "        nxt = closest_neighbour(current, layer, query)",# 2
    "        if dist(nxt) >= dist(current): break",          # 2
    "        current = nxt                      # greedy hop",# 3
    "    # descend to the next, denser layer",               # 4
    "return current",                                        # 5
]

_STOP = {"the", "a", "an", "of", "with", "and", "to", "in", "on", "for"}


def _tokens(s):
    out = []
    word = ""
    for ch in s.lower():
        if ch.isalnum():
            word += ch
        else:
            if word:
                out.append(word)
            word = ""
    if word:
        out.append(word)
    return out


def _bigrams(text):
    t = "".join(_tokens(text))
    return set(t[i:i + 2] for i in range(len(t) - 1))


def _similarity(query, doc):
    """Lexical similarity 0..1: blend of shared-word overlap and char-bigram overlap."""
    q_words = set(_tokens(query)) - _STOP
    d_words = set(_tokens(doc)) - _STOP
    if not q_words:
        return 0.0
    shared = q_words & d_words
    word_score = len(shared) / max(1, len(q_words))
    qb, db = _bigrams(query), _bigrams(doc)
    char_score = (len(qb & db) / max(1, len(qb))) if qb else 0.0
    return round(0.7 * word_score + 0.3 * char_score, 3)


@register(
    slug="hnsw",
    name="HNSW (Vector / Semantic Search)",
    section="computers",
    topic="Data Structures and Algorithms (DSA)",
    sub="Approximate Nearest Neighbour",
    order=10,
    summary="Search your own documents the way a vector database does - by similarity, animated as a layered graph walk.",
    formula="multi-layer navigable small-world graph; greedy descent layer by layer.",
    tags=["hnsw", "vector search", "ann", "approximate nearest neighbour",
          "embeddings", "rag", "semantic search", "vector database",
          "document search"],
    viz_template="viz/hnsw.html",
    related=["faiss", "lsh", "beam-search", "inverted-index"],
)
def compute(documents=None, query="dog"):
    """Rank up to 5 documents by lexical similarity to query; build a descent trace."""
    docs = documents if documents else list(_DEFAULT_DOCS)
    clean = []
    for d in docs:
        if d is None:
            continue
        text = str(d).strip()[:30]
        if text:
            clean.append(text)
        if len(clean) >= 5:
            break
    if not clean:
        return {"error": "Add at least one document (up to 30 characters each).",
                "steps": [], "disclaimer": _DISCLAIMER}

    q = str(query).strip()
    if not q:
        return {"error": "Type a word or phrase to search for.",
                "steps": [], "disclaimer": _DISCLAIMER}

    scored = []
    for i, d in enumerate(clean):
        scored.append({"index": i, "doc": d, "score": _similarity(q, d)})
    ranked = sorted(scored, key=lambda r: r["score"], reverse=True)
    best = ranked[0]

    n = len(clean)
    base = list(range(n))
    mid = [r["index"] for r in ranked[:max(1, (n + 1) // 2)]]
    top = [ranked[0]["index"]] if n >= 1 else []
    layers = [
        {"layer": 2, "members": top,
         "note": "Sparse top layer - one entry point for long-range hops."},
        {"layer": 1, "members": mid,
         "note": "Middle layer - the more promising documents."},
        {"layer": 0, "members": base,
         "note": "Dense base layer - every document; the walk settles on the closest."},
    ]

    steps = []
    steps.append({
        "line": 0,
        "label": "Query enters the graph",
        "math": "query = \"" + q + "\"",
        "note": "The search word enters at the sparse top layer and looks for the "
                "nearest document by similarity.",
    })
    for li, lv in enumerate(layers):
        names = ", ".join('"' + clean[m] + '"' for m in lv["members"]) or "(none)"
        steps.append({
            "line": min(1 + li, 4),
            "label": "Layer " + str(lv["layer"])
                     + (" (entry)" if li == 0 else "")
                     + (" (base)" if li == len(layers) - 1 else ""),
            "math": "candidates: " + names,
            "note": lv["note"] + " Greedily move toward the most similar, then drop "
                    "a layer.",
        })
    steps.append({
        "line": 5,
        "label": "Match found",
        "math": '"' + best["doc"] + '"  (similarity ' + str(best["score"]) + ")",
        "note": "The base-layer walk halts at the closest document - returned as the "
                "(approximate) nearest neighbour.",
    })

    if best["score"] <= 0:
        result = ('No document is lexically similar to "' + q + '". Try a word that '
                  'appears in one of your documents.')
    else:
        result = ('Closest document to "' + q + '": "' + best["doc"]
                  + '" (similarity ' + str(best["score"]) + ").")

    return {
        "result": result,
        "query": q,
        "documents": clean,
        "ranked": ranked,
        "layers": layers,
        "best_index": best["index"],
        "algorithm": {"pseudocode": _ALGO_PSEUDO, "python": _ALGO_PYTHON},
        "steps": steps,
        "explanation": _EXPLANATION,
        "law_statement": _DEF,
        "law_source_name": _DEF_SRC_NAME,
        "law_source_url": _DEF_SRC_URL,
        "disclaimer": _DISCLAIMER,
    }


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
