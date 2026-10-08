$ErrorActionPreference = "Stop"
$docxPath = "C:\Users\dathao\.gemini\antigravity-ide\scratch\bai-tap-form-dang-ky-nguoi-dung\Bao_Cao_Bai_Tap_Form_Dang_Ky_Nguoi_Dung.docx"
$pdfPath = "C:\Users\dathao\.gemini\antigravity-ide\scratch\bai-tap-form-dang-ky-nguoi-dung\Bao_Cao_Bai_Tap_Form_Dang_Ky_Nguoi_Dung.pdf"

Write-Host "Converting DOCX to PDF via Word COM..."
$word = New-Object -ComObject Word.Application
$word.Visible = $false
try {
    $doc = $word.Documents.Open($docxPath)
    $wdFormatPDF = 17
    $doc.SaveAs([ref]$pdfPath, [ref]$wdFormatPDF)
    $doc.Close()
    Write-Host "Successfully generated PDF: $pdfPath"
} finally {
    $word.Quit()
    [System.Runtime.Interopservices.Marshal]::ReleaseComObject($word) | Out-Null
}
