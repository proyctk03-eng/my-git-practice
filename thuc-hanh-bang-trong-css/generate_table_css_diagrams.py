import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image, ImageDraw, ImageFont
import os

output_dir = r"C:\Users\dathao\.gemini\antigravity-ide\scratch\thuc-hanh-bang-trong-css"
os.makedirs(output_dir, exist_ok=True)

# -------------------------------------------------------------------
# 1. BROWSER TABLE CSS SCREENSHOT MOCKUP
# -------------------------------------------------------------------
def generate_browser_mockup():
    width = 1350
    height = 980
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
    draw.text((115, 16), "CodeGym - [Thuc Hanh] Bang trong CSS", fill='#ffffff')

    # Address bar
    draw.rectangle([0, 44, width, 88], fill='#ffffff')
    draw.line([0, 88, width, 88], fill='#cbd5e1', width=1)
    draw.rounded_rectangle([80, 52, width - 80, 80], radius=8, fill='#f8fafc', outline='#e2e8f0', width=1)
    draw.text((105, 59), "https://proyctk03-eng.github.io/thuc-hanh-bang-trong-css/index.html", fill='#475569')

    # Page Header Banner
    draw.rectangle([0, 89, width, 185], fill='#ffffff')
    draw.text((510, 105), "[THUC HANH] BANG TRONG CSS", fill='#0f172a')
    draw.rounded_rectangle([450, 135, 900, 162], radius=14, fill='#eef2ff', outline='#c7d2fe')
    draw.text((470, 142), "BORDER, COLLAPSE, DIMENSIONS, ALIGNMENT, PADDING & COLORS", fill='#4f46e5')
    draw.line([0, 185, width, 185], fill='#e2e8f0', width=1)

    # 2 Column Cards Grid
    col1_x1, col1_x2 = 80, 680
    col2_x1, col2_x2 = 705, 1270

    # Card 1: Default Double Border vs Collapse
    draw.rounded_rectangle([col1_x1, 205, col1_x2, 435], radius=12, fill='#ffffff', outline='#e2e8f0', width=1)
    draw.rectangle([col1_x1 + 16, 218, col1_x1 + 76, 238], fill='#f1f5f9')
    draw.text((col1_x1 + 22, 222), "MUC 1-2", fill='#475569')
    draw.text((col1_x1 + 90, 220), "border-collapse: separate vs collapse", fill='#0f172a')

    # Mini Table 1: Separate (Vien kep)
    draw.text((col1_x1 + 25, 250), "1. border (Vien kep mac dinh):", fill='#475569')
    t1_y = 275
    draw.rectangle([col1_x1 + 25, t1_y, col1_x1 + 280, t1_y + 65], outline='#000000', width=2)
    draw.rectangle([col1_x1 + 29, t1_y + 4, col1_x1 + 110, t1_y + 28], outline='#000000', width=1)
    draw.text((col1_x1 + 35, t1_y + 8), "Ho ten", fill='#000000')
    draw.rectangle([col1_x1 + 114, t1_y + 4, col1_x1 + 195, t1_y + 28], outline='#000000', width=1)
    draw.text((col1_x1 + 120, t1_y + 8), "Tuoi", fill='#000000')
    draw.rectangle([col1_x1 + 199, t1_y + 4, col1_x1 + 276, t1_y + 28], outline='#000000', width=1)
    draw.text((col1_x1 + 210, t1_y + 8), "Lop", fill='#000000')

    draw.rectangle([col1_x1 + 29, t1_y + 32, col1_x1 + 110, t1_y + 58], outline='#000000', width=1)
    draw.text((col1_x1 + 35, t1_y + 38), "Van A", fill='#000000')
    draw.rectangle([col1_x1 + 114, t1_y + 32, col1_x1 + 195, t1_y + 58], outline='#000000', width=1)
    draw.text((col1_x1 + 120, t1_y + 38), "20", fill='#000000')
    draw.rectangle([col1_x1 + 199, t1_y + 32, col1_x1 + 276, t1_y + 58], outline='#000000', width=1)
    draw.text((col1_x1 + 210, t1_y + 38), "Web", fill='#000000')

    # Mini Table 2: Collapse (Vien don)
    draw.text((col1_x1 + 320, 250), "2. border-collapse: collapse (Vien don):", fill='#047857')
    t2_x = col1_x1 + 320
    draw.rectangle([t2_x, t1_y, t2_x + 250, t1_y + 60], outline='#059669', width=2)
    draw.line([t2_x, t1_y + 30, t2_x + 250, t1_y + 30], fill='#059669', width=1)
    draw.line([t2_x + 100, t1_y, t2_x + 100, t1_y + 60], fill='#059669', width=1)
    draw.line([t2_x + 175, t1_y, t2_x + 175, t1_y + 60], fill='#059669', width=1)
    draw.text((t2_x + 15, t1_y + 8), "Ho ten", fill='#065f46')
    draw.text((t2_x + 120, t1_y + 8), "Tuoi", fill='#065f46')
    draw.text((t2_x + 195, t1_y + 8), "Lop", fill='#065f46')
    draw.text((t2_x + 15, t1_y + 38), "Van A", fill='#065f46')
    draw.text((t2_x + 120, t1_y + 38), "20", fill='#065f46')
    draw.text((t2_x + 195, t1_y + 38), "Web", fill='#065f46')

    draw.text((col1_x1 + 25, 360), "• border-collapse: collapse giup gom 2 duong vien lien ke thanh 1 duong vien.", fill='#475569')
    draw.text((col1_x1 + 25, 385), "• Khac phuc hoan toan khoang trong (spacing) mac dinh giua cac o.", fill='#475569')

    # Card 2: Dimensions & Alignments
    draw.rounded_rectangle([col1_x1, 455, col1_x2, 705], radius=12, fill='#ffffff', outline='#e2e8f0', width=1)
    draw.rectangle([col1_x1 + 16, 468, col1_x1 + 76, 488], fill='#f1f5f9')
    draw.text((col1_x1 + 22, 472), "MUC 3-5", fill='#475569')
    draw.text((col1_x1 + 90, 470), "width: 100%, height, text-align & vertical-align", fill='#0f172a')

    # Dimension & Vertical align Table
    t3_y = 510
    draw.rectangle([col1_x1 + 25, t3_y, col1_x2 - 25, t3_y + 115], outline='#334155', width=1)
    draw.rectangle([col1_x1 + 25, t3_y, col1_x2 - 25, t3_y + 40], fill='#e2e8f0')
    draw.line([col1_x1 + 25, t3_y + 40, col1_x2 - 25, t3_y + 40], fill='#334155', width=1)
    draw.line([col1_x1 + 220, t3_y, col1_x1 + 220, t3_y + 115], fill='#334155', width=1)
    draw.line([col1_x1 + 380, t3_y, col1_x1 + 380, t3_y + 115], fill='#334155', width=1)

    draw.text((col1_x1 + 35, t3_y + 12), "th { height: 50px; text-align: left; }", fill='#0f172a')
    draw.text((col1_x1 + 240, t3_y + 12), "Tuoi", fill='#0f172a')
    draw.text((col1_x1 + 400, t3_y + 12), "Lop", fill='#0f172a')

    draw.text((col1_x1 + 35, t3_y + 88), "td { vertical-align: bottom; height: 80px; }", fill='#475569')
    draw.text((col1_x1 + 240, t3_y + 88), "20", fill='#475569')
    draw.text((col1_x1 + 400, t3_y + 88), "Web", fill='#475569')

    draw.text((col1_x1 + 25, 645), "• text-align: left dua tieu de th ve can le trai.", fill='#475569')
    draw.text((col1_x1 + 25, 670), "• vertical-align: bottom dua noi dung xuong sat day o theo chieu doc.", fill='#475569')

    # Card 3: Padding & Colors
    draw.rounded_rectangle([col1_x1, 725, col1_x2, 955], radius=12, fill='#ffffff', outline='#e2e8f0', width=1)
    draw.rectangle([col1_x1 + 16, 738, col1_x1 + 76, 758], fill='#f1f5f9')
    draw.text((col1_x1 + 22, 742), "MUC 6-7", fill='#475569')
    draw.text((col1_x1 + 90, 740), "Padding & Colors: #333 Dark Header, #f2f2f2 Light Rows", fill='#0f172a')

    # Colored Table
    t4_y = 775
    draw.rectangle([col1_x1 + 25, t4_y, col1_x2 - 25, t4_y + 90], outline='#000000', width=1)
    draw.rectangle([col1_x1 + 25, t4_y, col1_x2 - 25, t4_y + 32], fill='#333333')
    draw.rectangle([col1_x1 + 25, t4_y + 32, col1_x2 - 25, t4_y + 62], fill='#f2f2f2')
    draw.rectangle([col1_x1 + 25, t4_y + 62, col1_x2 - 25, t4_y + 90], fill='#ffffff')

    draw.line([col1_x1 + 220, t4_y, col1_x1 + 220, t4_y + 90], fill='#000000', width=1)
    draw.line([col1_x1 + 380, t4_y, col1_x1 + 380, t4_y + 90], fill='#000000', width=1)
    draw.line([col1_x1 + 25, t4_y + 32, col1_x2 - 25, t4_y + 32], fill='#000000', width=1)
    draw.line([col1_x1 + 25, t4_y + 62, col1_x2 - 25, t4_y + 62], fill='#000000', width=1)

    draw.text((col1_x1 + 35, t4_y + 8), "Ho ten (padding: 15px)", fill='#ffffff')
    draw.text((col1_x1 + 240, t4_y + 8), "Tuoi", fill='#ffffff')
    draw.text((col1_x1 + 400, t4_y + 8), "Lop", fill='#ffffff')

    draw.text((col1_x1 + 35, t4_y + 40), "Nguyen Van A", fill='#333333')
    draw.text((col1_x1 + 240, t4_y + 40), "20", fill='#333333')
    draw.text((col1_x1 + 400, t4_y + 40), "Web", fill='#333333')

    draw.text((col1_x1 + 35, t4_y + 70), "Tran Thi B", fill='#333333')
    draw.text((col1_x1 + 240, t4_y + 70), "21", fill='#333333')
    draw.text((col1_x1 + 400, t4_y + 70), "Web", fill='#333333')

    draw.text((col1_x1 + 25, 885), "• padding tao khoang dem thoang giua van ban va duong vien.", fill='#475569')
    draw.text((col1_x1 + 25, 910), "• Mau nen toi #333 chu trang lam bat phan cap thong tin.", fill='#475569')

    # Right Column: Big Modern Table (Mục 8)
    draw.rounded_rectangle([col2_x1, 205, col2_x2, 955], radius=14, fill='#ffffff', outline='#c7d2fe', width=2)
    draw.rectangle([col2_x1 + 16, 218, col2_x1 + 130, 238], fill='#4f46e5')
    draw.text((col2_x1 + 22, 222), "MUC 8 • TONG HOP", fill='#ffffff')
    draw.text((col2_x1 + 140, 220), "Bang quan ly hoc vien chuan UI/UX hien dai", fill='#0f172a')
    draw.text((col2_x1 + 25, 255), "Ket hop toan bo cac thuoc tinh: border-collapse, width: 100%, padding,", fill='#64748b')
    draw.text((col2_x1 + 25, 275), "zebra striping (ke soc xen ke), hover effect va badge trang thai.", fill='#64748b')

    # Big Pro Table Box
    tb_y = 310
    draw.rounded_rectangle([col2_x1 + 20, tb_y, col2_x2 - 20, tb_y + 550], radius=10, fill='#ffffff', outline='#cbd5e1', width=1)
    # Header row
    draw.rectangle([col2_x1 + 20, tb_y, col2_x2 - 20, tb_y + 48], fill='#0f172a')
    draw.text((col2_x1 + 35, tb_y + 15), "MA HV", fill='#ffffff')
    draw.text((col2_x1 + 120, tb_y + 15), "HO VA TEN", fill='#ffffff')
    draw.text((col2_x1 + 265, tb_y + 15), "TUOI", fill='#ffffff')
    draw.text((col2_x1 + 325, tb_y + 15), "KHOA HOC", fill='#ffffff')
    draw.text((col2_x1 + 470, tb_y + 15), "TRANG THAI", fill='#ffffff')

    students = [
        ("CG-101", "Nguyen Van A", "20", "Lap trinh Web Front-end", "Dang hoc", '#e0f2fe', '#0369a1'),
        ("CG-102", "Tran Thi B", "21", "Lap trinh Web Fullstack", "Xuat sac", '#dcfce7', '#15803d'),
        ("CG-103", "Le Hoang C", "22", "Khoa hoc Du lieu & AI", "Dang hoc", '#e0f2fe', '#0369a1'),
        ("CG-104", "Pham Minh D", "19", "Lap trinh Web Front-end", "Dang hoc", '#e0f2fe', '#0369a1'),
        ("CG-105", "Vu Thi Mai E", "23", "Kiem thu Phan mem QA", "Hoan thanh", '#dcfce7', '#15803d'),
        ("CG-106", "Dang Quoc F", "20", "Lap trinh Di dong Flutter", "Dang hoc", '#e0f2fe', '#0369a1'),
        ("CG-107", "Bui Thu Huyen", "21", "Thiet ke UI/UX Design", "Xuat sac", '#dcfce7', '#15803d'),
    ]
    for idx, (code, name, age, course, status, b_bg, b_fg) in enumerate(students):
        ry = tb_y + 48 + idx * 62
        bg = '#f8fafc' if idx % 2 == 1 else '#ffffff'
        draw.rectangle([col2_x1 + 20, ry, col2_x2 - 20, ry + 62], fill=bg)
        draw.line([col2_x1 + 20, ry + 62, col2_x2 - 20, ry + 62], fill='#e2e8f0', width=1)

        draw.text((col2_x1 + 35, ry + 22), code, fill='#4f46e5')
        draw.text((col2_x1 + 120, ry + 22), name, fill='#0f172a')
        draw.text((col2_x1 + 270, ry + 22), age, fill='#64748b')
        draw.text((col2_x1 + 325, ry + 22), course, fill='#1e293b')

        # Status badge
        draw.rounded_rectangle([col2_x1 + 465, ry + 16, col2_x1 + 540, ry + 44], radius=14, fill=b_bg)
        draw.text((col2_x1 + 475, ry + 22), status, fill=b_fg)

    # Footer note of pro table
    draw.rectangle([col2_x1 + 20, tb_y + 48 + len(students) * 62, col2_x2 - 20, tb_y + 550], fill='#f8fafc')
    draw.text((col2_x1 + 35, tb_y + 495), "Tong so hoc vien: 7 | Ty le hoan thanh khoa hoc: 100% | Chuan W3C CSS", fill='#64748b')

    out_path = os.path.join(output_dir, "browser_table_css_screenshot.png")
    img.save(out_path)
    print(f"Generated {out_path}")

# -------------------------------------------------------------------
# 2. ARCHITECTURAL CSS TABLE PROPERTIES DIAGRAM
# -------------------------------------------------------------------
def generate_properties_diagram():
    fig, ax = plt.subplots(figsize=(14, 9), dpi=300)
    ax.set_facecolor('#ffffff')
    fig.patch.set_facecolor('#f8fafc')

    # Title
    ax.text(0.5, 0.96, "SƠ ĐỒ CƠ CHẾ ĐỊNH KIỂU BẢNG TRONG CSS (W3C CSS TABLE MODEL)", 
            ha='center', va='center', fontsize=15, fontweight='bold', color='#0f172a')
    ax.text(0.5, 0.92, "Nguyên lý gộp đường viền, căn chỉnh đa chiều và tối ưu mô hình hộp cho Table Cells", 
            ha='center', va='center', fontsize=11, color='#64748b', style='italic')

    # 4 Quadrants
    # 1. border & border-collapse
    ax.add_patch(patches.FancyBboxPatch((0.05, 0.50), 0.42, 0.38, boxstyle="round,pad=0.02", 
                                        edgecolor='#818cf8', facecolor='#eef2ff', linewidth=1.5))
    ax.text(0.26, 0.84, "1. BORDER & BORDER-COLLAPSE", 
            ha='center', va='center', fontsize=12, fontweight='bold', color='#3730a3')
    b_info = [
        "• Mặc định: border-collapse: separate;",
        "  Mỗi ô <th>, <td> và <table> có viền riêng, tạo ra viền kép.",
        "• Chuẩn tối ưu: border-collapse: collapse;",
        "  Các đường viền liền kề được gộp thành một đường duy nhất,",
        "  loại bỏ triệt để khe hở giữa các ô.",
        "• Cú pháp: table { border-collapse: collapse; }",
        "           table, th, td { border: 1px solid black; }"
    ]
    for idx, t in enumerate(b_info):
        ax.text(0.08, 0.77 - idx * 0.048, t, fontsize=9.2, color='#1e293b')

    # 2. Width & Height
    ax.add_patch(patches.FancyBboxPatch((0.53, 0.50), 0.42, 0.38, boxstyle="round,pad=0.02", 
                                        edgecolor='#38bdf8', facecolor='#f0f9ff', linewidth=1.5))
    ax.text(0.74, 0.84, "2. CHIỀU RỘNG & CHIỀU CAO (WIDTH & HEIGHT)", 
            ha='center', va='center', fontsize=12, fontweight='bold', color='#0369a1')
    dim_info = [
        "• width: 100%: Bảng co giãn chiếm toàn bộ chiều ngang",
        "  của phần tử cha (container), đáp ứng responsive tốt.",
        "• height trên <th>/<td>: Thiết lập chiều cao tối thiểu cho ô.",
        "  Ví dụ: th { height: 50px; } giúp hàng tiêu đề cao ráo,",
        "  dễ phân biệt với các dòng dữ liệu thông thường.",
        "• Table layout: table-layout: fixed giúp kiểm soát độ rộng",
        "  chính xác theo từng cột thay vì tự động theo nội dung."
    ]
    for idx, t in enumerate(dim_info):
        ax.text(0.56, 0.77 - idx * 0.048, t, fontsize=9.2, color='#1e293b')

    # 3. Horizontal & Vertical Alignment
    ax.add_patch(patches.FancyBboxPatch((0.05, 0.08), 0.42, 0.38, boxstyle="round,pad=0.02", 
                                        edgecolor='#f472b6', facecolor='#fdf2f8', linewidth=1.5))
    ax.text(0.26, 0.42, "3. CĂN CHỈNH NGANG & DỌC (ALIGNMENTS)", 
            ha='center', va='center', fontsize=12, fontweight='bold', color='#9d174d')
    align_info = [
        "• text-align: left | center | right (Căn ngang):",
        "  - th mặc định căn giữa, thường đổi thành left để dễ đọc.",
        "  - Các cột số liệu (tiền, tuổi, số lượng) nên căn right.",
        "• vertical-align: top | middle | bottom (Căn dọc):",
        "  - Mặc định các ô bảng căn giữa theo chiều dọc (middle).",
        "  - Dùng vertical-align: bottom để ép văn bản sát đáy ô.",
        "  - Cú pháp: td { vertical-align: bottom; height: 80px; }"
    ]
    for idx, t in enumerate(align_info):
        ax.text(0.08, 0.35 - idx * 0.05, t, fontsize=9.2, color='#1e293b')

    # 4. Padding, Colors & UI/UX Best Practices
    ax.add_patch(patches.FancyBboxPatch((0.53, 0.08), 0.42, 0.38, boxstyle="round,pad=0.02", 
                                        edgecolor='#34d399', facecolor='#f0fdf4', linewidth=1.5))
    ax.text(0.74, 0.42, "4. PADDING, MÀU SẮC & CHUẨN UI/UX", 
            ha='center', va='center', fontsize=12, fontweight='bold', color='#047857')
    pad_info = [
        "• padding: Khoảng đệm giữa nội dung ô và đường viền.",
        "  Không dùng margin trên <td>/<th> (không có tác dụng).",
        "• Phối màu phân cấp (Visual Hierarchy):",
        "  - Header tối #333 chữ trắng hoặc gradient xanh đậm.",
        "  - Dòng dữ liệu xám nhạt #f2f2f2 hoặc kẻ sọc zebra.",
        "• Zebra Striping & Hover:",
        "  - tbody tr:nth-child(even) { background: #f8fafc; }",
        "  - tbody tr:hover td { background: #eef2ff; }"
    ]
    for idx, t in enumerate(pad_info):
        ax.text(0.56, 0.35 - idx * 0.05, t, fontsize=9.2, color='#1e293b')

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    plt.tight_layout()
    out_path = os.path.join(output_dir, "css_table_properties_diagram.png")
    plt.savefig(out_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Generated {out_path}")

if __name__ == "__main__":
    generate_browser_mockup()
    generate_properties_diagram()
    print("All CSS table diagrams created successfully!")
