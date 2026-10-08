import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image, ImageDraw, ImageFont
import os

output_dir = r"C:\Users\dathao\.gemini\antigravity-ide\scratch\bai-tap-form-survey-khach-hang"
os.makedirs(output_dir, exist_ok=True)

# -------------------------------------------------------------------
# 1. BROWSER SURVEY FORM SCREENSHOT MOCKUP
# -------------------------------------------------------------------
def generate_browser_mockup():
    width = 1400
    height = 1100
    img = Image.new('RGB', (width, height), color='#f1f5f9')
    draw = ImageDraw.Draw(img)

    # Browser Header bar
    draw.rectangle([0, 0, width, 44], fill='#1e293b')
    # Window controls (red, yellow, green)
    draw.ellipse([20, 16, 32, 28], fill='#ef4444')
    draw.ellipse([40, 16, 52, 28], fill='#f59e0b')
    draw.ellipse([60, 16, 72, 28], fill='#10b981')

    # Browser Tab
    draw.rounded_rectangle([90, 8, 440, 44], radius=6, fill='#334155')
    draw.text((115, 16), "CodeGym - [Bai tap] Tao form survey khach hang", fill='#ffffff')

    # Address bar
    draw.rectangle([0, 44, width, 88], fill='#ffffff')
    draw.line([0, 88, width, 88], fill='#cbd5e1', width=1)
    draw.rounded_rectangle([80, 52, width - 80, 80], radius=8, fill='#f8fafc', outline='#e2e8f0', width=1)
    draw.text((105, 59), "https://proyctk03-eng.github.io/bai-tap-form-survey-khach-hang/index.html", fill='#475569')

    # Main Card Box in center
    c_x1, c_y1, c_x2, c_y2 = 280, 110, 1120, 1060
    draw.rounded_rectangle([c_x1, c_y1, c_x2, c_y2], radius=16, fill='#ffffff', outline='#cbd5e1', width=2)

    # Header in Card
    draw.text((c_x1+35, c_y1+25), "Market Research Survey", fill='#0f172a')
    draw.text((c_x1+35, c_y1+50), "Please take a few moments to complete this satisfaction survey.", fill='#64748b')
    draw.line([c_x1+35, c_y1+78, c_x2-35, c_y1+78], fill='#e2e8f0', width=1)

    cur_y = c_y1 + 95

    # Q1: Age range
    draw.text((c_x1+35, cur_y), "1. What is your age range?", fill='#0f172a')
    cur_y += 24
    draw.rounded_rectangle([c_x1+35, cur_y, c_x2-35, cur_y+36], radius=6, fill='#ffffff', outline='#94a3b8', width=1)
    draw.text((c_x1+48, cur_y+10), "18-24   [v]", fill='#0f172a')
    cur_y += 50

    # Q2: Income range
    draw.text((c_x1+35, cur_y), "2. What is your yearly income range?", fill='#0f172a')
    cur_y += 24
    draw.rounded_rectangle([c_x1+35, cur_y, c_x2-35, cur_y+36], radius=6, fill='#ffffff', outline='#94a3b8', width=1)
    draw.text((c_x1+48, cur_y+10), "$25,001 - $50,000   [v]", fill='#0f172a')
    cur_y += 50

    # Q3: Gender Identity
    draw.text((c_x1+35, cur_y), "3. Gender Identity", fill='#0f172a')
    cur_y += 24
    # Male checked
    draw.ellipse([c_x1+38, cur_y+2, c_x1+52, cur_y+16], fill='#0284c7')
    draw.text((c_x1+60, cur_y+2), "(*) Male", fill='#0284c7')
    # Female
    draw.ellipse([c_x1+160, cur_y+2, c_x1+174, cur_y+16], fill='#ffffff', outline='#94a3b8')
    draw.text((c_x1+182, cur_y+2), "( ) Female", fill='#475569')
    # Nonbinary
    draw.ellipse([c_x1+290, cur_y+2, c_x1+304, cur_y+16], fill='#ffffff', outline='#94a3b8')
    draw.text((c_x1+312, cur_y+2), "( ) Nonbinary", fill='#475569')
    # Other
    draw.ellipse([c_x1+430, cur_y+2, c_x1+444, cur_y+16], fill='#ffffff', outline='#94a3b8')
    draw.text((c_x1+452, cur_y+2), "( ) Other", fill='#475569')
    cur_y += 45

    # Q4: Products Purchased
    draw.text((c_x1+35, cur_y), "4. Which of the following products have you purchased in the last 2 months?", fill='#0f172a')
    cur_y += 24
    # Product 1 checked
    draw.rectangle([c_x1+38, cur_y+2, c_x1+52, cur_y+16], fill='#0284c7')
    draw.text((c_x1+60, cur_y+2), "[v] Product 1", fill='#0f172a')
    # Product 2
    draw.rectangle([c_x1+200, cur_y+2, c_x1+214, cur_y+16], fill='#ffffff', outline='#94a3b8')
    draw.text((c_x1+222, cur_y+2), "[ ] Product 2", fill='#475569')
    # Product 3 checked
    draw.rectangle([c_x1+350, cur_y+2, c_x1+364, cur_y+16], fill='#0284c7')
    draw.text((c_x1+372, cur_y+2), "[v] Product 3", fill='#0f172a')
    cur_y += 45

    # Q5: Frequency
    draw.text((c_x1+35, cur_y), "5. How often would you use our new product?", fill='#0f172a')
    cur_y += 24
    draw.ellipse([c_x1+38, cur_y+2, c_x1+52, cur_y+16], fill='#0284c7')
    draw.text((c_x1+60, cur_y+2), "(*) Daily", fill='#0284c7')
    draw.ellipse([c_x1+170, cur_y+2, c_x1+184, cur_y+16], fill='#ffffff', outline='#94a3b8')
    draw.text((c_x1+192, cur_y+2), "( ) Weekly", fill='#475569')
    draw.ellipse([c_x1+300, cur_y+2, c_x1+314, cur_y+16], fill='#ffffff', outline='#94a3b8')
    draw.text((c_x1+322, cur_y+2), "( ) Monthly", fill='#475569')
    cur_y += 45

    # Q6: Price Currency
    draw.text((c_x1+35, cur_y), "6. What would you pay for the new product?", fill='#0f172a')
    cur_y += 24
    draw.text((c_x1+38, cur_y+8), "$", fill='#475569')
    draw.rounded_rectangle([c_x1+55, cur_y, c_x1+175, cur_y+36], radius=6, fill='#ffffff', outline='#94a3b8', width=1)
    draw.text((c_x1+70, cur_y+10), "49 Dollars", fill='#0f172a')
    draw.text((c_x1+185, cur_y+8), ".", fill='#475569')
    draw.rounded_rectangle([c_x1+198, cur_y, c_x1+278, cur_y+36], radius=6, fill='#ffffff', outline='#94a3b8', width=1)
    draw.text((c_x1+215, cur_y+10), "99 Cents", fill='#0f172a')
    cur_y += 50

    # Q7: Features Textarea
    draw.text((c_x1+35, cur_y), "7. What features would you like to see in the new product?", fill='#0f172a')
    cur_y += 24
    draw.rounded_rectangle([c_x1+35, cur_y, c_x2-35, cur_y+65], radius=6, fill='#ffffff', outline='#94a3b8', width=1)
    draw.text((c_x1+48, cur_y+10), "Giao dien than thien tren dien thoai, dong bo hoa du lieu thoi gian thuc...", fill='#475569')
    cur_y += 80

    # Q8: Likert Matrix Table
    draw.text((c_x1+35, cur_y), "8. Please rate your level of agreement with the following statements:", fill='#0f172a')
    cur_y += 24
    # Table box
    tbl_h = 135
    draw.rounded_rectangle([c_x1+35, cur_y, c_x2-35, cur_y+tbl_h], radius=6, fill='#ffffff', outline='#cbd5e1', width=1)
    # Thead
    draw.rectangle([c_x1+35, cur_y, c_x2-35, cur_y+30], fill='#f8fafc', outline='#e2e8f0')
    draw.text((c_x1+50, cur_y+8), "Statements", fill='#475569')
    draw.text((c_x1+390, cur_y+8), "Strongly Disagree", fill='#475569')
    draw.text((c_x1+515, cur_y+8), "Disagree", fill='#475569')
    draw.text((c_x1+610, cur_y+8), "Agree", fill='#475569')
    draw.text((c_x1+685, cur_y+8), "Strongly Agree", fill='#475569')

    # Row 1
    r1_y = cur_y + 35
    draw.text((c_x1+50, r1_y+6), "Our products are priced fairly.", fill='#1e293b')
    draw.text((c_x1+435, r1_y+6), "( )", fill='#94a3b8')
    draw.text((c_x1+535, r1_y+6), "( )", fill='#94a3b8')
    draw.text((c_x1+620, r1_y+6), "(*)", fill='#0284c7')
    draw.text((c_x1+720, r1_y+6), "( )", fill='#94a3b8')

    # Row 2
    r2_y = cur_y + 68
    draw.text((c_x1+50, r2_y+6), "Our products are high quality.", fill='#1e293b')
    draw.text((c_x1+435, r2_y+6), "( )", fill='#94a3b8')
    draw.text((c_x1+535, r2_y+6), "( )", fill='#94a3b8')
    draw.text((c_x1+620, r2_y+6), "( )", fill='#94a3b8')
    draw.text((c_x1+720, r2_y+6), "(*)", fill='#0284c7')

    # Row 3
    r3_y = cur_y + 101
    draw.text((c_x1+50, r3_y+6), "You would recommend our product to a friend...", fill='#1e293b')
    draw.text((c_x1+435, r3_y+6), "( )", fill='#94a3b8')
    draw.text((c_x1+535, r3_y+6), "( )", fill='#94a3b8')
    draw.text((c_x1+620, r3_y+6), "( )", fill='#94a3b8')
    draw.text((c_x1+720, r3_y+6), "(*)", fill='#0284c7')

    cur_y += tbl_h + 25

    # Submit Button
    draw.rounded_rectangle([c_x1+35, cur_y, c_x1+250, cur_y+45], radius=6, fill='#0284c7')
    draw.text((c_x1+85, cur_y+13), "Submit Survey ->", fill='#ffffff')

    # Save
    save_path = os.path.join(output_dir, "browser_survey_result_screenshot.png")
    img.save(save_path, quality=95)
    print("Generated:", save_path)

# -------------------------------------------------------------------
# 2. SURVEY FORM ARCHITECTURE DIAGRAM
# -------------------------------------------------------------------
def generate_architecture_diagram():
    fig, ax = plt.subplots(figsize=(13, 8), dpi=150)
    ax.set_facecolor("#f8fafc")
    fig.patch.set_facecolor("#f8fafc")

    # Title
    ax.text(0.5, 0.94, "KIẾN TRÚC FORM KHẢO SÁT KHÁCH HÀNG (WUFOO SURVEY ARCHITECTURE)", 
            ha='center', va='center', fontsize=15, fontweight='bold', color='#0f172a')
    ax.text(0.5, 0.89, "Phân loại các thành phần giao diện nhập liệu trong biểu mẫu nghiên cứu thị trường", 
            ha='center', va='center', fontsize=11, color='#64748b')

    components = [
        {"title": "1. Dropdown Select", "tag": "<select> <option>", "q": "Age & Income Range", "desc": "Lựa chọn 1 giá trị trong dải danh sách định sẵn", "color": "#eff6ff", "border": "#3b82f6"},
        {"title": "2. Radio Button List", "tag": "<input type=\"radio\">", "q": "Gender & Usage Frequency", "desc": "Chọn 1 tùy chọn duy nhất trong nhóm (Male/Female/Other...)", "color": "#f0fdf4", "border": "#22c55e"},
        {"title": "3. Multi-Select Checkboxes", "tag": "<input type=\"checkbox\">", "q": "Products Purchased", "desc": "Chọn nhiều sản phẩm cùng lúc (Product 1, 2, 3)", "color": "#fdf4ff", "border": "#c084fc"},
        {"title": "4. Currency Pricing Inputs", "tag": "<input type=\"number\">", "q": "Willingness To Pay", "desc": "Cặp ô nhập tách biệt Dollars và Cents chính xác", "color": "#fff7ed", "border": "#f97316"},
        {"title": "5. Multi-line Feedback", "tag": "<textarea>", "q": "Feature Requests & Suggestions", "desc": "Ô nhập văn bản tự do thu thập ý kiến khách hàng", "color": "#ecfeff", "border": "#06b6d4"},
        {"title": "6. Likert Scale Matrix", "tag": "<table> <thead> <tbody>", "q": "Level of Agreement", "desc": "Bảng ma trận đánh giá 4 mức độ đồng ý cho 3 phát biểu", "color": "#fefce8", "border": "#eab308"}
    ]

    x_positions = [0.08, 0.52]
    y_positions = [0.60, 0.37, 0.14]

    for i, c in enumerate(components):
        x = x_positions[i % 2]
        y = y_positions[i // 2]
        
        box = patches.FancyBboxPatch((x, y), 0.40, 0.18, boxstyle="round,pad=0.015", 
                                     fc=c['color'], ec=c['border'], lw=1.5)
        ax.add_patch(box)

        ax.text(x + 0.02, y + 0.14, c['title'], fontsize=11, fontweight='bold', color='#0f172a')
        ax.text(x + 0.02, y + 0.10, c['tag'], fontsize=9.5, fontweight='bold', color='#0284c7', family='monospace')
        ax.text(x + 0.02, y + 0.06, f"Mục khảo sát: {c['q']}", fontsize=9, fontweight='bold', color='#334155')
        ax.text(x + 0.02, y + 0.025, c['desc'], fontsize=8.5, color='#64748b')

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    plt.tight_layout()
    save_path = os.path.join(output_dir, "survey_form_architecture_diagram.png")
    plt.savefig(save_path, dpi=200, bbox_inches='tight')
    plt.close()
    print("Generated:", save_path)

# -------------------------------------------------------------------
# 3. LIKERT MATRIX STRUCTURE DIAGRAM
# -------------------------------------------------------------------
def generate_likert_diagram():
    fig, ax = plt.subplots(figsize=(13, 7.5), dpi=150)
    ax.set_facecolor("#f8fafc")
    fig.patch.set_facecolor("#f8fafc")

    # Title
    ax.text(0.5, 0.93, "CẤU TRÚC BẢNG ĐÁNH GIÁ MA TRẬN LIKERT SCALE TRONG HTML5", 
            ha='center', va='center', fontsize=15, fontweight='bold', color='#0f172a')
    ax.text(0.5, 0.88, "Nguyên lý gom nhóm Radio Buttons theo hàng để đánh giá mức độ hài lòng khách hàng", 
            ha='center', va='center', fontsize=11, color='#64748b')

    # Big Table Box
    tbl_box = patches.FancyBboxPatch((0.05, 0.22), 0.90, 0.60, boxstyle="round,pad=0.02", 
                                     fc="#ffffff", ec="#0284c7", lw=2)
    ax.add_patch(tbl_box)

    # Table Header Row
    th_box = patches.FancyBboxPatch((0.07, 0.68), 0.86, 0.10, boxstyle="round,pad=0.01", 
                                    fc="#f1f5f9", ec="#cbd5e1", lw=1)
    ax.add_patch(th_box)
    ax.text(0.24, 0.73, "<th> Câu hỏi (Statement) </th>", ha='center', fontsize=9.5, fontweight='bold', color='#334155', family='monospace')
    ax.text(0.50, 0.73, "Strongly Disagree (1)", ha='center', fontsize=9, fontweight='bold', color='#475569')
    ax.text(0.64, 0.73, "Disagree (2)", ha='center', fontsize=9, fontweight='bold', color='#475569')
    ax.text(0.77, 0.73, "Agree (3)", ha='center', fontsize=9, fontweight='bold', color='#475569')
    ax.text(0.88, 0.73, "Strongly Agree (4)", ha='center', fontsize=9, fontweight='bold', color='#475569')

    # Row 1
    ax.text(0.24, 0.59, "1. Our products are priced fairly.\n(name=\"rating_priced_fairly\")", 
            ha='center', fontsize=9, color='#1e293b')
    ax.text(0.50, 0.59, "( ) Radio", ha='center', fontsize=9, color='#64748b')
    ax.text(0.64, 0.59, "( ) Radio", ha='center', fontsize=9, color='#64748b')
    ax.text(0.77, 0.59, "(*) Radio [CHỌN]", ha='center', fontsize=9, fontweight='bold', color='#0284c7')
    ax.text(0.88, 0.59, "( ) Radio", ha='center', fontsize=9, color='#64748b')
    ax.plot([0.07, 0.93], [0.52, 0.52], color="#e2e8f0", lw=1)

    # Row 2
    ax.text(0.24, 0.44, "2. Our products are high quality.\n(name=\"rating_high_quality\")", 
            ha='center', fontsize=9, color='#1e293b')
    ax.text(0.50, 0.44, "( ) Radio", ha='center', fontsize=9, color='#64748b')
    ax.text(0.64, 0.44, "( ) Radio", ha='center', fontsize=9, color='#64748b')
    ax.text(0.77, 0.44, "( ) Radio", ha='center', fontsize=9, color='#64748b')
    ax.text(0.88, 0.44, "(*) Radio [CHỌN]", ha='center', fontsize=9, fontweight='bold', color='#0284c7')
    ax.plot([0.07, 0.93], [0.38, 0.38], color="#e2e8f0", lw=1)

    # Row 3
    ax.text(0.24, 0.30, "3. Recommend to a friend/coworker.\n(name=\"rating_recommend\")", 
            ha='center', fontsize=9, color='#1e293b')
    ax.text(0.50, 0.30, "( ) Radio", ha='center', fontsize=9, color='#64748b')
    ax.text(0.64, 0.30, "( ) Radio", ha='center', fontsize=9, color='#64748b')
    ax.text(0.77, 0.30, "( ) Radio", ha='center', fontsize=9, color='#64748b')
    ax.text(0.88, 0.30, "(*) Radio [CHỌN]", ha='center', fontsize=9, fontweight='bold', color='#0284c7')

    # Bottom Explanation
    exp_box = patches.FancyBboxPatch((0.05, 0.05), 0.90, 0.13, boxstyle="round,pad=0.015", 
                                     fc="#eff6ff", ec="#bfdbfe", lw=1)
    ax.add_patch(exp_box)
    ax.text(0.5, 0.12, "QUY TẮC NHÓM RADIO TRONG MA TRẬN: MỖI DÒNG PHẢI SỬ DỤNG 1 THUỘC TÍNH NAME RIÊNG BIỆT", 
            ha='center', fontsize=10, fontweight='bold', color='#1d4ed8')
    ax.text(0.5, 0.07, "Nhờ việc đặt tên khác nhau theo từng dòng, người dùng có thể chọn độc lập 1 mức điểm cho từng câu hỏi khảo sát.", 
            ha='center', fontsize=9, color='#475569')

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    plt.tight_layout()
    save_path = os.path.join(output_dir, "likert_matrix_structure_diagram.png")
    plt.savefig(save_path, dpi=200, bbox_inches='tight')
    plt.close()
    print("Generated:", save_path)

if __name__ == "__main__":
    generate_browser_mockup()
    generate_architecture_diagram()
    generate_likert_diagram()
    print("All survey diagrams generated successfully!")
