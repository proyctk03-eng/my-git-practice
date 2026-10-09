import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image, ImageDraw, ImageFont
import os

output_dir = r"C:\Users\dathao\.gemini\antigravity-ide\scratch\thuc-hanh-trang-web-ca-nhan-css"
os.makedirs(output_dir, exist_ok=True)

# -------------------------------------------------------------------
# 1. BROWSER PORTFOLIO SCREENSHOT MOCKUP
# -------------------------------------------------------------------
def generate_browser_mockup():
    width = 1350
    height = 1000
    img = Image.new('RGB', (width, height), color='#f5f5f5')
    draw = ImageDraw.Draw(img)

    # Browser Header bar
    draw.rectangle([0, 0, width, 44], fill='#1e293b')
    # Window controls
    draw.ellipse([20, 16, 32, 28], fill='#ef4444')
    draw.ellipse([40, 16, 52, 28], fill='#f59e0b')
    draw.ellipse([60, 16, 72, 28], fill='#10b981')

    # Browser Tab
    draw.rounded_rectangle([90, 8, 480, 44], radius=6, fill='#334155')
    draw.text((115, 16), "Trang Web Ca Nhan - Nguyen Van A", fill='#ffffff')

    # Address bar
    draw.rectangle([0, 44, width, 88], fill='#ffffff')
    draw.line([0, 88, width, 88], fill='#cbd5e1', width=1)
    draw.rounded_rectangle([80, 52, width - 80, 80], radius=8, fill='#f8fafc', outline='#e2e8f0', width=1)
    draw.text((105, 59), "https://proyctk03-eng.github.io/thuc-hanh-trang-web-ca-nhan-css/index.html", fill='#475569')

    # Header Green Banner (background-color: #4CAF50)
    draw.rectangle([0, 89, width, 185], fill='#4CAF50')
    draw.rounded_rectangle([520, 100, 830, 122], radius=11, fill='#388e3c')
    draw.text((545, 105), "PERSONAL PORTFOLIO • CODEGYM LAB", fill='#ffffff')
    draw.text((360, 135), "CHAO MUNG DEN VOI TRANG WEB CA NHAN CUA TOI", fill='#ffffff')

    # Central Container Wrapper (width: 860)
    cw_x1, cw_x2 = 245, 1105

    # Section 1: Profile & Avatar
    s1_y1, s1_y2 = 210, 430
    draw.rounded_rectangle([cw_x1, s1_y1, cw_x2, s1_y2], radius=12, fill='#ffffff', outline='#e0e0e0', width=1)
    # Circle Avatar with Green Border
    av_cx, av_cy = (cw_x1 + cw_x2) // 2, s1_y1 + 75
    draw.ellipse([av_cx - 50, av_cy - 50, av_cx + 50, av_cy + 50], fill='#3b82f6', outline='#4CAF50', width=4)
    # Draw simple avatar face
    draw.ellipse([av_cx - 20, av_cy - 30, av_cx + 20, av_cy + 5], fill='#fde047')
    draw.pieslice([av_cx - 35, av_cy + 5, av_cx + 35, av_cy + 55], 180, 360, fill='#4f46e5')

    draw.text((av_cx - 75, s1_y1 + 135), "GIOI THIEU BAN THAN", fill='#2e7d32')
    draw.text((av_cx - 240, s1_y1 + 165), "Xin chao! Toi la Nguyen Van A, mot lap trinh vien yeu thich cong nghe.", fill='#1e293b')
    draw.text((av_cx - 280, s1_y1 + 190), "Hien tai toi dang rèn luyen ky nang lap trinh web Front-end voi HTML5, CSS3 va JavaScript.", fill='#64748b')

    # Section 2: Hobbies & Goals in 2 Columns
    s2_y1, s2_y2 = 450, 680
    # Left: Hobbies (ul, list-style-type: square)
    hb_x1, hb_x2 = cw_x1, cw_x1 + 420
    draw.rounded_rectangle([hb_x1, s2_y1, hb_x2, s2_y2], radius=12, fill='#ffffff', outline='#e0e0e0', width=1)
    draw.text((hb_x1 + 160, s2_y1 + 20), "SO THICH", fill='#2e7d32')
    # Square list box
    draw.rounded_rectangle([hb_x1 + 40, s2_y1 + 55, hb_x2 - 40, s2_y2 - 25], radius=8, fill='#f9fbf9', outline='#4CAF50', width=1)
    hobbies = ["Doc sach cong nghe & kinh doanh", "Choi the thao (Bong da, chay bo)", "Lap trinh ung dung web mini", "Du lich kham pha van hoa"]
    for i, h in enumerate(hobbies):
        hy = s2_y1 + 75 + i * 32
        draw.rectangle([hb_x1 + 60, hy + 4, hb_x1 + 68, hy + 12], fill='#4CAF50')
        draw.text((hb_x1 + 80, hy), h, fill='#333333')

    # Right: Goals
    gl_x1, gl_x2 = cw_x1 + 440, cw_x2
    draw.rounded_rectangle([gl_x1, s2_y1, gl_x2, s2_y2], radius=12, fill='#ffffff', outline='#e0e0e0', width=1)
    draw.text((gl_x1 + 140, s2_y1 + 20), "MUC TIEU HOC TAP", fill='#2e7d32')
    draw.rounded_rectangle([gl_x1 + 30, s2_y1 + 55, gl_x2 - 30, s2_y1 + 115], radius=6, fill='#e8f5e9')
    draw.text((gl_x1 + 40, s2_y1 + 65), "\"Toi muon tro thanh mot lap trinh vien chuyen nghiep,", fill='#2e7d32')
    draw.text((gl_x1 + 40, s2_y1 + 88), "xay dung cac san pham huu ich phuc vu cong dong.\"", fill='#2e7d32')

    draw.rounded_rectangle([gl_x1 + 30, s2_y1 + 130, gl_x2 - 30, s2_y1 + 168], radius=6, fill='#f8fafc', outline='#e2e8f0')
    draw.text((gl_x1 + 45, s2_y1 + 140), "• Ngan han: Lam chu HTML5, CSS3, JavaScript ES6+", fill='#475569')

    draw.rounded_rectangle([gl_x1 + 30, s2_y1 + 178, gl_x2 - 30, s2_y1 + 215], radius=6, fill='#f8fafc', outline='#e2e8f0')
    draw.text((gl_x1 + 45, s2_y1 + 188), "• Dai han: Tro thanh Full-stack Engineer chuyen nghiep", fill='#475569')

    # Section 3: Footer & Contact Table (background-color: #ddd)
    f_y1, f_y2 = 705, 960
    draw.rectangle([0, f_y1, width, f_y2], fill='#dddddd')
    draw.line([0, f_y1, width, f_y1], fill='#cccccc', width=1)
    draw.text((width // 2 - 90, f_y1 + 20), "THONG TIN LIEN HE", fill='#2e7d32')

    # Contact Table (width: 50%, margin: auto)
    tb_w = 540
    tb_x1 = (width - tb_w) // 2
    tb_x2 = tb_x1 + tb_w
    tb_y1 = f_y1 + 55

    draw.rectangle([tb_x1, tb_y1, tb_x2, tb_y1 + 120], fill='#ffffff', outline='#000000', width=1)
    draw.line([tb_x1, tb_y1 + 40, tb_x2, tb_y1 + 40], fill='#000000', width=1)
    draw.line([tb_x1, tb_y1 + 80, tb_x2, tb_y1 + 80], fill='#000000', width=1)
    draw.line([tb_x1 + 160, tb_y1, tb_x1 + 160, tb_y1 + 120], fill='#000000', width=1)

    # Row 1: Email
    draw.rectangle([tb_x1, tb_y1, tb_x1 + 160, tb_y1 + 40], fill='#4CAF50')
    draw.text((tb_x1 + 55, tb_y1 + 12), "Email", fill='#ffffff')
    draw.text((tb_x1 + 180, tb_y1 + 12), "nguyenvana@example.com", fill='#2e7d32')

    # Row 2: Facebook
    draw.rectangle([tb_x1, tb_y1 + 40, tb_x1 + 160, tb_y1 + 80], fill='#4CAF50')
    draw.text((tb_x1 + 45, tb_y1 + 52), "Facebook", fill='#ffffff')
    draw.text((tb_x1 + 180, tb_y1 + 52), "facebook.com/nguyenvana", fill='#2e7d32')

    # Row 3: GitHub
    draw.rectangle([tb_x1, tb_y1 + 80, tb_x1 + 160, tb_y1 + 120], fill='#4CAF50')
    draw.text((tb_x1 + 50, tb_y1 + 92), "GitHub", fill='#ffffff')
    draw.text((tb_x1 + 180, tb_y1 + 92), "github.com/proyctk03-eng", fill='#2e7d32')

    draw.text((width // 2 - 250, f_y1 + 200), "© 2026 Trang Web Ca Nhan - Nguyen Van A. Repository: proyctk03-eng/thuc-hanh-trang-web-ca-nhan-css", fill='#666666')

    out_path = os.path.join(output_dir, "browser_portfolio_screenshot.png")
    img.save(out_path)
    print(f"Generated {out_path}")

# -------------------------------------------------------------------
# 2. ARCHITECTURAL CSS PORTFOLIO STRUCTURE DIAGRAM
# -------------------------------------------------------------------
def generate_structure_diagram():
    fig, ax = plt.subplots(figsize=(14, 9), dpi=300)
    ax.set_facecolor('#ffffff')
    fig.patch.set_facecolor('#f8fafc')

    # Title
    ax.text(0.5, 0.96, "SƠ ĐỒ CẤU TRÚC TRANG WEB CÁ NHÂN & CÁC BỘ CHỌN CSS3", 
            ha='center', va='center', fontsize=15, fontweight='bold', color='#0f172a')
    ax.text(0.5, 0.92, "Minh họa phân cấp cây DOM, thuộc tính định kiểu (Box Model, Border, Background, Typography)", 
            ha='center', va='center', fontsize=11, color='#64748b', style='italic')

    # 4 Quadrants
    # 1. Header & Typography
    ax.add_patch(patches.FancyBboxPatch((0.05, 0.50), 0.42, 0.38, boxstyle="round,pad=0.02", 
                                        edgecolor='#4CAF50', facecolor='#e8f5e9', linewidth=1.5))
    ax.text(0.26, 0.84, "1. HEADER & TIÊU ĐỀ TRANG WEB", 
            ha='center', va='center', fontsize=12, fontweight='bold', color='#1b5e20')
    h_info = [
        "• Bộ chọn phần tử: header, h1, p",
        "• background-color: #4CAF50; (Xanh lá nhận diện)",
        "• color: white; (Tương phản cao chữ trắng trên nền tối)",
        "• padding: 20px / 30px; (Khoảng đệm thông thoáng)",
        "• font-family: 'Plus Jakarta Sans', Arial, sans-serif;",
        "• box-shadow tạo chiều sâu cho thanh tiêu đề chính."
    ]
    for idx, t in enumerate(h_info):
        ax.text(0.08, 0.77 - idx * 0.048, t, fontsize=9.2, color='#1e293b')

    # 2. Avatar & Profile
    ax.add_patch(patches.FancyBboxPatch((0.53, 0.50), 0.42, 0.38, boxstyle="round,pad=0.02", 
                                        edgecolor='#38bdf8', facecolor='#f0f9ff', linewidth=1.5))
    ax.text(0.74, 0.84, "2. ẢNH ĐẠI DIỆN (.AVATAR) & PROFILE", 
            ha='center', va='center', fontsize=12, fontweight='bold', color='#0369a1')
    av_info = [
        "• Bộ chọn lớp: .avatar, .profile",
        "• border-radius: 50%; (Biến đổi ảnh vuông thành hình tròn)",
        "• border: 3px solid #4CAF50; (Đường viền màu xanh lá nổi bật)",
        "• width: 150px; height: 150px; (Kích thước ảnh chân dung)",
        "• margin: 20px; (Tạo khoảng cách với văn bản xung quanh)",
        "• object-fit: cover; (Bảo toàn tỷ lệ ảnh chân dung chuẩn)"
    ]
    for idx, t in enumerate(av_info):
        ax.text(0.56, 0.77 - idx * 0.048, t, fontsize=9.2, color='#1e293b')

    # 3. Hobbies (UL) & Goals
    ax.add_patch(patches.FancyBboxPatch((0.05, 0.08), 0.42, 0.38, boxstyle="round,pad=0.02", 
                                        edgecolor='#f59e0b', facecolor='#fef3c7', linewidth=1.5))
    ax.text(0.26, 0.42, "3. DANH SÁCH SỞ THÍCH (UL) & MỤC TIÊU", 
            ha='center', va='center', fontsize=12, fontweight='bold', color='#b45309')
    hb_info = [
        "• list-style-type: square; (Đánh dấu bullet hình vuông)",
        "• text-align: left; (Văn bản căn trái dễ đọc)",
        "• display: inline-block; (Cho phép khối danh sách nằm gọn)",
        "• margin-top: 10px; (Tạo khoảng cách với tiêu đề 'Sở thích')",
        "• Phối hợp thẻ card có bo góc và đổ bóng nhẹ nhàng,",
        "  nâng tầm giao diện cá nhân so với HTML thô."
    ]
    for idx, t in enumerate(hb_info):
        ax.text(0.08, 0.35 - idx * 0.05, t, fontsize=9.2, color='#1e293b')

    # 4. Table & Footer
    ax.add_patch(patches.FancyBboxPatch((0.53, 0.08), 0.42, 0.38, boxstyle="round,pad=0.02", 
                                        edgecolor='#94a3b8', facecolor='#f1f5f9', linewidth=1.5))
    ax.text(0.74, 0.42, "4. BẢNG LIÊN HỆ (TABLE) & FOOTER", 
            ha='center', va='center', fontsize=12, fontweight='bold', color='#334155')
    tb_info = [
        "• table { width: 50%; margin: auto; } (Căn giữa trang web)",
        "• border-collapse: collapse; (Gộp viền liền kề thành 1 viền)",
        "• th, td { border: 1px solid black; padding: 10px; }",
        "• th { background-color: #4CAF50; color: white; }",
        "• footer { background-color: #ddd; padding: 20px; }",
        "• background-image: url('bg_pattern.png'); trên body."
    ]
    for idx, t in enumerate(tb_info):
        ax.text(0.56, 0.35 - idx * 0.05, t, fontsize=9.2, color='#1e293b')

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    plt.tight_layout()
    out_path = os.path.join(output_dir, "css_portfolio_structure_diagram.png")
    plt.savefig(out_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Generated {out_path}")

if __name__ == "__main__":
    generate_browser_mockup()
    generate_structure_diagram()
    print("All personal website diagrams created successfully!")
