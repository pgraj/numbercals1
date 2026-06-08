"""Exponential Search - DSA explainer (auto-built to the pilot template).

Viz-first: the canvas teaches; compute() returns result, a stepped trace (each
frame carries a `line` into `algorithm` for the synced code highlight), the four
exam-fact cards plus a data-structure card, a definition line, and a disclaimer.
Never names a success field 'error'.
"""

from core.registry import register

_DISCLAIMER = 'Educational explainer. The doubling phase and the bounded binary-search phase are shown separately over a small sample.'
_DEF = 'Exponential search first finds a range containing the target by repeatedly doubling an index bound until the value there exceeds the target, then runs binary search within that bounded range; this finds the target in O(log n) even when the list size is unknown.'
_DEF_SRC_NAME = 'Wikipedia - Exponential search'
_DEF_SRC_URL = 'https://en.wikipedia.org/wiki/Exponential_search'

_ALGO_PSEUDO = [
        'if arr[0] == target: return 0',
        'bound = 1',
        'while bound < n and arr[bound] < target:   # double',
        '    bound *= 2',
        'lo = bound // 2; hi = min(bound, n - 1)',
        'binary search arr between lo and hi',
]
_ALGO_PYTHON = [
        'if arr[0]==target: return 0',
        'bound=1',
        'while bound<n and arr[bound]<target:',
        '    bound*=2',
        'lo, hi = bound//2, min(bound, n-1)',
        'return binary_search(arr, lo, hi, target)',
]

_EXPLANATION = [
    {"heading": 'Time complexity', "body": 'O(log n) - the doubling phase takes about log(position) steps, then binary search over a range of similar size takes another log. Both are logarithmic.'},
    {"heading": 'Space complexity', "body": 'O(1) - a doubling bound plus binary-search indices.'},
    {"heading": 'Best data type', "body": 'Sorted data of unknown or unbounded length, and cases where the target is likely near the start (the doubling finds it fast).'},
    {"heading": 'Real-world example', "body": 'Probing how deep a pond is by checking 1m, 2m, 4m, 8m until you overshoot, then narrowing between the last two depths.'},
    {"heading": 'The data structure', "body": 'Exponential search runs on a SORTED ARRAY but, crucially, does not need to know its length in advance - it discovers a bound by doubling. That makes it suited to unbounded or streamed sorted sequences where you cannot ask for the size up front, unlike plain binary search which needs both ends.'},
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
    slug='exponential-search',
    name='Exponential Search',
    section="computers",
    topic='Data Structures and Algorithms (DSA)',
    sub='Interval & Divide-and-Conquer',
    order=5,
    summary='Double the range (1,2,4,8...) until you pass the target, then binary-search that range.',
    formula='bound = 1; while arr[bound] < target: bound *= 2; binary_search(arr, bound/2, min(bound,n-1))',
    tags=['exponential search', 'galloping search', 'unbounded', 'sorted', 'O(log n)'],
    viz_template="viz/exponential-search.html",
    related=['binary-search', 'jump-search', 'interpolation-search'],
)
def compute(array=None, target=23):
    raw = array if array else [2,5,8,12,16,23,38,56,72,91]
    try:
        nums=[int(x) for x in raw]; tgt=int(target)
    except (TypeError,ValueError):
        return {"error":"List values and target must be whole numbers.","steps":[],"disclaimer":_DISCLAIMER}
    if not nums: return {"error":"Enter at least one number.","steps":[],"disclaimer":_DISCLAIMER}
    arr, sort_moves = _bubble_sort(nums)
    n=len(arr); frames=[]; steps=[]; found=-1
    if arr[0]==tgt:
        frames.append({"lo":0,"hi":0,"probe":0,"decided":"found","line":0,"msg":"arr[0] is the target"})
        steps.append({"label":"Check first","math":"arr[0] = "+_f(tgt),"note":"Target is the first element."})
        return _finish(arr, tgt, 0, frames, steps, sort_moves=sort_moves, input_array=nums)
    bound=1
    while bound<n and arr[bound]<tgt:
        frames.append({"lo":0,"hi":min(bound,n-1),"probe":bound,"decided":"double","line":2,"msg":"Double: arr["+str(bound)+"]="+_f(arr[bound])+" < "+_f(tgt)})
        steps.append({"label":"Double bound","math":"arr["+str(bound)+"] = "+_f(arr[bound])+" < "+_f(tgt),"note":"Still below target; double the bound to "+str(bound*2)+"."})
        bound*=2
    lo=bound//2; hi=min(bound,n-1)
    frames.append({"lo":lo,"hi":hi,"probe":hi,"decided":"bounded","line":4,"msg":"Range found: indices "+str(lo)+".."+str(hi)+" - now binary search"})
    steps.append({"label":"Bounded","math":"search arr["+str(lo)+".."+str(hi)+"]","note":"Target must lie in this doubled range; binary-search it."})
    # binary search in [lo,hi]
    while lo<=hi:
        mid=(lo+hi)//2; val=arr[mid]
        if val==tgt:
            frames.append({"lo":lo,"hi":hi,"probe":mid,"decided":"found","line":5,"msg":"Found "+_f(tgt)+" at index "+str(mid)})
            steps.append({"label":"Binary match","math":"arr["+str(mid)+"] = "+_f(tgt),"note":"Found at index "+str(mid)+"."})
            found=mid; break
        elif val<tgt:
            frames.append({"lo":lo,"hi":hi,"probe":mid,"decided":"right","line":5,"msg":"arr["+str(mid)+"]="+_f(val)+" < "+_f(tgt)})
            steps.append({"label":"Binary right","math":"arr["+str(mid)+"]="+_f(val)+" < "+_f(tgt),"note":"Go right."}); lo=mid+1
        else:
            frames.append({"lo":lo,"hi":hi,"probe":mid,"decided":"left","line":5,"msg":"arr["+str(mid)+"]="+_f(val)+" > "+_f(tgt)})
            steps.append({"label":"Binary left","math":"arr["+str(mid)+"]="+_f(val)+" > "+_f(tgt),"note":"Go left."}); hi=mid-1
    if found<0:
        frames.append({"lo":lo,"hi":hi,"probe":-1,"decided":"absent","line":5,"msg":_f(tgt)+" not in the list"})
        steps.append({"label":"End","math":"range empty","note":"Target not present."})
    return _finish(arr, tgt, found, frames, steps, sort_moves=sort_moves, input_array=nums)


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
