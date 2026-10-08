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
        hr = hp.add_run("Báo Cáo: [Bài tập] Tạo Giao Diện Form Đăng Ký Người Dùng (HTTP POST)")
        hr.font.name = "Arial"
        hr.font.size = Pt(8.5)
        hr.font.color.rgb = RGBColor(148, 163, 184)
        
        # Footer
        ftr = s.footer
        fp = ftr.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        fr = fp.add_run("Học viên: proyctk03-eng  |  Mô-đun: HTML5 Form Elements & HTTP POST  |  CodeGym 2026")
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
    r_sub = p_sub.add_run("CHƯƠNG TRÌNH ĐÀO TẠO PHÁT TRIỂN WEB FULL-STACK &middot; MÔ-ĐUN HTML & CSS")
    r_sub.font.name = "Arial"
    r_sub.font.size = Pt(9.5)
    r_sub.font.color.rgb = RGBColor(100, 116, 139)

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_after = Pt(8)
    r_title = p_title.add_run("BÁO CÁO THỰC HÀNH & KỸ THUẬT\n[BÀI TẬP] TẠO GIAO DIỆN FORM ĐĂNG KÝ NGƯỜI DÙNG")
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
        "Bài tập cài đặt đầy đủ biểu mẫu đăng ký người dùng với phương thức bắt buộc POST gửi lên địa chỉ: "
        "http://demo.codegym.vn/6/registration_form/register.php. Thiết lập chính xác 4 trường dữ liệu theo đúng "
        "đặc tả: Họ và tên (name=\"name\"), Email (name=\"email\"), Số điện thoại (name=\"phone\"), Giới tính (name=\"gender\"). "
        "Mã nguồn đã được đẩy lên kho lưu trữ GitHub công khai và đính kèm đầy đủ tài liệu, minh chứng kiểm thử.",
        title="TÓM TẮT KẾT QUẢ TRIỂN KHAI",
        hex_border="2563EB",
        hex_bg="EFF6FF"
    )

    # ------------------ CHƯƠNG 1: MỤC TIÊU & ĐẶC TẢ ĐỀ BÀI ------------------
    h1 = doc.add_heading(level=1)
    r_h1 = h1.add_run("1. Mục Tiêu Thực Hành & Yêu Cầu Kỹ Thuật")
    r_h1.font.name = "Arial"
    r_h1.font.size = Pt(14)
    r_h1.bold = True
    r_h1.font.color.rgb = RGBColor(30, 41, 59)

    p = doc.add_paragraph()
    p.add_run("Mục tiêu bài học nhằm giúp học viên nắm chắc kỹ năng xây dựng biểu mẫu đăng ký thành viên trên trang web "
              "và hiểu sâu sắc cơ chế hoạt động của giao thức truyền tải dữ liệu HTTP POST:\n"
              "1. Thuộc tính action: Chỉ định endpoint máy chủ tiếp nhận dữ liệu là http://demo.codegym.vn/6/registration_form/register.php.\n"
              "2. Thuộc tính method=\"POST\": Bắt buộc sử dụng phương thức POST để bảo mật thông tin và đóng gói tham số vào Request Body.\n"
              "3. Thuộc tính name: Định danh khóa dữ liệu chính xác để máy chủ phía backend đọc được qua mảng $_POST (name, email, phone, gender).\n"
              "4. Trải nghiệm người dùng: Bố cục form cân đối, trường nhập liệu có nhãn rõ ràng, hỗ trợ radio button chọn giới tính và nút submit nổi bật.")

    # ------------------ CHƯƠNG 2: PHÂN TÍCH GIAO THỨC HTTP POST ------------------
    h2 = doc.add_heading(level=1)
    r_h2 = h2.add_run("2. Phân Tích Giao Thức HTTP POST & Cơ Chế Đóng Gói Dữ Liệu")
    r_h2.font.name = "Arial"
    r_h2.font.size = Pt(14)
    r_h2.bold = True
    r_h2.font.color.rgb = RGBColor(30, 41, 59)

    p = doc.add_paragraph()
    p.add_run("Trong phát triển ứng dụng Web, phương thức POST đóng vai trò nền tảng khi người dùng gửi các thông tin nhạy cảm, "
              "thông tin tạo mới tài khoản hoặc biểu mẫu có kích thước lớn:")

    # Bảng so sánh GET và POST
    tbl_cmp = doc.add_table(rows=5, cols=3)
    tbl_cmp.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdrs = ["Tiêu chí so sánh", "Phương thức GET", "Phương thức POST (Áp dụng trong bài)"]
    for i, h in enumerate(hdrs):
        cell = tbl_cmp.cell(0, i)
        set_cell_background(cell, "1E293B")
        set_cell_margins(cell, top=100, bottom=100, left=120, right=120)
        p_c = cell.paragraphs[0]
        r_c = p_c.add_run(h)
        r_c.bold = True
        r_c.font.name = "Arial"
        r_c.font.size = Pt(9.5)
        r_c.font.color.rgb = RGBColor(255, 255, 255)

    data_cmp = [
        ("Vị trí chứa dữ liệu", "Gắn trực tiếp vào URL sau dấu hỏi (?)", "Đóng gói ẩn bên trong HTTP Request Body"),
        ("Mức độ an toàn", "Kém: Lộ dữ liệu trên URL, lưu lịch sử duyệt", "Cao: Không hiển thị trên thanh địa chỉ trình duyệt"),
        ("Giới hạn kích thước", "Bị giới hạn bởi độ dài URL (~2048 ký tự)", "Không bị giới hạn dung lượng, hỗ trợ gửi tệp"),
        ("Mục đích phù hợp", "Tìm kiếm, lọc dữ liệu, phân trang (Search)", "Đăng ký tài khoản, đăng nhập, thanh toán, upload")
    ]

    for row_idx, row_data in enumerate(data_cmp, start=1):
        bg = "F8FAFC" if row_idx % 2 == 1 else "FFFFFF"
        for col_idx, text in enumerate(row_data):
            cell = tbl_cmp.cell(row_idx, col_idx)
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=80, bottom=80, left=100, right=100)
            p_c = cell.paragraphs[0]
            r_c = p_c.add_run(text)
            r_c.font.name = "Arial"
            r_c.font.size = Pt(9)
            if col_idx == 0:
                r_c.bold = True

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # ------------------ CHƯƠNG 3: BẢNG ÁNH XẠ THUỘC TÍNH FORM ------------------
    h3 = doc.add_heading(level=1)
    r_h3 = h3.add_run("3. Bảng Ánh Xạ Thuộc Tính Form & Ràng Buộc Kỹ Thuật")
    r_h3.font.name = "Arial"
    r_h3.font.size = Pt(14)
    r_h3.bold = True
    r_h3.font.color.rgb = RGBColor(30, 41, 59)

    p = doc.add_paragraph()
    p.add_run("Các trường thông tin được thiết lập chính xác theo từng thẻ HTML và thuộc tính name:")

    tbl_fields = doc.add_table(rows=6, cols=5)
    tbl_fields.alignment = WD_TABLE_ALIGNMENT.CENTER
    headers_f = ["STT", "Trường thông tin", "Thuộc tính name", "Thẻ HTML & Kiểu", "Giá trị & Ràng buộc"]
    for i, h in enumerate(headers_f):
        cell = tbl_fields.cell(0, i)
        set_cell_background(cell, "2563EB")
        set_cell_margins(cell, top=100, bottom=100, left=100, right=100)
        p_c = cell.paragraphs[0]
        r_c = p_c.add_run(h)
        r_c.bold = True
        r_c.font.name = "Arial"
        r_c.font.size = Pt(9.5)
        r_c.font.color.rgb = RGBColor(255, 255, 255)

    data_fields = [
        ("1", "Họ và tên", "name", "<input type=\"text\">", "Bắt buộc (required), text họ và tên"),
        ("2", "Địa chỉ Email", "email", "<input type=\"email\">", "Bắt buộc (required), kiểm tra định dạng email"),
        ("3", "Số điện thoại", "phone", "<input type=\"tel\">", "Bắt buộc (required), pattern regex 10-11 số"),
        ("4", "Giới tính", "gender", "<input type=\"radio\">", "Cùng name=\"gender\", value: Nam / Nữ"),
        ("5", "Nút xác nhận", "(N/A)", "<button type=\"submit\">", "Kích hoạt submit toàn bộ gói tin POST")
    ]

    for row_idx, row_data in enumerate(data_fields, start=1):
        bg = "EFF6FF" if row_idx % 2 == 1 else "FFFFFF"
        for col_idx, text in enumerate(row_data):
            cell = tbl_fields.cell(row_idx, col_idx)
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=70, bottom=70, left=90, right=90)
            p_c = cell.paragraphs[0]
            r_c = p_c.add_run(text)
            r_c.font.name = "Arial"
            r_c.font.size = Pt(9)
            if col_idx == 2:
                r_c.bold = True
                r_c.font.color.rgb = RGBColor(37, 99, 235)

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # ------------------ CHƯƠNG 4: SƠ ĐỒ KIẾN TRÚC & MINH CHỨNG ------------------
    h4 = doc.add_heading(level=1)
    r_h4 = h4.add_run("4. Sơ Đồ Kiến Trúc & Luồng Dữ Liệu HTTP POST")
    r_h4.font.name = "Arial"
    r_h4.font.size = Pt(14)
    r_h4.bold = True
    r_h4.font.color.rgb = RGBColor(30, 41, 59)

    diag_post = r"C:\Users\dathao\.gemini\antigravity-ide\scratch\bai-tap-form-dang-ky-nguoi-dung\http_post_architecture_diagram.png"
    if os.path.exists(diag_post):
        doc.add_picture(diag_post, width=Inches(6.4))
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_cap = p_cap.add_run("Hình 1: Sơ đồ kiến trúc gói tin HTTP POST và tiếp nhận tại Server CodeGym")
        r_cap.font.name = "Arial"
        r_cap.font.size = Pt(8.5)
        r_cap.italic = True
        r_cap.font.color.rgb = RGBColor(100, 116, 139)

    diag_map = r"C:\Users\dathao\.gemini\antigravity-ide\scratch\bai-tap-form-dang-ky-nguoi-dung\form_fields_mapping_diagram.png"
    if os.path.exists(diag_map):
        doc.add_picture(diag_map, width=Inches(6.4))
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_cap = p_cap.add_run("Hình 2: Sơ đồ ánh xạ thuộc tính name của form vào biến máy chủ backend PHP")
        r_cap.font.name = "Arial"
        r_cap.font.size = Pt(8.5)
        r_cap.italic = True
        r_cap.font.color.rgb = RGBColor(100, 116, 139)

    # ------------------ CHƯƠNG 5: KẾT QUẢ HIỂN THỊ TRÊN TRÌNH DUYỆT ------------------
    h5 = doc.add_heading(level=1)
    r_h5 = h5.add_run("5. Kết Quả Hiển Thị Thực Tế Trên Trình Duyệt Web")
    r_h5.font.name = "Arial"
    r_h5.font.size = Pt(14)
    r_h5.bold = True
    r_h5.font.color.rgb = RGBColor(30, 41, 59)

    p = doc.add_paragraph()
    p.add_run("Ảnh chụp màn hình thực tế giao diện form đăng ký và bảng phân tích HTTP POST Payload Inspector:")

    mockup = r"C:\Users\dathao\.gemini\antigravity-ide\scratch\bai-tap-form-dang-ky-nguoi-dung\browser_register_form_screenshot.png"
    if os.path.exists(mockup):
        doc.add_picture(mockup, width=Inches(6.4))
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_cap = p_cap.add_run("Hình 3: Giao diện form đăng ký người dùng và bộ công cụ kiểm thử Live Inspector")
        r_cap.font.name = "Arial"
        r_cap.font.size = Pt(8.5)
        r_cap.italic = True
        r_cap.font.color.rgb = RGBColor(100, 116, 139)

    # ------------------ CHƯƠNG 6: THÔNG TIN NỘP BÀI GITHUB ------------------
    h6 = doc.add_heading(level=1)
    r_h6 = h6.add_run("6. Thông Tin Nộp Bài & Kho Lưu Trữ GitHub")
    r_h6.font.name = "Arial"
    r_h6.font.size = Pt(14)
    r_h6.bold = True
    r_h6.font.color.rgb = RGBColor(30, 41, 59)

    create_callout_box(
        doc,
        "Đường dẫn GitHub Repository nộp bài trên hệ thống CodeGymX:\n"
        "🔗 URL: https://github.com/proyctk03-eng/bai-tap-form-dang-ky-nguoi-dung\n\n"
        "Danh mục các file nộp trong kho lưu trữ:\n"
        "• index.html: Giao diện form đăng ký tương tác kèm Live Inspector\n"
        "• register_basic.html: Mã nguồn form HTML cơ bản thuần túy\n"
        "• browser_register_form_screenshot.png: Ảnh chụp màn hình kết quả chạy trên trình duyệt\n"
        "• http_post_architecture_diagram.png: Sơ đồ kiến trúc giao thức HTTP POST\n"
        "• form_fields_mapping_diagram.png: Sơ đồ ánh xạ thuộc tính name\n"
        "• README.md: Tài liệu hướng dẫn chi tiết",
        title="THÔNG TIN NỘP BÀI TRÊN CODEGYMX",
        hex_border="10B981",
        hex_bg="ECFDF5"
    )

    out_file = r"C:\Users\dathao\.gemini\antigravity-ide\scratch\bai-tap-form-dang-ky-nguoi-dung\Bao_Cao_Bai_Tap_Form_Dang_Ky_Nguoi_Dung.docx"
    doc.save(out_file)
    print("Report saved successfully:", out_file)

if __name__ == "__main__":
    build_report()
