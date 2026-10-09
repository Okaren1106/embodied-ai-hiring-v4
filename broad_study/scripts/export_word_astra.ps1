$ErrorActionPreference = 'Stop'
$reportRoot = Split-Path -Parent $PSScriptRoot
$reportDoc = Join-Path $reportRoot 'document/具身智能公开招聘研究_最终综合报告_Astra.docx'
$reportQa = Join-Path $reportRoot 'document_qa'
New-Item -ItemType Directory -Path $reportQa -Force | Out-Null
$reportPdf = Join-Path $reportQa 'Astra_final_report.pdf'
$reportWord = $null
$reportOpen = $null
try {
 $reportWord = New-Object -ComObject Word.Application
 $reportWord.Visible = $false
 $reportWord.DisplayAlerts = 0
 $reportOpen = $reportWord.Documents.Open($reportDoc, $false, $true, $false)
 $reportOpen.ExportAsFixedFormat($reportPdf, 17)
 Write-Output ('Exported ' + $reportOpen.ComputeStatistics(2) + ' pages')
} finally {
 if ($reportOpen) { $reportOpen.Close(0) }
 if ($reportWord) { $reportWord.Quit(0); [System.Runtime.InteropServices.Marshal]::FinalReleaseComObject($reportWord) | Out-Null }
}
