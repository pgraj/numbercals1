"""Fibonacci Search - DSA explainer (auto-built to the pilot template).

Viz-first: the canvas teaches; compute() returns result, a stepped trace (each
frame carries a `line` into `algorithm` for the synced code highlight), the four
exam-fact cards plus a data-structure card, a definition line, and a disclaimer.
Never names a success field 'error'.
"""

from core.registry import register

_DISCLAIMER = 'Educational explainer. The probe index is derived from Fibonacci numbers over a small sample; the division-free property is the point, not raw speed.'
_DEF = 'Fibonacci search narrows a sorted range using Fibonacci numbers to choose probe positions, so each probe uses only addition and subtraction (no division); it inspects positions that may be more cache- or storage-friendly and runs in O(log n).'
_DEF_SRC_NAME = 'Wikipedia - Fibonacci search technique'
_DEF_SRC_URL = 'https://en.wikipedia.org/wiki/Fibonacci_search_technique'

_ALGO_PSEUDO = [
        'find smallest Fibonacci fibM >= n',
        'offset = -1',
        'while fibM > 1:',
        '    i = min(offset + fibK_minus2, n-1)',
        '    if arr[i] < target: shift Fibs down, offset = i',
        '    elif arr[i] > target: shift Fibs down twice',
        '    else: return i',
        'return -1',
]
_ALGO_PYTHON = [
        'fib2, fib1 = 0, 1; fibM = fib1+fib2',
        'while fibM < n: fib2, fib1 = fib1, fibM; fibM = fib1+fib2',
        'offset = -1',
        'while fibM > 1:',
        '    i = min(offset+fib2, n-1)',
        '    if arr[i] < target: fibM,fib1,fib2 = fib1,fib2,fib1-fib2; offset=i',
        '    elif arr[i] > target: fibM,fib1,fib2 = fib2,fib1-fib2,fib2-(fib1-fib2)',
        '    else: return i',
        'return offset+1 if fib1 and offset+1<n and arr[offset+1]==target else -1',
]

_EXPLANATION = [
    {"heading": 'Time complexity', "body": 'O(log n) - the Fibonacci sequence grows exponentially, so the number of probes is logarithmic, comparable to binary search.'},
    {"heading": 'Space complexity', "body": 'O(1) - a few Fibonacci numbers and indices.'},
    {"heading": 'Best data type', "body": 'Sorted data, especially where division is slow or where the probe pattern suits non-uniform memory access.'},
    {"heading": 'Real-world example', "body": 'Splitting a measuring task using only whole-number additions - handy on simple hardware that cannot divide quickly.'},
    {"heading": 'The data structure', "body": 'Fibonacci search runs on a SORTED ARRAY with index access, like binary search, but it computes probe positions from Fibonacci numbers using only addition and subtraction. The structure is identical; the arithmetic is gentler, which historically mattered on hardware where division was slow.'},
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
    slug='fibonacci-search',
    name='Fibonacci Search',
    section="computers",
    topic='Data Structures and Algorithms (DSA)',
    sub='Interval & Divide-and-Conquer',
    order=7,
    summary='Use Fibonacci numbers to choose split points, needing only addition and subtraction.',
    formula='use consecutive Fibonacci numbers to pick the probe index; no division needed',
    tags=['fibonacci search', 'division-free', 'sorted', 'O(log n)', 'fibonacci numbers'],
    viz_template="viz/fibonacci-search.html",
    related=['binary-search', 'ternary-search', 'jump-search'],
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
    fib2,fib1=0,1; fibM=fib1+fib2
    while fibM<n:
        fib2,fib1=fib1,fibM; fibM=fib1+fib2
    offset=-1; guard=0
    while fibM>1 and guard<n+8:
        guard+=1
        i=min(offset+fib2, n-1)
        val=arr[i]
        if val<tgt:
            frames.append({"lo":offset+1,"hi":n-1,"probe":i,"decided":"right","line":4,"msg":"arr["+str(i)+"]="+_f(val)+" < "+_f(tgt)+" (Fib step)"})
            steps.append({"label":"Fib low","math":"arr["+str(i)+"]="+_f(val)+" < "+_f(tgt),"note":"Move up; shift Fibonacci numbers down one."})
            fibM,fib1=fib1,fib2; fib2=fibM-fib1; offset=i
        elif val>tgt:
            frames.append({"lo":offset+1,"hi":i,"probe":i,"decided":"left","line":5,"msg":"arr["+str(i)+"]="+_f(val)+" > "+_f(tgt)+" (Fib step)"})
            steps.append({"label":"Fib high","math":"arr["+str(i)+"]="+_f(val)+" > "+_f(tgt),"note":"Move down; shift Fibonacci numbers down two."})
            fibM,fib1=fib2,fib1-fib2; fib2=fibM-fib1
        else:
            frames.append({"lo":offset+1,"hi":n-1,"probe":i,"decided":"found","line":6,"msg":"Found "+_f(tgt)+" at index "+str(i)})
            steps.append({"label":"Match","math":"arr["+str(i)+"] = "+_f(tgt),"note":"Fibonacci probe landed on the target."})
            found=i; break
    if found<0 and fib1 and offset+1<n and arr[offset+1]==tgt:
        found=offset+1
        frames.append({"lo":offset+1,"hi":offset+1,"probe":found,"decided":"found","line":6,"msg":"Found "+_f(tgt)+" at index "+str(found)})
        steps.append({"label":"Match (tail)","math":"arr["+str(found)+"] = "+_f(tgt),"note":"Final check found the target."})
    if found<0:
        frames.append({"lo":0,"hi":n-1,"probe":-1,"decided":"absent","line":7,"msg":_f(tgt)+" not in the list"})
        steps.append({"label":"End","math":"Fibonacci range exhausted","note":"Target not present."})
    return _finish(arr, tgt, found, frames, steps, sort_moves=sort_moves, input_array=nums)


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
