"""Bloom Filter - DSA explainer (auto-built to the pilot template).

Viz-first: the canvas teaches; compute() returns result, a stepped trace (each
frame carries a `line` into `algorithm` for the synced code highlight), the four
exam-fact cards plus a data-structure card, a definition line, and a disclaimer.
Never names a success field 'error'.
"""

from core.registry import register

_DISCLAIMER = 'Educational explainer. Small demonstration hashes and a short bit array are used so the set/check of bits is visible; real filters use many bits and carefully chosen hashes to keep false positives low.'
_DEF = "A Bloom filter is a bit array with k hash functions; adding an item sets the k bits it hashes to, and a query reports 'definitely not present' if any of those bits is 0, or 'possibly present' if all are 1 - it can give false positives but never false negatives."
_DEF_SRC_NAME = 'Wikipedia - Bloom filter'
_DEF_SRC_URL = 'https://en.wikipedia.org/wiki/Bloom_filter'

_ALGO_PSEUDO = [
        'to query x:',
        'for each of the k hash functions:',
        '    if bit[ hash_i(x) ] == 0:',
        '        return DEFINITELY_NOT_PRESENT',
        'return POSSIBLY_PRESENT   # all k bits were 1',
]
_ALGO_PYTHON = [
        'def contains(x):',
        '    for i in range(k):',
        '        if bits[hash_i(x)] == 0:',
        '            return False      # certain: not present',
        '    return True               # maybe present',
]

_EXPLANATION = [
    {"heading": 'Time complexity', "body": 'O(k) - it computes k hashes and checks k bits, independent of how many items were added.'},
    {"heading": 'Space complexity', "body": 'Very small - a fixed bit array, far smaller than storing the actual items.'},
    {"heading": 'Best data type', "body": 'Cheap membership pre-checks before an expensive lookup, where occasional false positives are acceptable.'},
    {"heading": 'Real-world example', "body": "A bouncer with a rough memory: 'definitely not on the list' (skip the real check) versus 'might be, let me verify properly.'"},
    {"heading": 'The data structure', "body": "The data structure is a BIT ARRAY - just a row of 0s and 1s - plus k hash functions. It stores no keys at all, only the imprint of which bits each item set. That is why it is so memory-light, and also why it can only answer 'definitely no' or 'maybe', never 'definitely yes' with the actual item."},
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
    slug='bloom-filter',
    name='Bloom Filter',
    section="computers",
    topic='Data Structures and Algorithms (DSA)',
    sub='Hash-Based',
    order=2,
    summary="A memory-light structure that says 'definitely not present' for certain, or 'maybe present'.",
    formula='set k bits at hash1(x), hash2(x), ... hashk(x); query: all those bits set => maybe, any unset => definitely no',
    tags=['bloom filter', 'probabilistic', 'membership', 'false positive', 'bit array', 'hashing'],
    viz_template="viz/bloom-filter.html",
    related=['hash-table-lookup', 'lsh'],
)
def compute(items=None, query="mango", bits=16, k=3):
    raw = items if items else ["apple","grape","lemon","peach"]
    try:
        its=[str(x).strip() for x in raw if str(x).strip()]
        q=str(query).strip(); m=max(4,int(bits)); kk=max(1,min(5,int(k)))
    except (TypeError,ValueError):
        return {"error":"Provide items, a query, bit count and k.","steps":[],"disclaimer":_DISCLAIMER}
    if not its: return {"error":"Add at least one item.","steps":[],"disclaimer":_DISCLAIMER}
    def hashes(s):
        out=[]
        for i in range(kk):
            val=(sum(ord(c)*(i+2) for c in s) + i*31 + len(s)*7) % m
            out.append(val)
        return out
    bitarr=[0]*m
    for it in its:
        for pos in hashes(it): bitarr[pos]=1
    qh=hashes(q)
    frames=[]; steps=[]
    definitely_no=False
    for n,pos in enumerate(qh):
        bit=bitarr[pos]
        frames.append({"check":pos,"bit":bit,"bits":list(bitarr),"line":2 if bit==0 else 1,
                       "msg":"hash"+str(n+1)+'("'+q+'") = bit '+str(pos)+" -> "+str(bit)})
        steps.append({"label":"Check bit "+str(pos),"math":"bit["+str(pos)+"] = "+str(bit),
                      "note":("This bit is 0, so the item was definitely never added - stop immediately." if bit==0
                              else "This bit is 1 (set by some item); keep checking the remaining hashes.")})
        if bit==0: definitely_no=True; break
    if definitely_no:
        result='"'+q+'" is DEFINITELY NOT present (a 0 bit proves it was never added).'
        frames.append({"check":-1,"bit":0,"bits":list(bitarr),"line":3,"msg":"definitely not present"})
        steps.append({"label":"Verdict","math":"a checked bit was 0","note":"A Bloom filter never gives a false 'no' - this answer is certain."})
    else:
        actually_in = q in its
        verdict = "POSSIBLY present" + (" (and it really was added)" if actually_in else " - but this is a FALSE POSITIVE: it was never added")
        result='"'+q+'" is '+verdict+'.'
        frames.append({"check":-1,"bit":1,"bits":list(bitarr),"line":4,"msg":"all k bits set -> possibly present"})
        steps.append({"label":"Verdict","math":"all "+str(kk)+" bits were 1",
                      "note":"All bits are set, so the item is possibly present. " + ("It genuinely was added." if actually_in else "It was NOT added - the bits were set by other items. This is the false-positive case Bloom filters allow.")})
    return {"result":result,"query":q,"bits_array":bitarr,"checked":qh,"definitely_no":definitely_no,
            "frames":frames,"steps":steps,"algorithm":{"pseudocode":_ALGO_PSEUDO,"python":_ALGO_PYTHON},
            "explanation":_EXPLANATION,"law_statement":_DEF,
            "law_source_name":_DEF_SRC_NAME,"law_source_url":_DEF_SRC_URL,"disclaimer":_DISCLAIMER}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
