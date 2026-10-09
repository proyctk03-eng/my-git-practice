import os
import re

def test_portfolio():
    base_dir = r"C:\Users\dathao\.gemini\antigravity-ide\scratch\thuc-hanh-trang-web-ca-nhan-css"

    # 1. Check files exist
    html_path = os.path.join(base_dir, "index.html")
    basic_path = os.path.join(base_dir, "index_basic.html")
    css_path = os.path.join(base_dir, "style.css")
    avatar_path = os.path.join(base_dir, "avatar.jpg")

    assert os.path.exists(html_path), "index.html must exist"
    assert os.path.exists(basic_path), "index_basic.html must exist"
    assert os.path.exists(css_path), "style.css must exist"
    assert os.path.exists(avatar_path) and os.path.getsize(avatar_path) > 0, "avatar.jpg must exist"

    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()

    with open(basic_path, "r", encoding="utf-8") as f:
        basic_html = f.read()

    with open(css_path, "r", encoding="utf-8") as f:
        css = f.read()

    # Link CSS
    assert re.search(r'<link[^>]*rel=["\']stylesheet["\'][^>]*href=["\']style\.css["\']', html), "index.html must link style.css"
    assert re.search(r'<link[^>]*rel=["\']stylesheet["\'][^>]*href=["\']style\.css["\']', basic_html), "index_basic.html must link style.css"

    # Content checks
    assert "Chào mừng đến với trang web cá nhân của tôi" in html, "Must have header title"
    assert "Nguyễn Văn A" in html, "Must have author name"
    assert "avatar.jpg" in html and "avatar" in html, "Must have avatar img with class avatar"
    for h in ["Đọc sách", "Chơi thể thao", "Lập trình", "Du lịch"]:
        assert h in html, f"Must have hobby {h}"
    assert "Mục tiêu học tập" in html, "Must have goals section"
    assert "Thông tin liên hệ" in html, "Must have contact section"
    assert "Email" in html and "Facebook" in html, "Must have contact table rows"

    # CSS selectors and rules checks
    assert "background-color: #f5f5f5" in css or "background-color:#f5f5f5" in css, "Must have body background-color #f5f5f5"
    assert "background-image" in css, "Must have background-image in CSS"
    assert "text-align: center" in css or "text-align:center" in css, "Must have text-align center in body"
    assert "background-color: #4CAF50" in css or "background-color:#4CAF50" in css, "Must have #4CAF50"
    assert "border-radius: 50%" in css or "border-radius:50%" in css, "Must have border-radius 50%"
    assert "list-style-type: square" in css or "list-style-type:square" in css, "Must have list-style-type square"
    assert "border-collapse: collapse" in css or "border-collapse:collapse" in css, "Must have border-collapse collapse"
    assert "width: 50%" in css or "width:50%" in css, "Must have table width 50%"
    assert "background-color: #ddd" in css or "background-color:#ddd" in css, "Must have footer background-color #ddd"

    # Report checks
    pdf_path = os.path.join(base_dir, "Bao_Cao_Thuc_Hanh_Trang_Web_Ca_Nhan_CSS.pdf")
    docx_path = os.path.join(base_dir, "Bao_Cao_Thuc_Hanh_Trang_Web_Ca_Nhan_CSS.docx")
    assert os.path.exists(pdf_path), "PDF must exist"
    assert 0 < os.path.getsize(pdf_path) <= 2 * 1024 * 1024, "PDF must be <= 2MB"
    assert os.path.exists(docx_path) and os.path.getsize(docx_path) > 50000, "DOCX must exist and be > 50KB"

    # Diagram checks
    img1 = os.path.join(base_dir, "browser_portfolio_screenshot.png")
    img2 = os.path.join(base_dir, "css_portfolio_structure_diagram.png")
    assert os.path.exists(img1) and os.path.getsize(img1) > 10000, "Screenshot image must exist"
    assert os.path.exists(img2) and os.path.getsize(img2) > 10000, "Diagram image must exist"

    print("ALL PORTFOLIO VERIFICATION ASSERTIONS PASSED SUCCESSFULLY!")

if __name__ == "__main__":
    test_portfolio()
