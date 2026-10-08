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
        hr = hp.add_run("Báo Cáo: [Bài tập] Tạo Bảng Danh Sách Sản Phẩm Trong HTML")
        hr.font.name = "Arial"
        hr.font.size = Pt(8.5)
        hr.font.color.rgb = RGBColor(148, 163, 184)
        
        # Footer
        ftr = s.footer
        fp = ftr.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        fr = fp.add_run("Học viên: proyctk03-eng  |  Mô-đun: HTML Table Structure  |  CodeGym 2026")
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
    r_sub = p_sub.add_run("CHƯƠNG TRÌNH ĐÀO TẠO FULL-STACK WEB &middot; MÔ-ĐUN HTML/CSS CƠ BẢN")
    r_sub.font.name = "Arial"
    r_sub.font.size = Pt(9.5)
    r_sub.font.color.rgb = RGBColor(100, 116, 139)

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_after = Pt(8)
    r_title = p_title.add_run("BÁO CÁO THỰC HÀNH & KỸ THUẬT\n[BÀI TẬP] TẠO BẢNG DANH SÁCH SẢN PHẨM TRONG HTML")
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
        "Bài tập triển khai hoàn chỉnh bảng dữ liệu danh sách sản phẩm trong tệp index.html theo đúng yêu cầu đề bài: "
        "Bao gồm thẻ tiêu đề <h1> 'Danh sách sản phẩm', bảng dữ liệu chuẩn cấu trúc <table> chứa 3 cột: 'Tên sản phẩm', "
        "'Giá', 'Số lượng', và hiển thị 5 mẫu sản phẩm công nghệ (vượt mức yêu cầu tối thiểu 4 sản phẩm). "
        "Mã nguồn đã được đưa lên kho lưu trữ GitHub công khai và tích hợp đầy đủ tài liệu hướng dẫn.",
        title="TÓM TẮT BÀI NỘP",
        hex_border="0284C7",
        hex_bg="F0F9FF"
    )

    # ------------------ CHƯƠNG 1: MỤC TIÊU & ĐẶC TẢ ĐỀ BÀI ------------------
    h1 = doc.add_heading(level=1)
    r_h1 = h1.add_run("1. Mục Tiêu Thực Hành & Yêu Cầu Đề Bài")
    r_h1.font.name = "Arial"
    r_h1.font.size = Pt(14)
    r_h1.bold = True
    r_h1.font.color.rgb = RGBColor(30, 41, 59)

    p = doc.add_paragraph()
    p.add_run("Mục tiêu bài học nhằm giúp học viên nắm vững kỹ năng sử dụng bảng trong HTML để hiển thị dữ liệu dạng bảng (tabular data):\n"
              "1. Tên tệp chính: Tạo một tệp mới có tên index.html.\n"
              "2. Tiêu đề chính: Thêm vào trong thẻ <body> một tiêu đề <h1> với nội dung chính xác: \"Danh sách sản phẩm\".\n"
              "3. Cấu trúc bảng: Một bảng HTML chứa 3 cột dữ liệu lần lượt là: Tên sản phẩm, Giá, Số lượng.\n"
              "4. Số lượng bản ghi: Thêm ít nhất 4 sản phẩm vào bảng.\n"
              "5. Nộp bài: Đưa mã nguồn lên GitHub Repository và nộp đường dẫn URL trên hệ thống CodeGym.")

    # ------------------ CHƯƠNG 2: KIẾN TRÚC THẺ BẢNG HTML5 ------------------
    h2 = doc.add_heading(level=1)
    r_h2 = h2.add_run("2. Kiến Trúc & Phân Cấp Thẻ Bảng HTML5")
    r_h2.font.name = "Arial"
    r_h2.font.size = Pt(14)
    r_h2.bold = True
    r_h2.font.color.rgb = RGBColor(30, 41, 59)

    p = doc.add_paragraph()
    p.add_run("Bảng trong HTML5 được xây dựng dựa trên mô hình phân cấp thẻ rõ ràng, đảm bảo tính ngữ nghĩa (semantic HTML):")

    tbl_tags = doc.add_table(rows=8, cols=3)
    tbl_tags.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdrs = ["Thẻ HTML", "Tên đầy đủ & Cấp bậc", "Chức năng trong bảng sản phẩm"]
    for i, h in enumerate(hdrs):
        cell = tbl_tags.cell(0, i)
        set_cell_background(cell, "0284C7")
        set_cell_margins(cell, top=100, bottom=100, left=100, right=100)
        p_c = cell.paragraphs[0]
        r_c = p_c.add_run(h)
        r_c.bold = True
        r_c.font.name = "Arial"
        r_c.font.size = Pt(9.5)
        r_c.font.color.rgb = RGBColor(255, 255, 255)

    data_tags = [
        ("<table>", "Table (Thẻ gốc)", "Bao bọc toàn bộ cấu trúc bảng hiển thị sản phẩm"),
        ("<thead>", "Table Header Section", "Phần đầu bảng chứa hàng tiêu đề các cột"),
        ("<tbody>", "Table Body Section", "Phần thân bảng chứa các dòng sản phẩm thực tế"),
        ("<tfoot>", "Table Footer Section", "Phần chân bảng hiển thị dòng tổng kết tồn kho"),
        ("<tr>", "Table Row", "Định nghĩa một hàng trong bảng"),
        ("<th>", "Table Header Cell", "Ô tiêu đề cột (in đậm, căn giữa/trái mặc định): Tên sản phẩm, Giá, Số lượng"),
        ("<td>", "Table Data Cell", "Ô dữ liệu chi tiết cho từng thuộc tính của sản phẩm")
    ]

    for row_idx, row_data in enumerate(data_tags, start=1):
        bg = "F0F9FF" if row_idx % 2 == 1 else "FFFFFF"
        for col_idx, text in enumerate(row_data):
            cell = tbl_tags.cell(row_idx, col_idx)
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=70, bottom=70, left=90, right=90)
            p_c = cell.paragraphs[0]
            r_c = p_c.add_run(text)
            r_c.font.name = "Arial"
            r_c.font.size = Pt(9)
            if col_idx == 0:
                r_c.bold = True
                r_c.font.color.rgb = RGBColor(2, 132, 199)

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # ------------------ CHƯƠNG 3: DỮ LIỆU SẢN PHẨM THỰC TẾ ------------------
    h3 = doc.add_heading(level=1)
    r_h3 = h3.add_run("3. Dữ Liệu Sản Phẩm & Trình Bày Chuẩn Chuyên Nghiệp")
    r_h3.font.name = "Arial"
    r_h3.font.size = Pt(14)
    r_h3.bold = True
    r_h3.font.color.rgb = RGBColor(30, 41, 59)

    p = doc.add_paragraph()
    p.add_run("Bảng sản phẩm được thiết lập 5 bản ghi sản phẩm công nghệ cao cấp kèm quy tắc căn chỉnh tài chính chuẩn:")

    tbl_prod = doc.add_table(rows=7, cols=4)
    tbl_prod.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdrs_p = ["STT", "Tên sản phẩm", "Giá (VNĐ)", "Số lượng"]
    for i, h in enumerate(hdrs_p):
        cell = tbl_prod.cell(0, i)
        set_cell_background(cell, "1E293B")
        set_cell_margins(cell, top=100, bottom=100, left=100, right=100)
        p_c = cell.paragraphs[0]
        r_c = p_c.add_run(h)
        r_c.bold = True
        r_c.font.name = "Arial"
        r_c.font.size = Pt(9.5)
        r_c.font.color.rgb = RGBColor(255, 255, 255)

    data_prod = [
        ("1", "iPhone 16 Pro Max 256GB", "34.990.000 đ", "15 chiếc"),
        ("2", "MacBook Pro 14\" M3 Pro", "49.990.000 đ", "8 chiếc"),
        ("3", "iPad Pro 11\" M4 Ultra Retina", "28.500.000 đ", "20 chiếc"),
        ("4", "AirPods Pro Gen 2 USB-C", "5.990.000 đ", "35 chiếc"),
        ("5", "Apple Watch Series 10 GPS", "10.990.000 đ", "12 chiếc"),
        ("Tổng", "Tổng cộng tồn kho (5 mẫu sản phẩm)", "130.460.000 đ", "90 chiếc")
    ]

    for row_idx, row_data in enumerate(data_prod, start=1):
        bg = "F8FAFC" if row_idx % 2 == 1 else "FFFFFF"
        if row_idx == 6:
            bg = "EFF6FF"
        for col_idx, text in enumerate(row_data):
            cell = tbl_prod.cell(row_idx, col_idx)
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=70, bottom=70, left=90, right=90)
            p_c = cell.paragraphs[0]
            r_c = p_c.add_run(text)
            r_c.font.name = "Arial"
            r_c.font.size = Pt(9)
            if row_idx == 6 or col_idx == 1:
                r_c.bold = True

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # ------------------ CHƯƠNG 4: SƠ ĐỒ KIẾN TRÚC & MINH HỌA ------------------
    h4 = doc.add_heading(level=1)
    r_h4 = h4.add_run("4. Sơ Đồ Kiến Trúc Bảng HTML & Phân Cấp Dữ Liệu")
    r_h4.font.name = "Arial"
    r_h4.font.size = Pt(14)
    r_h4.bold = True
    r_h4.font.color.rgb = RGBColor(30, 41, 59)

    diag_arch = r"C:\Users\dathao\.gemini\antigravity-ide\scratch\bai-tap-tao-bang-danh-sach-san-pham\html_table_product_structure.png"
    if os.path.exists(diag_arch):
        doc.add_picture(diag_arch, width=Inches(6.4))
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_cap = p_cap.add_run("Hình 1: Sơ đồ kiến trúc phân cấp thẻ bảng HTML: table, thead, tbody, tfoot, tr, th, td")
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
    p.add_run("Ảnh chụp màn hình thực tế kết quả hiển thị trên trình duyệt web Google Chrome, thể hiện tiêu đề <h1> Danh sách sản phẩm và bảng dữ liệu:")

    mockup = r"C:\Users\dathao\.gemini\antigravity-ide\scratch\bai-tap-tao-bang-danh-sach-san-pham\browser_product_table_screenshot.png"
    if os.path.exists(mockup):
        doc.add_picture(mockup, width=Inches(6.4))
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_cap = p_cap.add_run("Hình 2: Kết quả hiển thị thực tế của bảng danh sách sản phẩm trên trình duyệt")
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
        "Đường dẫn GitHub Repository chính thức phục vụ chấm điểm trên CodeGym:\n"
        "🔗 URL: https://github.com/proyctk03-eng/bai-tap-tao-bang-danh-sach-san-pham\n\n"
        "Danh mục các file nộp trong kho lưu trữ:\n"
        "• index.html: Tệp chính theo đề bài, giao diện bảng sản phẩm hiện đại tích hợp Live Search\n"
        "• index_basic.html: Phiên bản bảng HTML thuần túy tối giản không chứa CSS\n"
        "• browser_product_table_screenshot.png: Ảnh chụp màn hình kết quả chạy trên trình duyệt\n"
        "• html_table_product_structure.png: Sơ đồ kiến trúc cấu trúc thẻ bảng\n"
        "• README.md: Tài liệu hướng dẫn kỹ thuật chi tiết",
        title="THÔNG TIN NỘP BÀI TRÊN CODEGYM",
        hex_border="10B981",
        hex_bg="ECFDF5"
    )

    out_file = r"C:\Users\dathao\.gemini\antigravity-ide\scratch\bai-tap-tao-bang-danh-sach-san-pham\Bao_Cao_Bai_Tap_Tao_Bang_Danh_Sach_San_Pham.docx"
    doc.save(out_file)
    print("Report saved successfully:", out_file)

if __name__ == "__main__":
    build_report()
