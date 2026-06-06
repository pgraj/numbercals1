# Stage 3 — Cluster A, Batch 1, Calc 1 of 3: trig-exact-values

## Placement
Create the slug folder and drop the two Python files in (rename off the `__`):

    calculators\maths\trigonometry\trigonometric-identities\trig-exact-values\
        calc.py      <- from trig-exact-values__calc.py  (rename)
        faq.py       <- from trig-exact-values__faq.py   (rename)

Viz goes flat (templates are keyed by filename):

    templates\viz\trig-exact-values.html   <- from trig-exact-values.html (keep name)

## After placing
Full server restart (registry walks calc.py at boot). Then verify:
- count goes 97 -> 98
- slug resolves; page loads at /calc/trig-exact-values
- toggle deg<->rad: dropdown relabels (30° <-> π/6), values unchanged, steps re-derive
- method dropdown switches the canvas + steps (special-triangle / unit-circle / cast / exact-value)
- tan at 90° and 270° shows "undefined"; axis angles draw no triangle

## Then commit
    git add -A
    git commit -m "Stage 3 Cluster A: trig-exact-values (exact surds, 4 derivation views, deg/rad)"
    git push

Verified in sandbox: all 17 special angles match the math library in both deg and
rad; rationalised surds (1/√3 -> √3/3); CAST signs + reference angles correct;
disclaimer verbatim on success and error; compute never raises (non-special angle
returns a guiding error, not an exception).
