"""Knuth-Morris-Pratt (KMP) - DSA explainer (auto-built to the pilot template).

Viz-first: the canvas teaches; compute() returns result, a stepped trace (each
frame carries a `line` into `algorithm` for the synced code highlight), the four
exam-fact cards plus a data-structure card, a definition line, and a disclaimer.
Never names a success field 'error'.
"""

from core.registry import register

_DISCLAIMER = 'Educational explainer. The text pointer never moves backward - the key property of KMP. The precomputed failure table is what lets the pattern jump forward intelligently on a mismatch.'
_DEF = 'The Knuth-Morris-Pratt algorithm precomputes, for each position in the pattern, the length of the longest proper prefix that is also a suffix; on a mismatch it shifts the pattern by that amount instead of restarting, so each text character is examined at most once, giving O(n + m) time.'
_DEF_SRC_NAME = 'Wikipedia - Knuth-Morris-Pratt algorithm'
_DEF_SRC_URL = 'https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm'

_ALGO_PSEUDO = [
        'build failure[] for the pattern',
        'i = 0 (text), j = 0 (pattern)',
        'while i < n:',
        '    if text[i] == pattern[j]: i++, j++',
        '        if j == m: MATCH at i-m; j = failure[j-1]',
        "    elif j > 0: j = failure[j-1]   # skip, don't move i",
        '    else: i++',
]
_ALGO_PYTHON = [
        'f = build_failure(pattern); i = j = 0',
        'while i < len(text):',
        '    if text[i] == pattern[j]:',
        '        i += 1; j += 1',
        '        if j == len(pattern): return i - j',
        '    elif j > 0: j = f[j-1]',
        '    else: i += 1',
]

_EXPLANATION = [
    {"heading": 'Time complexity', "body": 'O(n + m) - n for scanning the text, m to build the failure table. Linear, with no backtracking in the text.'},
    {"heading": 'Space complexity', "body": 'O(m) - the failure table, one entry per pattern character.'},
    {"heading": 'Best data type', "body": 'Searching for a single pattern in a long text, especially with repetitive patterns where naive matching wastes work.'},
    {"heading": 'Real-world example', "body": 'Find-in-page (Ctrl+F) in a document, or scanning a DNA sequence for a specific gene marker.'},
    {"heading": 'The data structure', "body": 'KMP works on a TEXT STRING and a PATTERN STRING, plus a small auxiliary ARRAY: the failure (or prefix) table. That table is the whole trick - it records, for each prefix of the pattern, how far you can safely jump on a mismatch without missing a possible match, so the text is never re-scanned.'},
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
    slug='knuth-morris-pratt',
    name='Knuth-Morris-Pratt (KMP)',
    section="computers",
    topic='Data Structures and Algorithms (DSA)',
    sub='String & Pattern Matching',
    order=1,
    summary='Never re-check characters: on a mismatch, skip ahead using a precomputed failure table.',
    formula='build failure[] (longest proper prefix that is also a suffix); on mismatch jump by it',
    tags=['kmp', 'knuth morris pratt', 'string matching', 'failure function', 'prefix', 'O(n+m)'],
    viz_template="viz/knuth-morris-pratt.html",
    related=['boyer-moore', 'rabin-karp', 'aho-corasick'],
)
def compute(text="abababcabababcab", pattern="ababc"):
    text=str(text); pat=str(pattern)
    if not pat: return {"error":"Enter a pattern to search for.","steps":[],"disclaimer":_DISCLAIMER}
    if not text: return {"error":"Enter text to search in.","steps":[],"disclaimer":_DISCLAIMER}
    m=len(pat); n=len(text)
    # build failure table
    f=[0]*m; k=0
    for q in range(1,m):
        while k>0 and pat[k]!=pat[q]: k=f[k-1]
        if pat[k]==pat[q]: k+=1
        f[q]=k
    frames=[]; steps=[]; found=[]
    steps.append({"label":"Failure table","math":"failure = "+str(f),"note":"For each prefix length, the longest proper prefix that is also a suffix - this tells the pattern how far to jump on a mismatch."})
    i=j=0; comparisons=0
    while i<n:
        comparisons+=1
        if text[i]==pat[j]:
            frames.append({"shift":i-j,"ti":i,"pi":j,"status":"match","line":3,
                           "msg":"match '"+text[i]+"' at text["+str(i)+"]","note2":"j -> "+str(j+1)})
            steps.append({"label":"Match","math":"text["+str(i)+"]='"+text[i]+"' = pattern["+str(j)+"]","note":"Characters agree; advance both pointers."})
            i+=1; j+=1
            if j==m:
                found.append(i-j)
                frames.append({"shift":i-j,"ti":i-1,"pi":j-1,"status":"found","line":4,
                               "msg":"FOUND at index "+str(i-j),"note2":"jump j -> failure["+str(j-1)+"]="+str(f[j-1])})
                steps.append({"label":"Full match","math":"pattern found at index "+str(i-j),"note":"Whole pattern matched. Use the failure table to look for further matches without rescanning."})
                j=f[j-1]
        elif j>0:
            frames.append({"shift":i-j,"ti":i,"pi":j,"status":"mismatch","line":5,
                           "msg":"mismatch at text["+str(i)+"]='"+text[i]+"'","note2":"jump j -> failure["+str(j-1)+"]="+str(f[j-1])+" (text pointer stays!)"})
            steps.append({"label":"Mismatch (skip)","math":"j = failure["+str(j-1)+"] = "+str(f[j-1]),"note":"Mismatch after a partial match: shift the pattern using the table - the text pointer i does NOT move back."})
            j=f[j-1]
        else:
            frames.append({"shift":i,"ti":i,"pi":0,"status":"mismatch","line":6,
                           "msg":"mismatch at start; slide pattern by 1","note2":""})
            steps.append({"label":"Mismatch at start","math":"i -> "+str(i+1),"note":"No partial match to reuse; move the pattern forward by one."})
            i+=1
    if found:
        result="Found \""+pat+"\" at index"+("es " if len(found)>1 else " ")+", ".join(str(x) for x in found)+" using "+str(comparisons)+" comparisons (text never rescanned)."
    else:
        result="\""+pat+"\" does not occur in the text ("+str(comparisons)+" comparisons, no backtracking)."
    return {"result":result,"text":text,"pattern":pat,"failure":f,"matches":found,
            "frames":frames,"steps":steps,"algorithm":{"pseudocode":_ALGO_PSEUDO,"python":_ALGO_PYTHON},
            "explanation":_EXPLANATION,"law_statement":_DEF,
            "law_source_name":_DEF_SRC_NAME,"law_source_url":_DEF_SRC_URL,"disclaimer":_DISCLAIMER}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
