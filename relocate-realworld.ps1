# Relocate Real-World Trigonometry calcs from section="real-world" to section="maths".
# Anchors on the script's own folder so relative-path issues cannot occur.

# Base = the folder this script sits in (your app root).
$base = $PSScriptRoot
if ([string]::IsNullOrEmpty($base)) { $base = (Get-Location).Path }
$target = Join-Path $base "calculators\real-world"

Write-Host "=== Relocating Real-World calcs to section=maths ===" -ForegroundColor Cyan
Write-Host ("Looking in: " + $target) -ForegroundColor DarkGray

if (-not (Test-Path $target)) {
    Write-Host ("Path not found: " + $target) -ForegroundColor Red
    Write-Host "Place this script in your app root (the folder that contains 'calculators') and re-run." -ForegroundColor Yellow
    return
}

$files = Get-ChildItem -Recurse -Path $target -Filter calc.py
Write-Host ("Found " + $files.Count + " calc.py file(s).") -ForegroundColor DarkGray

$changed = 0
foreach ($f in $files) {
    $raw = Get-Content $f.FullName -Raw
    if ($raw -match 'section\s*=\s*"real-world"') {
        $bak = "$($f.FullName).bak"
        if (-not (Test-Path $bak)) { Copy-Item $f.FullName $bak }
        $new = $raw -replace 'section\s*=\s*"real-world"', 'section="maths"'
        Set-Content -Path $f.FullName -Value $new -NoNewline
        Write-Host ("  changed: " + $f.Directory.Name + "\" + $f.Name) -ForegroundColor Green
        $changed++
    } else {
        Write-Host ("  skipped (no real-world section): " + $f.Directory.Name) -ForegroundColor DarkGray
    }
}

Write-Host ""
Write-Host "=== Verification: section + topic + sub for each ===" -ForegroundColor Cyan
foreach ($f in $files) {
    Write-Host ("--- " + $f.Directory.Name) -ForegroundColor Yellow
    Select-String -Path $f.FullName -Pattern 'section=|topic=|sub=' | ForEach-Object {
        Write-Host ("    " + $_.Line.Trim())
    }
}

Write-Host ""
Write-Host "Changed $changed file(s). Backups saved as calc.py.bak alongside each." -ForegroundColor Cyan
