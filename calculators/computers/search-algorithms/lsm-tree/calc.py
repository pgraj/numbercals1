"""LSM Tree (Log-Structured Merge Tree) - DSA explainer (auto-built to the pilot template).

Viz-first: the canvas teaches; compute() returns result, a stepped trace (each
frame carries a `line` into `algorithm` for the synced code highlight), the four
exam-fact cards plus a data-structure card, a definition line, and a disclaimer.
Never names a success field 'error'.
"""

from core.registry import register

_DISCLAIMER = 'Educational explainer. A small memtable plus a couple of sorted disk levels are shown; real LSM engines have many levels, background compaction, and Bloom filters per file (linked from the Bloom filter calculator).'
_DEF = 'A log-structured merge tree buffers writes in a sorted in-memory table, periodically flushing them as immutable sorted files on disk and merging those files in the background; reads check the memory table first, then disk files newest-to-oldest, often using Bloom filters to skip files that cannot contain the key.'
_DEF_SRC_NAME = 'Wikipedia - Log-structured merge-tree'
_DEF_SRC_URL = 'https://en.wikipedia.org/wiki/Log-structured_merge-tree'

_ALGO_PSEUDO = [
        'to read key:',
        'look in the in-memory memtable first',
        '    if found: return it (newest data)',
        'for each disk level, newest to oldest:',
        '    (Bloom filter may skip this level)',
        '    binary-search the sorted level for key',
        'return the first match found, else NOT_FOUND',
]
_ALGO_PYTHON = [
        'if key in memtable: return memtable[key]',
        'for level in disk_levels:          # newest first',
        '    if bloom[level].maybe(key):',
        '        v = bsearch(level, key)',
        '        if v is not None: return v',
        'return None',
]

_EXPLANATION = [
    {"heading": 'Time complexity', "body": 'Very fast writes (append to memory). Reads are O(log n) per layer but may check several layers, helped by Bloom filters to skip layers.'},
    {"heading": 'Space complexity', "body": 'O(n), with temporary extra space during background merges (compaction).'},
    {"heading": 'Best data type', "body": 'Write-heavy workloads - logging, metrics, messaging, time-series, sensor data.'},
    {"heading": 'Real-world example', "body": 'Jotting notes on sticky pads all day (fast writes), then filing them neatly into sorted folders each evening (compaction).'},
    {"heading": 'The data structure', "body": 'An LSM tree is a layered structure: a sorted in-memory table (often a skip list or balanced tree) backed by a stack of immutable sorted files on disk. Unlike a B-tree, which updates data in place, an LSM tree only ever appends and merges - turning random writes into fast sequential ones, at the cost of checking several places on read.'},
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
    slug='lsm-tree',
    name='LSM Tree (Log-Structured Merge Tree)',
    section="computers",
    topic='Data Structures and Algorithms (DSA)',
    sub='Tree-Based',
    order=6,
    summary='Collects writes in memory, then merges them to disk in sorted batches - built for heavy writing.',
    formula='writes -> in-memory memtable; flush to sorted disk files; reads check memtable then files (newest first)',
    tags=['lsm tree', 'write-heavy', 'memtable', 'sstable', 'compaction', 'cassandra', 'rocksdb'],
    viz_template="viz/lsm-tree.html",
    related=['b-tree', 'bloom-filter', 'skip-list'],
)
def compute(memtable=None, disk_levels=None, target=23):
    mem = memtable if memtable else [55,23,8]
    dl = disk_levels if disk_levels else [[12,16,33,42],[3,5,9,27,70,88]]
    try:
        mt=sorted(set(int(x) for x in mem)); tgt=int(target)
        levels=[sorted(set(int(x) for x in lv)) for lv in dl]
    except (TypeError,ValueError):
        return {"error":"Memtable, disk levels, and target must be whole numbers.","steps":[],"disclaimer":_DISCLAIMER}
    frames=[]; steps=[]; found=False; where=""
    # check memtable
    hit = tgt in mt
    frames.append({"layer":"mem","mem":mt,"levels":levels,"found_here":hit,"probe":(mt.index(tgt) if hit else -1),"line":1,
                   "msg":("found "+_f(tgt)+" in the in-memory memtable (newest)") if hit else "not in memtable - check disk levels"})
    steps.append({"label":"Check memtable","math":_f(tgt)+(" in" if hit else " not in")+" memtable","note":("Found in memory - the newest copy wins, no disk read needed.") if hit else "Recent writes live in memory; this key is not among them."})
    if hit: found=True; where="memtable"
    if not found:
        for li,lv in enumerate(levels):
            present = tgt in lv
            frames.append({"layer":li,"mem":mt,"levels":levels,"found_here":present,"probe":(lv.index(tgt) if present else -1),"line":5,
                           "msg":("found "+_f(tgt)+" in disk level "+str(li)) if present else ("binary-search disk level "+str(li)+": not here")})
            steps.append({"label":"Disk level "+str(li),"math":_f(tgt)+(" found" if present else " absent")+" in level "+str(li),"note":("Found on disk level "+str(li)+" (a Bloom filter would have allowed this read).") if present else "A Bloom filter would likely let us skip this level; shown here for clarity."})
            if present: found=True; where="disk level "+str(li); break
    if not found:
        frames.append({"layer":"end","mem":mt,"levels":levels,"found_here":False,"probe":-1,"line":7,"msg":_f(tgt)+" not present in any layer"})
        steps.append({"label":"Not found","math":"all layers checked","note":_f(tgt)+" is not stored."})
    result=("Found "+_f(tgt)+" in the "+where+".") if found else (_f(tgt)+" is not present in memory or on disk.")
    return {"result":result,"target":tgt,"mem":mt,"levels":levels,"found":found,
            "frames":frames,"steps":steps,"algorithm":{"pseudocode":_ALGO_PSEUDO,"python":_ALGO_PYTHON},
            "explanation":_EXPLANATION,"law_statement":_DEF,
            "law_source_name":_DEF_SRC_NAME,"law_source_url":_DEF_SRC_URL,"disclaimer":_DISCLAIMER}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
