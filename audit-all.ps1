$ErrorActionPreference = "Stop"

# Set encoding to UTF-8
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "         COMPOUNDING LOOP MASTER AUDITOR (BA ZONE)          " -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "Running comprehensive audits to ensure requirements standard..." -ForegroundColor Gray

# Array to store results of each suite
$global:suiteResults = @()
$global:allPassed = $true

function Record-Result {
    param (
        [string]$SuiteName,
        [bool]$Passed,
        [string]$Detail
    )
    $global:suiteResults += [PSCustomObject]@{
        Suite  = $SuiteName
        Passed = $Passed
        Detail = $Detail
    }
    if (-not $Passed) {
        $global:allPassed = $false
    }
}

# ----------------------------------------------------------------------
# SUITE 1: Python Use Case & User Story Formatting Audit
# ----------------------------------------------------------------------
Write-Host "`n[1/1] Auditing US/UC Output Format Integrity (audit_us_uc.py)..." -ForegroundColor White
try {
    $scriptPath = Join-Path $PSScriptRoot "us-uc-writer-skill\audit_us_uc.py"
    # We will test against the scratch directory
    $testFiles = @(
        "C:\Users\AMi.000\.gemini\antigravity-ide\brain\7d3ff2c1-37a8-4a4b-a162-5a6505db2f4b\scratch\sample_us.md",
        "C:\Users\AMi.000\.gemini\antigravity-ide\brain\7d3ff2c1-37a8-4a4b-a162-5a6505db2f4b\scratch\sample_uc.md"
    )

    $suiteSuccess = $true
    foreach ($file in $testFiles) {
        if (Test-Path $file) {
            Write-Host "  -> Auditing file: $($file | Split-Path -Leaf)" -ForegroundColor Gray
            $output = & python $scriptPath --file $file 2>&1
            if ($LASTEXITCODE -ne 0) {
                Write-Host "  -> FAIL: Validation issues found in $($file | Split-Path -Leaf)!" -ForegroundColor Red
                Write-Host $output
                $suiteSuccess = $false
            } else {
                Write-Host "  -> PASS: $($file | Split-Path -Leaf) is fully compliant." -ForegroundColor Green
            }
        } else {
            Write-Host "  -> WARN: Sample file not found ($file)" -ForegroundColor Yellow
        }
    }

    if ($suiteSuccess) {
        Record-Result "US/UC Format Integrity" $true "100% compliance across all audited files"
    } else {
        Record-Result "US/UC Format Integrity" $false "Formatting or standard violations detected"
    }
} catch {
    Write-Host "  -> ERROR: $_" -ForegroundColor Red
    Record-Result "US/UC Format Integrity" $false $_.Exception.Message
}

# ----------------------------------------------------------------------
# FINAL SUMMARY
# ----------------------------------------------------------------------
Write-Host "`n============================================================" -ForegroundColor Cyan
Write-Host "                  AUDIT SUMMARY REPORT                      " -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan

foreach ($r in $suiteResults) {
    $statusText = if ($r.Passed) { "[PASS]" } else { "[FAIL]" }
    $color = if ($r.Passed) { "Green" } else { "Red" }
    Write-Host ("{0,-25} : {1,-8} ({2})" -f $r.Suite, $statusText, $r.Detail) -ForegroundColor $color
}

Write-Host "============================================================" -ForegroundColor Cyan
if ($allPassed) {
    Write-Host "   🎉 RESULT: ALL COMPOUNDING LOOP AUDITS PASSED 100%!     " -ForegroundColor Green
    Write-Host "============================================================`n" -ForegroundColor Cyan
    exit 0
} else {
    Write-Host "   ❌ RESULT: AUDIT FAILED - RESOLVE DISCREPANCIES!       " -ForegroundColor Red
    Write-Host "============================================================`n" -ForegroundColor Cyan
    exit 1
}
