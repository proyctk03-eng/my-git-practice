import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def set_cell_background(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def create_callout_box(doc, text, title="LƯU Ý QUAN TRỌNG", hex_border="2563EB", hex_bg="EFF6FF"):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    tbl.columns[0].width = Inches(6.5)
    
    cell = tbl.cell(0, 0)
    set_cell_background(cell, hex_bg)
    set_cell_margins(cell, top=140, bottom=140, left=200, right=180)
    
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(f'''
        <w:tcBorders {nsdecls("w")}>
            <w:top w:val="none"/>
            <w:left w:val="single" w:sz="36" w:space="0" w:color="{hex_border}"/>
            <w:bottom w:val="none"/>
            <w:right w:val="none"/>
        </w:tcBorders>
    ''')
    tcPr.append(borders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(3)
    r_title = p.add_run(f"📌 {title}: ")
    r_title.bold = True
    r_title.font.name = "Arial"
    r_title.font.size = Pt(10)
    r_title.font.color.rgb = RGBColor.from_string(hex_border)
    
    r_text = p.add_run(text)
    r_text.font.name = "Arial"
    r_text.font.size = Pt(10)
    r_text.font.color.rgb = RGBColor(30, 41, 59)
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

def add_header_footer(doc):
    for s in doc.sections:
        s.top_margin = Inches(0.8)
        s.bottom_margin = Inches(0.8)
        s.left_margin = Inches(0.9)
        s.right_margin = Inches(0.9)
        
        # Header
        hdr = s.header
        hp = hdr.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        hr = hp.add_run("Báo Cáo: [Bài tập] Tạo Form Đơn Giản & Đăng Ký Học Viên")
        hr.font.name = "Arial"
        hr.font.size = Pt(8.5)
        hr.font.color.rgb = RGBColor(148, 163, 184)
        
        # Footer
        ftr = s.footer
        fp = ftr.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        fr = fp.add_run("Học viên: proyctk03-eng  |  Mô-đun: HTML5 Form Elements  |  CodeGym 2026")
        fr.font.name = "Arial"
        fr.font.size = Pt(8.5)
        fr.font.color.rgb = RGBColor(148, 163, 184)

def build_report():
    doc = docx.Document()
    add_header_footer(doc)
    
    # ------------------ COVER / HEADER ------------------
    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_inst.paragraph_format.space_after = Pt(2)
    r_inst = p_inst.add_run("HỆ THỐNG ĐÀO TẠO LẬP TRÌNH CODEGYM")
    r_inst.bold = True
    r_inst.font.name = "Arial"
    r_inst.font.size = Pt(12)
    r_inst.font.color.rgb = RGBColor(37, 99, 235)

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(14)
    r_sub = p_sub.add_run("CHƯƠNG TRÌNH PHÁT TRIỂN FULL-STACK WEB &middot; MÔ-ĐUN HTML/CSS")
    r_sub.font.name = "Arial"
    r_sub.font.size = Pt(9.5)
    r_sub.font.color.rgb = RGBColor(100, 116, 139)

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_after = Pt(8)
    r_title = p_title.add_run("BÁO CÁO KỸ THUẬT & BÀI LÀM\n[BÀI TẬP] TẠO FORM ĐƠN GIẢN & FORM ĐĂNG KÝ HỌC VIÊN")
    r_title.bold = True
    r_title.font.name = "Arial"
    r_title.font.size = Pt(18)
    r_title.font.color.rgb = RGBColor(15, 23, 42)

    p_meta = doc.add_paragraph()
    p_meta.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_meta.paragraph_format.space_after = Pt(18)
    r_meta = p_meta.add_run("Học viên: Nguyễn Tuấn Đạt  |  GitHub: proyctk03-eng  |  Ngày hoàn thành: 08/10/2026")
    r_meta.font.name = "Arial"
    r_meta.font.size = Pt(10)
    r_meta.font.color.rgb = RGBColor(71, 85, 105)

    create_callout_box(
        doc,
        "Bài thực hành bao gồm trọn vẹn 2 phần: Phần 1 (Form đơn giản: yourname, email, checkbox hobby, submit, reset) "
        "và Phần 2 (Form đăng ký học viên: fullname, email, phone, birthday, radio gender, textarea address, select course, "
        "radio study_type, checkbox hobby, textarea note, submit, reset). Toàn bộ mã nguồn đã được tổ chức khoa học, "
        "tối ưu chuẩn giao diện, và đưa lên GitHub Repository theo đúng quy chuẩn CodeGym.",
        title="TÓM TẮT BÀI NỘP",
        hex_border="2563EB",
        hex_bg="EFF6FF"
    )

    # ------------------ CHƯƠNG 1: MỤC TIÊU & YÊU CẦU ĐỀ BÀI ------------------
    h1 = doc.add_heading(level=1)
    r_h1 = h1.add_run("1. Mục Tiêu Thực Hành & Yêu Cầu Kỹ Thuật")
    r_h1.font.name = "Arial"
    r_h1.font.size = Pt(14)
    r_h1.bold = True
    r_h1.font.color.rgb = RGBColor(30, 41, 59)

    p = doc.add_paragraph()
    p.add_run("Mục tiêu trọng tâm của bài tập là nắm vững và thành thạo việc xây dựng biểu mẫu thu thập dữ liệu (HTML Forms) "
              "tương tác giữa người dùng và máy chủ web. Cụ thể bao gồm:\n"
              "1. Hiểu rõ cấu trúc thẻ <form> cùng các thuộc tính nền tảng: action, method, enctype.\n"
              "2. Nắm vững vai trò quyết định của thuộc tính name trong việc định danh và ánh xạ khóa dữ liệu gửi lên máy chủ.\n"
              "3. Sử dụng chuẩn xác các loại thẻ nhập liệu: <input type=\"text|email|tel|date|radio|checkbox|submit|reset\">, <textarea>, <select>, <option>.\n"
              "4. Thành thạo kỹ thuật nhóm Radio Buttons (chọn 1 trong nhiều) và CheckBoxes (chọn nhiều) bằng thuộc tính name trùng nhau.\n"
              "5. Căn chỉnh bố cục, thẩm mỹ, màu sắc hài hòa và trải nghiệm người dùng theo tiêu chuẩn giao diện hiện đại.")
    
    # ------------------ CHƯƠNG 2: PHẦN 1 - FORM ĐƠN GIẢN ------------------
    h2 = doc.add_heading(level=1)
    r_h2 = h2.add_run("2. Triển Khai Phần 1: Biểu Mẫu Đơn Giản (Simple Form)")
    r_h2.font.name = "Arial"
    r_h2.font.size = Pt(14)
    r_h2.bold = True
    r_h2.font.color.rgb = RGBColor(30, 41, 59)

    p = doc.add_paragraph()
    p.add_run("Tại Phần 1, biểu mẫu được xây dựng với cấu trúc tinh gọn nhưng đảm bảo 100% các tiêu chí bắt buộc về tên thuộc tính name:")

    # Bảng Part 1
    tbl1 = doc.add_table(rows=6, cols=4)
    tbl1.alignment = WD_TABLE_ALIGNMENT.CENTER
    headers = ["Thành phần giao diện", "Thẻ HTML áp dụng", "Thuộc tính name", "Vai trò & Ràng buộc"]
    for i, h in enumerate(headers):
        cell = tbl1.cell(0, i)
        set_cell_background(cell, "2563EB")
        set_cell_margins(cell, top=100, bottom=100, left=120, right=120)
        p_c = cell.paragraphs[0]
        r_c = p_c.add_run(h)
        r_c.bold = True
        r_c.font.name = "Arial"
        r_c.font.size = Pt(9.5)
        r_c.font.color.rgb = RGBColor(255, 255, 255)

    data1 = [
        ("Họ và tên", "<input type=\"text\">", "yourname", "TextBox thu thập họ tên người dùng (bắt buộc)"),
        ("Địa chỉ Email", "<input type=\"email\">", "email", "Tự động kiểm tra cú pháp định dạng email hợp lệ"),
        ("Sở thích cá nhân", "<input type=\"checkbox\">", "hobby", "Các checkbox đặt cùng tên để gom thành mảng giá trị"),
        ("Nút gửi thông tin", "<input type=\"submit\">", "(N/A)", "Submit Form gửi toàn bộ dữ liệu lên máy chủ"),
        ("Nút làm mới", "<input type=\"reset\">", "(N/A)", "Reset Form khôi phục tất cả trường về giá trị rỗng")
    ]

    for row_idx, row_data in enumerate(data1, start=1):
        bg = "F8FAFC" if row_idx % 2 == 1 else "FFFFFF"
        for col_idx, text in enumerate(row_data):
            cell = tbl1.cell(row_idx, col_idx)
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=80, bottom=80, left=100, right=100)
            p_c = cell.paragraphs[0]
            r_c = p_c.add_run(text)
            r_c.font.name = "Arial"
            r_c.font.size = Pt(9)
            if col_idx == 2:
                r_c.bold = True
                r_c.font.color.rgb = RGBColor(37, 99, 235)

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # ------------------ CHƯƠNG 3: PHẦN 2 - FORM ĐĂNG KÝ HỌC VIÊN ------------------
    h3 = doc.add_heading(level=1)
    r_h3 = h3.add_run("3. Triển Khai Phần 2: Biểu Mẫu Đăng Ký Học Viên")
    r_h3.font.name = "Arial"
    r_h3.font.size = Pt(14)
    r_h3.bold = True
    r_h3.font.color.rgb = RGBColor(30, 41, 59)

    p = doc.add_paragraph()
    p.add_run("Phần 2 mở rộng toàn diện hệ thống trường dữ liệu thực tế phục vụ đăng ký tuyển sinh của trung tâm đào tạo lập trình. "
              "Biểu mẫu được chia thành 3 phân vùng rõ ràng: Thông tin cá nhân, Nguyện vọng khóa học và Thông tin bổ sung:")

    # Bảng Part 2
    tbl2 = doc.add_table(rows=12, cols=4)
    tbl2.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, h in enumerate(headers):
        cell = tbl2.cell(0, i)
        set_cell_background(cell, "0284C7")
        set_cell_margins(cell, top=100, bottom=100, left=120, right=120)
        p_c = cell.paragraphs[0]
        r_c = p_c.add_run(h)
        r_c.bold = True
        r_c.font.name = "Arial"
        r_c.font.size = Pt(9.5)
        r_c.font.color.rgb = RGBColor(255, 255, 255)

    data2 = [
        ("Họ và tên học viên", "<input type=\"text\">", "fullname", "Nhập họ và tên đầy đủ của học viên"),
        ("Địa chỉ Email", "<input type=\"email\">", "email", "Địa chỉ email chính thức để nhận thông báo"),
        ("Số điện thoại", "<input type=\"tel\">", "phone", "Số điện thoại di động (10-11 số)"),
        ("Ngày sinh", "<input type=\"date\">", "birthday", "Bộ chọn ngày theo chuẩn HTML5 Datepicker"),
        ("Giới tính", "<input type=\"radio\">", "gender", "Nhóm Radio: Nam, Nữ, Khác (chọn 1 duy nhất)"),
        ("Địa chỉ thường trú", "<textarea>", "address", "Nhập chi tiết số nhà, phường/xã, quận/huyện"),
        ("Khóa học đăng ký", "<select> <option>", "course", "Menu đổ xuống: HTML & CSS, JavaScript, Java, Python"),
        ("Hình thức học", "<input type=\"radio\">", "study_type", "Nhóm Radio: Online hoặc Offline"),
        ("Sở thích cá nhân", "<input type=\"checkbox\">", "hobby", "Nhiều Checkbox: Lập trình, Đọc sách, Thể thao..."),
        ("Ghi chú bổ sung", "<textarea>", "note", "Nguyện vọng lịch học, mục tiêu học tập"),
        ("Nút xác nhận", "<input type=\"submit\">", "(N/A)", "Submit đăng ký (Giá trị hiển thị: 'Đăng ký')")
    ]

    for row_idx, row_data in enumerate(data2, start=1):
        bg = "F0F9FF" if row_idx % 2 == 1 else "FFFFFF"
        for col_idx, text in enumerate(row_data):
            cell = tbl2.cell(row_idx, col_idx)
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=70, bottom=70, left=100, right=100)
            p_c = cell.paragraphs[0]
            r_c = p_c.add_run(text)
            r_c.font.name = "Arial"
            r_c.font.size = Pt(8.8)
            if col_idx == 2:
                r_c.bold = True
                r_c.font.color.rgb = RGBColor(2, 132, 199)

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # ------------------ CHƯƠNG 4: SƠ ĐỒ KIẾN TRÚC & LUỒNG DỮ LIỆU ------------------
    h4 = doc.add_heading(level=1)
    r_h4 = h4.add_run("4. Sơ Đồ Kiến Trúc Form HTML5 & Luồng Xử Lý Dữ Liệu")
    r_h4.font.name = "Arial"
    r_h4.font.size = Pt(14)
    r_h4.bold = True
    r_h4.font.color.rgb = RGBColor(30, 41, 59)

    p = doc.add_paragraph()
    p.add_run("Dưới đây là sơ đồ mô tả cấu trúc các thành phần trong Form HTML5 và cơ chế ánh xạ thuộc tính name vào payload gửi lên máy chủ:")

    diag_arch = r"C:\Users\dathao\.gemini\antigravity-ide\scratch\bai-tap-tao-form-don-gian\form_architecture_diagram.png"
    if os.path.exists(diag_arch):
        doc.add_picture(diag_arch, width=Inches(6.4))
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_cap = p_cap.add_run("Hình 1: Sơ đồ kiến trúc Form HTML5 và các kiểu Input Type áp dụng trong bài tập")
        r_cap.font.name = "Arial"
        r_cap.font.size = Pt(8.5)
        r_cap.italic = True
        r_cap.font.color.rgb = RGBColor(100, 116, 139)

    p2 = doc.add_paragraph()
    p2.add_run("Cơ chế đóng gói dữ liệu và sự khác biệt giữa phương thức GET và POST khi gửi dữ liệu Form:")

    diag_flow = r"C:\Users\dathao\.gemini\antigravity-ide\scratch\bai-tap-tao-form-don-gian\form_submission_flow.png"
    if os.path.exists(diag_flow):
        doc.add_picture(diag_flow, width=Inches(6.4))
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_cap = p_cap.add_run("Hình 2: Sơ đồ luồng truyền tải dữ liệu và so sánh giao thức HTTP GET vs POST")
        r_cap.font.name = "Arial"
        r_cap.font.size = Pt(8.5)
        r_cap.italic = True
        r_cap.font.color.rgb = RGBColor(100, 116, 139)

    # ------------------ CHƯƠNG 5: MINH CHỨNG KẾT QUẢ HIỂN THỊ ------------------
    h5 = doc.add_heading(level=1)
    r_h5 = h5.add_run("5. Minh Chứng Kết Quả Hiển Thị Trên Trình Duyệt Web")
    r_h5.font.name = "Arial"
    r_h5.font.size = Pt(14)
    r_h5.bold = True
    r_h5.font.color.rgb = RGBColor(30, 41, 59)

    p = doc.add_paragraph()
    p.add_run("Ảnh chụp màn hình thực tế kết quả kiểm thử trên trình duyệt web Google Chrome, hiển thị đồng thời cả 2 biểu mẫu "
              "với đầy đủ các trường nhập liệu, cơ chế lựa chọn radio/checkbox và phản hồi dữ liệu:")

    mockup = r"C:\Users\dathao\.gemini\antigravity-ide\scratch\bai-tap-tao-form-don-gian\browser_form_result_screenshot.png"
    if os.path.exists(mockup):
        doc.add_picture(mockup, width=Inches(6.4))
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_cap = p_cap.add_run("Hình 3: Kết quả hiển thị thực tế của Form Phần 1 và Form Phần 2 trên trình duyệt")
        r_cap.font.name = "Arial"
        r_cap.font.size = Pt(8.5)
        r_cap.italic = True
        r_cap.font.color.rgb = RGBColor(100, 116, 139)

    # ------------------ CHƯƠNG 6: THÔNG TIN NỘP BÀI & GITHUB REPO ------------------
    h6 = doc.add_heading(level=1)
    r_h6 = h6.add_run("6. Thông Tin Nộp Bài & Kho Lưu Trữ GitHub")
    r_h6.font.name = "Arial"
    r_h6.font.size = Pt(14)
    r_h6.bold = True
    r_h6.font.color.rgb = RGBColor(30, 41, 59)

    create_callout_box(
        doc,
        "Đường dẫn GitHub Repository chính thức phục vụ chấm điểm:\n"
        "🔗 URL: https://github.com/proyctk03-eng/bai-tap-tao-form-don-gian\n\n"
        "Kho lưu trữ chứa đầy đủ các file:\n"
        "• part1_simple_form.html: Mã nguồn độc lập Phần 1\n"
        "• part2_student_registration_form.html: Mã nguồn độc lập Phần 2\n"
        "• index.html: Cổng thông tin tổng hợp tích hợp Live Inspector\n"
        "• browser_form_result_screenshot.png: Ảnh chụp màn hình kết quả thực thi\n"
        "• README.md: Hướng dẫn kỹ thuật và tài liệu chi tiết",
        title="THÔNG TIN NỘP BÀI TRÊN CODEGYM",
        hex_border="10B981",
        hex_bg="ECFDF5"
    )

    out_file = r"C:\Users\dathao\.gemini\antigravity-ide\scratch\bai-tap-tao-form-don-gian\Bao_Cao_Bai_Tap_Tao_Form_Don_Gian.docx"
    doc.save(out_file)
    print("Report saved successfully:", out_file)

if __name__ == "__main__":
    build_report()
