import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image, ImageDraw, ImageFont
import os

output_dir = r"C:\Users\dathao\.gemini\antigravity-ide\scratch\bai-tap-form-dang-ky-nguoi-dung"
os.makedirs(output_dir, exist_ok=True)

# -------------------------------------------------------------------
# 1. BROWSER REGISTRATION FORM SCREENSHOT MOCKUP
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
    draw.rounded_rectangle([90, 8, 420, 44], radius=6, fill='#334155')
    draw.text((115, 16), "CodeGym - [Bai tap] Form dang ky nguoi dung", fill='#ffffff')

    # Address bar
    draw.rectangle([0, 44, width, 88], fill='#ffffff')
    draw.line([0, 88, width, 88], fill='#cbd5e1', width=1)
    draw.rounded_rectangle([80, 52, width - 80, 80], radius=8, fill='#f8fafc', outline='#e2e8f0', width=1)
    draw.text((105, 59), "https://proyctk03-eng.github.io/bai-tap-form-dang-ky-nguoi-dung/index.html", fill='#475569')

    # Page Header Banner
    draw.rectangle([0, 89, width, 180], fill='#ffffff')
    draw.text((450, 105), "[BAI TAP] TAO GIAO DIEN FORM DANG KY NGUOI DUNG", fill='#0f172a')
    draw.rounded_rectangle([480, 132, 870, 160], radius=14, fill='#eff6ff', outline='#bfdbfe')
    draw.text((500, 140), "PHUONG THUC: POST  |  ENDPOINT: register.php", fill='#2563eb')
    draw.line([0, 180, width, 180], fill='#e2e8f0', width=1)

    # ------------------ CỘT 1: FORM CARD ------------------
    f1_x1, f1_y1, f1_x2, f1_y2 = 70, 210, 680, 870
    draw.rounded_rectangle([f1_x1, f1_y1, f1_x2, f1_y2], radius=16, fill='#ffffff', outline='#cbd5e1', width=2)

    # Header Form
    draw.text((f1_x1+25, f1_y1+24), "Dang ky nguoi dung", fill='#0f172a')
    draw.text((f1_x1+25, f1_y1+50), "Dien thong tin de gui qua HTTP POST len CodeGym Server", fill='#64748b')

    # Action badge
    draw.rounded_rectangle([f1_x1+25, f1_y1+78, f1_x2-25, f1_y1+114], radius=6, fill='#f8fafc', outline='#e2e8f0', width=1)
    draw.rectangle([f1_x1+35, f1_y1+85, f1_x1+85, f1_y1+107], fill='#2563eb')
    draw.text((f1_x1+44, f1_y1+89), "POST", fill='#ffffff')
    draw.text((f1_x1+95, f1_y1+89), "http://demo.codegym.vn/6/registration_form/register.php", fill='#0284c7')

    # 1. Field name
    draw.text((f1_x1+25, f1_y1+135), "Ho va ten (name=\"name\") *", fill='#334155')
    draw.rounded_rectangle([f1_x1+25, f1_y1+158, f1_x2-25, f1_y1+202], radius=8, fill='#ffffff', outline='#94a3b8', width=1)
    draw.text((f1_x1+40, f1_y1+172), "Nguyen Tuan Dat", fill='#0f172a')

    # 2. Field email
    draw.text((f1_x1+25, f1_y1+225), "Dia chi Email (name=\"email\") *", fill='#334155')
    draw.rounded_rectangle([f1_x1+25, f1_y1+248, f1_x2-25, f1_y1+292], radius=8, fill='#ffffff', outline='#94a3b8', width=1)
    draw.text((f1_x1+40, f1_y1+262), "proyctk03@gmail.com", fill='#0f172a')

    # 3. Field phone
    draw.text((f1_x1+25, f1_y1+315), "So dien thoai (name=\"phone\") *", fill='#334155')
    draw.rounded_rectangle([f1_x1+25, f1_y1+338, f1_x2-25, f1_y1+382], radius=8, fill='#ffffff', outline='#94a3b8', width=1)
    draw.text((f1_x1+40, f1_y1+352), "0988 123 456", fill='#0f172a')

    # 4. Field gender (radio)
    draw.text((f1_x1+25, f1_y1+405), "Gioi tinh (radio name=\"gender\") *", fill='#334155')
    # Radio Nam checked
    draw.rounded_rectangle([f1_x1+25, f1_y1+428, f1_x1+280, f1_y1+472], radius=8, fill='#eff6ff', outline='#2563eb', width=2)
    draw.ellipse([f1_x1+45, f1_y1+442, f1_x1+61, f1_y1+458], fill='#2563eb')
    draw.text((f1_x1+75, f1_y1+442), "(*) Nam", fill='#1e293b')
    # Radio Nu
    draw.rounded_rectangle([f1_x1+305, f1_y1+428, f1_x2-25, f1_y1+472], radius=8, fill='#f8fafc', outline='#cbd5e1', width=1)
    draw.ellipse([f1_x1+325, f1_y1+442, f1_x1+341, f1_y1+458], fill='#ffffff', outline='#94a3b8')
    draw.text((f1_x1+355, f1_y1+442), "( ) Nu", fill='#64748b')

    # 5. Submit Button
    draw.rounded_rectangle([f1_x1+25, f1_y1+505, f1_x2-25, f1_y1+560], radius=8, fill='#2563eb')
    draw.text((f1_x1+240, f1_y1+523), "Dang ky nguoi dung ->", fill='#ffffff')

    # ------------------ CỘT 2: HTTP POST INSPECTOR ------------------
    f2_x1, f2_y1, f2_x2, f2_y2 = 730, 210, 1280, 870
    draw.rounded_rectangle([f2_x1, f2_y1, f2_x2, f2_y2], radius=16, fill='#ffffff', outline='#cbd5e1', width=2)

    # Header Inspector
    draw.text((f2_x1+25, f2_y1+24), "HTTP POST Payload Inspector", fill='#0f172a')
    draw.text((f2_x1+25, f2_y1+50), "Goi tin du lieu duoc gui an trong HTTP Request Body", fill='#64748b')

    # Dark Terminal Box
    draw.rounded_rectangle([f2_x1+25, f2_y1+85, f2_x2-25, f2_y1+290], radius=8, fill='#0f172a')
    draw.text((f2_x1+40, f2_y1+100), "POST /6/registration_form/register.php HTTP/1.1", fill='#38bdf8')
    draw.text((f2_x1+40, f2_y1+125), "Host: demo.codegym.vn", fill='#94a3b8')
    draw.text((f2_x1+40, f2_y1+150), "Content-Type: application/x-www-form-urlencoded", fill='#f59e0b')
    draw.text((f2_x1+40, f2_y1+175), "Content-Length: 104", fill='#94a3b8')
    draw.text((f2_x1+40, f2_y1+205), "// REQUEST BODY (PAYLOAD):", fill='#10b981')
    draw.text((f2_x1+40, f2_y1+230), "name=Nguyen+Tuan+Dat&email=proyctk03%40gmail.com", fill='#e2e8f0')
    draw.text((f2_x1+40, f2_y1+255), "&phone=0988123456&gender=Nam", fill='#e2e8f0')

    # Table Mapping
    draw.text((f2_x1+25, f2_y1+315), "Bang anh xa thuoc tinh name -> Gia tri gui len:", fill='#1e293b')

    # Table Header
    draw.rectangle([f2_x1+25, f2_y1+345, f2_x2-25, f2_y1+380], fill='#f8fafc', outline='#e2e8f0')
    draw.text((f2_x1+40, f2_y1+355), "Thuoc tinh (name)", fill='#475569')
    draw.text((f2_x1+200, f2_y1+355), "Kieu the HTML", fill='#475569')
    draw.text((f2_x1+350, f2_y1+355), "Gia tri (value)", fill='#475569')

    # Rows
    rows = [
        ("name", "input type=\"text\"", "Nguyen Tuan Dat"),
        ("email", "input type=\"email\"", "proyctk03@gmail.com"),
        ("phone", "input type=\"tel\"", "0988123456"),
        ("gender", "input type=\"radio\"", "Nam")
    ]
    cur_y = f2_y1 + 380
    for key, itype, val in rows:
        draw.rectangle([f2_x1+25, cur_y, f2_x2-25, cur_y+35], fill='#ffffff', outline='#f1f5f9')
        draw.text((f2_x1+40, cur_y+10), key, fill='#2563eb')
        draw.text((f2_x1+200, cur_y+10), itype, fill='#64748b')
        draw.text((f2_x1+350, cur_y+10), val, fill='#0f172a')
        cur_y += 35

    # Server Response Box
    draw.rounded_rectangle([f2_x1+25, f2_y1+545, f2_x2-25, f2_y1+630], radius=8, fill='#f0fdf4', outline='#bbf7d0', width=1)
    draw.text((f2_x1+40, f2_y1+560), "[+] Server CodeGym Response (HTTP 200 OK):", fill='#166534')
    draw.text((f2_x1+40, f2_y1+585), "Dang ky thanh cong hoc vien: Nguyen Tuan Dat (Email: proyctk03@gmail.com)", fill='#15803d')

    # Save
    save_path = os.path.join(output_dir, "browser_register_form_screenshot.png")
    img.save(save_path, quality=95)
    print("Generated:", save_path)

# -------------------------------------------------------------------
# 2. HTTP POST ARCHITECTURE DIAGRAM
# -------------------------------------------------------------------
def generate_post_architecture_diagram():
    fig, ax = plt.subplots(figsize=(13, 8), dpi=150)
    ax.set_facecolor("#f8fafc")
    fig.patch.set_facecolor("#f8fafc")

    # Title
    ax.text(0.5, 0.94, "KIẾN TRÚC GIAO THỨC HTTP POST & BINDING THUỘC TÍNH FORM", 
            ha='center', va='center', fontsize=16, fontweight='bold', color='#0f172a')
    ax.text(0.5, 0.89, "Cơ chế đóng gói dữ liệu trong HTTP Request Body và tiếp nhận tại Server CodeGym (register.php)", 
            ha='center', va='center', fontsize=11, color='#64748b')

    # 1. Client Browser Box
    client_box = patches.FancyBboxPatch((0.05, 0.40), 0.28, 0.42, boxstyle="round,pad=0.02", 
                                        fc="#ffffff", ec="#2563eb", lw=2)
    ax.add_patch(client_box)
    ax.text(0.19, 0.78, "TRÌNH DUYỆT (CLIENT)", ha='center', fontsize=12, fontweight='bold', color='#2563eb')
    ax.text(0.19, 0.72, "<form action=\"register.php\"\n      method=\"POST\">", 
            ha='center', fontsize=9.5, family='monospace', color='#0369a1')
    ax.text(0.19, 0.58, "Các trường dữ liệu:\n• name: 'Nguyễn Tuấn Đạt'\n• email: 'proyctk03@gmail.com'\n• phone: '0988123456'\n• gender: 'Nam'", 
            ha='center', fontsize=9.5, color='#334155')
    ax.text(0.19, 0.45, "Sự kiện: submit\n-> Serialize FormData", ha='center', fontsize=9, fontweight='bold', color='#1e293b')

    # Arrow Client -> HTTP Request
    ax.annotate("", xy=(0.40, 0.61), xytext=(0.34, 0.61),
                arrowprops=dict(arrowstyle="->", lw=2.5, color="#2563eb"))

    # 2. HTTP Request Packet Box
    packet_box = patches.FancyBboxPatch((0.41, 0.38), 0.28, 0.46, boxstyle="round,pad=0.02", 
                                        fc="#ffffff", ec="#f59e0b", lw=2)
    ax.add_patch(packet_box)
    ax.text(0.55, 0.80, "GÓI TIN HTTP POST", ha='center', fontsize=12, fontweight='bold', color='#d97706')
    ax.text(0.55, 0.74, "Headers:\nPOST /6/.../register.php\nContent-Type:\napplication/x-www-form-urlencoded", 
            ha='center', fontsize=8.8, family='monospace', color='#b45309')
    
    # Body separator
    body_box = patches.FancyBboxPatch((0.43, 0.41), 0.24, 0.20, boxstyle="round,pad=0.015", 
                                       fc="#0f172a", ec="#334155", lw=1)
    ax.add_patch(body_box)
    ax.text(0.55, 0.57, "HTTP REQUEST BODY:", ha='center', fontsize=8.5, fontweight='bold', color='#38bdf8')
    ax.text(0.55, 0.48, "name=...&email=...\n&phone=...&gender=...", 
            ha='center', fontsize=8.5, family='monospace', color='#ffffff')

    # Arrow HTTP Request -> Server
    ax.annotate("", xy=(0.76, 0.61), xytext=(0.70, 0.61),
                arrowprops=dict(arrowstyle="->", lw=2.5, color="#10b981"))

    # 3. Server Box
    server_box = patches.FancyBboxPatch((0.77, 0.40), 0.18, 0.42, boxstyle="round,pad=0.02", 
                                        fc="#ffffff", ec="#10b981", lw=2)
    ax.add_patch(server_box)
    ax.text(0.86, 0.78, "MÁY CHỦ (SERVER)", ha='center', fontsize=12, fontweight='bold', color='#059669')
    ax.text(0.86, 0.72, "register.php", ha='center', fontsize=10, family='monospace', color='#047857')
    ax.text(0.86, 0.58, "Đọc mảng $_POST:\n$name = $_POST['name'];\n$email = $_POST['email'];\n$phone = $_POST['phone'];\n$gender = $_POST['gender'];", 
            ha='center', fontsize=8.5, family='monospace', color='#1e293b')
    ax.text(0.86, 0.45, "Lưu CSDL & Phản hồi\nHTTP 200 OK", ha='center', fontsize=9, fontweight='bold', color='#047857')

    # Comparison Table at bottom
    cmp_box = patches.FancyBboxPatch((0.05, 0.08), 0.90, 0.24, boxstyle="round,pad=0.02", 
                                     fc="#f1f5f9", ec="#cbd5e1", lw=1.5)
    ax.add_patch(cmp_box)
    ax.text(0.5, 0.27, "SO SÁNH: VÌ SAO FORM ĐĂNG KÝ PHẢI DÙNG PHƯƠNG THỨC POST?", 
            ha='center', fontsize=11, fontweight='bold', color='#0f172a')

    # GET column
    ax.text(0.27, 0.22, "[X] Phuong thuc GET (Khong phu hop dang ky)", fontsize=9.5, fontweight='bold', color='#dc2626')
    ax.text(0.27, 0.18, "• Du lieu lo toan bo tren thanh URL: ?name=...&email=...&phone=...", fontsize=8.5, color='#334155')
    ax.text(0.27, 0.14, "• Bi luu lai trong lich su duyet web va server log -> Rui ro bao mat", fontsize=8.5, color='#64748b')
    ax.text(0.27, 0.10, "• Gioi han kich thuoc khoang 2048 ky tu", fontsize=8.5, color='#64748b')

    # POST column
    ax.text(0.73, 0.22, "[V] Phuong thuc POST (Bat buoc theo de bai)", fontsize=9.5, fontweight='bold', color='#16a34a')
    ax.text(0.73, 0.18, "• Du lieu gui an trong HTTP Request Body, khong hien thi tren URL", fontsize=8.5, color='#334155')
    ax.text(0.73, 0.14, "• Bao ve quyen rieng tu nguoi dung, an toan cho so dien thoai & email", fontsize=8.5, color='#64748b')
    ax.text(0.73, 0.10, "• Khong gioi han kich thuoc, tieu chuan cho bieu mau tao moi (Create)", fontsize=8.5, color='#64748b')

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    plt.tight_layout()
    save_path = os.path.join(output_dir, "http_post_architecture_diagram.png")
    plt.savefig(save_path, dpi=200, bbox_inches='tight')
    plt.close()
    print("Generated:", save_path)

# -------------------------------------------------------------------
# 3. FORM FIELDS MAPPING DIAGRAM
# -------------------------------------------------------------------
def generate_fields_mapping_diagram():
    fig, ax = plt.subplots(figsize=(12, 7), dpi=150)
    ax.set_facecolor("#f8fafc")
    fig.patch.set_facecolor("#f8fafc")

    # Title
    ax.text(0.5, 0.93, "BẢNG ÁNH XẠ THUỘC TÍNH FORM ĐĂNG KÝ VÀO BACKEND SERVER", 
            ha='center', va='center', fontsize=15, fontweight='bold', color='#0f172a')
    ax.text(0.5, 0.88, "Quy tắc định danh khóa dữ liệu chính xác theo yêu cầu đề bài CodeGym", 
            ha='center', va='center', fontsize=11, color='#64748b')

    fields = [
        {"ui": "1. Họ và tên", "tag": "<input type=\"text\">", "name": "name", "desc": "Bắt buộc (required), nhận họ tên đầy đủ", "server": "$_POST['name']"},
        {"ui": "2. Địa chỉ Email", "tag": "<input type=\"email\">", "name": "email", "desc": "Kiểm tra định dạng email hợp lệ RFC", "server": "$_POST['email']"},
        {"ui": "3. Số điện thoại", "tag": "<input type=\"tel\">", "name": "phone", "desc": "Pattern regex 10-11 số", "server": "$_POST['phone']"},
        {"ui": "4. Giới tính", "tag": "<input type=\"radio\">", "name": "gender", "desc": "Nhóm Radio: Nam hoặc Nữ", "server": "$_POST['gender']"}
    ]

    y_start = 0.72
    for i, f in enumerate(fields):
        y = y_start - i * 0.17
        
        # UI Box
        box_ui = patches.FancyBboxPatch((0.06, y), 0.28, 0.13, boxstyle="round,pad=0.015", 
                                        fc="#ffffff", ec="#2563eb", lw=1.5)
        ax.add_patch(box_ui)
        ax.text(0.08, y + 0.08, f['ui'], fontsize=10.5, fontweight='bold', color='#0f172a')
        ax.text(0.08, y + 0.03, f['tag'], fontsize=9, family='monospace', color='#0284c7')

        # Arrow UI -> Name attribute
        ax.annotate("", xy=(0.42, y + 0.065), xytext=(0.35, y + 0.065),
                    arrowprops=dict(arrowstyle="->", lw=2, color="#64748b"))

        # Name Attribute Box
        box_name = patches.FancyBboxPatch((0.43, y), 0.22, 0.13, boxstyle="round,pad=0.015", 
                                          fc="#eff6ff", ec="#3b82f6", lw=1.5)
        ax.add_patch(box_name)
        ax.text(0.54, y + 0.08, f"name=\"{f['name']}\"", ha='center', fontsize=11, fontweight='bold', family='monospace', color='#1d4ed8')
        ax.text(0.54, y + 0.03, f['desc'], ha='center', fontsize=8, color='#64748b')

        # Arrow Name -> Server variable
        ax.annotate("", xy=(0.73, y + 0.065), xytext=(0.66, y + 0.065),
                    arrowprops=dict(arrowstyle="->", lw=2, color="#10b981"))

        # Server Box
        box_srv = patches.FancyBboxPatch((0.74, y), 0.20, 0.13, boxstyle="round,pad=0.015", 
                                         fc="#f0fdf4", ec="#10b981", lw=1.5)
        ax.add_patch(box_srv)
        ax.text(0.84, y + 0.08, f['server'], ha='center', fontsize=10.5, fontweight='bold', family='monospace', color='#059669')
        ax.text(0.84, y + 0.03, "PHP Backend Variable", ha='center', fontsize=8, color='#047857')

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    plt.tight_layout()
    save_path = os.path.join(output_dir, "form_fields_mapping_diagram.png")
    plt.savefig(save_path, dpi=200, bbox_inches='tight')
    plt.close()
    print("Generated:", save_path)

if __name__ == "__main__":
    generate_browser_mockup()
    generate_post_architecture_diagram()
    generate_fields_mapping_diagram()
    print("All registration diagrams generated successfully!")
