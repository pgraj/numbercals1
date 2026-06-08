"""Sentinel Linear Search - DSA explainer (auto-built to the pilot template).

Viz-first: the canvas teaches; compute() returns result, a stepped trace (each
frame carries a `line` into `algorithm` for the synced code highlight), the four
exam-fact cards plus a data-structure card, a definition line, and a disclaimer.
Never names a success field 'error'.
"""

from core.registry import register

_DISCLAIMER = 'Educational explainer. The sentinel is shown as an extra cell at the end; it is removed conceptually after the search. Behaviour matches plain linear search but with one fewer comparison per step.'
_DEF = 'Sentinel linear search appends the target as an extra final element so the loop is guaranteed to stop on a match, removing the per-iteration check for running past the end; a found result is real only if the match occurred before the appended sentinel position.'
_DEF_SRC_NAME = 'Wikipedia - Sentinel value'
_DEF_SRC_URL = 'https://en.wikipedia.org/wiki/Sentinel_value'

_ALGO_PSEUDO = [
        'arr[n] = target        # place sentinel past the data',
        'i = 0',
        'while arr[i] != target:',
        '    i = i + 1',
        'if i < n: return i      # real match',
        'return -1               # only the sentinel matched',
]
_ALGO_PYTHON = [
        'arr.append(target)     # sentinel',
        'i = 0',
        'while arr[i] != target:',
        '    i += 1',
        'arr.pop()              # remove sentinel',
        'return i if i < n else -1',
]

_EXPLANATION = [
    {"heading": 'Time complexity', "body": 'O(n) - same growth as plain linear search, but with one fewer comparison per iteration (no end-of-array check), so a measurable constant-factor speedup.'},
    {"heading": 'Space complexity', "body": 'O(1) - just one extra slot for the sentinel value.'},
    {"heading": 'Best data type', "body": 'Performance-sensitive linear scans over arrays where you can write a spare final cell.'},
    {"heading": 'Real-world example', "body": 'Putting a bookmark at the very end of a shelf so you always stop searching when you reach it - no need to keep checking whether you have run off the end.'},
    {"heading": 'The data structure', "body": 'Like plain linear search this runs on an ARRAY, but it relies on being able to write one extra slot at the end to hold the sentinel. That tiny structural requirement (a spare cell) is what removes the boundary test from the inner loop - a neat example of trading a sliver of space for speed.'},
]


def _f(x):
    if isinstance(x, float) and x.is_integer():
        return str(int(x))
    return str(x)


@register(
    slug='sentinel-linear-search',
    name='Sentinel Linear Search',
    section="computers",
    topic='Data Structures and Algorithms (DSA)',
    sub='Linear & Sequential',
    order=2,
    summary="A linear search that places the target at the end as a 'sentinel' to skip the bounds check each loop.",
    formula='arr[n] = target; i = 0; while arr[i] != target: i += 1',
    tags=['sentinel', 'linear search', 'optimization', 'O(n)', 'bounds check'],
    viz_template="viz/sentinel-linear-search.html",
    related=['linear-search', 'binary-search'],
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
    n = len(arr)
    work = arr + [tgt]   # sentinel appended
    frames = []
    steps = []
    i = 0
    while work[i] != tgt:
        frames.append({"i": i, "match": False, "sentinel_n": n, "line": 2})
        steps.append({"label": "Step " + str(i + 1),
                      "math": "arr[" + str(i) + "] = " + _f(work[i]) + " != " + _f(tgt),
                      "note": "No match and no end-of-array check needed - just advance."})
        i += 1
    is_real = (i < n)
    frames.append({"i": i, "match": True, "sentinel_n": n, "line": 4, "real": is_real})
    if is_real:
        steps.append({"label": "Match", "math": "arr[" + str(i) + "] = " + _f(tgt),
                      "note": "Found before the sentinel - a real match at index " + str(i) + "."})
        result = "Found " + _f(tgt) + " at index " + str(i) + " (sentinel removed the end-check each step)."
    else:
        steps.append({"label": "Sentinel hit", "math": "stopped at the sentinel (index " + str(n) + ")",
                      "note": "Only the appended sentinel matched, so the target is not really present."})
        result = _f(tgt) + " is not in the list - the loop stopped at the sentinel."
    return {"result": result, "target": tgt, "array": arr, "found_index": (i if is_real else -1),
            "frames": frames, "steps": steps,
            "algorithm": {"pseudocode": _ALGO_PSEUDO, "python": _ALGO_PYTHON},
            "explanation": _EXPLANATION, "law_statement": _DEF,
            "law_source_name": _DEF_SRC_NAME, "law_source_url": _DEF_SRC_URL,
            "disclaimer": _DISCLAIMER}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
