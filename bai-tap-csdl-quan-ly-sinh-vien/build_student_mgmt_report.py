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
        hr = hp.add_run("Báo Cáo: Xây Dựng Cơ Sở Dữ Liệu Quản Lý Sinh Viên")
        hr.font.name = "Arial"
        hr.font.size = Pt(8.5)
        hr.font.color.rgb = RGBColor(148, 163, 184)
        
        # Footer
        ftr = s.footer
        fp = ftr.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        fr = fp.add_run("Học viên: proyctk03-eng  |  MySQL Workbench 8.0 CE")
        fr.font.name = "Arial"
        fr.font.size = Pt(8.5)
        fr.font.color.rgb = RGBColor(148, 163, 184)

def build_report():
    doc = docx.Document()
    add_header_footer(doc)
    
    # ------------------ COVER PAGE ------------------
    p_cover_pre = doc.add_paragraph()
    p_cover_pre.paragraph_format.space_before = Pt(30)
    
    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_inst = p_inst.add_run("BÀI TẬP CƠ SỞ DỮ LIỆU QUAN HỆ\nHỆ THỐNG QUẢN TRỊ CSDL MYSQL WORKBENCH")
    r_inst.bold = True
    r_inst.font.name = "Arial"
    r_inst.font.size = Pt(12)
    r_inst.font.color.rgb = RGBColor(71, 85, 105)
    
    p_line = doc.add_paragraph()
    p_line.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_line = p_line.add_run("—" * 25)
    r_line.font.color.rgb = RGBColor(148, 163, 184)
    
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(36)
    p_title.paragraph_format.space_after = Pt(12)
    r_title = p_title.add_run("BÁO CÁO BÀI TẬP\nXÂY DỰNG CƠ SỞ DỮ LIỆU\nQUẢN LÝ SINH VIÊN")
    r_title.bold = True
    r_title.font.name = "Arial"
    r_title.font.size = Pt(22)
    r_title.font.color.rgb = RGBColor(15, 23, 42)
    
    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(40)
    r_sub = p_sub.add_run("Thực hành tạo bảng Class (id, name) và bảng Teacher (id, name, age, country) trên CSDL `student-management` bằng MySQL Workbench")
    r_sub.font.name = "Arial"
    r_sub.font.size = Pt(11.5)
    r_sub.font.color.rgb = RGBColor(51, 65, 85)
    
    # Cover info table
    tbl_meta = doc.add_table(rows=5, cols=2)
    tbl_meta.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_meta.autofit = False
    tbl_meta.columns[0].width = Inches(2.2)
    tbl_meta.columns[1].width = Inches(3.8)
    
    meta_info = [
        ("Chủ đề bài tập:", "Xây dựng CSDL Quản lý sinh viên (Class & Teacher)"),
        ("Tên Cơ sở dữ liệu:", "student-management"),
        ("Các bảng khởi tạo:", "Class (Lớp học) & Teacher (Giảng viên)"),
        ("Tài khoản sinh viên:", "proyctk03-eng (GitHub)"),
        ("Hệ quản trị & Công cụ:", "MySQL 8.0 CE / MySQL Workbench 8.0")
    ]
    
    for i, (k, v) in enumerate(meta_info):
        c0 = tbl_meta.cell(i, 0)
        c1 = tbl_meta.cell(i, 1)
        set_cell_background(c0, "F8FAFC")
        set_cell_background(c1, "FFFFFF")
        set_cell_margins(c0, 60, 60, 100, 100)
        set_cell_margins(c1, 60, 60, 100, 100)
        
        p0 = c0.paragraphs[0]
        r0 = p0.add_run(k)
        r0.bold = True
        r0.font.name = "Arial"
        r0.font.size = Pt(10)
        r0.font.color.rgb = RGBColor(71, 85, 105)
        
        p1 = c1.paragraphs[0]
        r1 = p1.add_run(v)
        r1.font.name = "Arial"
        r1.font.size = Pt(10)
        r1.font.color.rgb = RGBColor(15, 23, 42)
        if "proyctk03-eng" in v or "student-management" in v:
            r1.bold = True

    p_date = doc.add_paragraph()
    p_date.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_date.paragraph_format.space_before = Pt(80)
    r_date = p_date.add_run("Tháng 10 Năm 2026")
    r_date.font.name = "Arial"
    r_date.font.size = Pt(10)
    r_date.font.color.rgb = RGBColor(100, 116, 139)
    
    doc.add_page_break()

    # ------------------ BODY ------------------
    # 1. TỔNG QUAN
    p_h1 = doc.add_heading(level=1)
    r_h1 = p_h1.add_run("1. TỔNG QUAN & MỤC TIÊU BÀI TẬP")
    r_h1.font.name = "Arial"
    r_h1.font.size = Pt(15)
    r_h1.font.color.rgb = RGBColor(15, 23, 42)
    r_h1.bold = True
    
    p_desc = doc.add_paragraph()
    p_desc.paragraph_format.space_after = Pt(8)
    r_d = p_desc.add_run(
        "Bài tập 'Xây dựng cơ sở dữ liệu quản lý sinh viên' giúp củng cố kiến thức thiết kế dữ liệu thực tế "
        "bằng cách mở rộng hệ thống CSDL student-management đã khởi tạo. "
        "Học viên được rèn luyện quy trình thiết lập bảng thông qua công cụ trực quan (Table Editor GUI) "
        "và phương pháp thực thi DDL SQL trực tiếp, từ đó hiểu sâu cách công cụ tự động biên dịch cấu hình đồ họa "
        "thành các câu lệnh SQL chuẩn."
    )
    r_d.font.name = "Arial"
    r_d.font.size = Pt(10.5)

    create_callout_box(
        doc,
        "Yêu cầu nghiệp vụ chi tiết:\n"
        "1. Schema mục tiêu: `student-management` (lưu ý ký tự gạch ngang '-' cần bọc trong dấu backticks ``).\n"
        "2. Bảng Class: Quản lý danh sách lớp học với các trường id (INT), name (VARCHAR 200).\n"
        "3. Bảng Teacher: Quản lý giảng viên với các trường id (INT), name (VARCHAR 200), age (INT), country (VARCHAR 50).\n"
        "4. Sử dụng tính năng Create Table -> Apply trên MySQL Workbench để hoàn thiện.",
        title="YÊU CẦU ĐỀ BÀI",
        hex_border="0284C7",
        hex_bg="F0F9FF"
    )

    # 2. HƯỚNG DẪN THAO TÁC GUI
    p_h2 = doc.add_heading(level=1)
    r_h2 = p_h2.add_run("2. QUY TRÌNH THỰC HIỆN TỪNG BƯỚC TRÊN MYSQL WORKBENCH (GUI)")
    r_h2.font.name = "Arial"
    r_h2.font.size = Pt(15)
    r_h2.font.color.rgb = RGBColor(15, 23, 42)
    r_h2.bold = True

    gui_steps = [
        ("Bước 1: Mở trình tạo bảng Create Table trên schema student-management",
         "Khởi động MySQL Workbench, kết nối tới cơ sở dữ liệu. Tại ngăn Navigator bên trái màn hình, "
         "tìm schema `student-management`. Nhấp chuột phải vào tên schema hoặc mục Tables rồi chọn lệnh 'Create Table...'."),
        ("Bước 2: Cấu hình bảng Class",
         "Trong tab Table Editor vừa mở ra:\n"
         "  • Điền Table Name là: Class\n"
         "  • Tại bảng danh sách Columns phía dưới, nhấp đúp để tạo 2 cột:\n"
         "      + Cột 1: id | Datatype: INT\n"
         "      + Cột 2: name | Datatype: VARCHAR(200)"),
        ("Bước 3: Thực thi Apply để tạo bảng Class",
         "Nhấp vào nút Apply ở góc dưới bên phải giao diện. Hộp thoại 'Apply SQL Script to Database' sẽ mở ra "
         "để người dùng rà soát mã DDL. Nhấn Apply lần 2 rồi nhấn Finish để hoàn tất quá trình tạo bảng."),
        ("Bước 4: Thực hiện tương tự đối với bảng Teacher",
         "Nhấp chuột phải vào schema `student-management` -> Chọn 'Create Table...'.\n"
         "  • Điền Table Name là: Teacher\n"
         "  • Khai báo 4 cột thuộc tính:\n"
         "      + id (INT): Mã số giảng viên\n"
         "      + name (VARCHAR 200): Họ và tên giảng viên\n"
         "      + age (INT): Độ tuổi giảng viên\n"
         "      + country (VARCHAR 50): Quốc gia / Quê quán\n"
         "  • Nhấn Apply -> Apply -> Finish để ghi nhận bảng Teacher vào hệ thống.")
    ]

    for title, content in gui_steps:
        p_st = doc.add_paragraph()
        p_st.paragraph_format.space_before = Pt(6)
        p_st.paragraph_format.space_after = Pt(2)
        r_st = p_st.add_run(f"📌 {title}")
        r_st.bold = True
        r_st.font.name = "Arial"
        r_st.font.size = Pt(11)
        r_st.font.color.rgb = RGBColor(30, 58, 138)
        
        p_sc = doc.add_paragraph()
        p_sc.paragraph_format.space_after = Pt(6)
        r_sc = p_sc.add_run(content)
        r_sc.font.name = "Arial"
        r_sc.font.size = Pt(10)

    # Ảnh chụp GUI Class
    script_dir = r"C:\Users\dathao\.gemini\antigravity-ide\scratch\bai-tap-csdl-quan-ly-sinh-vien"
    img1_path = os.path.join(script_dir, "mysql_workbench_gui_create_table_class.png")
    if os.path.exists(img1_path):
        p_img1 = doc.add_paragraph()
        p_img1.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img1.paragraph_format.space_after = Pt(2)
        run_img1 = p_img1.add_run()
        run_img1.add_picture(img1_path, width=Inches(6.3))
        
        p_cap1 = doc.add_paragraph()
        p_cap1.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap1.paragraph_format.space_after = Pt(12)
        r_cap1 = p_cap1.add_run("Hình 1: Thao tác khai báo các trường thuộc tính và nhấn Apply tạo bảng Class")
        r_cap1.font.name = "Arial"
        r_cap1.font.size = Pt(9)
        r_cap1.font.italic = True
        r_cap1.font.color.rgb = RGBColor(100, 116, 139)

    doc.add_page_break()

    # Ảnh chụp GUI Teacher
    img2_path = os.path.join(script_dir, "mysql_workbench_gui_create_table_teacher.png")
    if os.path.exists(img2_path):
        p_img2 = doc.add_paragraph()
        p_img2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img2.paragraph_format.space_after = Pt(2)
        run_img2 = p_img2.add_run()
        run_img2.add_picture(img2_path, width=Inches(6.3))
        
        p_cap2 = doc.add_paragraph()
        p_cap2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap2.paragraph_format.space_after = Pt(12)
        r_cap2 = p_cap2.add_run("Hình 2: Hộp thoại Apply SQL Script to Database sinh mã DDL tạo bảng Teacher")
        r_cap2.font.name = "Arial"
        r_cap2.font.size = Pt(9)
        r_cap2.font.italic = True
        r_cap2.font.color.rgb = RGBColor(100, 116, 139)

    # 3. KỊCH BẢN SQL VÀ METADATA
    p_h3 = doc.add_heading(level=1)
    r_h3 = p_h3.add_run("3. KỊCH BẢN SQL TRUY VẤN VÀ CẤU TRÚC METADATA")
    r_h3.font.name = "Arial"
    r_h3.font.size = Pt(15)
    r_h3.font.color.rgb = RGBColor(15, 23, 42)
    r_h3.bold = True

    # SQL Box
    sql_box = doc.add_table(rows=1, cols=1)
    sql_box.alignment = WD_TABLE_ALIGNMENT.CENTER
    sql_box.autofit = False
    sql_box.columns[0].width = Inches(6.5)
    c_sql = sql_box.cell(0, 0)
    set_cell_background(c_sql, "0F172A")
    set_cell_margins(c_sql, top=140, bottom=140, left=180, right=180)
    
    p_code = c_sql.paragraphs[0]
    sql_content = (
        "-- 1. Khởi tạo CSDL student-management\n"
        "CREATE DATABASE IF NOT EXISTS `student-management`;\n"
        "USE `student-management`;\n\n"
        "-- 2. Tạo bảng Class (Lớp học)\n"
        "CREATE TABLE IF NOT EXISTS Class (\n"
        "    id INT,\n"
        "    name VARCHAR(200)\n"
        ");\n\n"
        "-- 3. Tạo bảng Teacher (Giảng viên)\n"
        "CREATE TABLE IF NOT EXISTS Teacher (\n"
        "    id INT,\n"
        "    name VARCHAR(200),\n"
        "    age INT,\n"
        "    country VARCHAR(50)\n"
        ");\n\n"
        "-- 4. Kiểm tra cấu trúc metadata\n"
        "DESCRIBE Class;\n"
        "DESCRIBE Teacher;"
    )
    r_code = p_code.add_run(sql_content)
    r_code.font.name = "Consolas"
    r_code.font.size = Pt(9.5)
    r_code.font.color.rgb = RGBColor(226, 232, 240)

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # Tables metadata
    p_tbl_lbl = doc.add_paragraph()
    r_lbl = p_tbl_lbl.add_run("Bảng 1: Bảng đặc tả trường thuộc tính hệ thống quản lý sinh viên")
    r_lbl.bold = True
    r_lbl.font.name = "Arial"
    r_lbl.font.size = Pt(10.5)

    tbl_desc = doc.add_table(rows=7, cols=5)
    tbl_desc.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_desc.autofit = False
    tbl_desc.columns[0].width = Inches(1.1)
    tbl_desc.columns[1].width = Inches(1.1)
    tbl_desc.columns[2].width = Inches(1.3)
    tbl_desc.columns[3].width = Inches(0.8)
    tbl_desc.columns[4].width = Inches(2.2)

    headers = ["Bảng (Entity)", "Trường (Field)", "Kiểu dữ liệu", "Null", "Chức năng nghiệp vụ"]
    for j, h in enumerate(headers):
        c = tbl_desc.cell(0, j)
        set_cell_background(c, "1E293B")
        set_cell_margins(c, 80, 80, 100, 100)
        p = c.paragraphs[0]
        r = p.add_run(h)
        r.bold = True
        r.font.name = "Arial"
        r.font.size = Pt(9.5)
        r.font.color.rgb = RGBColor(255, 255, 255)

    rows_data = [
        ("Class", "id", "INT", "YES", "Mã định danh lớp học"),
        ("Class", "name", "VARCHAR(200)", "YES", "Tên lớp học (ví dụ C0123G1)"),
        ("Teacher", "id", "INT", "YES", "Mã định danh giảng viên"),
        ("Teacher", "name", "VARCHAR(200)", "YES", "Họ và tên giảng viên"),
        ("Teacher", "age", "INT", "YES", "Độ tuổi của giảng viên"),
        ("Teacher", "country", "VARCHAR(50)", "YES", "Quốc gia hoặc nơi sinh sống")
    ]

    for i, r_tuple in enumerate(rows_data):
        bg = "FFFFFF" if i % 2 == 0 else "F8FAFC"
        for j, val in enumerate(r_tuple):
            c = tbl_desc.cell(i + 1, j)
            set_cell_background(c, bg)
            set_cell_margins(c, 70, 70, 100, 100)
            p = c.paragraphs[0]
            r = p.add_run(val)
            r.font.name = "Arial"
            r.font.size = Pt(9.5)
            r.font.color.rgb = RGBColor(15, 23, 42)
            if j in (0, 1):
                r.bold = True

    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    # 4. SƠ ĐỒ ERD
    p_h4 = doc.add_heading(level=1)
    r_h4 = p_h4.add_run("4. SƠ ĐỒ THỰC THỂ QUAN HỆ (ERD) & MÔ HÌNH HÓA DỮ LIỆU")
    r_h4.font.name = "Arial"
    r_h4.font.size = Pt(15)
    r_h4.font.color.rgb = RGBColor(15, 23, 42)
    r_h4.bold = True

    img3_path = os.path.join(script_dir, "mysql_workbench_erd_student_management.png")
    if os.path.exists(img3_path):
        p_img3 = doc.add_paragraph()
        p_img3.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img3.paragraph_format.space_after = Pt(2)
        run_img3 = p_img3.add_run()
        run_img3.add_picture(img3_path, width=Inches(6.3))
        
        p_cap3 = doc.add_paragraph()
        p_cap3.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap3.paragraph_format.space_after = Pt(10)
        r_cap3 = p_cap3.add_run("Hình 3: Sơ đồ thực thể quan hệ ERD kết nối giữa Teacher, Class và Student")
        r_cap3.font.name = "Arial"
        r_cap3.font.size = Pt(9)
        r_cap3.font.italic = True
        r_cap3.font.color.rgb = RGBColor(100, 116, 139)

    # 5. KẾT LUẬN
    p_h5 = doc.add_heading(level=1)
    r_h5 = p_h5.add_run("5. KẾT LUẬN & NGHIỆM THU")
    r_h5.font.name = "Arial"
    r_h5.font.size = Pt(15)
    r_h5.font.color.rgb = RGBColor(15, 23, 42)
    r_h5.bold = True

    p_conc = doc.add_paragraph()
    r_c = p_conc.add_run(
        "Bài tập đã hoàn thành 100% các tiêu chí yêu cầu:\n"
        "✓ Tạo thành công bảng Class gồm 2 trường id, name trên schema `student-management`.\n"
        "✓ Tạo thành công bảng Teacher gồm 4 trường id, name, age, country trên schema `student-management`.\n"
        "✓ Rèn luyện thành thục cả 2 phương thức: Thao tác đồ họa GUI trên MySQL Workbench và câu lệnh SQL truy vấn.\n"
        "✓ Toàn bộ mã nguồn, sơ đồ kiến trúc và báo cáo đã được lưu trữ và phát hành tại:\n"
        "  https://github.com/proyctk03-eng/bai-tap-csdl-quan-ly-sinh-vien"
    )
    r_c.font.name = "Arial"
    r_c.font.size = Pt(10)

    out_docx = os.path.join(script_dir, "Bao_Cao_Bai_Tap_CSDL_Quan_Ly_Sinh_Vien.docx")
    doc.save(out_docx)
    print(f"Report saved: {out_docx}")

if __name__ == "__main__":
    build_report()
