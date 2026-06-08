"""Binary Search — 2D explainer with the SORT prerequisite shown first.

Sorts the input (bubble sort, recording every comparison/swap), then binary-
searches the sorted result. Each animation frame carries a `line` index pointing
into the returned `algorithm` (pseudocode + python) so the viz can highlight the
executing line in sync. Never names a success field 'error'.
"""

from core.registry import register

_DISCLAIMER = (
    "Educational explainer. Binary search REQUIRES sorted data - so this tool sorts "
    "first (shown step by step using bubble sort for clarity), then searches. "
    "Production code would sort once with a fast library routine; bubble sort is "
    "used here only because every swap is easy to watch."
)
_DEF = (
    "Binary search finds a target in a SORTED list by repeatedly halving the search "
    "range: compare the middle element, then keep only the half that could still "
    "contain the target. It needs sorted data first - which is why this tool sorts "
    "before it searches."
)
_DEF_SRC_NAME = "Wikipedia - Binary search algorithm"
_DEF_SRC_URL = "https://en.wikipedia.org/wiki/Binary_search_algorithm"

_SAMPLE = [38, 5, 72, 16, 2, 91, 23, 8, 56, 12]

# Algorithm shown in Step-by-step. `line` indices in frames refer to these rows
# (search lines are indexed; the sort phase highlights the sort block as a whole).
_ALGO_PSEUDO = [
    "sort the array first (binary search needs sorted data)",   # 0  (sort phase)
    "low = 0;  high = n - 1",                                    # 1
    "while low <= high:",                                        # 2
    "    mid = (low + high) // 2",                               # 3
    "    if arr[mid] == target:  return mid   # found",          # 4
    "    elif arr[mid] < target:  low = mid + 1   # go right",   # 5
    "    else:  high = mid - 1   # go left",                     # 6
    "return -1   # not present",                                 # 7
]
_ALGO_PYTHON = [
    "arr.sort()                      # sorted data required",   # 0
    "low, high = 0, len(arr) - 1",                              # 1
    "while low <= high:",                                       # 2
    "    mid = (low + high) // 2",                              # 3
    "    if arr[mid] == target:",                              # 4
    "        return mid",                                       # 4 (found)
    "    elif arr[mid] < target:",                             # 5
    "        low = mid + 1",                                    # 5
    "    else:",                                                # 6
    "        high = mid - 1",                                   # 6
    "return -1",                                                # 7
]

_EXPLANATION = [
    {"heading": "Time complexity",
     "body": "The search is O(log n) - each comparison throws away half of what's "
             "left, so a million sorted items take only about 20 checks. The sort "
             "shown first is the one-time price you pay to unlock that speed."},
    {"heading": "Space complexity",
     "body": "O(1) for the iterative search - it only tracks a low, mid, and high "
             "index, no matter how large the array."},
    {"heading": "Best data type",
     "body": "Sorted arrays or lists that don't change often. You sort once, then "
             "every later search is extremely fast."},
    {"heading": "Real-world example",
     "body": "Finding a name in a phone book by repeatedly opening to the middle - "
             "and 'git bisect', which finds the commit that introduced a bug by "
             "halving a range of commits."},
    {"heading": "The data structure",
     "body": "Binary search runs on a SORTED ARRAY - a block of items kept in "
             "order, where any position can be reached instantly by its index. "
             "That random access is what lets the algorithm jump straight to the "
             "middle each step. Order is the precondition: lose it and the halving "
             "logic breaks. Contrast HNSW, which walks a graph - each algorithm is "
             "really defined by the data structure beneath it."},
]


def _f(x):
    if isinstance(x, float) and x.is_integer():
        return str(int(x))
    return str(x)


def _bubble_sort(arr, descending):
    a = list(arr)
    moves = []
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            left, right = a[j], a[j + 1]
            do_swap = (left > right) if not descending else (left < right)
            moves.append({"i": j, "j": j + 1, "swap": bool(do_swap),
                          "snapshot": list(a), "line": 0})
            if do_swap:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    moves.append({"i": -1, "j": -1, "swap": False, "snapshot": list(a), "line": 0})
    return a, moves


@register(
    slug="binary-search",
    name="Binary Search",
    section="computers",
    topic="Data Structures and Algorithms (DSA)",
    sub="Interval & Divide-and-Conquer",
    order=2,
    summary="Sort first, then find an item fast by repeatedly halving the search range.",
    formula="sort the data; then mid = (low + high) // 2; keep the half that can hold the target.",
    tags=["binary search", "logarithmic", "sorted", "divide and conquer",
          "bubble sort", "search algorithm", "O(log n)"],
    viz_template="viz/binary-search.html",
    related=["jump-search", "interpolation-search", "exponential-search",
             "linear-search"],
)
def compute(array=None, target=23, order="asc"):
    raw = array if array else list(_SAMPLE)
    descending = str(order).lower().startswith("desc")
    try:
        nums = [int(x) for x in raw]
        tgt = int(target)
    except (TypeError, ValueError):
        return {"error": "Array values and target must be whole numbers.",
                "steps": [], "disclaimer": _DISCLAIMER}
    if not nums:
        return {"error": "Enter at least one number.",
                "steps": [], "disclaimer": _DISCLAIMER}

    sorted_arr, sort_moves = _bubble_sort(nums, descending)

    lo, hi = 0, len(sorted_arr) - 1
    search_frames = []
    steps = []
    found_at = -1
    cmp = 0
    # frame: entering the loop / setting low,high
    search_frames.append({"lo": lo, "hi": hi, "mid": -1, "decided": "init", "line": 1})
    while lo <= hi:
        cmp += 1
        mid = (lo + hi) // 2
        val = sorted_arr[mid]
        window = "[" + ", ".join(_f(v) for v in sorted_arr[lo:hi + 1]) + "]"
        search_frames.append({"lo": lo, "hi": hi, "mid": mid, "decided": "mid", "line": 3})
        if val == tgt:
            search_frames.append({"lo": lo, "hi": hi, "mid": mid, "decided": "found", "line": 4})
            steps.append({"label": "Search step " + str(cmp) + " - match",
                          "math": "arr[" + str(mid) + "] = " + _f(val) + " = target",
                          "note": "Middle element equals the target. Found at index "
                                  + str(mid) + "."})
            found_at = mid
            break
        go_right = (val < tgt) if not descending else (val > tgt)
        if go_right:
            search_frames.append({"lo": lo, "hi": hi, "mid": mid, "decided": "right", "line": 5})
            steps.append({"label": "Search step " + str(cmp) + " - go right",
                          "math": "arr[" + str(mid) + "] = " + _f(val)
                                  + (" < " if not descending else " > ") + _f(tgt),
                          "note": "Discard the left half. Window was " + window
                                  + "; continue on the right."})
            lo = mid + 1
        else:
            search_frames.append({"lo": lo, "hi": hi, "mid": mid, "decided": "left", "line": 6})
            steps.append({"label": "Search step " + str(cmp) + " - go left",
                          "math": "arr[" + str(mid) + "] = " + _f(val)
                                  + (" > " if not descending else " < ") + _f(tgt),
                          "note": "Discard the right half. Window was " + window
                                  + "; continue on the left."})
            hi = mid - 1

    if found_at < 0:
        search_frames.append({"lo": -1, "hi": -2, "mid": -1, "decided": "absent", "line": 7})
        steps.append({"label": "Search step " + str(cmp + 1) + " - exhausted",
                      "math": "low > high",
                      "note": "The window is empty, so the target is not present."})

    order_word = "descending" if descending else "ascending"
    sorted_str = "[" + ", ".join(_f(v) for v in sorted_arr) + "]"
    if found_at >= 0:
        result = ("Sorted " + order_word + " to " + sorted_str + ", then found "
                  + _f(tgt) + " at index " + str(found_at) + " in " + str(cmp)
                  + " comparison" + ("s" if cmp != 1 else "") + ".")
    else:
        result = ("Sorted " + order_word + " to " + sorted_str + ", then ruled out "
                  + _f(tgt) + " in " + str(cmp) + " comparison"
                  + ("s" if cmp != 1 else "") + " - not in the array.")

    return {
        "result": result,
        "target": tgt,
        "order": order_word,
        "input_array": nums,
        "sorted_array": sorted_arr,
        "sort_moves": sort_moves,
        "search_frames": search_frames,
        "found_index": found_at,
        "comparisons": cmp,
        "algorithm": {"pseudocode": _ALGO_PSEUDO, "python": _ALGO_PYTHON},
        "steps": steps,
        "explanation": _EXPLANATION,
        "law_statement": _DEF,
        "law_source_name": _DEF_SRC_NAME,
        "law_source_url": _DEF_SRC_URL,
        "disclaimer": _DISCLAIMER,
    }


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
