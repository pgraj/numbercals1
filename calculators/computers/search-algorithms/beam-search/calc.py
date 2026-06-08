"""Beam Search - DSA explainer (auto-built to the pilot template).

Viz-first: the canvas teaches; compute() returns result, a stepped trace (each
frame carries a `line` into `algorithm` for the synced code highlight), the four
exam-fact cards plus a data-structure card, a definition line, and a disclaimer.
Never names a success field 'error'.
"""

from core.registry import register

_DISCLAIMER = "Educational explainer. A small branching tree of scored sequences is shown; at each level only the top-k survive. Token scores here are illustrative; in a language model they come from the model's predicted probabilities."
_DEF = 'Beam search explores a sequence space level by level, keeping only the k highest-scoring partial sequences (k = the beam width) at each step and discarding the rest; it is a memory-bounded heuristic that trades guaranteed optimality for tractable search over exponentially many sequences.'
_DEF_SRC_NAME = 'Wikipedia - Beam search'
_DEF_SRC_URL = 'https://en.wikipedia.org/wiki/Beam_search'

_ALGO_PSEUDO = [
        'beam = [empty sequence]',
        'for each step:',
        '    candidates = expand every sequence in beam by each next option',
        '    score all candidates',
        '    beam = top-k candidates (k = beam width)',
        'return the best sequence in the beam',
]
_ALGO_PYTHON = [
        'beam = [([], 0.0)]',
        'for _ in range(steps):',
        '    cand = [(seq+[t], score+s) for seq,score in beam',
        '            for t,s in next_options(seq)]',
        '    beam = sorted(cand, key=score)[-k:]   # top-k',
        'return max(beam, key=score)',
]

_EXPLANATION = [
    {"heading": 'Time complexity', "body": 'O(beam_width * branches * length) - each step expands k sequences over the branching options, for the length of the sequence.'},
    {"heading": 'Space complexity', "body": 'O(beam_width) - only the k surviving sequences are held at any time.'},
    {"heading": 'Best data type', "body": 'Sequence generation with huge branching - machine translation, speech recognition, LLM text decoding.'},
    {"heading": 'Real-world example', "body": 'An AI completing a sentence: it keeps a few promising phrasings going and drops the unlikely ones, rather than committing to the first word that looks best.'},
    {"heading": 'The data structure', "body": 'Beam search explores a TREE of partial sequences but keeps only a fixed-size frontier - the BEAM, a list of the top-k sequences so far. That bounded frontier is the whole idea: it sits between greedy search (k=1, keep only the single best) and exhaustive search (keep everything), giving a tunable balance of quality and cost.'},
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
    slug='beam-search',
    name='Beam Search',
    section="computers",
    topic='Data Structures and Algorithms (DSA)',
    sub='Probabilistic & Sequence',
    order=1,
    summary='Keep only the best few partial sequences at each step - how AI text generation explores options.',
    formula='at each step, expand all kept sequences, score them, keep the top-k (the beam width)',
    tags=['beam search', 'sequence', 'nlp', 'text generation', 'beam width', 'heuristic', 'decoding'],
    viz_template="viz/beam-search.html",
    related=['monte-carlo-tree-search', 'greedy-best-first-search', 'a-star-search'],
)
def compute(beam_width=2, steps=3):

    import random
    try:
        k=max(1,min(4,int(beam_width))); L=max(1,min(5,int(steps)))
    except (TypeError,ValueError):
        k=2; L=3
    tokens=["the","a","cat","dog","runs","sleeps","fast","now"]
    rng=random.Random(7)
    # fixed pseudo log-probabilities for each token given a step (illustrative)
    def options(step):
        opts=[]
        for t in tokens[: 4 ]:
            # deterministic-ish score
            sc=round(-((sum(ord(c) for c in t)+step*13)%9)/3.0,2)
            opts.append((t,sc))
        return opts
    beam=[([],0.0)]
    frames=[]; steps_log=[]
    for step in range(L):
        cand=[]
        for seq,score in beam:
            for t,s in options(step):
                cand.append((seq+[t], round(score+s,2)))
        cand.sort(key=lambda x:-x[1])
        kept=cand[:k]
        frames.append({"step":step+1,"cand":[[ " ".join(c[0]), c[1]] for c in cand],
                       "kept":[[ " ".join(c[0]), c[1]] for c in kept],"k":k,"line":4,
                       "msg":"step "+str(step+1)+": expand to "+str(len(cand))+" candidates, keep top "+str(k)})
        steps_log.append({"label":"Step "+str(step+1),"math":"keep "+str(k)+" of "+str(len(cand)),"note":"All kept sequences are extended by each option, scored, and only the top "+str(k)+" survive to the next step."})
        beam=kept
    best=max(beam,key=lambda x:x[1])
    steps_log.append({"label":"Best sequence","math":"highest cumulative score","note":"The top-scoring sequence in the final beam is returned: \""+" ".join(best[0])+"\"."})
    result="Best sequence (beam width "+str(k)+", "+str(L)+" steps): \""+" ".join(best[0])+"\" (score "+str(best[1])+"). A wider beam explores more options but costs more."
    return {"result":result,"beam_width":k,"steps_n":L,"best":" ".join(best[0]),"final_beam":[[ " ".join(b[0]), b[1]] for b in beam],
            "frames":frames,"steps":steps_log,"algorithm":{"pseudocode":_ALGO_PSEUDO,"python":_ALGO_PYTHON},
            "explanation":_EXPLANATION,"law_statement":_DEF,
            "law_source_name":_DEF_SRC_NAME,"law_source_url":_DEF_SRC_URL,"disclaimer":_DISCLAIMER}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
