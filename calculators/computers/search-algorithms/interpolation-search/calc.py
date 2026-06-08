"""Interpolation Search - DSA explainer (auto-built to the pilot template).

Viz-first: the canvas teaches; compute() returns result, a stepped trace (each
frame carries a `line` into `algorithm` for the synced code highlight), the four
exam-fact cards plus a data-structure card, a definition line, and a disclaimer.
Never names a success field 'error'.
"""

from core.registry import register

_DISCLAIMER = 'Educational explainer. The estimated probe position is computed from the values at the current ends; on non-uniform data it can degrade toward O(n), which the FAQ explains.'
_DEF = "Interpolation search predicts the target's position by linear interpolation between the low and high values, probing that estimated index rather than the midpoint; on uniformly distributed sorted data this reaches the target in about log log n probes."
_DEF_SRC_NAME = 'Wikipedia - Interpolation search'
_DEF_SRC_URL = 'https://en.wikipedia.org/wiki/Interpolation_search'

_ALGO_PSEUDO = [
        'while lo <= hi and arr[lo] <= target <= arr[hi]:',
        '    pos = lo + (target-arr[lo])*(hi-lo) // (arr[hi]-arr[lo])',
        '    if arr[pos] == target: return pos',
        '    elif arr[pos] < target: lo = pos + 1',
        '    else: hi = pos - 1',
        'return -1',
]
_ALGO_PYTHON = [
        'while lo<=hi and arr[lo]<=target<=arr[hi]:',
        '    if arr[hi]==arr[lo]: pos=lo',
        '    else: pos=lo+(target-arr[lo])*(hi-lo)//(arr[hi]-arr[lo])',
        '    if arr[pos]==target: return pos',
        '    elif arr[pos]<target: lo=pos+1',
        '    else: hi=pos-1',
        'return -1',
]

_EXPLANATION = [
    {"heading": 'Time complexity', "body": 'O(log log n) average on uniformly distributed data - even faster than binary search. But O(n) worst case when values are unevenly spread.'},
    {"heading": 'Space complexity', "body": 'O(1) - just the two end indices and an arithmetic estimate.'},
    {"heading": 'Best data type', "body": 'Sorted AND uniformly distributed numbers - phone numbers, evenly spaced IDs, timestamps.'},
    {"heading": 'Real-world example', "body": "Opening a phone book near the back for 'Wilson' instead of the middle, because you know W is late in the alphabet."},
    {"heading": 'The data structure', "body": 'Interpolation search runs on a SORTED ARRAY of numbers, but it reads the VALUES (not just positions) to guess where the target lies. That makes it sensitive to how the values are distributed - the same sorted array gives fast results when evenly spread and slow ones when clustered.'},
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
    slug='interpolation-search',
    name='Interpolation Search',
    section="computers",
    topic='Data Structures and Algorithms (DSA)',
    sub='Interval & Divide-and-Conquer',
    order=4,
    summary='Estimate where the target likely sits (not always the middle) using the values themselves.',
    formula='pos = lo + (target - arr[lo]) * (hi - lo) / (arr[hi] - arr[lo])',
    tags=['interpolation search', 'sorted', 'uniform distribution', 'O(log log n)', 'estimate'],
    viz_template="viz/interpolation-search.html",
    related=['binary-search', 'jump-search', 'exponential-search'],
)
def compute(array=None, target=23):
    raw = array if array else [2,5,8,12,16,23,38,56,72,91]
    try:
        nums=[int(x) for x in raw]; tgt=int(target)
    except (TypeError,ValueError):
        return {"error":"List values and target must be whole numbers.","steps":[],"disclaimer":_DISCLAIMER}
    if not nums: return {"error":"Enter at least one number.","steps":[],"disclaimer":_DISCLAIMER}
    arr, sort_moves = _bubble_sort(nums)
    n=len(arr); lo=0; hi=n-1; frames=[]; steps=[]; found=-1; guard=0
    while lo<=hi and arr[lo]<=tgt<=arr[hi] and guard<n+5:
        guard+=1
        if arr[hi]==arr[lo]:
            pos=lo
        else:
            pos=lo+(tgt-arr[lo])*(hi-lo)//(arr[hi]-arr[lo])
        pos=max(lo,min(hi,pos))
        val=arr[pos]
        if val==tgt:
            frames.append({"lo":lo,"hi":hi,"probe":pos,"decided":"found","line":2,"msg":"Estimate hit: arr["+str(pos)+"]="+_f(val)})
            steps.append({"label":"Estimate & match","math":"pos="+str(pos)+", arr["+str(pos)+"]="+_f(val)+" = target","note":"The interpolated guess landed on the target."})
            found=pos; break
        elif val<tgt:
            frames.append({"lo":lo,"hi":hi,"probe":pos,"decided":"right","line":3,"msg":"arr["+str(pos)+"]="+_f(val)+" < "+_f(tgt)+" -> search right"})
            steps.append({"label":"Estimate low","math":"arr["+str(pos)+"]="+_f(val)+" < "+_f(tgt),"note":"Guess too low; move the low end past it."})
            lo=pos+1
        else:
            frames.append({"lo":lo,"hi":hi,"probe":pos,"decided":"left","line":4,"msg":"arr["+str(pos)+"]="+_f(val)+" > "+_f(tgt)+" -> search left"})
            steps.append({"label":"Estimate high","math":"arr["+str(pos)+"]="+_f(val)+" > "+_f(tgt),"note":"Guess too high; move the high end before it."})
            hi=pos-1
    if found<0:
        frames.append({"lo":lo,"hi":hi,"probe":-1,"decided":"absent","line":5,"msg":_f(tgt)+" not in the list"})
        steps.append({"label":"End","math":"range empty or target out of bounds","note":"Target is not present."})
    return _finish(arr, tgt, found, frames, steps, sort_moves=sort_moves, input_array=nums)


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
