#!/usr/bin/env python
r"""
migrate_maths_topics.py  —  NumberCals maths topic/order migration (Option B1)

Adds  topic=<TOPIC>, order=<N>  to the @register(...) call of every existing
maths calculator that is currently missing them, keyed by (section, sub).

B1 policy: the topic name equals the existing sub name. The sub value is left
UNCHANGED. Only `topic=` and `order=` are inserted, immediately after `sub=`.

Safe by design:
  * AST-driven  — never a blind regex; survives commas/ampersands/unicode in
    summary=, formula=, tags=, etc.
  * Idempotent  — a calc that already has topic= is skipped; re-running is a no-op.
  * Backup      — writes <file>.bak before changing <file>.
  * rglob       — walks calculators\maths\ at ANY nesting depth.
  * Dry-run by default. Pass --apply to actually write.

USAGE (PowerShell, from the app root that contains main.py + core\registry.py):
    .venv\Scripts\python migrate_maths_topics.py
    .venv\Scripts\python migrate_maths_topics.py --apply

After --apply, VERIFY at the data level:
    .venv\Scripts\python -c "from core import registry; import pathlib; registry.load_all(pathlib.Path('.')); print([(t['topic'], t['order']) for t in registry.topics_in_section('maths')])"
Expected:
    [('Algebra', 0), ('Arithmetic', 0)]
(and ('Trigonometry', 0) once the Stage 1 trig calcs are dropped in.)
"""

import argparse
import ast
import pathlib
import sys

# (section, sub) -> (topic, order)
MAPPING = {
    ("maths", "Algebra"):    ("Algebra", 0),
    ("maths", "Arithmetic"): ("Arithmetic", 0),
}

MATHS_ROOT = pathlib.Path("calculators") / "maths"


def _kw_str_value(call: ast.Call, name: str):
    """Return the constant string value of keyword `name` in a call, or None."""
    for kw in call.keywords:
        if kw.arg == name and isinstance(kw.value, ast.Constant) \
                and isinstance(kw.value.value, str):
            return kw.value.value
    return None


def _has_kw(call: ast.Call, name: str) -> bool:
    return any(kw.arg == name for kw in call.keywords)


def _find_register_call(tree: ast.Module):
    """Find the @register(...) call node (decorator or bare call). Returns node or None."""
    for node in ast.walk(tree):
        # decorator form: @register(...)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            for dec in node.decorator_list:
                if isinstance(dec, ast.Call) and _is_register(dec.func):
                    return dec
        # bare call form: register(...)
        if isinstance(node, ast.Call) and _is_register(node.func):
            return node
    return None


def _is_register(func) -> bool:
    if isinstance(func, ast.Name):
        return func.id == "register"
    if isinstance(func, ast.Attribute):
        return func.attr == "register"
    return False


def _sub_keyword_node(call: ast.Call):
    for kw in call.keywords:
        if kw.arg == "sub":
            return kw
    return None


def process_file(path: pathlib.Path, apply: bool):
    """Return a status string describing what happened (or would happen)."""
    src = path.read_text(encoding="utf-8")
    try:
        tree = ast.parse(src)
    except SyntaxError as e:
        return f"SKIP (syntax error: {e})"

    call = _find_register_call(tree)
    if call is None:
        return "SKIP (no register call)"

    section = _kw_str_value(call, "section")
    sub = _kw_str_value(call, "sub")
    if section is None or sub is None:
        return f"SKIP (section/sub not literal: section={section!r}, sub={sub!r})"

    key = (section, sub)
    if key not in MAPPING:
        return f"SKIP (no mapping for {key})"

    topic, order = MAPPING[key]

    if _has_kw(call, "topic"):
        existing = _kw_str_value(call, "topic")
        return f"OK already has topic={existing!r} (no change)"

    # Locate the sub= keyword's source span to insert after it.
    sub_kw = _sub_keyword_node(call)
    # The value node carries position info; insert after the end of the value.
    val = sub_kw.value
    end_line = val.end_lineno
    end_col = val.end_col_offset

    lines = src.splitlines(keepends=True)
    target = lines[end_line - 1]
    insertion = f', topic="{topic}", order={order}'
    new_target = target[:end_col] + insertion + target[end_col:]
    lines[end_line - 1] = new_target
    new_src = "".join(lines)

    # Validate the edit re-parses and that topic now reads back correctly.
    try:
        new_tree = ast.parse(new_src)
    except SyntaxError as e:
        return f"ERROR (edit broke syntax, not written: {e})"
    new_call = _find_register_call(new_tree)
    if _kw_str_value(new_call, "topic") != topic or \
            not _has_kw(new_call, "order"):
        return "ERROR (post-edit verify failed, not written)"

    if apply:
        bak = path.with_suffix(path.suffix + ".bak")
        bak.write_text(src, encoding="utf-8")
        path.write_text(new_src, encoding="utf-8")
        return f"WROTE topic={topic!r}, order={order} (backup {bak.name})"
    else:
        return f"WOULD ADD topic={topic!r}, order={order}"


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true",
                    help="actually write changes (default: dry-run)")
    args = ap.parse_args()

    if not MATHS_ROOT.exists():
        print(f"ERROR: {MATHS_ROOT} not found. Run from the app root "
              f"(the folder with main.py + core\\registry.py).", file=sys.stderr)
        sys.exit(1)

    calc_files = sorted(MATHS_ROOT.rglob("calc.py"))
    if not calc_files:
        print(f"No calc.py found under {MATHS_ROOT}.", file=sys.stderr)
        sys.exit(1)

    mode = "APPLY" if args.apply else "DRY-RUN"
    print(f"[{mode}] scanning {len(calc_files)} calc.py under {MATHS_ROOT}\n")
    changed = 0
    for f in calc_files:
        status = process_file(f, args.apply)
        rel = f.relative_to(MATHS_ROOT.parent.parent) \
            if (MATHS_ROOT.parent.parent in f.parents) else f
        print(f"  {rel}\n      -> {status}")
        if status.startswith(("WROTE", "WOULD ADD")):
            changed += 1

    print(f"\n[{mode}] {changed} file(s) "
          f"{'changed' if args.apply else 'would change'}.")
    if not args.apply and changed:
        print("Re-run with --apply to write (each change writes a .bak first).")


if __name__ == "__main__":
    main()
