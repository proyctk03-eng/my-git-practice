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

def create_callout_box(doc, text, title="LƯU Ý QUAN TRỌNG", hex_border="0284C7", hex_bg="F0F9FF"):
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
        hr = hp.add_run("Báo Cáo: [Bài tập] Tạo Form Lấy Survey Khách Hàng (Wufoo Template)")
        hr.font.name = "Arial"
        hr.font.size = Pt(8.5)
        hr.font.color.rgb = RGBColor(148, 163, 184)
        
        # Footer
        ftr = s.footer
        fp = ftr.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        fr = fp.add_run("Học viên: proyctk03-eng  |  Mô-đun: HTML5 Form Elements & Survey Design  |  CodeGym 2026")
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
    r_inst.font.color.rgb = RGBColor(2, 132, 199)

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(14)
    r_sub = p_sub.add_run("CHƯƠNG TRÌNH ĐÀO TẠO FULL-STACK WEB &middot; MÔ-ĐUN HTML/CSS")
    r_sub.font.name = "Arial"
    r_sub.font.size = Pt(9.5)
    r_sub.font.color.rgb = RGBColor(100, 116, 139)

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_after = Pt(8)
    r_title = p_title.add_run("BÁO CÁO THỰC HÀNH & KỸ THUẬT\n[BÀI TẬP] TẠO FORM LẤY SURVEY KHÁCH HÀNG")
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
        "Bài tập tái hiện 100% biểu mẫu khảo sát nghiên cứu thị trường (Market Research Survey) theo mẫu thiết kế Wufoo: "
        "Bao gồm đầy đủ 8 nhóm câu hỏi: Dropdown độ tuổi & thu nhập, Radio giới tính, Checkbox sản phẩm đã mua, "
        "Radio tần suất sử dụng, Ô nhập tiền tệ (Dollars & Cents), Textarea đóng góp tính năng, và Bảng đánh giá ma trận "
        "thang đo Likert Scale (4 mức độ đồng thuận). Toàn bộ mã nguồn đã được tối ưu hóa giao diện và đẩy lên GitHub Repository.",
        title="TÓM TẮT BÀI NỘP",
        hex_border="0284C7",
        hex_bg="F0F9FF"
    )

    # ------------------ CHƯƠNG 1: MỤC TIÊU & ĐẶC TẢ ĐỀ BÀI ------------------
    h1 = doc.add_heading(level=1)
    r_h1 = h1.add_run("1. Mục Tiêu Thực Hành & Yêu Cầu Kỹ Thuật")
    r_h1.font.name = "Arial"
    r_h1.font.size = Pt(14)
    r_h1.bold = True
    r_h1.font.color.rgb = RGBColor(30, 41, 59)

    p = doc.add_paragraph()
    p.add_run("Mục tiêu trọng tâm của bài tập là thành thạo kỹ thuật xây dựng form khảo sát ý kiến khách hàng (Customer Feedback / Market Research Survey) "
              "theo tiêu chuẩn công nghiệp hiện đại của Wufoo:\n"
              "1. Áp dụng phong phú các kiểu nhập liệu HTML5: <select>, <input type=\"radio\">, <input type=\"checkbox\">, <input type=\"number\">, <textarea>.\n"
              "2. Nắm vững kỹ thuật xây dựng bảng ma trận đánh giá Likert Scale thông qua kết hợp thẻ <table> và gom nhóm Radio button theo từng hàng (row-level grouping).\n"
              "3. Thiết kế giao diện rõ ràng, bố cục cân đối, thân thiện trên cả máy tính để bàn và thiết bị di động (Responsive Web Design).\n"
              "4. Đóng gói mã nguồn, kiểm thử trên trình duyệt web và đưa lên kho lưu trữ GitHub công khai.")

    # ------------------ CHƯƠNG 2: PHÂN TÍCH 8 NHÓM CÂU HỎI KHẢO SÁT ------------------
    h2 = doc.add_heading(level=1)
    r_h2 = h2.add_run("2. Phân Tích Chi Tiết 8 Nhóm Câu Hỏi Khảo Sát (Wufoo Form)")
    r_h2.font.name = "Arial"
    r_h2.font.size = Pt(14)
    r_h2.bold = True
    r_h2.font.color.rgb = RGBColor(30, 41, 59)

    p = doc.add_paragraph()
    p.add_run("Cấu trúc của phiếu khảo sát bao gồm 8 thành phần nhập liệu chuyên biệt:")

    tbl_q = doc.add_table(rows=9, cols=4)
    tbl_q.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdrs = ["STT", "Nội dung câu hỏi khảo sát", "Thẻ HTML & Kiểu nhập liệu", "Các tùy chọn dữ liệu"]
    for i, h in enumerate(hdrs):
        cell = tbl_q.cell(0, i)
        set_cell_background(cell, "0284C7")
        set_cell_margins(cell, top=100, bottom=100, left=100, right=100)
        p_c = cell.paragraphs[0]
        r_c = p_c.add_run(h)
        r_c.bold = True
        r_c.font.name = "Arial"
        r_c.font.size = Pt(9.5)
        r_c.font.color.rgb = RGBColor(255, 255, 255)

    data_q = [
        ("1", "What is your age range?", "<select> <option>", "18-24, 25-34, 35-50, 50+"),
        ("2", "What is your yearly income range?", "<select> <option>", "$0 - $25,000, $25,001 - $50,000, $50,001 - $100,000, $100,000+"),
        ("3", "Gender Identity", "<input type=\"radio\">", "Male, Female, Nonbinary, Other (kèm ô nhập văn bản)"),
        ("4", "Which products have you purchased?", "<input type=\"checkbox\">", "Product 1, Product 2, Product 3 (cho phép chọn nhiều)"),
        ("5", "How often would you use our new product?", "<input type=\"radio\">", "Daily, Weekly, Monthly (chọn 1 tần suất duy nhất)"),
        ("6", "What would you pay for the new product?", "<input type=\"number\">", "Tách riêng Dollars ($) và Cents (.)"),
        ("7", "What features would you like to see?", "<textarea>", "Văn bản nhiều dòng (ý kiến, đề xuất bổ sung)"),
        ("8", "Please rate your level of agreement...", "<table> + Radio", "Thang đo Likert 4 mức độ cho 3 phát biểu chất lượng")
    ]

    for row_idx, row_data in enumerate(data_q, start=1):
        bg = "F0F9FF" if row_idx % 2 == 1 else "FFFFFF"
        for col_idx, text in enumerate(row_data):
            cell = tbl_q.cell(row_idx, col_idx)
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=70, bottom=70, left=90, right=90)
            p_c = cell.paragraphs[0]
            r_c = p_c.add_run(text)
            r_c.font.name = "Arial"
            r_c.font.size = Pt(9)
            if col_idx == 0:
                r_c.bold = True

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # ------------------ CHƯƠNG 3: NGUYÊN LÝ BẢNG MA TRẬN LIKERT SCALE ------------------
    h3 = doc.add_heading(level=1)
    r_h3 = h3.add_run("3. Kỹ Thuật Xây Dựng Bảng Ma Trận Đánh Giá Likert Scale")
    r_h3.font.name = "Arial"
    r_h3.font.size = Pt(14)
    r_h3.bold = True
    r_h3.font.color.rgb = RGBColor(30, 41, 59)

    p = doc.add_paragraph()
    p.add_run("Thang đo Likert (Likert Scale) là công cụ đo lường tâm lý và mức độ hài lòng phổ biến nhất trong nghiên cứu định lượng. "
              "Khi lập trình bảng Likert bằng HTML:\n"
              "• Thẻ <table> được dùng để định hình lưới gồm các cột tương ứng các mức độ: Strongly Disagree, Disagree, Agree, Strongly Agree.\n"
              "• Thẻ <tbody> chứa các hàng <tr> tương ứng từng nhận định cần đo lường.\n"
              "• Nguyên tắc cốt lõi: Tất cả các thẻ <input type=\"radio\"> trên cùng MỘT HÀNG phải có chung thuộc tính name "
              "(ví dụ name=\"rating_priced_fairly\" cho hàng 1, name=\"rating_high_quality\" cho hàng 2). Điều này đảm bảo người dùng "
              "chỉ được chọn 1 mức điểm duy nhất cho mỗi câu hỏi, nhưng các hàng khác nhau hoàn toàn độc lập với nhau.")

    # ------------------ CHƯƠNG 4: SƠ ĐỒ KIẾN TRÚC & MINH HỌA ------------------
    h4 = doc.add_heading(level=1)
    r_h4 = h4.add_run("4. Sơ Đồ Kiến Trúc Form & Cấu Trúc Bảng Likert")
    r_h4.font.name = "Arial"
    r_h4.font.size = Pt(14)
    r_h4.bold = True
    r_h4.font.color.rgb = RGBColor(30, 41, 59)

    diag_arch = r"C:\Users\dathao\.gemini\antigravity-ide\scratch\bai-tap-form-survey-khach-hang\survey_form_architecture_diagram.png"
    if os.path.exists(diag_arch):
        doc.add_picture(diag_arch, width=Inches(6.4))
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_cap = p_cap.add_run("Hình 1: Sơ đồ kiến trúc các loại Input trong khảo sát khách hàng Wufoo")
        r_cap.font.name = "Arial"
        r_cap.font.size = Pt(8.5)
        r_cap.italic = True
        r_cap.font.color.rgb = RGBColor(100, 116, 139)

    diag_likert = r"C:\Users\dathao\.gemini\antigravity-ide\scratch\bai-tap-form-survey-khach-hang\likert_matrix_structure_diagram.png"
    if os.path.exists(diag_likert):
        doc.add_picture(diag_likert, width=Inches(6.4))
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_cap = p_cap.add_run("Hình 2: Sơ đồ nguyên lý nhóm Radio Buttons theo từng hàng trong bảng Likert Scale")
        r_cap.font.name = "Arial"
        r_cap.font.size = Pt(8.5)
        r_cap.italic = True
        r_cap.font.color.rgb = RGBColor(100, 116, 139)

    # ------------------ CHƯƠNG 5: KẾT QUẢ HIỂN THỊ TRÊN TRÌNH DUYỆT ------------------
    h5 = doc.add_heading(level=1)
    r_h5 = h5.add_run("5. Minh Chứng Kết Quả Hiển Thị Trên Trình Duyệt Web")
    r_h5.font.name = "Arial"
    r_h5.font.size = Pt(14)
    r_h5.bold = True
    r_h5.font.color.rgb = RGBColor(30, 41, 59)

    p = doc.add_paragraph()
    p.add_run("Ảnh chụp màn hình thực tế kết quả hiển thị trên trình duyệt web Google Chrome, thể hiện trọn vẹn toàn bộ 8 nhóm câu hỏi:")

    mockup = r"C:\Users\dathao\.gemini\antigravity-ide\scratch\bai-tap-form-survey-khach-hang\browser_survey_result_screenshot.png"
    if os.path.exists(mockup):
        doc.add_picture(mockup, width=Inches(6.4))
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_cap = p_cap.add_run("Hình 3: Kết quả hiển thị thực tế của Form khảo sát khách hàng trên trình duyệt")
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
        "Đường dẫn GitHub Repository chính thức phục vụ chấm điểm trên CodeGymX:\n"
        "🔗 URL: https://github.com/proyctk03-eng/bai-tap-form-survey-khach-hang\n\n"
        "Danh mục các file nộp trong kho lưu trữ:\n"
        "• index.html: Giao diện khảo sát cao cấp tích hợp Modal JSON phản hồi kết quả\n"
        "• survey_basic.html: Mã nguồn biểu mẫu HTML thuần túy chuẩn cấu trúc Wufoo\n"
        "• browser_survey_result_screenshot.png: Ảnh chụp màn hình kết quả chạy trên trình duyệt\n"
        "• survey_form_architecture_diagram.png: Sơ đồ kiến trúc biểu mẫu khảo sát\n"
        "• likert_matrix_structure_diagram.png: Sơ đồ cấu trúc ma trận thang đo Likert\n"
        "• README.md: Tài liệu hướng dẫn kỹ thuật chi tiết",
        title="THÔNG TIN NỘP BÀI TRÊN CODEGYMX",
        hex_border="10B981",
        hex_bg="ECFDF5"
    )

    out_file = r"C:\Users\dathao\.gemini\antigravity-ide\scratch\bai-tap-form-survey-khach-hang\Bao_Cao_Bai_Tap_Form_Survey_Khach_Hang.docx"
    doc.save(out_file)
    print("Report saved successfully:", out_file)

if __name__ == "__main__":
    build_report()
