# dump_physics.ps1 - dump a representative Physics calc + viz, ASCII only.
$cand = Get-ChildItem .\calculators -Recurse -Filter calc.py |
  Where-Object { $_.FullName -match "physics" -and $_.FullName -match "kinetic|energy" } |
  Select-Object -First 1
if (-not $cand) {
  $cand = Get-ChildItem .\calculators -Recurse -Filter calc.py | Where-Object { $_.FullName -match "physics" } | Select-Object -First 1
}

Write-Host "===== CALC.PY:" $cand.FullName
Get-Content $cand.FullName

$dir = Split-Path $cand.FullName
$faq = Join-Path $dir "faq.py"
Write-Host ""
Write-Host "===== FAQ.PY:" $faq
if (Test-Path $faq) { Get-Content $faq } else { Write-Host "(no faq.py)" }

$viz = (Select-String -Path $cand.FullName -Pattern 'viz_template\s*=\s*"viz/([^"]+)"').Matches.Groups[1].Value
$vizpath = ".\templates\viz\$viz"
Write-Host ""
Write-Host "===== VIZ:" $vizpath
if (Test-Path $vizpath) { Get-Content $vizpath } else { Write-Host "(viz not found)" }
