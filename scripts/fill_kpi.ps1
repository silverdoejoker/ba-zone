$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

$xlsxPath = "d:\repo\ba-zone\docs\outputs\KPI - CVCC Phân tích Nghiệp vụ - 38108.xlsx"
$backupPath = "d:\repo\ba-zone\docs\outputs\KPI - CVCC Phân tích Nghiệp vụ - 38108_backup.xlsx"
$contentFile = "d:\repo\ba-zone\scripts\content_c13.txt"

Write-Host "==================================================" -ForegroundColor Cyan
Write-Host " AUTO-FILL KPI (UTF-8 CLEAN / ZERO MOJIBAKE)       " -ForegroundColor Cyan
Write-Host "==================================================" -ForegroundColor Cyan

# 1. Restore from pristine backup if available, to guarantee clean start
if (Test-Path $backupPath) {
    Copy-Item -Path $backupPath -Destination $xlsxPath -Force
    Write-Host "[1/4] Restored pristine template from backup: $backupPath" -ForegroundColor Green
} else {
    # If backup doesn't exist, create it now
    Copy-Item -Path $xlsxPath -Destination $backupPath -Force
    Write-Host "[1/4] Created backup at: $backupPath" -ForegroundColor Green
}

# 2. Read new content from UTF-8 file (100% immune to PowerShell encoding issues)
if (-not (Test-Path $contentFile)) {
    Write-Host "ERROR: $contentFile not found!" -ForegroundColor Red
    exit 1
}
$newContent = Get-Content -Path $contentFile -Encoding UTF8 -Raw
Write-Host "[2/4] Loaded UTF-8 content successfully ($($newContent.Length) chars)." -ForegroundColor White

# 3. Extract Excel package
$tempDir = Join-Path $env:TEMP ("kpi_utf8_" + [System.Guid]::NewGuid().ToString("N"))
New-Item -ItemType Directory -Path $tempDir -Force | Out-Null
Write-Host "[3/4] Extracting Excel package to temp..." -ForegroundColor White

Add-Type -AssemblyName System.IO.Compression.FileSystem
[System.IO.Compression.ZipFile]::ExtractToDirectory($xlsxPath, $tempDir)

$sharedStringsPath = Join-Path $tempDir "xl\sharedStrings.xml"
$sheet1Path = Join-Path $tempDir "xl\worksheets\sheet1.xml"
$replaced = $false

if (Test-Path $sharedStringsPath) {
    $content = [System.IO.File]::ReadAllText($sharedStringsPath, [System.Text.Encoding]::UTF8)
    
    # We look for the C13 block (starts with Phân tích, Xác định or 1. GMS-OM or PhÃ¢n)
    $pattern = "<si>(?:(?!</si>).)*?(?:Phân tích|PhÃ¢n|GMS-OM|TAS - REF-TAS-2026).*?</si>"
    
    if ($content -match $pattern) {
        Write-Host "  -> Found target C13 pattern in sharedStrings.xml!" -ForegroundColor Green
        $escapedNew = [System.Security.SecurityElement]::Escape($newContent)
        $newSi = "<si><t xml:space=`"preserve`">$escapedNew</t></si>"
        
        $content = [System.Text.RegularExpressions.Regex]::Replace($content, $pattern, $newSi, [System.Text.RegularExpressions.RegexOptions]::Singleline)
        [System.IO.File]::WriteAllText($sharedStringsPath, $content, [System.Text.Encoding]::UTF8)
        $replaced = $true
        Write-Host "  -> Updated sharedStrings.xml with clean UTF-8!" -ForegroundColor Green
    }
}

if (-not $replaced) {
    Write-Host "  -> Fallback to sheet1.xml inlineStr..." -ForegroundColor Yellow
    $sheetContent = [System.IO.File]::ReadAllText($sheet1Path, [System.Text.Encoding]::UTF8)
    $escapedNew = [System.Security.SecurityElement]::Escape($newContent)
    $newCell = "<c r=`"C13`" t=`"inlineStr`"><is><t xml:space=`"preserve`">$escapedNew</t></is></c>"
    $cellPattern = "<c r=`"C13`"[^>]*>.*?</c>"
    if ($sheetContent -match $cellPattern) {
        $sheetContent = [System.Text.RegularExpressions.Regex]::Replace($sheetContent, $cellPattern, $newCell, [System.Text.RegularExpressions.RegexOptions]::Singleline)
        [System.IO.File]::WriteAllText($sheet1Path, $sheetContent, [System.Text.Encoding]::UTF8)
        $replaced = $true
        Write-Host "  -> Updated sheet1.xml cell C13 as inlineStr!" -ForegroundColor Green
    }
}

# 4. Repack into xlsx
if ($replaced) {
    Write-Host "[4/4] Repacking Excel package..." -ForegroundColor White
    $tempZip = Join-Path $env:TEMP ("kpi_clean_" + [System.Guid]::NewGuid().ToString("N") + ".zip")
    [System.IO.Compression.ZipFile]::CreateFromDirectory($tempDir, $tempZip)
    
    Copy-Item -Path $tempZip -Destination $xlsxPath -Force
    Remove-Item -Path $tempZip -Force
    Remove-Item -Path $tempDir -Recurse -Force
    
    Write-Host "`n🎉 THÀNH CÔNG: Đã ghi đè ô C13 chuẩn 100% tiếng Việt UTF-8 (Sạch Mojibake)!" -ForegroundColor Green
    Write-Host "File đã ghi: $xlsxPath" -ForegroundColor Cyan
    Write-Host "Anh hãy ĐÓNG file Excel trước (nếu đang mở), rồi mở lại để xem nhé!`n" -ForegroundColor Yellow
} else {
    Write-Host "❌ Không tìm thấy ô C13 để thay thế." -ForegroundColor Red
    Remove-Item -Path $tempDir -Recurse -Force
    exit 1
}
