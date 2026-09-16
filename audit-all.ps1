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

function Add-Result {
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

# Locate valid Python runtime
$pythonExe = $null
$candidates = @(
    "python",
    "py",
    "C:\Program Files\Unity\Hub\Editor\6000.6.0f1\Editor\Data\PlaybackEngines\WebGLSupport\BuildTools\Emscripten\python\python.exe",
    "$env:LOCALAPPDATA\Programs\Python\Python313\python.exe",
    "$env:LOCALAPPDATA\Programs\Python\Python312\python.exe",
    "$env:LOCALAPPDATA\Programs\Python\Python311\python.exe"
)

foreach ($c in $candidates) {
    try {
        $testOut = & $c --version 2>&1
        if ($LASTEXITCODE -eq 0 -and $testOut -match "Python \d") {
            $pythonExe = $c
            Write-Host "Detected Python Runtime: $c ($testOut)" -ForegroundColor DarkGray
            break
        }
    } catch {}
}

if (-not $pythonExe) {
    Write-Host "WARNING: No working Python runtime detected. Attempting default 'python' command..." -ForegroundColor Yellow
    $pythonExe = "python"
}

# ----------------------------------------------------------------------
# SUITE 1: Use Case Standard & Format Integrity (Karl Wiegers / IIBA 16 Fields)
# ----------------------------------------------------------------------
Write-Host "`n[1/3] Auditing Use Case Template & Quality Integrity (scripts/audit_uc.py)..." -ForegroundColor White
try {
    $scriptPath = Join-Path $PSScriptRoot "scripts\audit_uc.py"
    $testFiles = @(
        (Join-Path $PSScriptRoot "use-case-writer-skill\samples\sample_uc_en.md"),
        (Join-Path $PSScriptRoot "use-case-writer-skill\samples\sample_uc_vi.md")
    )

    $suiteSuccess = $true
    foreach ($file in $testFiles) {
        if (Test-Path $file) {
            Write-Host "  -> Auditing file: $($file | Split-Path -Leaf)" -ForegroundColor Gray
            $output = & $pythonExe $scriptPath --file $file 2>&1
            if ($LASTEXITCODE -ne 0) {
                Write-Host "  -> FAIL: Validation issues found in $($file | Split-Path -Leaf)!" -ForegroundColor Red
                Write-Host $output
                $suiteSuccess = $false
            } else {
                Write-Host "  -> PASS: $($file | Split-Path -Leaf) is 100% compliant." -ForegroundColor Green
            }
        } else {
            Write-Host "  -> WARN: Sample file not found ($file)" -ForegroundColor Yellow
        }
    }

    if ($suiteSuccess) {
        Add-Result "Use Case Standards (IIBA 16 Fields)" $true "All sample files passed 100%"
    } else {
        Add-Result "Use Case Standards (IIBA 16 Fields)" $false "Formatting or standard violations detected"
    }
} catch {
    Write-Host "  -> ERROR: $_" -ForegroundColor Red
    Add-Result "Use Case Standards (IIBA 16 Fields)" $false $_.Exception.Message
}

# ----------------------------------------------------------------------
# SUITE 2: User Story & AC Specification Integrity (INVEST + Gherkin)
# ----------------------------------------------------------------------
Write-Host "`n[2/3] Auditing User Story & AC Specification Integrity (scripts/audit_us.py)..." -ForegroundColor White
try {
    $scriptPath = Join-Path $PSScriptRoot "scripts\audit_us.py"
    $testFiles = @(
        (Join-Path $PSScriptRoot "user-story-writer-skill\samples\sample_us_en.md"),
        (Join-Path $PSScriptRoot "user-story-writer-skill\samples\sample_us_vi.md")
    )

    $suiteSuccess = $true
    foreach ($file in $testFiles) {
        if (Test-Path $file) {
            Write-Host "  -> Auditing file: $($file | Split-Path -Leaf)" -ForegroundColor Gray
            $output = & $pythonExe $scriptPath --file $file 2>&1
            if ($LASTEXITCODE -ne 0) {
                Write-Host "  -> FAIL: Validation issues found in $($file | Split-Path -Leaf)!" -ForegroundColor Red
                Write-Host $output
                $suiteSuccess = $false
            } else {
                Write-Host "  -> PASS: $($file | Split-Path -Leaf) is 100% compliant." -ForegroundColor Green
            }
        } else {
            Write-Host "  -> WARN: Sample file not found ($file)" -ForegroundColor Yellow
        }
    }

    if ($suiteSuccess) {
        Add-Result "User Story & AC (INVEST + Gherkin)" $true "All sample files passed 100%"
    } else {
        Add-Result "User Story & AC (INVEST + Gherkin)" $false "Formatting or standard violations detected"
    }
} catch {
    Write-Host "  -> ERROR: $_" -ForegroundColor Red
    Add-Result "User Story & AC (INVEST + Gherkin)" $false $_.Exception.Message
}

# ----------------------------------------------------------------------
# SUITE 3: Web App UAT & Live Experience Integrity (scripts/audit_uat.py)
# ----------------------------------------------------------------------
Write-Host "`n[3/3] Auditing Web App UAT & Live Experience Integrity (scripts/audit_uat.py)..." -ForegroundColor White
try {
    $scriptPath = Join-Path $PSScriptRoot "scripts\audit_uat.py"
    $testFiles = @(
        (Join-Path $PSScriptRoot "web-app-uat-skill\samples\sample_uat_report_en.md"),
        (Join-Path $PSScriptRoot "web-app-uat-skill\samples\sample_uat_report_vi.md")
    )

    $suiteSuccess = $true
    foreach ($file in $testFiles) {
        if (Test-Path $file) {
            Write-Host "  -> Auditing file: $($file | Split-Path -Leaf)" -ForegroundColor Gray
            $output = & $pythonExe $scriptPath --file $file 2>&1
            if ($LASTEXITCODE -ne 0) {
                Write-Host "  -> FAIL: Validation issues found in $($file | Split-Path -Leaf)!" -ForegroundColor Red
                Write-Host $output
                $suiteSuccess = $false
            } else {
                Write-Host "  -> PASS: $($file | Split-Path -Leaf) is 100% compliant." -ForegroundColor Green
            }
        } else {
            Write-Host "  -> WARN: Sample file not found ($file)" -ForegroundColor Yellow
        }
    }

    if ($suiteSuccess) {
        Add-Result "Web App UAT (TrọBill Methodology)" $true "All sample files passed 100%"
    } else {
        Add-Result "Web App UAT (TrọBill Methodology)" $false "Formatting or standard violations detected"
    }
} catch {
    Write-Host "  -> ERROR: $_" -ForegroundColor Red
    Add-Result "Web App UAT (TrọBill Methodology)" $false $_.Exception.Message
}

# ----------------------------------------------------------------------
# FINAL SUMMARY REPORT
# ----------------------------------------------------------------------
Write-Host "`n============================================================" -ForegroundColor Cyan
Write-Host "                  AUDIT SUMMARY REPORT                      " -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan

foreach ($r in $suiteResults) {
    $statusText = if ($r.Passed) { "[PASS]" } else { "[FAIL]" }
    $color = if ($r.Passed) { "Green" } else { "Red" }
    Write-Host ("{0,-38} : {1,-8} ({2})" -f $r.Suite, $statusText, $r.Detail) -ForegroundColor $color
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
