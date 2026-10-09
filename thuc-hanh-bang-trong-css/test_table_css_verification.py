import os
import re

def test_table_css():
    base_dir = r"C:\Users\dathao\.gemini\antigravity-ide\scratch\thuc-hanh-bang-trong-css"

    # 1. Check files exist
    html_path = os.path.join(base_dir, "index.html")
    basic_path = os.path.join(base_dir, "index_basic.html")
    css_path = os.path.join(base_dir, "style.css")

    assert os.path.exists(html_path), "index.html must exist"
    assert os.path.exists(basic_path), "index_basic.html must exist"
    assert os.path.exists(css_path), "style.css must exist"

    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()

    with open(basic_path, "r", encoding="utf-8") as f:
        basic_html = f.read()

    with open(css_path, "r", encoding="utf-8") as f:
        css = f.read()

    # Link CSS
    assert re.search(r'<link[^>]*rel=["\']stylesheet["\'][^>]*href=["\']style\.css["\']', html), "index.html must link style.css"

    # Check content in HTML
    for content in ["Họ tên", "Tuổi", "Lớp", "Nguyễn Văn A", "20", "Web", "Trần Thị B", "21"]:
        assert content in html, f"index.html must contain '{content}'"
        assert content in basic_html, f"index_basic.html must contain '{content}'"

    # Check CSS properties in style.css
    assert "border: 1px solid black" in css, "Must have 'border: 1px solid black'"
    assert "border-collapse: collapse" in css, "Must have 'border-collapse: collapse'"
    assert "width: 100%" in css, "Must have 'width: 100%'"
    assert "height: 50px" in css, "Must have 'height: 50px'"
    assert "text-align: left" in css, "Must have 'text-align: left'"
    assert "vertical-align: bottom" in css, "Must have 'vertical-align: bottom'"
    assert "height: 80px" in css, "Must have 'height: 80px'"
    assert "padding: 15px" in css, "Must have 'padding: 15px'"
    assert "background-color: #333" in css, "Must have 'background-color: #333'"
    assert "color: white" in css, "Must have 'color: white'"
    assert "background-color: #f2f2f2" in css, "Must have 'background-color: #f2f2f2'"

    # Check reports
    pdf_path = os.path.join(base_dir, "Bao_Cao_Thuc_Hanh_Bang_Trong_CSS.pdf")
    docx_path = os.path.join(base_dir, "Bao_Cao_Thuc_Hanh_Bang_Trong_CSS.docx")
    assert os.path.exists(pdf_path), "PDF must exist"
    assert 0 < os.path.getsize(pdf_path) <= 2 * 1024 * 1024, "PDF must be <= 2MB"
    assert os.path.exists(docx_path) and os.path.getsize(docx_path) > 50000, "DOCX must exist and be > 50KB"

    # Check diagrams
    img1 = os.path.join(base_dir, "browser_table_css_screenshot.png")
    img2 = os.path.join(base_dir, "css_table_properties_diagram.png")
    assert os.path.exists(img1) and os.path.getsize(img1) > 10000, "Screenshot image must exist"
    assert os.path.exists(img2) and os.path.getsize(img2) > 10000, "Diagram image must exist"

    print("ALL CSS TABLE VERIFICATION ASSERTIONS PASSED SUCCESSFULLY!")

if __name__ == "__main__":
    test_table_css()
