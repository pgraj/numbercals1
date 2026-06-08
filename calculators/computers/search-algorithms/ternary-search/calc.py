"""Ternary Search - DSA explainer (auto-built to the pilot template).

Viz-first: the canvas teaches; compute() returns result, a stepped trace (each
frame carries a `line` into `algorithm` for the synced code highlight), the four
exam-fact cards plus a data-structure card, a definition line, and a disclaimer.
Never names a success field 'error'.
"""

from core.registry import register

_DISCLAIMER = 'Educational explainer. Shown here for sorted-array searching; the same splitting idea also finds the peak of hill-shaped functions, noted in the FAQ.'
_DEF = 'Ternary search divides the range into three parts using two probe points m1 and m2, discarding one or two thirds each step; for sorted-array searching it is O(log base 3 of n), and it is also used to locate the extremum of a unimodal function.'
_DEF_SRC_NAME = 'Wikipedia - Ternary search'
_DEF_SRC_URL = 'https://en.wikipedia.org/wiki/Ternary_search'

_ALGO_PSEUDO = [
        'while lo <= hi:',
        '    m1 = lo + (hi - lo)//3',
        '    m2 = hi - (hi - lo)//3',
        '    if arr[m1] == target: return m1',
        '    if arr[m2] == target: return m2',
        '    if target < arr[m1]: hi = m1 - 1',
        '    elif target > arr[m2]: lo = m2 + 1',
        '    else: lo = m1 + 1; hi = m2 - 1',
        'return -1',
]
_ALGO_PYTHON = [
        'while lo<=hi:',
        '    m1=lo+(hi-lo)//3; m2=hi-(hi-lo)//3',
        '    if arr[m1]==target: return m1',
        '    if arr[m2]==target: return m2',
        '    if target<arr[m1]: hi=m1-1',
        '    elif target>arr[m2]: lo=m2+1',
        '    else: lo,hi=m1+1,m2-1',
        'return -1',
]

_EXPLANATION = [
    {"heading": 'Time complexity', "body": 'O(log base 3 of n) iterations, but with two comparisons each, so in practice slightly more comparisons than binary search overall.'},
    {"heading": 'Space complexity', "body": 'O(1) iterative - two probe indices.'},
    {"heading": 'Best data type', "body": "Sorted data; and especially finding the maximum or minimum of 'hill-shaped' (unimodal) functions."},
    {"heading": 'Real-world example', "body": 'Narrowing down the best price point on a demand curve that rises then falls - testing two points and discarding the worse third.'},
    {"heading": 'The data structure', "body": "Ternary search runs on a SORTED ARRAY (for searching) or over a unimodal function's domain (for optimization). It uses index access to two probe points per step. Although it cuts more per step than binary search, it also does more comparisons per step - the same sorted structure, a different splitting strategy."},
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
    slug='ternary-search',
    name='Ternary Search',
    section="computers",
    topic='Data Structures and Algorithms (DSA)',
    sub='Interval & Divide-and-Conquer',
    order=6,
    summary='Like binary search but split the range into three parts each step using two probe points.',
    formula='m1 = lo + (hi-lo)/3; m2 = hi - (hi-lo)/3; compare target with arr[m1], arr[m2]',
    tags=['ternary search', 'three-way', 'sorted', 'unimodal', 'optimization', 'O(log n)'],
    viz_template="viz/ternary-search.html",
    related=['binary-search', 'fibonacci-search'],
)
def compute(array=None, target=23):
    raw = array if array else [2,5,8,12,16,23,38,56,72,91]
    try:
        nums=[int(x) for x in raw]; tgt=int(target)
    except (TypeError,ValueError):
        return {"error":"List values and target must be whole numbers.","steps":[],"disclaimer":_DISCLAIMER}
    if not nums: return {"error":"Enter at least one number.","steps":[],"disclaimer":_DISCLAIMER}
    arr, sort_moves = _bubble_sort(nums)
    n=len(arr); lo=0; hi=n-1; frames=[]; steps=[]; found=-1
    while lo<=hi:
        m1=lo+(hi-lo)//3; m2=hi-(hi-lo)//3
        if arr[m1]==tgt:
            frames.append({"lo":lo,"hi":hi,"probe":m1,"decided":"found","line":3,"msg":"arr[m1="+str(m1)+"] = target"})
            steps.append({"label":"Match m1","math":"arr["+str(m1)+"] = "+_f(tgt),"note":"First probe hit the target."}); found=m1; break
        if arr[m2]==tgt:
            frames.append({"lo":lo,"hi":hi,"probe":m2,"decided":"found","line":4,"msg":"arr[m2="+str(m2)+"] = target"})
            steps.append({"label":"Match m2","math":"arr["+str(m2)+"] = "+_f(tgt),"note":"Second probe hit the target."}); found=m2; break
        if tgt<arr[m1]:
            frames.append({"lo":lo,"hi":hi,"probe":m1,"decided":"left","line":5,"msg":"target < arr[m1] -> keep first third"})
            steps.append({"label":"First third","math":_f(tgt)+" < arr["+str(m1)+"]="+_f(arr[m1]),"note":"Discard the other two thirds."}); hi=m1-1
        elif tgt>arr[m2]:
            frames.append({"lo":lo,"hi":hi,"probe":m2,"decided":"right","line":6,"msg":"target > arr[m2] -> keep last third"})
            steps.append({"label":"Last third","math":_f(tgt)+" > arr["+str(m2)+"]="+_f(arr[m2]),"note":"Discard the first two thirds."}); lo=m2+1
        else:
            frames.append({"lo":lo,"hi":hi,"probe":m1,"decided":"mid","line":7,"msg":"between probes -> keep middle third"})
            steps.append({"label":"Middle third","math":"arr["+str(m1)+"] < "+_f(tgt)+" < arr["+str(m2)+"]","note":"Target is in the middle third."}); lo=m1+1; hi=m2-1
    if found<0:
        frames.append({"lo":lo,"hi":hi,"probe":-1,"decided":"absent","line":8,"msg":_f(tgt)+" not in the list"})
        steps.append({"label":"End","math":"range empty","note":"Target not present."})
    return _finish(arr, tgt, found, frames, steps, sort_moves=sort_moves, input_array=nums)


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
