import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image, ImageDraw, ImageFont
import os

output_dir = r"C:\Users\dathao\.gemini\antigravity-ide\scratch\thuc-hanh-danh-sach-css"
os.makedirs(output_dir, exist_ok=True)

# -------------------------------------------------------------------
# 1. BROWSER CSS LIST SCREENSHOT MOCKUP
# -------------------------------------------------------------------
def generate_browser_mockup():
    width = 1350
    height = 1000
    img = Image.new('RGB', (width, height), color='#f8fafc')
    draw = ImageDraw.Draw(img)

    # Browser Header bar
    draw.rectangle([0, 0, width, 44], fill='#1e293b')
    # Window controls
    draw.ellipse([20, 16, 32, 28], fill='#ef4444')
    draw.ellipse([40, 16, 52, 28], fill='#f59e0b')
    draw.ellipse([60, 16, 72, 28], fill='#10b981')

    # Browser Tab
    draw.rounded_rectangle([90, 8, 480, 44], radius=6, fill='#334155')
    draw.text((115, 16), "CodeGym - [Thuc Hanh] Danh sach trong CSS", fill='#ffffff')

    # Address bar
    draw.rectangle([0, 44, width, 88], fill='#ffffff')
    draw.line([0, 88, width, 88], fill='#cbd5e1', width=1)
    draw.rounded_rectangle([80, 52, width - 80, 80], radius=8, fill='#f8fafc', outline='#e2e8f0', width=1)
    draw.text((105, 59), "https://proyctk03-eng.github.io/thuc-hanh-danh-sach-css/index.html", fill='#475569')

    # Page Header Banner
    draw.rectangle([0, 89, width, 185], fill='#ffffff')
    draw.text((500, 105), "[THUC HANH] DANH SACH TRONG CSS", fill='#0f172a')
    draw.rounded_rectangle([450, 135, 900, 162], radius=14, fill='#eef2ff', outline='#c7d2fe')
    draw.text((475, 142), "LIST-STYLE-TYPE, IMAGE, POSITION, SHORTHAND & COLORS", fill='#4f46e5')
    draw.line([0, 185, width, 185], fill='#e2e8f0', width=1)

    # 2 Column Cards Grid
    # Left Column: Sections 2, 3, 4
    col1_x1, col1_x2 = 80, 680
    # Card 1: Square
    draw.rounded_rectangle([col1_x1, 205, col1_x2, 385], radius=12, fill='#ffffff', outline='#e2e8f0', width=1)
    draw.rectangle([col1_x1 + 16, 220, col1_x1 + 76, 240], fill='#f1f5f9')
    draw.text((col1_x1 + 22, 224), "MUC 2", fill='#475569')
    draw.text((col1_x1 + 90, 222), "list-style-type: square (Danh sach khong thu tu)", fill='#0f172a')
    items_sq = ["HTML", "CSS", "JavaScript", "Git"]
    for i, it in enumerate(items_sq):
        y = 255 + i * 30
        draw.rectangle([col1_x1 + 35, y + 4, col1_x1 + 43, y + 12], fill='#4f46e5')
        draw.text((col1_x1 + 55, y), it, fill='#1e293b')

    # Card 2: Upper Roman
    draw.rounded_rectangle([col1_x1, 405, col1_x2, 585], radius=12, fill='#ffffff', outline='#e2e8f0', width=1)
    draw.rectangle([col1_x1 + 16, 420, col1_x1 + 76, 440], fill='#f1f5f9')
    draw.text((col1_x1 + 22, 424), "MUC 3", fill='#475569')
    draw.text((col1_x1 + 90, 422), "list-style-type: upper-roman (Danh sach co thu tu)", fill='#0f172a')
    items_ro = [("I.", "Hoc HTML"), ("II.", "Hoc CSS"), ("III.", "Hoc JavaScript"), ("IV.", "Hoc Git")]
    for i, (num, it) in enumerate(items_ro):
        y = 455 + i * 30
        draw.text((col1_x1 + 32, y), num, fill='#7c3aed')
        draw.text((col1_x1 + 75, y), it, fill='#1e293b')

    # Card 3: Image Bullet
    draw.rounded_rectangle([col1_x1, 605, col1_x2, 785], radius=12, fill='#ffffff', outline='#e2e8f0', width=1)
    draw.rectangle([col1_x1 + 16, 620, col1_x1 + 76, 640], fill='#f1f5f9')
    draw.text((col1_x1 + 22, 624), "MUC 4", fill='#475569')
    draw.text((col1_x1 + 90, 622), "list-style-image: url('bullet.png')", fill='#0f172a')
    items_img = ["Visual Studio Code", "Google Chrome", "GitHub", "Git"]
    for i, it in enumerate(items_img):
        y = 655 + i * 30
        draw.ellipse([col1_x1 + 32, y + 2, col1_x1 + 44, y + 14], fill='#0284c7')
        draw.ellipse([col1_x1 + 35, y + 5, col1_x1 + 41, y + 11], fill='#38bdf8')
        draw.text((col1_x1 + 55, y), it, fill='#1e293b')

    # Card 4: Shorthand
    draw.rounded_rectangle([col1_x1, 805, col1_x2, 965], radius=12, fill='#f0fdf4', outline='#86efac', width=1)
    draw.rectangle([col1_x1 + 16, 818, col1_x1 + 76, 838], fill='#dcfce7')
    draw.text((col1_x1 + 22, 822), "MUC 6", fill='#166534')
    draw.text((col1_x1 + 90, 820), "list-style: square inside url('bullet.png')", fill='#166534')
    draw.text((col1_x1 + 35, 855), "• HTML5 kien truc ngu nghia & tieu chuan W3C", fill='#166534')
    draw.text((col1_x1 + 35, 885), "• CSS3 Flexbox & Grid Layout hien dai", fill='#166534')
    draw.text((col1_x1 + 35, 915), "• JavaScript DOM & Xu ly su kien tuong tac", fill='#166534')

    # Right Column: Sections 5, 7, 8
    col2_x1, col2_x2 = 705, 1270
    # Card 5: Outside vs Inside
    draw.rounded_rectangle([col2_x1, 205, col2_x2, 455], radius=12, fill='#ffffff', outline='#e2e8f0', width=1)
    draw.rectangle([col2_x1 + 16, 220, col2_x1 + 76, 240], fill='#f1f5f9')
    draw.text((col2_x1 + 22, 224), "MUC 5", fill='#475569')
    draw.text((col2_x1 + 90, 222), "list-style-position: outside vs inside", fill='#0f172a')

    # Outside box
    draw.rounded_rectangle([col2_x1 + 20, 255, col2_x1 + 265, 435], radius=8, fill='#eef2ff', outline='#6366f1', width=1)
    draw.text((col2_x1 + 30, 265), "outside (Dau nam ngoai)", fill='#3730a3')
    draw.ellipse([col2_x1 + 26, 298, col2_x1 + 32, 304], fill='#4338ca')
    draw.text((col2_x1 + 38, 294), "Visual Studio Code", fill='#3730a3')
    draw.ellipse([col2_x1 + 26, 328, col2_x1 + 32, 334], fill='#4338ca')
    draw.text((col2_x1 + 38, 324), "Google Chrome", fill='#3730a3')
    draw.ellipse([col2_x1 + 26, 358, col2_x1 + 32, 364], fill='#4338ca')
    draw.text((col2_x1 + 38, 354), "GitHub & Git", fill='#3730a3')

    # Inside box
    draw.rounded_rectangle([col2_x1 + 285, 255, col2_x2 - 20, 435], radius=8, fill='#fdf2f8', outline='#ec4899', width=1)
    draw.text((col2_x1 + 295, 265), "inside (Dau nam trong)", fill='#9d174d')
    draw.ellipse([col2_x1 + 305, 298, col2_x1 + 311, 304], fill='#db2777')
    draw.text((col2_x1 + 320, 294), "Visual Studio Code", fill='#9d174d')
    draw.ellipse([col2_x1 + 305, 328, col2_x1 + 311, 334], fill='#db2777')
    draw.text((col2_x1 + 320, 324), "Google Chrome", fill='#9d174d')
    draw.ellipse([col2_x1 + 305, 358, col2_x1 + 311, 364], fill='#db2777')
    draw.text((col2_x1 + 320, 354), "GitHub & Git", fill='#9d174d')

    # Card 7: Colors & Spacing
    draw.rounded_rectangle([col2_x1, 475, col2_x2, 695], radius=12, fill='#ffffff', outline='#e2e8f0', width=1)
    draw.rectangle([col2_x1 + 16, 490, col2_x1 + 76, 510], fill='#f1f5f9')
    draw.text((col2_x1 + 22, 494), "MUC 7", fill='#475569')
    draw.text((col2_x1 + 90, 492), "Dinh kieu mau sac, padding & margin", fill='#0f172a')
    # Dark container
    draw.rounded_rectangle([col2_x1 + 20, 525, col2_x2 - 20, 680], radius=10, fill='#0f172a')
    langs = ["HTML - Ngu nghia sieu van ban", "CSS - Dinh kieu tang & bo cuc", "JavaScript - Tuong tac nguoi dung", "Python - Da nang & AI"]
    for i, it in enumerate(langs):
        ly = 540 + i * 32
        draw.rounded_rectangle([col2_x1 + 35, ly, col2_x2 - 35, ly + 26], radius=4, fill='#1e293b')
        draw.text((col2_x1 + 48, ly + 4), "• " + it, fill='#38bdf8')

    # Card 8: Roadmap Web
    draw.rounded_rectangle([col2_x1, 715, col2_x2, 965], radius=14, fill='#1e1b4b', outline='#6366f1', width=2)
    draw.rounded_rectangle([col2_x1 + 16, 728, col2_x1 + 140, 748], radius=4, fill='#4f46e5')
    draw.text((col2_x1 + 22, 732), "MUC 8 • TONG HOP", fill='#ffffff')
    draw.text((col2_x1 + 150, 730), "Lo trinh hoc lap trinh Web", fill='#ffffff')

    stages = [
        ("CHANG 1", "HTML - Xay dung cau truc vung chac chuan W3C"),
        ("CHANG 2", "CSS - Giao dien tham my, Responsive Layout"),
        ("CHANG 3", "JavaScript - Xu ly logic tuong tac & API"),
        ("CHANG 4", "Git - Quan ly phien ban ma nguon cuc bo"),
        ("CHANG 5", "GitHub - Cong tac nhom, Pull Request, CI/CD")
    ]
    for i, (badge, desc) in enumerate(stages):
        ry = 760 + i * 38
        draw.rounded_rectangle([col2_x1 + 25, ry, col2_x2 - 25, ry + 32], radius=6, fill='#312e81', outline='#4f46e5')
        draw.rounded_rectangle([col2_x1 + 35, ry + 6, col2_x1 + 105, ry + 26], radius=3, fill='#38bdf8')
        draw.text((col2_x1 + 40, ry + 8), badge, fill='#0f172a')
        draw.text((col2_x1 + 115, ry + 7), desc, fill='#f8fafc')

    out_path = os.path.join(output_dir, "browser_css_list_screenshot.png")
    img.save(out_path)
    print(f"Generated {out_path}")

# -------------------------------------------------------------------
# 2. ARCHITECTURAL CSS LIST PROPERTIES DIAGRAM
# -------------------------------------------------------------------
def generate_properties_diagram():
    fig, ax = plt.subplots(figsize=(14, 9), dpi=300)
    ax.set_facecolor('#ffffff')
    fig.patch.set_facecolor('#f8fafc')

    # Title
    ax.text(0.5, 0.96, "SƠ ĐỒ TỔNG QUAN CÁC THUỘC TÍNH ĐỊNH KIỂU DANH SÁCH TRONG CSS (W3C)", 
            ha='center', va='center', fontsize=15, fontweight='bold', color='#0f172a')
    ax.text(0.5, 0.92, "Cơ chế phân cấp, cấu trúc mô hình hộp (Box Model) và cú pháp rút gọn của CSS Lists", 
            ha='center', va='center', fontsize=11, color='#64748b', style='italic')

    # 4 Quadrants
    # 1. list-style-type
    ax.add_patch(patches.FancyBboxPatch((0.05, 0.50), 0.42, 0.38, boxstyle="round,pad=0.02", 
                                        edgecolor='#818cf8', facecolor='#eef2ff', linewidth=1.5))
    ax.text(0.26, 0.84, "1. LIST-STYLE-TYPE (Kiểu đánh dấu)", 
            ha='center', va='center', fontsize=12, fontweight='bold', color='#3730a3')
    type_info = [
        "• Unordered (ul): disc (mặc định), circle, square, none",
        "• Ordered (ol): decimal (1,2,3), upper-roman (I,II,III),",
        "                lower-roman (i,ii,iii), upper-alpha (A,B,C),",
        "                lower-alpha (a,b,c)",
        "• Cú pháp: ul { list-style-type: square; }",
        "           ol { list-style-type: upper-roman; }"
    ]
    for idx, t in enumerate(type_info):
        ax.text(0.08, 0.77 - idx * 0.05, t, fontsize=9.5, color='#1e293b')

    # 2. list-style-position
    ax.add_patch(patches.FancyBboxPatch((0.53, 0.50), 0.42, 0.38, boxstyle="round,pad=0.02", 
                                        edgecolor='#f472b6', facecolor='#fdf2f8', linewidth=1.5))
    ax.text(0.74, 0.84, "2. LIST-STYLE-POSITION (Vị trí đánh dấu)", 
            ha='center', va='center', fontsize=12, fontweight='bold', color='#9d174d')
    pos_info = [
        "• outside (Mặc định):",
        "  Dấu marker nằm NGOÀI lề khối nội dung của <li>.",
        "  Khi văn bản xuống dòng, dòng 2 thẳng hàng với dòng 1.",
        "• inside:",
        "  Dấu marker nằm TRONG khối nội dung của <li>.",
        "  Khi văn bản xuống dòng, dòng 2 thụt lề về phía marker.",
        "• Cú pháp: ul { list-style-position: inside; }"
    ]
    for idx, t in enumerate(pos_info):
        ax.text(0.56, 0.77 - idx * 0.05, t, fontsize=9.5, color='#1e293b')

    # 3. list-style-image
    ax.add_patch(patches.FancyBboxPatch((0.05, 0.08), 0.42, 0.38, boxstyle="round,pad=0.02", 
                                        edgecolor='#38bdf8', facecolor='#f0f9ff', linewidth=1.5))
    ax.text(0.26, 0.42, "3. LIST-STYLE-IMAGE (Đánh dấu bằng ảnh)", 
            ha='center', va='center', fontsize=12, fontweight='bold', color='#0369a1')
    img_info = [
        "• Cho phép thay thế marker mặc định bằng icon/hình ảnh.",
        "• Luôn cần list-style-type làm giá trị dự phòng (fallback)",
        "  nếu đường dẫn ảnh gặp sự cố hoặc đang tải chậm.",
        "• Kích thước khuyến nghị: 16x16 px hoặc 20x20 px.",
        "• Cú pháp: ul { list-style-image: url('bullet.png'); }"
    ]
    for idx, t in enumerate(img_info):
        ax.text(0.08, 0.35 - idx * 0.055, t, fontsize=9.5, color='#1e293b')

    # 4. list-style Shorthand & Box Model
    ax.add_patch(patches.FancyBboxPatch((0.53, 0.08), 0.42, 0.38, boxstyle="round,pad=0.02", 
                                        edgecolor='#34d399', facecolor='#f0fdf4', linewidth=1.5))
    ax.text(0.74, 0.42, "4. LIST-STYLE SHORTHAND & BOX MODEL", 
            ha='center', va='center', fontsize=12, fontweight='bold', color='#047857')
    short_info = [
        "• Thuộc tính rút gọn list-style gom 3 thuộc tính:",
        "  list-style: [type] [position] [image];",
        "  Ví dụ: ul { list-style: square inside url('bullet.png'); }",
        "• Mô hình hộp: Mặc định trình duyệt cấp padding-left: 40px",
        "  cho <ul>/<ol>. Cần dùng padding và margin để điều chỉnh",
        "  khoảng cách trong và ngoài danh sách một cách tối ưu."
    ]
    for idx, t in enumerate(short_info):
        ax.text(0.56, 0.35 - idx * 0.055, t, fontsize=9.5, color='#1e293b')

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    plt.tight_layout()
    out_path = os.path.join(output_dir, "css_list_properties_diagram.png")
    plt.savefig(out_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Generated {out_path}")

if __name__ == "__main__":
    generate_browser_mockup()
    generate_properties_diagram()
    print("All CSS list diagrams created successfully!")
