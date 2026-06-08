"""Boyer-Moore - DSA explainer (auto-built to the pilot template).

Viz-first: the canvas teaches; compute() returns result, a stepped trace (each
frame carries a `line` into `algorithm` for the synced code highlight), the four
exam-fact cards plus a data-structure card, a definition line, and a disclaimer.
Never names a success field 'error'.
"""

from core.registry import register

_DISCLAIMER = 'Educational explainer. The bad-character rule is shown (comparisons run right-to-left, then the pattern jumps); the good-suffix rule is described in the FAQ. Larger alphabets give bigger skips.'
_DEF = "Boyer-Moore matches a pattern against text by comparing from the pattern's rightmost character leftward; on a mismatch it uses the bad-character and good-suffix rules to shift the pattern as far right as safely possible, often skipping large chunks of text and achieving sublinear average time."
_DEF_SRC_NAME = 'Wikipedia - Boyer-Moore string-search algorithm'
_DEF_SRC_URL = 'https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_string-search_algorithm'

_ALGO_PSEUDO = [
        'build last-occurrence table for the pattern',
        'align pattern at the start; compare RIGHT to LEFT',
        'on mismatch at text char c:',
        '    shift so c aligns with its last occurrence in pattern',
        '    (if c not in pattern, skip the whole pattern length)',
        'on full match: record it, then shift',
]
_ALGO_PYTHON = [
        'last = {c: i for i, c in enumerate(pattern)}',
        's = 0',
        'while s <= n - m:',
        '    j = m - 1',
        '    while j >= 0 and pattern[j] == text[s+j]: j -= 1',
        '    if j < 0: record match; s += 1',
        '    else: s += max(1, j - last.get(text[s+j], -1))',
]

_EXPLANATION = [
    {"heading": 'Time complexity', "body": 'O(n/m) best/average (sublinear - it can skip most characters); O(n*m) pathological worst case, rare in practice.'},
    {"heading": 'Space complexity', "body": 'O(m + alphabet) for the shift tables.'},
    {"heading": 'Best data type', "body": 'Searching long texts with a reasonably long pattern over a large alphabet - the classic engine behind grep.'},
    {"heading": 'Real-world example', "body": 'Skimming a page for a long word by glancing at spots and jumping past regions that clearly cannot contain it.'},
    {"heading": 'The data structure', "body": "Boyer-Moore works on a TEXT and a PATTERN, with a precomputed TABLE of each character's last position in the pattern (the bad-character table). Comparing right-to-left plus that table is what lets it leap forward by many characters at once, sometimes examining only a fraction of the text."},
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
    slug='boyer-moore',
    name='Boyer-Moore',
    section="computers",
    topic='Data Structures and Algorithms (DSA)',
    sub='String & Pattern Matching',
    order=2,
    summary='Compare from the END of the pattern and skip ahead in big jumps using a bad-character rule.',
    formula="on mismatch, shift the pattern so the text's bad character aligns with its last occurrence in the pattern",
    tags=['boyer-moore', 'string matching', 'bad character', 'good suffix', 'sublinear', 'grep'],
    viz_template="viz/boyer-moore.html",
    related=['knuth-morris-pratt', 'rabin-karp', 'aho-corasick'],
)
def compute(text="HERE IS A SIMPLE EXAMPLE", pattern="EXAMPLE"):
    text=str(text); pat=str(pattern)
    if not pat: return {"error":"Enter a pattern to search for.","steps":[],"disclaimer":_DISCLAIMER}
    if not text: return {"error":"Enter text to search in.","steps":[],"disclaimer":_DISCLAIMER}
    m=len(pat); n=len(text)
    last={}
    for idx,c in enumerate(pat): last[c]=idx
    frames=[]; steps=[]; found=[]
    steps.append({"label":"Last-occurrence table","math":"; ".join(c+"->"+str(i) for c,i in last.items())[:80],"note":"For each character, its rightmost position in the pattern - used to decide the shift on a mismatch."})
    s=0; comparisons=0
    while s<=n-m:
        j=m-1
        while j>=0 and pat[j]==text[s+j]:
            comparisons+=1
            frames.append({"shift":s,"ti":s+j,"pi":j,"status":"match","line":4,
                           "msg":"compare right-to-left: '"+text[s+j]+"' matches at text["+str(s+j)+"]","note2":"j = "+str(j)})
            steps.append({"label":"Match (R-to-L)","math":"pattern["+str(j)+"]='"+pat[j]+"' = text["+str(s+j)+"]","note":"Matching from the right; keep moving left."})
            j-=1
        if j<0:
            found.append(s)
            frames.append({"shift":s,"ti":s,"pi":0,"status":"found","line":5,"msg":"FOUND at index "+str(s),"note2":"shift by 1 to seek more"})
            steps.append({"label":"Full match","math":"pattern found at index "+str(s),"note":"All characters matched right-to-left."})
            s+=1
        else:
            comparisons+=1
            c=text[s+j]
            shift=max(1, j - last.get(c,-1))
            frames.append({"shift":s,"ti":s+j,"pi":j,"status":"mismatch","line":3,
                           "msg":"mismatch '"+c+"' at text["+str(s+j)+"]","note2":"bad-char rule: jump pattern by "+str(shift)})
            steps.append({"label":"Mismatch -> jump","math":"shift = max(1, "+str(j)+" - last['"+c+"']) = "+str(shift),"note":("'"+c+"' is in the pattern; align its last occurrence." if c in last else "'"+c+"' is not in the pattern at all; skip the whole pattern width.")})
            s+=shift
    if found:
        result="Found \""+pat+"\" at index"+("es " if len(found)>1 else " ")+", ".join(str(x) for x in found)+" using only "+str(comparisons)+" comparisons - many characters were skipped."
    else:
        result="\""+pat+"\" does not occur ("+str(comparisons)+" comparisons; large jumps skipped most of the text)."
    return {"result":result,"text":text,"pattern":pat,"matches":found,
            "frames":frames,"steps":steps,"algorithm":{"pseudocode":_ALGO_PSEUDO,"python":_ALGO_PYTHON},
            "explanation":_EXPLANATION,"law_statement":_DEF,
            "law_source_name":_DEF_SRC_NAME,"law_source_url":_DEF_SRC_URL,"disclaimer":_DISCLAIMER}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
