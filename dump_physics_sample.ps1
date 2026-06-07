# dump_physics_sample.ps1 — show a representative Physics calc + its viz template,
# so a new calc can be built in the exact same style.
# Run from project root:  .\dump_physics_sample.ps1

# Prefer kinetic-energy (closest analog to E=mc^2: one formula, few inputs)
$cand = Get-ChildItem -Recurse -Filter calc.py |
  Where-Object { $_.FullName -match "physics" -and $_.FullName -match "kinetic|energy|mechanic" -and $_.FullName -notlike "*\.venv\*" } |
  Select-Object -First 1
if (-not $cand) {
  $cand = Get-ChildItem -Recurse -Filter calc.py | Where-Object { $_.FullName -match "physics" -and $_.FullName -notlike "*\.venv\*" } | Select-Object -First 1
}

Write-Host "=== CALC.PY: $($cand.FullName) ===" -ForegroundColor Cyan
Get-Content $cand.FullName

$dir = Split-Path $cand.FullName
Write-Host "`n=== FAQ.PY (same folder) ===" -ForegroundColor Cyan
$faq = Join-Path $dir "faq.py"
if (Test-Path $faq) { Get-Content $faq } else { Write-Host "(no faq.py)" }

# find its viz_template name and dump it
$viz = (Select-String -Path $cand.FullName -Pattern 'viz_template\s*=\s*"viz/([^"]+)"').Matches.Groups[1].Value
Write-Host "`n=== VIZ TEMPLATE: templates\viz\$viz ===" -ForegroundColor Cyan
$vizpath = ".\templates\viz\$viz"
if (Test-Path $vizpath) { Get-Content $vizpath } else { Write-Host "(viz template not found at $vizpath — it may use the generic viz)" }
