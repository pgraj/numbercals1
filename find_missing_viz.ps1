$declared = Get-ChildItem .\calculators -Recurse -Filter calc.py |
  Select-String -Pattern 'viz_template\s*=\s*"viz/([^"]+)"' |
  ForEach-Object { $_.Matches.Groups[1].Value } |
  Sort-Object -Unique

$missing = $declared | Where-Object { -not (Test-Path (Join-Path '.\templates\viz' $_)) }

Write-Host ("declared viz templates : {0}" -f $declared.Count)
Write-Host ("on disk now            : {0}" -f (Get-ChildItem .\templates\viz -File -Filter *.html | Measure-Object).Count)
Write-Host ("MISSING                : {0}" -f $missing.Count) -ForegroundColor Yellow
if ($missing.Count -gt 0) {
  Write-Host "`n--- missing template names ---" -ForegroundColor Yellow
  $missing | ForEach-Object { Write-Host "  $_" }
}

Write-Host "`n--- how many viz templates each recent commit has ---" -ForegroundColor Cyan
foreach ($c in @('HEAD~1','a2006a1','309357f','9665fb3')) {
  $n = (git ls-tree -r --name-only $c -- templates/viz 2>$null | Measure-Object -Line).Lines
  Write-Host ("  {0,-10} {1} templates" -f $c, $n)
}
