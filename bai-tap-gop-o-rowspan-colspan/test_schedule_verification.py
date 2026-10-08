import os
import re

def test_schedule_requirements():
    base_dir = r"C:\Users\dathao\.gemini\antigravity-ide\scratch\bai-tap-gop-o-rowspan-colspan"
    
    # 1. Check index_basic.html
    basic_path = os.path.join(base_dir, "index_basic.html")
    assert os.path.exists(basic_path), "index_basic.html must exist"
    with open(basic_path, "r", encoding="utf-8") as f:
        basic_html = f.read()

    # Exact h1
    assert "<h1>Lịch họp công ty</h1>" in basic_html, "Must contain exact '<h1>Lịch họp công ty</h1>'"

    # Table columns
    assert "<th>Ngày</th>" in basic_html, "Must have header '<th>Ngày</th>'"
    assert "<th>Giờ</th>" in basic_html, "Must have header '<th>Giờ</th>'"
    assert "<th>Nội dung cuộc họp</th>" in basic_html, "Must have header '<th>Nội dung cuộc họp</th>'"

    # Rowspan usage
    assert 'rowspan=' in basic_html, "Must use 'rowspan' attribute"
    assert re.search(r'<td[^>]*rowspan="[2-9]"[^>]*>.*?Thứ', basic_html, re.DOTALL), "rowspan must be applied on day column"

    # Colspan usage
    assert 'colspan=' in basic_html, "Must use 'colspan' attribute"
    assert re.search(r'<td[^>]*colspan="[2-9]"[^>]*>.*?kéo dài', basic_html, re.IGNORECASE | re.DOTALL), "colspan must be applied for multi-hour meetings"

    # 2. Check index.html
    index_path = os.path.join(base_dir, "index.html")
    assert os.path.exists(index_path), "index.html must exist"
    with open(index_path, "r", encoding="utf-8") as f:
        index_html = f.read()

    assert re.search(r"<h1[^>]*>.*?Lịch họp công ty.*?</h1>", index_html, re.IGNORECASE | re.DOTALL), "index.html must have h1 Lịch họp công ty"
    assert 'rowspan=' in index_html, "index.html must have rowspan"
    assert 'colspan=' in index_html, "index.html must have colspan"

    # 3. Check reports
    pdf_path = os.path.join(base_dir, "Bao_Cao_Bai_Tap_Gop_O_Rowspan_Colspan.pdf")
    assert os.path.exists(pdf_path), "PDF report must exist"
    pdf_sz = os.path.getsize(pdf_path)
    assert 0 < pdf_sz <= 2 * 1024 * 1024, f"PDF must be <= 2MB, got {pdf_sz} bytes"

    docx_path = os.path.join(base_dir, "Bao_Cao_Bai_Tap_Gop_O_Rowspan_Colspan.docx")
    assert os.path.exists(docx_path) and os.path.getsize(docx_path) > 50000, "DOCX report must exist and be > 50KB"

    # 4. Check diagram images
    img1 = os.path.join(base_dir, "browser_schedule_table_screenshot.png")
    img2 = os.path.join(base_dir, "html_rowspan_colspan_diagram.png")
    assert os.path.exists(img1) and os.path.getsize(img1) > 10000, "Screenshot image must exist"
    assert os.path.exists(img2) and os.path.getsize(img2) > 10000, "Structure diagram must exist"

    print("ALL SCHEDULE TEST VERIFICATIONS PASSED SUCCESSFULLY!")

if __name__ == "__main__":
    test_schedule_requirements()
