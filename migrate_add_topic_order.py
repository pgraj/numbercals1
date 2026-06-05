#!/usr/bin/env python3
"""
NumberCals migration — add `topic=` and `order=` to every @register(...) call.

WHAT IT DOES
  Walks calculators/ to ANY depth, finds each calc.py, locates its
  register(...) call via Python's AST (NOT regex — your sub= strings contain
  commas and ampersands, which would break naive string editing), and inserts
  topic="..." and order=N as new keyword arguments if they are not already
  present. The values come from the MAPPING table below, keyed by the
  calculator's existing (section, sub). Edit that table, then run.

SAFE BY DESIGN
  * Idempotent: a file that already has topic= is left untouched.
  * Backups: writes <file>.bak before changing anything (unless --no-backup).
  * Dry-run by default: prints what it WOULD do; pass --apply to write.
  * AST-located insert: never parses your strings by hand.
  * Reports anything it can't handle instead of guessing.

USAGE (from the app root, the folder containing main.py + core/registry.py)
  python migrate_add_topic_order.py                # dry run, shows the plan
  python migrate_add_topic_order.py --apply        # writes changes + .bak files
  python migrate_add_topic_order.py --apply --no-backup   # if you use git instead
  python migrate_add_topic_order.py --section conversions # limit to one section

After --apply: restart uvicorn so load_all() re-runs, then verify.
"""
from __future__ import annotations

import argparse
import ast
import pathlib
import sys

# ---------------------------------------------------------------------------
# MAPPING: (section, sub)  ->  {"topic": <str>, "order": <int>}
# Fill this in for every (section, sub) pair you want migrated. Any calc whose
# (section, sub) is not listed here is REPORTED and SKIPPED (never guessed).
# `order` sets the TOPIC sequence in the sidebar (lower first).
#
# Conversions pilot — all three current sub-sections map under one "Converters"
# topic for now; adjust freely. (You can also split them into real topics.)
# ---------------------------------------------------------------------------
MAPPING: dict[tuple[str, str], dict] = {
    # Conversions — Option B: four clusters under "Converters", plus Dimensionless.
    ("conversions", "Everyday, Geometric & Physical Measures"):
        {"topic": "Converters", "order": 1},
    ("conversions", "Advanced Engineering & Dynamic Physics"):
        {"topic": "Converters", "order": 1},
    ("conversions", "Aerospace Heat Transfer & Materials"):
        {"topic": "Converters", "order": 1},
    ("conversions", "Commerce, Merchandising & Clinical Medicine"):
        {"topic": "Converters", "order": 1},
    ("conversions", "Dimensionless Number Engines"):
        {"topic": "Dimensionless Numbers", "order": 2},
}


def find_register_call(tree: ast.AST):
    """Return the ast.Call node for register(...), or None."""
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            f = node.func
            name = (f.id if isinstance(f, ast.Name)
                    else f.attr if isinstance(f, ast.Attribute) else None)
            if name == "register":
                return node
    return None


def kw_value(call: ast.Call, key: str):
    for kw in call.keywords:
        if kw.arg == key and isinstance(kw.value, ast.Constant):
            return kw.value.value
    return None


def has_kw(call: ast.Call, key: str) -> bool:
    return any(kw.arg == key for kw in call.keywords)


def migrate_file(path: pathlib.Path, mapping, section_filter=None):
    """Return a dict describing the action taken/planned for one file."""
    src = path.read_text(encoding="utf-8")
    try:
        tree = ast.parse(src)
    except SyntaxError as e:
        return {"path": path, "status": "PARSE-ERROR", "detail": str(e)}

    call = find_register_call(tree)
    if call is None:
        return {"path": path, "status": "no-register", "detail": "no register() call found"}

    section = kw_value(call, "section")
    sub = kw_value(call, "sub")
    if section is None or sub is None:
        return {"path": path, "status": "SKIP", "detail": "section/sub not literal strings"}

    if section_filter and section != section_filter:
        return {"path": path, "status": "filtered", "detail": section}

    if has_kw(call, "topic"):
        return {"path": path, "status": "already", "detail": "topic= present"}

    key = (section, sub)
    if key not in mapping:
        return {"path": path, "status": "UNMAPPED", "detail": f"{key!r} not in MAPPING"}

    topic = mapping[key]["topic"]
    order = mapping[key]["order"]

    # Insert after the `sub=` keyword's line. We find the source line that
    # contains the sub keyword (by its lineno) and insert two new lines after,
    # matching its indentation. This keeps the multi-line, trailing-comma style.
    sub_kw = next(kw for kw in call.keywords if kw.arg == "sub")
    insert_line = sub_kw.value.end_lineno  # 1-based; may span lines if quoted oddly
    lines = src.splitlines(keepends=True)

    # indentation from the sub line
    sub_line_text = lines[sub_kw.value.lineno - 1]
    indent = sub_line_text[:len(sub_line_text) - len(sub_line_text.lstrip())]

    topic_esc = topic.replace('"', '\\"')
    new_lines = [
        f'{indent}topic="{topic_esc}",\n',
        f'{indent}order={order},\n',
    ]
    # splice
    out = lines[:insert_line] + new_lines + lines[insert_line:]
    new_src = "".join(out)

    # validate the result still parses AND register args are intact
    try:
        new_tree = ast.parse(new_src)
        new_call = find_register_call(new_tree)
        assert kw_value(new_call, "topic") == topic
        assert kw_value(new_call, "order") == order
        assert kw_value(new_call, "slug") == kw_value(call, "slug")  # unchanged
    except (SyntaxError, AssertionError) as e:
        return {"path": path, "status": "VERIFY-FAIL", "detail": str(e)}

    return {"path": path, "status": "edit", "detail": f'topic="{topic}", order={order}',
            "new_src": new_src}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="write changes (default: dry run)")
    ap.add_argument("--no-backup", action="store_true", help="skip .bak files (use with git)")
    ap.add_argument("--section", default=None, help="limit to one section id")
    ap.add_argument("--root", default=".", help="app root (has calculators/)")
    args = ap.parse_args()

    root = pathlib.Path(args.root)
    calc_dir = root / "calculators"
    if not calc_dir.exists():
        print(f"ERROR: {calc_dir} not found. Run from the app root.", file=sys.stderr)
        sys.exit(2)

    files = sorted(p for p in calc_dir.rglob("calc.py") if not p.name.startswith("_"))
    results = [migrate_file(p, MAPPING, args.section) for p in files]

    edits   = [r for r in results if r["status"] == "edit"]
    already = [r for r in results if r["status"] == "already"]
    skipped = [r for r in results if r["status"] in
               ("UNMAPPED", "SKIP", "no-register", "PARSE-ERROR", "VERIFY-FAIL")]

    print(f"Scanned {len(files)} calc.py file(s) under {calc_dir}\n")
    for r in edits:
        print(f"  [EDIT]    {r['path']}  ->  {r['detail']}")
    for r in already:
        print(f"  [skip]    {r['path']}  (already has topic=)")
    for r in skipped:
        print(f"  [WARN]    {r['path']}  ({r['status']}: {r['detail']})")

    print(f"\n{len(edits)} to edit, {len(already)} already done, {len(skipped)} need attention.")

    if skipped:
        print("\n⚠ Files marked WARN were NOT edited. Add their (section, sub) to "
              "MAPPING (UNMAPPED), or inspect (SKIP/PARSE/VERIFY) before re-running.")

    if not args.apply:
        print("\nDRY RUN — nothing written. Re-run with --apply to write changes.")
        return

    for r in edits:
        p = r["path"]
        if not args.no_backup:
            p.with_suffix(p.suffix + ".bak").write_text(
                p.read_text(encoding="utf-8"), encoding="utf-8")
        p.write_text(r["new_src"], encoding="utf-8")
    print(f"\n✔ Wrote {len(edits)} file(s)." +
          ("" if args.no_backup else " Backups: <file>.bak beside each."))
    print("Now restart uvicorn so load_all() re-runs, then verify the sidebar.")


if __name__ == "__main__":
    main()
