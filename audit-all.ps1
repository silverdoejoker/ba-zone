$ErrorActionPreference = "Stop"

# Set encoding to UTF-8
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

# Root runner forwarder to scripts/audit-all.ps1
$targetScript = Join-Path $PSScriptRoot "scripts\audit-all.ps1"
if (Test-Path $targetScript) {
    & $targetScript @args
} else {
    Write-Host "Error: Could not find scripts\audit-all.ps1" -ForegroundColor Red
    exit 1
}
