import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image, ImageDraw, ImageFont
import os

output_dir = r"C:\Users\dathao\.gemini\antigravity-ide\scratch\bai-tap-tao-form-don-gian"
os.makedirs(output_dir, exist_ok=True)

# -------------------------------------------------------------------
# 1. BROWSER RESULT SCREENSHOT MOCKUP
# -------------------------------------------------------------------
def generate_browser_mockup():
    width = 1400
    height = 1000
    img = Image.new('RGB', (width, height), color='#f1f5f9')
    draw = ImageDraw.Draw(img)

    # Browser Header bar
    draw.rectangle([0, 0, width, 44], fill='#1e293b')
    # Window controls (red, yellow, green dots)
    draw.ellipse([20, 16, 32, 28], fill='#ef4444')
    draw.ellipse([40, 16, 52, 28], fill='#f59e0b')
    draw.ellipse([60, 16, 72, 28], fill='#10b981')

    # Browser Tab
    draw.rounded_rectangle([90, 8, 380, 44], radius=6, fill='#334155')
    draw.text((115, 16), "CodeGym - [Bai tap] Tao form don gian", fill='#ffffff')

    # Address bar
    draw.rectangle([0, 44, width, 88], fill='#ffffff')
    draw.line([0, 88, width, 88], fill='#cbd5e1', width=1)
    draw.rounded_rectangle([80, 52, width - 80, 80], radius=8, fill='#f8fafc', outline='#e2e8f0', width=1)
    draw.text((105, 59), "https://proyctk03-eng.github.io/bai-tap-tao-form-don-gian/index.html", fill='#475569')

    # Page Hero Section
    draw.rectangle([0, 89, width, 185], fill='#ffffff')
    draw.text((500, 105), "[BAI TAP] TAO FORM DON GIAN & DANG KY HOC VIEN", fill='#0f172a')
    draw.rounded_rectangle([530, 135, 870, 165], radius=15, fill='#eff6ff', outline='#bfdbfe')
    draw.text((550, 142), "PHAN 1: FORM DON GIAN  |  PHAN 2: DANG KY HOC VIEN", fill='#2563eb')
    draw.line([0, 185, width, 185], fill='#e2e8f0', width=1)

    # ------------------ FORM 1 (LEFT COLUMN) ------------------
    f1_x1, f1_y1, f1_x2, f1_y2 = 60, 215, 660, 950
    draw.rounded_rectangle([f1_x1, f1_y1, f1_x2, f1_y2], radius=14, fill='#ffffff', outline='#cbd5e1', width=2)
    
    # Header Form 1
    draw.rounded_rectangle([f1_x1+20, f1_y1+20, f1_x1+200, f1_y1+48], radius=6, fill='#eff6ff')
    draw.text((f1_x1+30, f1_y1+26), "PHAN 1: FORM DON GIAN", fill='#2563eb')
    draw.text((f1_x1+20, f1_y1+60), "Bieu mau nhap thong tin co ban", fill='#0f172a')

    # Field 1: yourname
    draw.text((f1_x1+20, f1_y1+105), "Ho va ten (name=\"yourname\") *", fill='#334155')
    draw.rounded_rectangle([f1_x1+20, f1_y1+130, f1_x2-20, f1_y1+175], radius=8, fill='#ffffff', outline='#94a3b8')
    draw.text((f1_x1+35, f1_y1+145), "Nguyen Tuan Dat", fill='#0f172a')

    # Field 2: email
    draw.text((f1_x1+20, f1_y1+195), "Dia chi Email (name=\"email\") *", fill='#334155')
    draw.rounded_rectangle([f1_x1+20, f1_y1+220, f1_x2-20, f1_y1+265], radius=8, fill='#ffffff', outline='#94a3b8')
    draw.text((f1_x1+35, f1_y1+235), "proyctk03@gmail.com", fill='#0f172a')

    # Field 3: hobby
    draw.text((f1_x1+20, f1_y1+285), "So thich ca nhan (cung name=\"hobby\"):", fill='#334155')
    # Checkbox 1
    draw.rounded_rectangle([f1_x1+20, f1_y1+315, f1_x1+285, f1_y1+360], radius=8, fill='#eff6ff', outline='#3b82f6')
    draw.rectangle([f1_x1+35, f1_y1+328, f1_x1+53, f1_y1+346], fill='#2563eb')
    draw.text((f1_x1+65, f1_y1+328), "[v] The thao", fill='#1e293b')
    # Checkbox 2
    draw.rounded_rectangle([f1_x1+305, f1_y1+315, f1_x2-20, f1_y1+360], radius=8, fill='#f8fafc', outline='#cbd5e1')
    draw.rectangle([f1_x1+320, f1_y1+328, f1_x1+338, f1_y1+346], fill='#ffffff', outline='#94a3b8')
    draw.text((f1_x1+350, f1_y1+328), "[ ] Am nhac", fill='#64748b')
    # Checkbox 3
    draw.rounded_rectangle([f1_x1+20, f1_y1+375, f1_x1+285, f1_y1+420], radius=8, fill='#eff6ff', outline='#3b82f6')
    draw.rectangle([f1_x1+35, f1_y1+388, f1_x1+53, f1_y1+406], fill='#2563eb')
    draw.text((f1_x1+65, f1_y1+388), "[v] Doc sach", fill='#1e293b')
    # Checkbox 4
    draw.rounded_rectangle([f1_x1+305, f1_y1+375, f1_x2-20, f1_y1+420], radius=8, fill='#eff6ff', outline='#3b82f6')
    draw.rectangle([f1_x1+320, f1_y1+388, f1_x1+338, f1_y1+406], fill='#2563eb')
    draw.text((f1_x1+350, f1_y1+388), "[v] Lap trinh", fill='#1e293b')

    # Submit & Reset buttons
    draw.rounded_rectangle([f1_x1+20, f1_y1+460, f1_x1+285, f1_y1+515], radius=8, fill='#2563eb')
    draw.text((f1_x1+90, f1_y1+478), "Gui thong tin", fill='#ffffff')

    draw.rounded_rectangle([f1_x1+305, f1_y1+460, f1_x2-20, f1_y1+515], radius=8, fill='#f1f5f9', outline='#cbd5e1')
    draw.text((f1_x1+385, f1_y1+478), "Nhap lai", fill='#475569')

    # Info summary box for Part 1
    draw.rounded_rectangle([f1_x1+20, f1_y1+545, f1_x2-20, f1_y2-25], radius=8, fill='#0f172a')
    draw.text((f1_x1+35, f1_y1+560), "// FormData Serialized (HTTP GET Query):", fill='#38bdf8')
    draw.text((f1_x1+35, f1_y1+590), "?yourname=Nguyen+Tuan+Dat", fill='#e2e8f0')
    draw.text((f1_x1+35, f1_y1+615), "&email=proyctk03%40gmail.com", fill='#e2e8f0')
    draw.text((f1_x1+35, f1_y1+640), "&hobby=the_thao&hobby=doc_sach&hobby=lap_trinh", fill='#e2e8f0')

    # ------------------ FORM 2 (RIGHT COLUMN) ------------------
    f2_x1, f2_y1, f2_x2, f2_y2 = 720, 215, 1340, 950
    draw.rounded_rectangle([f2_x1, f2_y1, f2_x2, f2_y2], radius=14, fill='#ffffff', outline='#cbd5e1', width=2)

    # Header Form 2
    draw.rounded_rectangle([f2_x1+20, f2_y1+20, f2_x1+230, f2_y1+48], radius=6, fill='#f0f9ff')
    draw.text((f2_x1+30, f2_y1+26), "PHAN 2: DANG KY HOC VIEN", fill='#0284c7')
    draw.text((f2_x1+20, f2_y1+60), "Form dang ky khoa hoc day du thuoc tinh", fill='#0f172a')

    # Row 1: fullname
    draw.text((f2_x1+20, f2_y1+100), "Ho va ten (name=\"fullname\") *", fill='#334155')
    draw.rounded_rectangle([f2_x1+20, f2_y1+122, f2_x2-20, f2_y1+162], radius=8, fill='#ffffff', outline='#94a3b8')
    draw.text((f2_x1+35, f2_y1+134), "Le Hai Dang", fill='#0f172a')

    # Row 2: email & phone (2 columns)
    draw.text((f2_x1+20, f2_y1+175), "Email (name=\"email\") *", fill='#334155')
    draw.rounded_rectangle([f2_x1+20, f2_y1+197, f2_x1+285, f2_y1+237], radius=8, fill='#ffffff', outline='#94a3b8')
    draw.text((f2_x1+35, f2_y1+209), "haidang@codegym.vn", fill='#0f172a')

    draw.text((f2_x1+305, f2_y1+175), "Dien thoai (name=\"phone\") *", fill='#334155')
    draw.rounded_rectangle([f2_x1+305, f2_y1+197, f2_x2-20, f2_y1+237], radius=8, fill='#ffffff', outline='#94a3b8')
    draw.text((f2_x1+320, f2_y1+209), "0988 123 456", fill='#0f172a')

    # Row 3: birthday & gender (radio)
    draw.text((f2_x1+20, f2_y1+250), "Ngay sinh (name=\"birthday\") *", fill='#334155')
    draw.rounded_rectangle([f2_x1+20, f2_y1+272, f2_x1+285, f2_y1+312], radius=8, fill='#ffffff', outline='#94a3b8')
    draw.text((f2_x1+35, f2_y1+284), "2003-05-15", fill='#0f172a')

    draw.text((f2_x1+305, f2_y1+250), "Gioi tinh (radio name=\"gender\") *", fill='#334155')
    # Radio Nam checked, Nu, Khac
    draw.rounded_rectangle([f2_x1+305, f2_y1+272, f2_x1+385, f2_y1+312], radius=6, fill='#f0f9ff', outline='#0284c7')
    draw.text((f2_x1+318, f2_y1+284), "(*) Nam", fill='#0284c7')
    draw.rounded_rectangle([f2_x1+395, f2_y1+272, f2_x1+475, f2_y1+312], radius=6, fill='#f8fafc', outline='#cbd5e1')
    draw.text((f2_x1+412, f2_y1+284), "( ) Nu", fill='#64748b')
    draw.rounded_rectangle([f2_x1+485, f2_y1+272, f2_x2-20, f2_y1+312], radius=6, fill='#f8fafc', outline='#cbd5e1')
    draw.text((f2_x1+500, f2_y1+284), "( ) Khac", fill='#64748b')

    # Row 4: course (select) & study_type (radio)
    draw.text((f2_x1+20, f2_y1+325), "Khoa hoc (select name=\"course\") *", fill='#334155')
    draw.rounded_rectangle([f2_x1+20, f2_y1+347, f2_x1+285, f2_y1+387], radius=8, fill='#ffffff', outline='#94a3b8')
    draw.text((f2_x1+35, f2_y1+359), "JavaScript [v]", fill='#0f172a')

    draw.text((f2_x1+305, f2_y1+325), "Hinh thuc (radio name=\"study_type\") *", fill='#334155')
    draw.rounded_rectangle([f2_x1+305, f2_y1+347, f2_x1+445, f2_y1+387], radius=6, fill='#f0f9ff', outline='#0284c7')
    draw.text((f2_x1+322, f2_y1+359), "(*) Online", fill='#0284c7')
    draw.rounded_rectangle([f2_x1+455, f2_y1+347, f2_x2-20, f2_y1+387], radius=6, fill='#f8fafc', outline='#cbd5e1')
    draw.text((f2_x1+470, f2_y1+359), "( ) Offline", fill='#64748b')

    # Row 5: address (textarea)
    draw.text((f2_x1+20, f2_y1+400), "Dia chi (textarea name=\"address\")", fill='#334155')
    draw.rounded_rectangle([f2_x1+20, f2_y1+422, f2_x2-20, f2_y1+467], radius=8, fill='#ffffff', outline='#94a3b8')
    draw.text((f2_x1+35, f2_y1+435), "Toa nha Handico, Pham Hung, Nam Tu Liem, Ha Noi", fill='#0f172a')

    # Row 6: note (textarea)
    draw.text((f2_x1+20, f2_y1+480), "Ghi chu (textarea name=\"note\")", fill='#334155')
    draw.rounded_rectangle([f2_x1+20, f2_y1+502, f2_x2-20, f2_y1+547], radius=8, fill='#ffffff', outline='#94a3b8')
    draw.text((f2_x1+35, f2_y1+515), "Nguyen vong tham gia lop buoi toi tu 19h00...", fill='#0f172a')

    # Submit & Reset buttons
    draw.rounded_rectangle([f2_x1+20, f2_y1+570, f2_x1+285, f2_y1+625], radius=8, fill='#0284c7')
    draw.text((f2_x1+105, f2_y1+588), "Dang ky", fill='#ffffff')

    draw.rounded_rectangle([f2_x1+305, f2_y1+570, f2_x2-20, f2_y1+625], radius=8, fill='#f1f5f9', outline='#cbd5e1')
    draw.text((f2_x1+385, f2_y1+588), "Nhap lai", fill='#475569')

    # Footer note Form 2
    draw.rounded_rectangle([f2_x1+20, f2_y1+650, f2_x2-20, f2_y2-25], radius=8, fill='#f8fafc', outline='#e2e8f0')
    draw.text((f2_x1+35, f2_y1+668), "Xac thuc HTML5 & Su kien: form.onsubmit -> Validate hop le 100%", fill='#10b981')

    # Save image
    save_path = os.path.join(output_dir, "browser_form_result_screenshot.png")
    img.save(save_path, quality=95)
    print("Generated:", save_path)

# -------------------------------------------------------------------
# 2. HTML FORM ARCHITECTURE DIAGRAM
# -------------------------------------------------------------------
def generate_architecture_diagram():
    fig, ax = plt.subplots(figsize=(13, 8), dpi=150)
    ax.set_facecolor("#f8fafc")
    fig.patch.set_facecolor("#f8fafc")

    # Title
    ax.text(0.5, 0.94, "KIẾN TRÚC BIỂU MẪU HTML5 & BINDING THUỘC TÍNH 'NAME'", 
            ha='center', va='center', fontsize=16, fontweight='bold', color='#0f172a')
    ax.text(0.5, 0.89, "Cơ chế ánh xạ thẻ Form, định danh khóa tham số dữ liệu và điều khiển người dùng", 
            ha='center', va='center', fontsize=11, color='#64748b')

    # Form Container Box
    form_box = patches.FancyBboxPatch((0.05, 0.08), 0.90, 0.76, boxstyle="round,pad=0.03", 
                                      fc="#ffffff", ec="#3b82f6", lw=2, linestyle='--')
    ax.add_patch(form_box)
    ax.text(0.08, 0.81, "<form action=\"/submit\" method=\"GET / POST\">", 
            fontsize=13, fontweight='bold', color='#2563eb', family='monospace')

    # Elements Boxes
    elements = [
        {"title": "1. Text & Email", "tag": "<input type=\"text|email\">", "names": "yourname, fullname, email", "desc": "Nhập văn bản dòng đơn, email validate định dạng", "color": "#eff6ff", "border": "#3b82f6"},
        {"title": "2. Phone & Date", "tag": "<input type=\"tel|date\">", "names": "phone, birthday", "desc": "Số điện thoại regex, chọn ngày sinh qua datepicker", "color": "#f0fdf4", "border": "#22c55e"},
        {"title": "3. Radio Buttons", "tag": "<input type=\"radio\">", "names": "gender, study_type", "desc": "Cùng name -> Chọn 1 duy nhất (Nam/Nữ, Online/Offline)", "color": "#fff7ed", "border": "#f97316"},
        {"title": "4. Checkboxes", "tag": "<input type=\"checkbox\">", "names": "hobby (Multiple values)", "desc": "Cùng name -> Chọn nhiều sở thích, gửi dạng mảng giá trị", "color": "#fdf4ff", "border": "#c084fc"},
        {"title": "5. Select Dropdown", "tag": "<select> <option>", "names": "course (HTML, JS, Java...)", "desc": "Menu thả xuống tiết kiệm diện tích giao diện", "color": "#ecfeff", "border": "#06b6d4"},
        {"title": "6. Textarea", "tag": "<textarea rows=\"...\">", "names": "address, note", "desc": "Văn bản nhiều dòng (địa chỉ, ghi chú chi tiết)", "color": "#fefce8", "border": "#eab308"},
        {"title": "7. Submit Action", "tag": "<input type=\"submit\">", "names": "value=\"Gửi thông tin / Đăng ký\"", "desc": "Kích hoạt gửi dữ liệu biểu mẫu lên máy chủ", "color": "#f1f5f9", "border": "#64748b"},
        {"title": "8. Reset Action", "tag": "<input type=\"reset\">", "names": "value=\"Nhập lại\"", "desc": "Khôi phục toàn bộ trường về trạng thái ban đầu", "color": "#f1f5f9", "border": "#64748b"},
    ]

    x_positions = [0.08, 0.52]
    y_positions = [0.63, 0.45, 0.27, 0.11]

    for i, el in enumerate(elements):
        x = x_positions[i % 2]
        y = y_positions[i // 2]
        
        box = patches.FancyBboxPatch((x, y), 0.40, 0.14, boxstyle="round,pad=0.015", 
                                     fc=el['color'], ec=el['border'], lw=1.5)
        ax.add_patch(box)

        ax.text(x + 0.02, y + 0.105, el['title'], fontsize=11, fontweight='bold', color='#0f172a')
        ax.text(x + 0.02, y + 0.075, el['tag'], fontsize=9.5, fontweight='bold', color='#0369a1', family='monospace')
        ax.text(x + 0.02, y + 0.045, f"Name: {el['names']}", fontsize=9, fontweight='bold', color='#475569')
        ax.text(x + 0.02, y + 0.018, el['desc'], fontsize=8.5, color='#64748b')

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    plt.tight_layout()
    save_path = os.path.join(output_dir, "form_architecture_diagram.png")
    plt.savefig(save_path, dpi=200, bbox_inches='tight')
    plt.close()
    print("Generated:", save_path)

# -------------------------------------------------------------------
# 3. FORM SUBMISSION FLOW DIAGRAM
# -------------------------------------------------------------------
def generate_submission_flow_diagram():
    fig, ax = plt.subplots(figsize=(13, 7.5), dpi=150)
    ax.set_facecolor("#f8fafc")
    fig.patch.set_facecolor("#f8fafc")

    # Title
    ax.text(0.5, 0.94, "LUỒNG XỬ LÝ DỮ LIỆU BIỂU MẪU: CLIENT SUBMIT & HTTP TRANSPORT", 
            ha='center', va='center', fontsize=16, fontweight='bold', color='#0f172a')
    ax.text(0.5, 0.89, "So sánh cơ chế đóng gói tham số thuộc tính Name qua phương thức GET và POST", 
            ha='center', va='center', fontsize=11, color='#64748b')

    # Step 1: User Input
    box1 = patches.FancyBboxPatch((0.05, 0.42), 0.22, 0.36, boxstyle="round,pad=0.02", 
                                  fc="#ffffff", ec="#2563eb", lw=2)
    ax.add_patch(box1)
    ax.text(0.16, 0.73, "BƯỚC 1: NHẬP LIỆU", ha='center', fontsize=11, fontweight='bold', color='#2563eb')
    ax.text(0.16, 0.66, "Người dùng điền Form:\n• yourname / fullname\n• email, phone\n• radio & checkboxes", 
            ha='center', fontsize=9.5, color='#334155')
    ax.text(0.16, 0.48, "Nhấn nút Submit:\n[Gửi thông tin / Đăng ký]", 
            ha='center', fontsize=9.5, fontweight='bold', color='#0f172a')

    # Arrow 1 -> 2
    ax.annotate("", xy=(0.33, 0.60), xytext=(0.28, 0.60),
                arrowprops=dict(arrowstyle="->", lw=2.5, color="#2563eb"))

    # Step 2: Serialization
    box2 = patches.FancyBboxPatch((0.34, 0.42), 0.28, 0.36, boxstyle="round,pad=0.02", 
                                  fc="#ffffff", ec="#0284c7", lw=2)
    ax.add_patch(box2)
    ax.text(0.48, 0.73, "BƯỚC 2: SERIALIZE DỮ LIỆU", ha='center', fontsize=11, fontweight='bold', color='#0284c7')
    ax.text(0.48, 0.64, "Trình duyệt duyệt các trường:\nChỉ thu thập trường CÓ name:\n• key: thuộc tính name\n• value: thuộc tính value", 
            ha='center', fontsize=9.5, color='#334155')
    ax.text(0.48, 0.49, "Tạo cấu trúc URL-Encoded:\napplication/x-www-form-urlencoded", 
            ha='center', fontsize=9, family='monospace', color='#0369a1')

    # Arrow 2 -> 3
    ax.annotate("", xy=(0.68, 0.60), xytext=(0.63, 0.60),
                arrowprops=dict(arrowstyle="->", lw=2.5, color="#0284c7"))

    # Step 3: HTTP Protocol Sending
    box3 = patches.FancyBboxPatch((0.69, 0.42), 0.26, 0.36, boxstyle="round,pad=0.02", 
                                  fc="#ffffff", ec="#10b981", lw=2)
    ax.add_patch(box3)
    ax.text(0.82, 0.73, "BƯỚC 3: GỬI HTTP REQUEST", ha='center', fontsize=11, fontweight='bold', color='#10b981')
    ax.text(0.82, 0.64, "Gửi đến Action URL:\n• GET: Gắn vào Query URL\n• POST: Đưa vào Body", 
            ha='center', fontsize=9.5, color='#334155')
    ax.text(0.82, 0.49, "Máy chủ giải mã:\nreq.query (GET) hoặc\nreq.body (POST)", 
            ha='center', fontsize=9.5, family='monospace', color='#047857')

    # Comparison Table at bottom
    box_cmp = patches.FancyBboxPatch((0.05, 0.08), 0.90, 0.28, boxstyle="round,pad=0.02", 
                                     fc="#f1f5f9", ec="#cbd5e1", lw=1.5)
    ax.add_patch(box_cmp)
    ax.text(0.5, 0.31, "SO SÁNH PHƯƠNG THỨC GỬI DỮ LIỆU: METHOD GET vs POST", 
            ha='center', fontsize=11, fontweight='bold', color='#0f172a')

    # GET Box
    box_get = patches.FancyBboxPatch((0.08, 0.11), 0.40, 0.16, boxstyle="round,pad=0.015", 
                                     fc="#ffffff", ec="#3b82f6", lw=1)
    ax.add_patch(box_get)
    ax.text(0.10, 0.23, "PHƯƠNG THỨC GET (Phần 1):", fontsize=9.5, fontweight='bold', color='#2563eb')
    ax.text(0.10, 0.19, "• Tham số hiển thị trên URL: ?yourname=...&email=...", fontsize=8.5, color='#334155')
    ax.text(0.10, 0.15, "• Dễ dàng bookmark, chia sẻ link; không an toàn cho mật khẩu", fontsize=8.5, color='#64748b')
    ax.text(0.10, 0.12, "• Giới hạn độ dài URL (~2048 ký tự)", fontsize=8.5, color='#64748b')

    # POST Box
    box_post = patches.FancyBboxPatch((0.52, 0.11), 0.40, 0.16, boxstyle="round,pad=0.015", 
                                      fc="#ffffff", ec="#10b981", lw=1)
    ax.add_patch(box_post)
    ax.text(0.54, 0.23, "PHƯƠNG THỨC POST (Phần 2):", fontsize=9.5, fontweight='bold', color='#059669')
    ax.text(0.54, 0.19, "• Dữ liệu nằm trong HTTP Request Body, ẩn khỏi thanh URL", fontsize=8.5, color='#334155')
    ax.text(0.54, 0.15, "• Phù hợp với thông tin cá nhân học viên, form đăng ký", fontsize=8.5, color='#64748b')
    ax.text(0.54, 0.12, "• Không bị giới hạn kích thước, hỗ trợ tải file (multipart)", fontsize=8.5, color='#64748b')

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    plt.tight_layout()
    save_path = os.path.join(output_dir, "form_submission_flow.png")
    plt.savefig(save_path, dpi=200, bbox_inches='tight')
    plt.close()
    print("Generated:", save_path)

if __name__ == "__main__":
    generate_browser_mockup()
    generate_architecture_diagram()
    generate_submission_flow_diagram()
    print("All diagrams generated successfully!")
