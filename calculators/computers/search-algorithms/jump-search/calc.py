"""Jump Search - DSA explainer (auto-built to the pilot template).

Viz-first: the canvas teaches; compute() returns result, a stepped trace (each
frame carries a `line` into `algorithm` for the synced code highlight), the four
exam-fact cards plus a data-structure card, a definition line, and a disclaimer.
Never names a success field 'error'.
"""

from core.registry import register

_DISCLAIMER = 'Educational explainer. Block size is shown as floor(sqrt(n)) over a small sample; the two phases (jump, then scan) are animated separately.'
_DEF = 'Jump search divides a sorted list into blocks of size about sqrt(n), jumps block by block until it passes the target, then linear-searches within the last block; the optimal block size sqrt(n) balances the jumping and scanning costs.'
_DEF_SRC_NAME = 'Wikipedia - Jump search'
_DEF_SRC_URL = 'https://en.wikipedia.org/wiki/Jump_search'

_ALGO_PSEUDO = [
        'step = floor(sqrt(n))',
        'prev = 0',
        'while arr[min(step, n) - 1] < target:   # jump',
        '    prev = step; step += floor(sqrt(n))',
        '    if prev >= n: return -1',
        'while arr[prev] < target:               # scan block',
        '    prev += 1',
        'if arr[prev] == target: return prev',
        'return -1',
]
_ALGO_PYTHON = [
        'import math',
        'step = int(math.sqrt(n)); prev = 0',
        'while arr[min(step, n)-1] < target:',
        '    prev = step; step += int(math.sqrt(n))',
        '    if prev >= n: return -1',
        'while arr[prev] < target:',
        '    prev += 1',
        'return prev if arr[prev]==target else -1',
]

_EXPLANATION = [
    {"heading": 'Time complexity', "body": "O(sqrt n) - it makes about sqrt(n) jumps plus sqrt(n) steps in the final block. Slower than binary search's O(log n) but faster than linear's O(n)."},
    {"heading": 'Space complexity', "body": 'O(1) - only a couple of indices.'},
    {"heading": 'Best data type', "body": 'Sorted data, especially on storage where jumping backward is costly (binary search jumps around; jump search mostly moves forward).'},
    {"heading": 'Real-world example', "body": 'Flipping through a dictionary 20 pages at a time until you pass your word, then reading that span carefully.'},
    {"heading": 'The data structure', "body": 'Jump search needs a SORTED ARRAY with index access, like binary search, but it moves in fixed forward strides rather than halving. That forward-only stepping is why it suits storage where jumping backward is expensive - the structure is the same sorted array, but the access pattern is gentler on certain media.'},
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
    slug='jump-search',
    name='Jump Search',
    section="computers",
    topic='Data Structures and Algorithms (DSA)',
    sub='Interval & Divide-and-Conquer',
    order=3,
    summary='Jump ahead in fixed blocks of about sqrt(n), then linear-search the final block.',
    formula='step = floor(sqrt(n)); jump while arr[min(step,n)-1] < target; then scan the block',
    tags=['jump search', 'block search', 'sqrt n', 'sorted', 'O(sqrt n)'],
    viz_template="viz/jump-search.html",
    related=['binary-search', 'linear-search', 'exponential-search'],
)
def compute(array=None, target=23):
    import math
    raw = array if array else [2,5,8,12,16,23,38,56,72,91]
    try:
        nums = [int(x) for x in raw]; tgt = int(target)
    except (TypeError, ValueError):
        return {"error":"List values and target must be whole numbers.","steps":[],"disclaimer":_DISCLAIMER}
    if not nums: return {"error":"Enter at least one number.","steps":[],"disclaimer":_DISCLAIMER}
    arr, sort_moves = _bubble_sort(nums)
    n=len(arr); step=int(math.sqrt(n)) or 1; frames=[]; steps=[]; prev=0; jstep=step; found=-1
    # jump phase
    while True:
        idx=min(jstep,n)-1
        frames.append({"lo":prev,"hi":idx,"probe":idx,"decided":"jump","line":2,"msg":"Jump: check block end arr["+str(idx)+"]="+_f(arr[idx])})
        steps.append({"label":"Jump","math":"arr["+str(idx)+"] = "+_f(arr[idx])+(" < " if arr[idx]<tgt else " >= ")+_f(tgt),
                      "note":("Still below target - jump to the next block." if arr[idx]<tgt else "Block end reached or passed target - scan this block.")})
        if arr[idx]>=tgt: break
        prev=jstep; jstep+=step
        if prev>=n:
            frames.append({"lo":prev,"hi":n-1,"probe":-1,"decided":"absent","line":4,"msg":_f(tgt)+" is beyond the list"})
            steps.append({"label":"End","math":"prev >= n","note":"Jumped past the end; target not present."})
            return _finish(arr, tgt, -1, frames, steps, sort_moves=sort_moves, input_array=nums)
    # scan phase
    i=prev
    while i<min(jstep,n) and arr[i]<tgt:
        frames.append({"lo":prev,"hi":min(jstep,n)-1,"probe":i,"decided":"scan","line":5,"msg":"Scan block: arr["+str(i)+"]="+_f(arr[i])})
        steps.append({"label":"Scan","math":"arr["+str(i)+"] = "+_f(arr[i])+" < "+_f(tgt),"note":"Within the block, step forward."})
        i+=1
    if i<n and arr[i]==tgt:
        found=i
        frames.append({"lo":prev,"hi":min(jstep,n)-1,"probe":i,"decided":"found","line":7,"msg":"Found "+_f(tgt)+" at index "+str(i)})
        steps.append({"label":"Match","math":"arr["+str(i)+"] = "+_f(tgt),"note":"Found inside the block at index "+str(i)+"."})
    else:
        frames.append({"lo":prev,"hi":min(jstep,n)-1,"probe":i if i<n else -1,"decided":"absent","line":8,"msg":_f(tgt)+" not in the block"})
        steps.append({"label":"End","math":"block exhausted","note":"Scanned the block without a match; target not present."})
    return _finish(arr, tgt, found, frames, steps, sort_moves=sort_moves, input_array=nums)


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
