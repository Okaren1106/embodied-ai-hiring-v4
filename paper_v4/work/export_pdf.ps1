$ErrorActionPreference = 'Stop'
$revisionRoot = Split-Path $PSScriptRoot -Parent
$releaseDir = Join-Path $revisionRoot 'release'
$exportDir = Join-Path (Join-Path $revisionRoot 'verification') ('word_export_' + [guid]::NewGuid().ToString('N'))
New-Item -ItemType Directory -Path $exportDir | Out-Null
$word = New-Object -ComObject Word.Application
$word.Visible = $false
$word.DisplayAlerts = 0
$word.AutomationSecurity = 3
$counts = @{}
try {
    foreach ($name in @('IJM_Research_Reading_Copy','IJM_Main_Working_Text','IJM_Research_Tables','IJM_Research_Supplement')) {
        $sourcePath = Join-Path $exportDir ($name + '.docx')
        $targetPath = Join-Path $exportDir ($name + '.pdf')
        Copy-Item -LiteralPath (Join-Path $releaseDir ($name + '.docx')) -Destination $sourcePath
        $doc = $word.Documents.Open($sourcePath, $false, $true)
        try {
            $doc.ExportAsFixedFormat($targetPath, 17)
            if (-not (Test-Path -LiteralPath $targetPath)) { throw "PDF not created: $targetPath" }
            $counts[$name] = @{pages=$doc.ComputeStatistics(2);words=$doc.ComputeStatistics(0);pdf=$targetPath}
            Write-Output "$name : $($counts[$name].pages) pages; $($counts[$name].words) Word words"
        } finally { $doc.Close(0) }
    }
} finally { $word.Quit() }
$counts | ConvertTo-Json | Set-Content -LiteralPath (Join-Path (Join-Path $revisionRoot 'verification') 'word_statistics.json') -Encoding utf8
