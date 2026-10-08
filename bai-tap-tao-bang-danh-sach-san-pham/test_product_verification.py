import os
import re

def test_requirements():
    base_dir = r"C:\Users\dathao\.gemini\antigravity-ide\scratch\bai-tap-tao-bang-danh-sach-san-pham"
    
    # Check index.html
    index_path = os.path.join(base_dir, "index.html")
    assert os.path.exists(index_path), "index.html must exist"
    with open(index_path, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Heading h1
    assert re.search(r"<h1[^>]*>.*?Danh sách sản phẩm.*?</h1>", html, re.IGNORECASE | re.DOTALL), "h1 must contain 'Danh sách sản phẩm'"
    
    # Table elements
    assert "<table" in html, "Must contain <table> tag"
    assert "<tr" in html, "Must contain <tr> tag"
    assert "<th" in html, "Must contain <th> tag"
    assert "<td" in html, "Must contain <td> tag"
    
    # Required columns
    assert "Tên sản phẩm" in html, "Must have column 'Tên sản phẩm'"
    assert "Giá" in html, "Must have column 'Giá'"
    assert "Số lượng" in html, "Must have column 'Số lượng'"
    
    # Check products count (at least 4)
    # Check index_basic.html
    basic_path = os.path.join(base_dir, "index_basic.html")
    assert os.path.exists(basic_path), "index_basic.html must exist"
    with open(basic_path, "r", encoding="utf-8") as f:
        basic_html = f.read()
        
    assert "<h1>Danh sách sản phẩm</h1>" in basic_html, "index_basic.html must have exact h1"
    assert "<th>Tên sản phẩm</th>" in basic_html, "index_basic.html must have 'Tên sản phẩm' header"
    assert "<th>Giá</th>" in basic_html, "index_basic.html must have 'Giá' header"
    assert "<th>Số lượng</th>" in basic_html, "index_basic.html must have 'Số lượng' header"
    
    # Count rows in basic_html tbody/tr
    tr_matches = re.findall(r"<tr>(.*?)</tr>", basic_html, re.DOTALL)
    # 1 header row + data rows
    assert len(tr_matches) >= 5, f"Must have at least 1 header + 4 products, found {len(tr_matches)} rows"
    
    # PDF report check
    pdf_path = os.path.join(base_dir, "Bao_Cao_Bai_Tap_Tao_Bang_Danh_Sach_San_Pham.pdf")
    assert os.path.exists(pdf_path), "PDF report must exist"
    pdf_size = os.path.getsize(pdf_path)
    assert 0 < pdf_size <= 2 * 1024 * 1024, f"PDF size must be <= 2MB, got {pdf_size} bytes"
    
    # DOCX report check
    docx_path = os.path.join(base_dir, "Bao_Cao_Bai_Tap_Tao_Bang_Danh_Sach_San_Pham.docx")
    assert os.path.exists(docx_path), "DOCX report must exist"
    assert os.path.getsize(docx_path) > 50000, "DOCX report must be substantial (>50KB)"
    
    # Screenshot and diagram checks
    img1 = os.path.join(base_dir, "browser_product_table_screenshot.png")
    img2 = os.path.join(base_dir, "html_table_product_structure.png")
    assert os.path.exists(img1) and os.path.getsize(img1) > 10000, "Screenshot image must exist"
    assert os.path.exists(img2) and os.path.getsize(img2) > 10000, "Structure diagram must exist"
    
    print("ALL VERIFICATION ASSERTIONS PASSED SUCCESSFULLY!")

if __name__ == "__main__":
    test_requirements()
