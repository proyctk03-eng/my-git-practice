$docxPath = "C:\Users\dathao\.gemini\antigravity-ide\scratch\bai-tap-gop-o-rowspan-colspan\Bao_Cao_Bai_Tap_Gop_O_Rowspan_Colspan.docx"
$pdfPath = "C:\Users\dathao\.gemini\antigravity-ide\scratch\bai-tap-gop-o-rowspan-colspan\Bao_Cao_Bai_Tap_Gop_O_Rowspan_Colspan.pdf"

$word = New-Object -ComObject Word.Application
$word.Visible = $false
try {
    $doc = $word.Documents.Open($docxPath)
    $wdFormatPDF = 17
    $doc.SaveAs([ref]$pdfPath, [ref]$wdFormatPDF)
    $doc.Close()
    Write-Host "PDF Exported Successfully: $pdfPath"
} catch {
    Write-Error $_
} finally {
    $word.Quit()
    [System.Runtime.Interopservices.Marshal]::ReleaseComObject($word) | Out-Null
}
