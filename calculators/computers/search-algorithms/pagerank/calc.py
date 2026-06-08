"""PageRank - DSA explainer (auto-built to the pilot template).

Viz-first: the canvas teaches; compute() returns result, a stepped trace (each
frame carries a `line` into `algorithm` for the synced code highlight), the four
exam-fact cards plus a data-structure card, a definition line, and a disclaimer.
Never names a success field 'error'.
"""

from core.registry import register

_DISCLAIMER = 'Educational explainer. A small link graph is iterated until the ranks stabilise; the bars show ranks converging. Real PageRank runs over billions of pages with refinements, but the core iteration is exactly this.'
_DEF = "PageRank scores each web page by the probability that a random surfer - who follows links with probability d and jumps to a random page with probability 1-d - lands on it; a page's rank is the sum of fractions of rank passed along incoming links, computed by iterating to convergence."
_DEF_SRC_NAME = 'Wikipedia - PageRank'
_DEF_SRC_URL = 'https://en.wikipedia.org/wiki/PageRank'

_ALGO_PSEUDO = [
        'initialise PR[p] = 1/N for all pages',
        'repeat until stable:',
        '    for each page p:',
        '        PR_new[p] = (1-d)/N + d * sum(PR[q]/out(q) for q -> p)',
        '    PR = PR_new',
        'rank pages by final PR',
]
_ALGO_PYTHON = [
        'PR = {p: 1/N for p in pages}',
        'for _ in range(iterations):',
        '    new = {p: (1-d)/N for p in pages}',
        '    for q in pages:',
        '        for p in links[q]: new[p] += d * PR[q]/len(links[q])',
        '    PR = new',
]

_EXPLANATION = [
    {"heading": 'Time complexity', "body": 'O(iterations * edges) - each iteration pushes rank along every link; usually converges in a few dozen iterations.'},
    {"heading": 'Space complexity', "body": 'O(V + E) - the rank vector plus the link graph.'},
    {"heading": 'Best data type', "body": 'Directed graphs where importance flows along edges - web links, citations, social influence.'},
    {"heading": 'Real-world example', "body": 'An academic paper is influential if many influential papers cite it - importance flows through citations.'},
    {"heading": 'The data structure', "body": "PageRank runs on a DIRECTED GRAPH where nodes are pages and edges are hyperlinks. It repeatedly pushes each page's current rank out along its outgoing links and sums what arrives - an iterative computation on the link graph that converges to the dominant eigenvector of the link matrix."},
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
    slug='pagerank',
    name='PageRank',
    section="computers",
    topic='Data Structures and Algorithms (DSA)',
    sub='Information Retrieval',
    order=3,
    summary='Rank pages by importance: a page is important if important pages link to it.',
    formula='PR(p) = (1-d)/N + d * sum(PR(q)/outlinks(q)) for all q linking to p',
    tags=['pagerank', 'google', 'link analysis', 'random surfer', 'eigenvector', 'importance'],
    viz_template="viz/pagerank.html",
    related=['tf-idf-bm25', 'inverted-index'],
)
def compute(links=None, damping=0.85):

    links = links if links else {"A":["B","C"],"B":["C"],"C":["A"],"D":["C"]}
    try:
        d=float(damping)
    except (TypeError,ValueError):
        d=0.85
    if isinstance(links,str):
        # parse "A>B,C; B>C; C>A; D>C"
        g={}
        for part in links.split(";"):
            if ">" in part:
                src,dst=part.split(">",1); src=src.strip()
                g[src]=[x.strip() for x in dst.split(",") if x.strip()]
        links=g
    if not links: return {"error":"Provide a link graph like A>B,C; B>C; C>A.","steps":[],"disclaimer":_DISCLAIMER}
    pages=sorted(set(list(links.keys())+[p for outs in links.values() for p in outs]))
    N=len(pages)
    for p in pages: links.setdefault(p,[])
    PR={p:1.0/N for p in pages}
    frames=[]; steps=[]
    steps.append({"label":"Initialise","math":"PR = 1/"+str(N)+" each","note":"Every page starts with equal rank; importance will flow along links over several iterations."})
    frames.append({"PR":{p:round(PR[p],3) for p in pages},"iter":0,"pages":pages,"line":1,"msg":"start: all ranks equal (1/"+str(N)+")"})
    for it in range(1,16):
        new={p:(1-d)/N for p in pages}
        for q in pages:
            outs=links[q]
            if outs:
                share=PR[q]/len(outs)
                for p in outs: new[p]+=d*share
            else:
                # dangling node: distribute evenly
                for p in pages: new[p]+=d*PR[q]/N
        delta=sum(abs(new[p]-PR[p]) for p in pages)
        PR=new
        frames.append({"PR":{p:round(PR[p],3) for p in pages},"iter":it,"pages":pages,"line":4,"msg":"iteration "+str(it)+": ranks updated (change "+str(round(delta,4))+")"})
        if it<=3 or delta<1e-4:
            steps.append({"label":"Iteration "+str(it),"math":"total change = "+str(round(delta,4)),"note":"Rank flows along links; pages linked by high-rank pages gain. " + ("Converged." if delta<1e-4 else "Continuing to settle.")})
        if delta<1e-4: break
    ranked=sorted(pages,key=lambda p:-PR[p])
    result="Highest PageRank: "+ranked[0]+" ("+str(round(PR[ranked[0]],3))+"). A page ranks high when important pages link to it - importance flows through the link graph."
    return {"result":result,"pages":pages,"PR":{p:round(PR[p],3) for p in pages},"ranking":ranked,"links":links,
            "frames":frames,"steps":steps,"algorithm":{"pseudocode":_ALGO_PSEUDO,"python":_ALGO_PYTHON},
            "explanation":_EXPLANATION,"law_statement":_DEF,
            "law_source_name":_DEF_SRC_NAME,"law_source_url":_DEF_SRC_URL,"disclaimer":_DISCLAIMER}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
