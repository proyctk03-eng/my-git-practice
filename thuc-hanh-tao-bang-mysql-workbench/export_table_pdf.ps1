$docxPath = "C:\Users\dathao\.gemini\antigravity-ide\scratch\thuc-hanh-tao-bang-mysql-workbench\Bao_Cao_Thuc_Hanh_Tao_Bang_MySQL_Workbench.docx"
$pdfPath = "C:\Users\dathao\.gemini\antigravity-ide\scratch\thuc-hanh-tao-bang-mysql-workbench\Bao_Cao_Thuc_Hanh_Tao_Bang_MySQL_Workbench.pdf"

try {
    $word = New-Object -ComObject Word.Application
    $word.Visible = $false
    $doc = $word.Documents.Open($docxPath)
    # 17 = wdFormatPDF
    $doc.SaveAs([ref]$pdfPath, [ref]17)
    $doc.Close()
    $word.Quit()
    [System.Runtime.Interopservices.Marshal]::ReleaseComObject($word) | Out-Null
    Write-Output "Successfully exported PDF via Word COM: $pdfPath"
} catch {
    Write-Error "Failed to export PDF: $_"
}
