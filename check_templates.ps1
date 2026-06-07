# check_templates.ps1 — is the templates folder actually intact on disk?
# Run from project root:  .\check_templates.ps1

Write-Host "=== does templates\ exist and what's in it? ===" -ForegroundColor Cyan
if (Test-Path .\templates) {
  Write-Host "templates\ EXISTS. Top-level files:" -ForegroundColor Green
  Get-ChildItem .\templates -File | Select-Object Name
  Write-Host "`nbase.html present? " -NoNewline
  if (Test-Path .\templates\base.html) { Write-Host "YES" -ForegroundColor Green } else { Write-Host "NO — MISSING" -ForegroundColor Red }
  Write-Host "viz template count: " -NoNewline
  (Get-ChildItem .\templates\viz -File -ErrorAction SilentlyContinue | Measure-Object).Count
} else {
  Write-Host "templates\ DOES NOT EXIST at project root!" -ForegroundColor Red
}

Write-Host "`n=== is there a templates folder somewhere ELSE (moved)? ===" -ForegroundColor Cyan
Get-ChildItem -Recurse -Directory -Filter templates -ErrorAction SilentlyContinue |
  Where-Object { $_.FullName -notlike "*\.venv\*" } | Select-Object FullName

Write-Host "`n=== what git thinks is the current state ===" -ForegroundColor Cyan
git status

Write-Host "`n=== does the app still import / templates resolve? quick smoke ===" -ForegroundColor Cyan
if (Test-Path .\templates\base.html) { Write-Host "Looks intact." } else { Write-Host "Templates appear gone from working tree — DO NOT PUSH until resolved." -ForegroundColor Red }
