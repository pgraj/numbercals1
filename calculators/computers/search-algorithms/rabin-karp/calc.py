"""Rabin-Karp - DSA explainer (auto-built to the pilot template).

Viz-first: the canvas teaches; compute() returns result, a stepped trace (each
frame carries a `line` into `algorithm` for the synced code highlight), the four
exam-fact cards plus a data-structure card, a definition line, and a disclaimer.
Never names a success field 'error'.
"""

from core.registry import register

_DISCLAIMER = "Educational explainer. A simple rolling hash is shown so the slide-and-update is visible; hash collisions trigger a direct character check (a 'spurious hit'), explained in the FAQ. Real implementations use a large modulus to keep collisions rare."
_DEF = 'Rabin-Karp computes a hash of the pattern and a rolling hash of each equal-length text window; it only does a character-by-character check where the hashes match, using the rolling hash to update from one window to the next in constant time, giving O(n + m) average time.'
_DEF_SRC_NAME = 'Wikipedia - Rabin-Karp algorithm'
_DEF_SRC_URL = 'https://en.wikipedia.org/wiki/Rabin%E2%80%93Karp_algorithm'

_ALGO_PSEUDO = [
        'pat_hash = hash(pattern)',
        'win_hash = hash(text[0..m-1])',
        'for each window position:',
        '    if win_hash == pat_hash: verify characters directly',
        '    roll the hash to the next window in O(1)',
]
_ALGO_PYTHON = [
        'pat_hash = hash(pattern)',
        'win_hash = hash(text[:m])',
        'for s in range(n - m + 1):',
        '    if win_hash == pat_hash and text[s:s+m] == pattern:',
        '        record match',
        '    win_hash = roll(win_hash, text[s], text[s+m])',
]

_EXPLANATION = [
    {"heading": 'Time complexity', "body": 'O(n + m) average; O(n*m) worst case if many hash collisions force verification. The rolling hash makes each slide O(1).'},
    {"heading": 'Space complexity', "body": 'O(1) for a single pattern - just the hash values and a few variables.'},
    {"heading": 'Best data type', "body": 'Detecting one or many patterns, and especially plagiarism / duplicate detection where fingerprints of substrings are compared.'},
    {"heading": 'Real-world example', "body": 'Comparing document fingerprints to spot copied passages, instead of comparing every word directly.'},
    {"heading": 'The data structure', "body": 'Rabin-Karp works on a TEXT and a PATTERN using a ROLLING HASH - a number summarising a window of characters that can be updated in O(1) as the window slides. Reducing each window to a single comparable number is the core idea; characters are only compared on a hash hit.'},
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
    slug='rabin-karp',
    name='Rabin-Karp',
    section="computers",
    topic='Data Structures and Algorithms (DSA)',
    sub='String & Pattern Matching',
    order=3,
    summary='Compare cheap rolling hashes of each window; only check characters when hashes match.',
    formula='hash each text window with a rolling hash; if it equals the pattern hash, verify directly',
    tags=['rabin-karp', 'rolling hash', 'string matching', 'multiple patterns', 'plagiarism', 'fingerprint'],
    viz_template="viz/rabin-karp.html",
    related=['knuth-morris-pratt', 'boyer-moore', 'aho-corasick'],
)
def compute(text="abracadabra", pattern="cad"):
    text=str(text); pat=str(pattern)
    if not pat: return {"error":"Enter a pattern to search for.","steps":[],"disclaimer":_DISCLAIMER}
    if not text: return {"error":"Enter text to search in.","steps":[],"disclaimer":_DISCLAIMER}
    m=len(pat); n=len(text)
    if m>n: return {"error":"Pattern is longer than the text.","steps":[],"disclaimer":_DISCLAIMER}
    BASE=256; MOD=101
    def h(s):
        v=0
        for c in s: v=(v*BASE+ord(c))%MOD
        return v
    pat_hash=h(pat)
    frames=[]; steps=[]; found=[]; spurious=0
    steps.append({"label":"Hash the pattern","math":"hash('"+pat+"') = "+str(pat_hash),"note":"The pattern is reduced to a single number; text windows with a different number cannot match."})
    win_hash=h(text[:m])
    high=pow(BASE,m-1,MOD)
    comparisons=0
    for s in range(n-m+1):
        comparisons+=1
        hit=(win_hash==pat_hash)
        if hit:
            verify=(text[s:s+m]==pat)
            if verify:
                found.append(s)
                frames.append({"shift":s,"ti":s,"pi":0,"status":"found","line":4,"msg":"hash hit AND chars match -> FOUND at "+str(s),"note2":"window hash "+str(win_hash)+" = pattern hash"})
                steps.append({"label":"Hash hit + verified","math":"hash="+str(win_hash)+" and text matches","note":"Hashes equal and characters confirmed: a real match at index "+str(s)+"."})
            else:
                spurious+=1
                frames.append({"shift":s,"ti":s,"pi":0,"status":"mismatch","line":4,"msg":"hash hit but chars differ -> spurious hit at "+str(s),"note2":"collision: verify then reject"})
                steps.append({"label":"Spurious hit","math":"hashes equal, characters differ","note":"A hash collision: the numbers matched by chance, so we verify and reject. Rare with a large modulus."})
        else:
            frames.append({"shift":s,"ti":s,"pi":-1,"status":"cmp","line":3,"msg":"window hash "+str(win_hash)+" != pattern hash "+str(pat_hash),"note2":"skip - no character check needed"})
            steps.append({"label":"Hash differs","math":"window hash "+str(win_hash)+" != "+str(pat_hash),"note":"Different number, so this window cannot be the pattern - skip without comparing characters."})
        if s<n-m:
            win_hash=((win_hash-ord(text[s])*high)*BASE+ord(text[s+m]))%MOD
            win_hash%=MOD
    if found:
        result="Found \""+pat+"\" at index"+("es " if len(found)>1 else " ")+", ".join(str(x) for x in found)+". Most windows were rejected by a single cheap hash comparison ("+str(spurious)+" spurious hit"+("s" if spurious!=1 else "")+")."
    else:
        result="\""+pat+"\" not found. Windows were screened by hash; characters checked only on hash hits ("+str(spurious)+" spurious)."
    return {"result":result,"text":text,"pattern":pat,"pat_hash":pat_hash,"matches":found,"spurious":spurious,
            "frames":frames,"steps":steps,"algorithm":{"pseudocode":_ALGO_PSEUDO,"python":_ALGO_PYTHON},
            "explanation":_EXPLANATION,"law_statement":_DEF,
            "law_source_name":_DEF_SRC_NAME,"law_source_url":_DEF_SRC_URL,"disclaimer":_DISCLAIMER}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
