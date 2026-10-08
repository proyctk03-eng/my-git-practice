import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image, ImageDraw, ImageFont
import os

output_dir = r"C:\Users\dathao\.gemini\antigravity-ide\scratch\bai-tap-tao-bang-danh-sach-san-pham"
os.makedirs(output_dir, exist_ok=True)

# -------------------------------------------------------------------
# 1. BROWSER PRODUCT TABLE SCREENSHOT MOCKUP
# -------------------------------------------------------------------
def generate_browser_mockup():
    width = 1350
    height = 920
    img = Image.new('RGB', (width, height), color='#f1f5f9')
    draw = ImageDraw.Draw(img)

    # Browser Header bar
    draw.rectangle([0, 0, width, 44], fill='#1e293b')
    # Window controls (red, yellow, green)
    draw.ellipse([20, 16, 32, 28], fill='#ef4444')
    draw.ellipse([40, 16, 52, 28], fill='#f59e0b')
    draw.ellipse([60, 16, 72, 28], fill='#10b981')

    # Browser Tab
    draw.rounded_rectangle([90, 8, 450, 44], radius=6, fill='#334155')
    draw.text((115, 16), "CodeGym - Danh sach san pham trong HTML", fill='#ffffff')

    # Address bar
    draw.rectangle([0, 44, width, 88], fill='#ffffff')
    draw.line([0, 88, width, 88], fill='#cbd5e1', width=1)
    draw.rounded_rectangle([80, 52, width - 80, 80], radius=8, fill='#f8fafc', outline='#e2e8f0', width=1)
    draw.text((105, 59), "https://proyctk03-eng.github.io/bai-tap-tao-bang-danh-sach-san-pham/index.html", fill='#475569')

    # Page Header Banner
    draw.rectangle([0, 89, width, 185], fill='#ffffff')
    draw.text((500, 105), "DANH SACH SAN PHAM", fill='#0f172a')
    draw.rounded_rectangle([520, 135, 830, 162], radius=14, fill='#f0f9ff', outline='#bae6fd')
    draw.text((540, 142), "BANG HTML5: TABLE, TR, TH, TD", fill='#0284c7')
    draw.line([0, 185, width, 185], fill='#e2e8f0', width=1)

    # Card Table Box
    c_x1, c_y1, c_x2, c_y2 = 120, 215, 1230, 850
    draw.rounded_rectangle([c_x1, c_y1, c_x2, c_y2], radius=16, fill='#ffffff', outline='#cbd5e1', width=2)

    # Search Toolbar
    draw.rounded_rectangle([c_x1+25, c_y1+20, c_x1+380, c_y1+58], radius=8, fill='#f8fafc', outline='#cbd5e1', width=1)
    draw.text((c_x1+40, c_y1+30), "Tim kiem ten san pham...", fill='#64748b')
    draw.text((c_x2-260, c_y1+30), "Hien thi: 5 san pham trong kho", fill='#0f172a')

    # Table Header Row
    tbl_y = c_y1 + 75
    draw.rectangle([c_x1, tbl_y, c_x2, tbl_y+45], fill='#f8fafc', outline='#e2e8f0')
    draw.text((c_x1+40, tbl_y+14), "TEN SAN PHAM", fill='#475569')
    draw.text((c_x1+720, tbl_y+14), "GIA (VND)", fill='#475569')
    draw.text((c_x1+950, tbl_y+14), "SO LUONG", fill='#475569')

    # Products List
    products = [
        ("iPhone 16 Pro Max 256GB", "Dien thoai thong minh - Apple A18 Pro", "34.990.000 d", "15 chiec", True),
        ("MacBook Pro 14\" M3 Pro", "May tinh xach tay - 18GB RAM / 512GB SSD", "49.990.000 d", "8 chiec", False),
        ("iPad Pro 11\" M4 Ultra Retina", "May tinh bang - OLED Tandem / 256GB", "28.500.000 d", "20 chiec", True),
        ("AirPods Pro Gen 2 USB-C", "Tai nghe khong day - Chong on ANC", "5.990.000 d", "35 chiec", True),
        ("Apple Watch Series 10 GPS 46mm", "Dong ho thong minh - Vien nhom Jet Black", "10.990.000 d", "12 chiec", True),
    ]

    cur_row_y = tbl_y + 45
    for i, (name, cat, price, qty, in_stock) in enumerate(products):
        row_bg = '#ffffff' if i % 2 == 0 else '#fbfcfe'
        draw.rectangle([c_x1, cur_row_y, c_x2, cur_row_y+68], fill=row_bg, outline='#f1f5f9')

        # Product icon & name
        draw.rounded_rectangle([c_x1+30, cur_row_y+14, c_x1+70, cur_row_y+54], radius=8, fill='#f1f5f9', outline='#e2e8f0', width=1)
        draw.text((c_x1+44, cur_row_y+24), "#", fill='#0284c7')
        draw.text((c_x1+85, cur_row_y+16), name, fill='#0f172a')
        draw.text((c_x1+85, cur_row_y+38), cat, fill='#64748b')

        # Price
        draw.text((c_x1+720, cur_row_y+24), price, fill='#0369a1')

        # Quantity badge
        badge_bg = '#ecfdf5' if in_stock else '#fffbeb'
        badge_text = '#059669' if in_stock else '#d97706'
        draw.rounded_rectangle([c_x1+950, cur_row_y+20, c_x1+1040, cur_row_y+48], radius=14, fill=badge_bg)
        draw.text((c_x1+965, cur_row_y+26), qty, fill=badge_text)

        cur_row_y += 68

    # Table Footer (Tfoot)
    draw.rectangle([c_x1, cur_row_y, c_x2, cur_row_y+55], fill='#f8fafc', outline='#cbd5e1')
    draw.text((c_x1+40, cur_row_y+18), "Tong cong ton kho (5 mau san pham)", fill='#0f172a')
    draw.text((c_x1+720, cur_row_y+18), "130.460.000 d", fill='#0f172a')
    draw.text((c_x1+950, cur_row_y+18), "90 chiec", fill='#0f172a')

    # Footer note
    draw.text((c_x1+25, c_y2-35), "Cau truc HTML: <table> -> <thead>/<tbody>/<tfoot> -> <tr> -> <th>/<td>", fill='#64748b')

    # Save
    save_path = os.path.join(output_dir, "browser_product_table_screenshot.png")
    img.save(save_path, quality=95)
    print("Generated:", save_path)

# -------------------------------------------------------------------
# 2. HTML TABLE ARCHITECTURE DIAGRAM
# -------------------------------------------------------------------
def generate_table_architecture_diagram():
    fig, ax = plt.subplots(figsize=(13, 8), dpi=150)
    ax.set_facecolor("#f8fafc")
    fig.patch.set_facecolor("#f8fafc")

    # Title
    ax.text(0.5, 0.94, "KIẾN TRÚC BẢNG HTML VÀ PHÂN CẤP THẺ DỮ LIỆU", 
            ha='center', va='center', fontsize=16, fontweight='bold', color='#0f172a')
    ax.text(0.5, 0.89, "Mô hình phân tầng <table> -> <thead> / <tbody> / <tfoot> -> <tr> -> <th> / <td>", 
            ha='center', va='center', fontsize=11, color='#64748b')

    # Outer Table Box
    tbl_box = patches.FancyBboxPatch((0.06, 0.10), 0.88, 0.74, boxstyle="round,pad=0.02", 
                                     fc="#ffffff", ec="#0284c7", lw=2, linestyle='--')
    ax.add_patch(tbl_box)
    ax.text(0.09, 0.80, "<table border=\"1\">  [Phần tử gốc chứa toàn bộ bảng]", 
            fontsize=12, fontweight='bold', color='#0284c7', family='monospace')

    # Section 1: THEAD
    thead_box = patches.FancyBboxPatch((0.09, 0.58), 0.82, 0.18, boxstyle="round,pad=0.015", 
                                       fc="#eff6ff", ec="#3b82f6", lw=1.5)
    ax.add_patch(thead_box)
    ax.text(0.12, 0.71, "1. Tiêu đề bảng (<thead>):", fontsize=11, fontweight='bold', color='#1d4ed8')
    ax.text(0.12, 0.65, "<tr> [Hàng tiêu đề] -> Chứa các thẻ <th> (Table Header):", fontsize=10, color='#334155')
    ax.text(0.15, 0.60, "• <th>Tên sản phẩm</th>    • <th>Giá</th>    • <th>Số lượng</th>", 
            fontsize=10.5, fontweight='bold', color='#2563eb', family='monospace')

    # Section 2: TBODY
    tbody_box = patches.FancyBboxPatch((0.09, 0.28), 0.82, 0.27, boxstyle="round,pad=0.015", 
                                       fc="#f0fdf4", ec="#22c55e", lw=1.5)
    ax.add_patch(tbody_box)
    ax.text(0.12, 0.50, "2. Dữ liệu bảng (<tbody>):", fontsize=11, fontweight='bold', color='#15803d')
    ax.text(0.12, 0.44, "Chứa ít nhất 4 hàng dữ liệu <tr>, mỗi hàng gồm 3 ô dữ liệu <td> (Table Data):", fontsize=10, color='#334155')
    ax.text(0.15, 0.38, "• Hàng 1: <td>iPhone 16 Pro Max</td>  <td>34.990.000 đ</td>  <td>15</td>", 
            fontsize=9.5, color='#166534', family='monospace')
    ax.text(0.15, 0.34, "• Hàng 2: <td>MacBook Pro M3</td>      <td>49.990.000 đ</td>  <td>8</td>", 
            fontsize=9.5, color='#166534', family='monospace')
    ax.text(0.15, 0.30, "• Hàng 3 & 4: iPad Pro M4, AirPods Pro 2, Apple Watch Series 10...", 
            fontsize=9.5, color='#166534', family='monospace')

    # Section 3: TFOOT
    tfoot_box = patches.FancyBboxPatch((0.09, 0.13), 0.82, 0.12, boxstyle="round,pad=0.015", 
                                       fc="#fefce8", ec="#eab308", lw=1.5)
    ax.add_patch(tfoot_box)
    ax.text(0.12, 0.20, "3. Chân bảng (<tfoot>):", fontsize=11, fontweight='bold', color='#a16207')
    ax.text(0.12, 0.15, "<tr> -> <td>Tổng cộng tồn kho</td>  <td>130.460.000 đ</td>  <td>90 chiếc</td>", 
            fontsize=9.5, color='#854d0e', family='monospace')

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    plt.tight_layout()
    save_path = os.path.join(output_dir, "html_table_product_structure.png")
    plt.savefig(save_path, dpi=200, bbox_inches='tight')
    plt.close()
    print("Generated:", save_path)

if __name__ == "__main__":
    generate_browser_mockup()
    generate_table_architecture_diagram()
    print("All product table diagrams generated successfully!")
