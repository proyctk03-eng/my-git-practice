$docxPath = "C:\Users\dathao\.gemini\antigravity-ide\scratch\thuc-hanh-bang-trong-css\Bao_Cao_Thuc_Hanh_Bang_Trong_CSS.docx"
$pdfPath = "C:\Users\dathao\.gemini\antigravity-ide\scratch\thuc-hanh-bang-trong-css\Bao_Cao_Thuc_Hanh_Bang_Trong_CSS.pdf"

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
