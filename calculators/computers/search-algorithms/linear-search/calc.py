"""Linear Search - DSA explainer (auto-built to the pilot template).

Viz-first: the canvas teaches; compute() returns result, a stepped trace (each
frame carries a `line` into `algorithm` for the synced code highlight), the four
exam-fact cards plus a data-structure card, a definition line, and a disclaimer.
Never names a success field 'error'.
"""

from core.registry import register

_DISCLAIMER = 'Educational explainer. The scan runs over a small sample list so each comparison is easy to follow; behaviour is identical at any size.'
_DEF = 'Linear search scans a collection element by element from start to end, comparing each with the target, and stops at the first match (or reports absence after the last element).'
_DEF_SRC_NAME = 'Wikipedia - Linear search'
_DEF_SRC_URL = 'https://en.wikipedia.org/wiki/Linear_search'

_ALGO_PSEUDO = [
        'for i from 0 to n-1:',
        '    if arr[i] == target:',
        '        return i        # found',
        'return -1               # not found',
]
_ALGO_PYTHON = [
        'for i in range(len(arr)):',
        '    if arr[i] == target:',
        '        return i',
        'return -1',
]

_EXPLANATION = [
    {"heading": 'Time complexity', "body": 'O(n) - in the worst case (target last or absent) it touches every one of the n items. On average it checks about half.'},
    {"heading": 'Space complexity', "body": 'O(1) - it only needs a single loop index, no matter how large the list.'},
    {"heading": 'Best data type', "body": 'Small or unsorted collections, or one-off scans where building an index would not pay off.'},
    {"heading": 'Real-world example', "body": 'Looking for a friend by walking down a line of people and checking each face until you spot them.'},
    {"heading": 'The data structure', "body": 'Linear search runs on a plain ARRAY or LIST - items in sequence with no ordering requirement. It needs nothing more than the ability to read each element once, which is why it works on unsorted data where faster searches cannot. Contrast binary search, which demands a sorted array.'},
]


def _f(x):
    if isinstance(x, float) and x.is_integer():
        return str(int(x))
    return str(x)


@register(
    slug='linear-search',
    name='Linear Search',
    section="computers",
    topic='Data Structures and Algorithms (DSA)',
    sub='Linear & Sequential',
    order=1,
    summary='Check every item one by one until you find the target - works on any data, sorted or not.',
    formula='for i in 0..n-1: if arr[i] == target: return i',
    tags=['linear search', 'sequential search', 'unsorted', 'O(n)', 'brute force'],
    viz_template="viz/linear-search.html",
    related=['sentinel-linear-search', 'binary-search', 'jump-search'],
)
def compute(array=None, target=7):
    raw = array if array else [4, 15, 8, 23, 16, 42, 7, 11, 30, 9]
    try:
        arr = [int(x) for x in raw]
        tgt = int(target)
    except (TypeError, ValueError):
        return {"error": "List values and target must be whole numbers.", "steps": [], "disclaimer": _DISCLAIMER}
    if not arr:
        return {"error": "Enter at least one number.", "steps": [], "disclaimer": _DISCLAIMER}
    frames = []
    steps = []
    found = -1
    for i in range(len(arr)):
        match = (arr[i] == tgt)
        frames.append({"i": i, "match": match, "line": 1 if not match else 2})
        steps.append({"label": "Step " + str(i + 1),
                      "math": "arr[" + str(i) + "] = " + _f(arr[i]) + (" = " if match else " != ") + _f(tgt),
                      "note": ("Match - target found at index " + str(i) + ".") if match
                              else ("Not a match; move to the next item.")})
        if match:
            found = i
            break
    if found < 0:
        frames.append({"i": -1, "match": False, "line": 3})
        steps.append({"label": "End", "math": "scanned all " + str(len(arr)) + " items",
                      "note": "Reached the end with no match - the target is not present."})
        result = "Scanned all " + str(len(arr)) + " items; " + _f(tgt) + " is not in the list."
    else:
        result = "Found " + _f(tgt) + " at index " + str(found) + " after " + str(found + 1) + " comparison" + ("s" if found != 0 else "") + "."
    return {"result": result, "target": tgt, "array": arr, "found_index": found,
            "frames": frames, "steps": steps,
            "algorithm": {"pseudocode": _ALGO_PSEUDO, "python": _ALGO_PYTHON},
            "explanation": _EXPLANATION, "law_statement": _DEF,
            "law_source_name": _DEF_SRC_NAME, "law_source_url": _DEF_SRC_URL,
            "disclaimer": _DISCLAIMER}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
