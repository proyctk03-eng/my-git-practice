import os
import re

def test_css_list():
    base_dir = r"C:\Users\dathao\.gemini\antigravity-ide\scratch\thuc-hanh-danh-sach-css"

    # 1. Check HTML and CSS exist
    html_path = os.path.join(base_dir, "index.html")
    css_path = os.path.join(base_dir, "style.css")
    assert os.path.exists(html_path), "index.html must exist"
    assert os.path.exists(css_path), "style.css must exist"

    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()

    with open(css_path, "r", encoding="utf-8") as f:
        css = f.read()

    # Link CSS
    assert re.search(r'<link[^>]*rel=["\']stylesheet["\'][^>]*href=["\']style\.css["\']', html), "index.html must link style.css"

    # Mục 2: square
    assert "list-style-type: square" in css or "list-style-type:square" in css, "Must have 'list-style-type: square'"
    assert "HTML" in html and "CSS" in html and "JavaScript" in html and "Git" in html, "Must have 4 subjects"

    # Mục 3: upper-roman
    assert "list-style-type: upper-roman" in css or "list-style-type:upper-roman" in css, "Must have 'list-style-type: upper-roman'"
    assert "Học HTML" in html and "Học CSS" in html and "Học JavaScript" in html and "Học Git" in html, "Must have 4 steps"

    # Mục 4: list-style-image
    assert "list-style-image" in css and "bullet.png" in css, "Must use list-style-image with bullet.png"
    bullet_path = os.path.join(base_dir, "bullet.png")
    assert os.path.exists(bullet_path) and os.path.getsize(bullet_path) > 0, "bullet.png must exist and be valid"
    assert "Visual Studio Code" in html and "Google Chrome" in html and "GitHub" in html, "Must have tools"

    # Mục 5: outside & inside
    assert "list-style-position: outside" in css or "list-style-position:outside" in css, "Must have outside position"
    assert "list-style-position: inside" in css or "list-style-position:inside" in css, "Must have inside position"

    # Mục 6: shorthand list-style
    assert re.search(r'list-style\s*:\s*[^;]+;', css), "Must have list-style shorthand property"

    # Mục 7: colors & spacing
    assert "background-color" in css, "Must have background-color"
    assert "color" in css, "Must have color"
    assert "padding" in css, "Must have padding"
    assert "margin" in css, "Must have margin"
    assert "Python" in html, "Must have Python in languages"

    # Mục 8: Roadmap
    assert "Lộ trình học lập trình Web" in html, "Must have Web Roadmap section"

    # PDF & DOCX
    pdf_path = os.path.join(base_dir, "Bao_Cao_Thuc_Hanh_Danh_Sach_Trong_CSS.pdf")
    docx_path = os.path.join(base_dir, "Bao_Cao_Thuc_Hanh_Danh_Sach_Trong_CSS.docx")
    assert os.path.exists(pdf_path), "PDF must exist"
    assert 0 < os.path.getsize(pdf_path) <= 2 * 1024 * 1024, "PDF must be <= 2MB"
    assert os.path.exists(docx_path) and os.path.getsize(docx_path) > 50000, "DOCX must exist and be > 50KB"

    # Images
    img1 = os.path.join(base_dir, "browser_css_list_screenshot.png")
    img2 = os.path.join(base_dir, "css_list_properties_diagram.png")
    assert os.path.exists(img1) and os.path.getsize(img1) > 10000, "Screenshot image must exist"
    assert os.path.exists(img2) and os.path.getsize(img2) > 10000, "Diagram image must exist"

    print("ALL CSS LIST VERIFICATION ASSERTIONS PASSED SUCCESSFULLY!")

if __name__ == "__main__":
    test_css_list()
