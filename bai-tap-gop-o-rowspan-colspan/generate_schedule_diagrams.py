import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image, ImageDraw, ImageFont
import os

output_dir = r"C:\Users\dathao\.gemini\antigravity-ide\scratch\bai-tap-gop-o-rowspan-colspan"
os.makedirs(output_dir, exist_ok=True)

# -------------------------------------------------------------------
# 1. BROWSER SCHEDULE TABLE SCREENSHOT MOCKUP
# -------------------------------------------------------------------
def generate_browser_mockup():
    width = 1350
    height = 960
    img = Image.new('RGB', (width, height), color='#f8fafc')
    draw = ImageDraw.Draw(img)

    # Browser Header bar
    draw.rectangle([0, 0, width, 44], fill='#1e293b')
    # Window controls (red, yellow, green)
    draw.ellipse([20, 16, 32, 28], fill='#ef4444')
    draw.ellipse([40, 16, 52, 28], fill='#f59e0b')
    draw.ellipse([60, 16, 72, 28], fill='#10b981')

    # Browser Tab
    draw.rounded_rectangle([90, 8, 480, 44], radius=6, fill='#334155')
    draw.text((115, 16), "CodeGym - Lich hop cong ty (rowspan & colspan)", fill='#ffffff')

    # Address bar
    draw.rectangle([0, 44, width, 88], fill='#ffffff')
    draw.line([0, 88, width, 88], fill='#cbd5e1', width=1)
    draw.rounded_rectangle([80, 52, width - 80, 80], radius=8, fill='#f8fafc', outline='#e2e8f0', width=1)
    draw.text((105, 59), "https://proyctk03-eng.github.io/bai-tap-gop-o-rowspan-colspan/index.html", fill='#475569')

    # Page Header Banner
    draw.rectangle([0, 89, width, 185], fill='#ffffff')
    draw.text((530, 105), "LICH HOP CONG TY", fill='#0f172a')
    draw.rounded_rectangle([480, 135, 870, 162], radius=14, fill='#eef2ff', outline='#c7d2fe')
    draw.text((500, 142), "QUAN LY LICH HOP - ROWSPAN & COLSPAN HTML5", fill='#4f46e5')
    draw.line([0, 185, width, 185], fill='#e2e8f0', width=1)

    # 4 Stats Cards
    card_w = 260
    gap = 20
    start_x = 120
    y_stat = 205
    stats = [
        ("📅 5 Ngay", "Tu Thu Hai den Thu Sau", '#e0f2fe', '#0284c7'),
        ("👥 9 Cuoc hop", "Tong cac phien lam viec", '#f3e8ff', '#7c3aed'),
        ("⏱️ 2 Su kien dai", "Hop ca ngay (Colspan)", '#d1fae5', '#059669'),
        ("📌 3 Ngay kep", "Nhieu cuoc hop (Rowspan)", '#fef3c7', '#d97706'),
    ]
    for i, (title, sub, bg, txt_col) in enumerate(stats):
        cx = start_x + i * (card_w + gap)
        draw.rounded_rectangle([cx, y_stat, cx + card_w, y_stat + 68], radius=10, fill='#ffffff', outline='#cbd5e1', width=1)
        draw.rounded_rectangle([cx + 10, y_stat + 14, cx + 50, y_stat + 54], radius=8, fill=bg)
        draw.text((cx + 60, y_stat + 14), title, fill=txt_col)
        draw.text((cx + 60, y_stat + 38), sub, fill='#64748b')

    # Card Table Box
    c_x1, c_y1, c_x2, c_y2 = 120, 295, 1230, 890
    draw.rounded_rectangle([c_x1, c_y1, c_x2, c_y2], radius=16, fill='#ffffff', outline='#cbd5e1', width=2)

    # Table Top Bar
    draw.rectangle([c_x1, c_y1, c_x2, c_y1 + 48], fill='#1e293b')
    draw.text((c_x1 + 20, c_y1 + 15), "📋 BANG LICH HOP TUAN 42 (HTML TABLE WITH ROWSPAN & COLSPAN)", fill='#ffffff')
    draw.rounded_rectangle([c_x2 - 270, c_y1 + 10, c_x2 - 145, c_y1 + 38], radius=6, fill='#c084fc')
    draw.text((c_x2 - 260, c_y1 + 16), "ROWSPAN (Doc)", fill='#3b0764')
    draw.rounded_rectangle([c_x2 - 135, c_y1 + 10, c_x2 - 15, c_y1 + 38], radius=6, fill='#34d399')
    draw.text((c_x2 - 125, c_y1 + 16), "COLSPAN (Ngang)", fill='#064e3b')

    # Table Header Row
    th_y = c_y1 + 48
    draw.rectangle([c_x1, th_y, c_x2, th_y + 40], fill='#f1f5f9')
    draw.line([c_x1, th_y + 40, c_x2, th_y + 40], fill='#cbd5e1', width=2)
    draw.text((c_x1 + 25, th_y + 12), "NGAY", fill='#334155')
    draw.text((c_x1 + 240, th_y + 12), "GIO", fill='#334155')
    draw.text((c_x1 + 460, th_y + 12), "NOI DUNG CUOC HOP", fill='#334155')
    draw.line([c_x1 + 220, th_y, c_x1 + 220, c_y2 - 40], fill='#e2e8f0', width=1)
    draw.line([c_x1 + 440, th_y, c_x1 + 440, c_y2 - 40], fill='#e2e8f0', width=1)

    # Data Rows
    # Row 1: Thu Hai (Rowspan=2)
    r1_y = th_y + 40
    draw.rectangle([c_x1, r1_y, c_x1 + 220, r1_y + 96], fill='#faf5ff', outline='#c084fc', width=2)
    draw.text((c_x1 + 30, r1_y + 25), "Thu Hai (12/10)", fill='#1e293b')
    draw.rounded_rectangle([c_x1 + 30, r1_y + 50, c_x1 + 165, r1_y + 72], radius=4, fill='#7e22ce')
    draw.text((c_x1 + 38, r1_y + 54), "rowspan=\"2\"", fill='#ffffff')

    draw.text((c_x1 + 240, r1_y + 15), "08:30 - 10:00", fill='#475569')
    draw.text((c_x1 + 460, r1_y + 15), "Hop giao ban dau tuan toan cong ty (Hoi truong A)", fill='#0f172a')
    draw.line([c_x1 + 220, r1_y + 48, c_x2, r1_y + 48], fill='#e2e8f0', width=1)

    draw.text((c_x1 + 240, r1_y + 63), "14:00 - 15:30", fill='#475569')
    draw.text((c_x1 + 460, r1_y + 63), "Bao cao tien do du an ERP & Tu dong hoa (Phong 201)", fill='#0f172a')
    draw.line([c_x1, r1_y + 96, c_x2, r1_y + 96], fill='#cbd5e1', width=1)

    # Row 2: Thu Ba (Colspan=2)
    r2_y = r1_y + 96
    draw.rectangle([c_x1, r2_y, c_x1 + 220, r2_y + 64], fill='#ffffff')
    draw.text((c_x1 + 30, r2_y + 20), "Thu Ba (13/10)", fill='#1e293b')

    draw.rectangle([c_x1 + 220, r2_y, c_x2, r2_y + 64], fill='#f0fdf4', outline='#34d399', width=2)
    draw.rounded_rectangle([c_x1 + 240, r2_y + 10, c_x1 + 540, r2_y + 32], radius=4, fill='#047857')
    draw.text((c_x1 + 250, r2_y + 14), "colspan=\"2\" (Hop keo dai nhieu gio / Ca ngay)", fill='#ffffff')
    draw.text((c_x1 + 240, r2_y + 38), "08:00 - 17:00: Hoi thao dinh huong chien luoc cong nghe & Chuyen doi so 2026", fill='#065f46')
    draw.line([c_x1, r2_y + 64, c_x2, r2_y + 64], fill='#cbd5e1', width=1)

    # Row 3: Thu Tu (Rowspan=3)
    r3_y = r2_y + 64
    draw.rectangle([c_x1, r3_y, c_x1 + 220, r3_y + 144], fill='#faf5ff', outline='#c084fc', width=2)
    draw.text((c_x1 + 30, r3_y + 40), "Thu Tu (14/10)", fill='#1e293b')
    draw.rounded_rectangle([c_x1 + 30, r3_y + 70, c_x1 + 165, r3_y + 92], radius=4, fill='#7e22ce')
    draw.text((c_x1 + 38, r3_y + 74), "rowspan=\"3\"", fill='#ffffff')

    draw.text((c_x1 + 240, r3_y + 15), "09:00 - 10:30", fill='#475569')
    draw.text((c_x1 + 460, r3_y + 15), "Phong van ky thuat: Ung vien Senior Frontend Engineer (Phong 102)", fill='#0f172a')
    draw.line([c_x1 + 220, r3_y + 48, c_x2, r3_y + 48], fill='#e2e8f0', width=1)

    draw.text((c_x1 + 240, r3_y + 63), "11:00 - 12:00", fill='#475569')
    draw.text((c_x1 + 460, r3_y + 63), "Thong nhat quy chuan thiet ke UI/UX Design System (Google Meet)", fill='#0f172a')
    draw.line([c_x1 + 220, r3_y + 96, c_x2, r3_y + 96], fill='#e2e8f0', width=1)

    draw.text((c_x1 + 240, r3_y + 111), "15:00 - 16:30", fill='#475569')
    draw.text((c_x1 + 460, r3_y + 111), "Tap huan an toan thong tin mang & Bao mat du lieu ISO 27001", fill='#0f172a')
    draw.line([c_x1, r3_y + 144, c_x2, r3_y + 144], fill='#cbd5e1', width=1)

    # Row 4: Thu Sau (Colspan=2)
    r4_y = r3_y + 144
    draw.rectangle([c_x1, r4_y, c_x1 + 220, r4_y + 64], fill='#ffffff')
    draw.text((c_x1 + 30, r4_y + 20), "Thu Sau (16/10)", fill='#1e293b')

    draw.rectangle([c_x1 + 220, r4_y, c_x2, r4_y + 64], fill='#f0fdf4', outline='#34d399', width=2)
    draw.rounded_rectangle([c_x1 + 240, r4_y + 10, c_x1 + 540, r4_y + 32], radius=4, fill='#047857')
    draw.text((c_x1 + 250, r4_y + 14), "colspan=\"2\" (Hackathon keo dai ca ngay)", fill='#ffffff')
    draw.text((c_x1 + 240, r4_y + 38), "08:30 - 16:30: Ngay hoi Sang tao cong nghe & Lap trinh Hackathon AI 2026", fill='#065f46')
    draw.line([c_x1, r4_y + 64, c_x2, r4_y + 64], fill='#cbd5e1', width=1)

    # Footer note
    draw.rectangle([c_x1, c_y2 - 40, c_x2, c_y2], fill='#f8fafc')
    draw.text((c_x1 + 25, c_y2 - 28), "Ghi chu: Ap dung day du rowspan va colspan dung tieu chuan ky thuat W3C HTML5.", fill='#64748b')

    out_path = os.path.join(output_dir, "browser_schedule_table_screenshot.png")
    img.save(out_path)
    print(f"Generated {out_path}")

# -------------------------------------------------------------------
# 2. ARCHITECTURAL ROWSPAN & COLSPAN STRUCTURE DIAGRAM
# -------------------------------------------------------------------
def generate_table_structure_diagram():
    fig, ax = plt.subplots(figsize=(14, 9), dpi=300)
    ax.set_facecolor('#ffffff')
    fig.patch.set_facecolor('#f8fafc')

    # Title
    ax.text(0.5, 0.96, "SƠ ĐỒ CƠ CHẾ GỘP Ô: ROWSPAN VÀ COLSPAN TRONG BẢNG HTML", 
            ha='center', va='center', fontsize=16, fontweight='bold', color='#0f172a')
    ax.text(0.5, 0.92, "Minh họa phân bổ không gian ma trận lưới và quy tắc cân bằng số ô trên từng hàng <tr>", 
            ha='center', va='center', fontsize=11, color='#64748b', style='italic')

    # Left Column: ROWSPAN (Vertical span)
    ax.add_patch(patches.FancyBboxPatch((0.05, 0.48), 0.42, 0.40, boxstyle="round,pad=0.02", 
                                        edgecolor='#c084fc', facecolor='#faf5ff', linewidth=2))
    ax.text(0.26, 0.85, "1. ROWSPAN=\"N\" (GỘP HÀNG THEO CHIỀU DỌC)", 
            ha='center', va='center', fontsize=12, fontweight='bold', color='#7e22ce')
    ax.text(0.26, 0.81, "Ô chiếm n hàng dọc liên tiếp. Hàng sau bỏ qua thẻ <td> tương ứng.", 
            ha='center', va='center', fontsize=9.5, color='#475569')

    # Grid visual for Rowspan
    # Header
    ax.add_patch(patches.Rectangle((0.08, 0.72), 0.12, 0.06, facecolor='#e2e8f0', edgecolor='#94a3b8'))
    ax.text(0.14, 0.75, "Ngày", ha='center', va='center', fontsize=9, fontweight='bold')
    ax.add_patch(patches.Rectangle((0.21, 0.72), 0.11, 0.06, facecolor='#e2e8f0', edgecolor='#94a3b8'))
    ax.text(0.265, 0.75, "Giờ", ha='center', va='center', fontsize=9, fontweight='bold')
    ax.add_patch(patches.Rectangle((0.33, 0.72), 0.11, 0.06, facecolor='#e2e8f0', edgecolor='#94a3b8'))
    ax.text(0.385, 0.75, "Nội dung", ha='center', va='center', fontsize=9, fontweight='bold')

    # Merged Rowspan Box
    ax.add_patch(patches.Rectangle((0.08, 0.54), 0.12, 0.16, facecolor='#d8b4fe', edgecolor='#7e22ce', linewidth=2))
    ax.text(0.14, 0.63, "<td rowspan=\"2\">\nThứ Hai\n(2 hàng)", ha='center', va='center', fontsize=9, fontweight='bold', color='#3b0764')

    # Row 1 other cells
    ax.add_patch(patches.Rectangle((0.21, 0.63), 0.11, 0.07, facecolor='#ffffff', edgecolor='#cbd5e1'))
    ax.text(0.265, 0.665, "08:30", ha='center', va='center', fontsize=8.5)
    ax.add_patch(patches.Rectangle((0.33, 0.63), 0.11, 0.07, facecolor='#ffffff', edgecolor='#cbd5e1'))
    ax.text(0.385, 0.665, "Giao ban", ha='center', va='center', fontsize=8.5)

    # Row 2 other cells
    ax.add_patch(patches.Rectangle((0.21, 0.54), 0.11, 0.07, facecolor='#ffffff', edgecolor='#cbd5e1'))
    ax.text(0.265, 0.575, "14:00", ha='center', va='center', fontsize=8.5)
    ax.add_patch(patches.Rectangle((0.33, 0.54), 0.11, 0.07, facecolor='#ffffff', edgecolor='#cbd5e1'))
    ax.text(0.385, 0.575, "Báo cáo", ha='center', va='center', fontsize=8.5)

    # Right Column: COLSPAN (Horizontal span)
    ax.add_patch(patches.FancyBboxPatch((0.53, 0.48), 0.42, 0.40, boxstyle="round,pad=0.02", 
                                        edgecolor='#34d399', facecolor='#f0fdf4', linewidth=2))
    ax.text(0.74, 0.85, "2. COLSPAN=\"M\" (GỘP CỘT THEO CHIỀU NGANG)", 
            ha='center', va='center', fontsize=12, fontweight='bold', color='#047857')
    ax.text(0.74, 0.81, "Ô chiếm m cột ngang liên tiếp. Dùng cho cuộc họp kéo dài nhiều giờ.", 
            ha='center', va='center', fontsize=9.5, color='#475569')

    # Grid visual for Colspan
    # Header
    ax.add_patch(patches.Rectangle((0.56, 0.72), 0.11, 0.06, facecolor='#e2e8f0', edgecolor='#94a3b8'))
    ax.text(0.615, 0.75, "Ngày", ha='center', va='center', fontsize=9, fontweight='bold')
    ax.add_patch(patches.Rectangle((0.68, 0.72), 0.11, 0.06, facecolor='#e2e8f0', edgecolor='#94a3b8'))
    ax.text(0.735, 0.75, "Giờ", ha='center', va='center', fontsize=9, fontweight='bold')
    ax.add_patch(patches.Rectangle((0.80, 0.72), 0.12, 0.06, facecolor='#e2e8f0', edgecolor='#94a3b8'))
    ax.text(0.86, 0.75, "Nội dung", ha='center', va='center', fontsize=9, fontweight='bold')

    # Row 1 Colspan Box
    ax.add_patch(patches.Rectangle((0.56, 0.58), 0.11, 0.10, facecolor='#ffffff', edgecolor='#cbd5e1'))
    ax.text(0.615, 0.63, "Thứ Ba\n(1 ngày)", ha='center', va='center', fontsize=8.5)

    ax.add_patch(patches.Rectangle((0.68, 0.58), 0.24, 0.10, facecolor='#a7f3d0', edgecolor='#047857', linewidth=2))
    ax.text(0.80, 0.63, "<td colspan=\"2\">\n08:00 - 17:00: Hội thảo cả ngày (2 cột)", 
            ha='center', va='center', fontsize=9, fontweight='bold', color='#064e3b')

    # Bottom Formula & Rule Container
    ax.add_patch(patches.FancyBboxPatch((0.05, 0.05), 0.90, 0.38, boxstyle="round,pad=0.02", 
                                        edgecolor='#cbd5e1', facecolor='#ffffff', linewidth=1.5))
    ax.text(0.5, 0.39, "QUY TẮC BẢO TOÀN LƯỚI & TRÁNH LỖI LỆCH BẢNG TRONG THỰC TẾ", 
            ha='center', va='center', fontsize=12, fontweight='bold', color='#0f172a')

    rules = [
        "1. Nguyên tắc đếm cột: Mỗi hàng <tr> phải có tổng số ô (tính cả giá trị colspan và ô do rowspan chiếm) = Tổng số cột của bảng.",
        "2. Không tạo ô dư thừa: Khi hàng trước dùng rowspan=\"2\", hàng ngay dưới PHẢI giảm bớt 1 thẻ <td> ở đúng vị trí cột đó.",
        "3. Ngữ nghĩa bảng: Kết hợp các thẻ <thead>, <tbody>, <tfoot> để tăng tính chuẩn hóa, khả năng truy cập (A11y) và SEO.",
        "4. Tùy biến hiển thị: Sử dụng CSS border-collapse: collapse; để loại bỏ khoảng cách thừa giữa các đường viền ô."
    ]
    for idx, rule in enumerate(rules):
        ax.text(0.08, 0.32 - idx * 0.065, rule, fontsize=10, color='#334155', va='center')

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    plt.tight_layout()
    out_path = os.path.join(output_dir, "html_rowspan_colspan_diagram.png")
    plt.savefig(out_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Generated {out_path}")

if __name__ == "__main__":
    generate_browser_mockup()
    generate_table_structure_diagram()
    print("All schedule diagrams created successfully!")
