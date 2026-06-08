"""Hash Table Lookup - DSA explainer (auto-built to the pilot template).

Viz-first: the canvas teaches; compute() returns result, a stepped trace (each
frame carries a `line` into `algorithm` for the synced code highlight), the four
exam-fact cards plus a data-structure card, a definition line, and a disclaimer.
Never names a success field 'error'.
"""

from core.registry import register

_DISCLAIMER = 'Educational explainer. A small demonstration hash (sum of character codes, modulo the table size) is used so collisions are easy to see; real hash functions are far more sophisticated.'
_DEF = 'A hash table stores key-value pairs in an array of buckets, using a hash function to map each key to an index; lookups, inserts and deletes take O(1) on average, degrading to O(n) only when many keys collide into the same bucket.'
_DEF_SRC_NAME = 'Wikipedia - Hash table'
_DEF_SRC_URL = 'https://en.wikipedia.org/wiki/Hash_table'

_ALGO_PSEUDO = [
        'index = hash(key) mod table_size',
        'bucket = table[index]',
        'for entry in bucket:          # walk the chain',
        '    if entry.key == key: return entry.value',
        'return NOT_FOUND',
]
_ALGO_PYTHON = [
        'index = hash(key) % len(table)',
        'for entry in table[index]:',
        '    if entry.key == key:',
        '        return entry.value',
        'return None',
]

_EXPLANATION = [
    {"heading": 'Time complexity', "body": 'O(1) average - the hash jumps straight to the bucket. O(n) worst case if every key collides into one bucket (a bad hash or an attack).'},
    {"heading": 'Space complexity', "body": 'O(n) - the table needs room for all entries plus some spare capacity to keep collisions rare.'},
    {"heading": 'Best data type', "body": 'Lookups by an exact key - dictionaries, caches, database indexes, login systems, de-duplication.'},
    {"heading": 'Real-world example', "body": 'A coat-check ticket: the number tells you exactly which hook your coat is on, with no searching.'},
    {"heading": 'The data structure', "body": 'A hash table IS the data structure - an array of buckets plus a hash function. Unlike a sorted array (binary search) where position carries meaning, here position is computed from the key itself. Collisions, where two keys map to the same bucket, are resolved by chaining (a list per bucket) or open addressing.'},
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
    slug='hash-table-lookup',
    name='Hash Table Lookup',
    section="computers",
    topic='Data Structures and Algorithms (DSA)',
    sub='Hash-Based',
    order=1,
    summary='A hash function turns a key into a bucket index, so you jump straight to the value.',
    formula='index = hash(key) mod table_size',
    tags=['hash table', 'hash map', 'dictionary', 'O(1)', 'hashing', 'buckets'],
    viz_template="viz/hash-table-lookup.html",
    related=['bloom-filter', 'lsh', 'binary-search'],
)
def compute(keys=None, query="mango", size=8):
    raw = keys if keys else ["apple","mango","grape","lemon","peach","melon","berry"]
    try:
        ks=[str(k).strip() for k in raw if str(k).strip()]
        q=str(query).strip(); size=max(2,int(size))
    except (TypeError,ValueError):
        return {"error":"Provide keys, a query, and a table size.","steps":[],"disclaimer":_DISCLAIMER}
    if not ks: return {"error":"Add at least one key.","steps":[],"disclaimer":_DISCLAIMER}
    def h(s):
        return sum(ord(c) for c in s) % size
    table=[[] for _ in range(size)]
    for k in ks: table[h(k)].append(k)
    frames=[]; steps=[]
    qi=h(q)
    frames.append({"phase":"hash","bucket":qi,"probe":-1,"line":0,"table":[list(b) for b in table],
                   "msg":'hash("'+q+'") = '+str(qi)})
    steps.append({"label":"Hash the key","math":'hash("'+q+'") mod '+str(size)+' = '+str(qi),
                  "note":"The hash function sends the query straight to bucket "+str(qi)+" - no scanning of other buckets."})
    chain=table[qi]; found=False
    for pos,entry in enumerate(chain):
        hit=(entry==q)
        frames.append({"phase":"probe","bucket":qi,"probe":pos,"line":3 if hit else 2,
                       "table":[list(b) for b in table],"msg":('match: "'+entry+'"') if hit else ('check "'+entry+'" - no')})
        steps.append({"label":"Check bucket entry","math":'"'+entry+'"'+(" == " if hit else " != ")+'"'+q+'"',
                      "note":("Found in bucket "+str(qi)+(" after "+str(pos+1)+" check"+("s" if pos else "")+".")) if hit
                              else "Collision in this bucket; check the next chained entry."})
        if hit: found=True; break
    if not found:
        frames.append({"phase":"miss","bucket":qi,"probe":-1,"line":4,"table":[list(b) for b in table],
                       "msg":'"'+q+'" not in bucket '+str(qi)})
        steps.append({"label":"Not found","math":"bucket "+str(qi)+" exhausted",
                      "note":'"'+q+'" is not present - and we only ever looked in one bucket.'})
    occupancy=sum(1 for b in table if b)
    result=('Found "'+q+'" in bucket '+str(qi)+' (one hash jump).') if found else ('"'+q+'" is not in the table (checked only bucket '+str(qi)+').')
    return {"result":result,"query":q,"size":size,"table":[list(b) for b in table],"bucket":qi,
            "found":found,"occupancy":occupancy,"frames":frames,"steps":steps,
            "algorithm":{"pseudocode":_ALGO_PSEUDO,"python":_ALGO_PYTHON},
            "explanation":_EXPLANATION,"law_statement":_DEF,
            "law_source_name":_DEF_SRC_NAME,"law_source_url":_DEF_SRC_URL,"disclaimer":_DISCLAIMER}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
