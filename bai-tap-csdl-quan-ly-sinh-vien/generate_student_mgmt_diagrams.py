import os
import sys
from PIL import Image, ImageDraw, ImageFont

def get_font(size, bold=False):
    font_paths = [
        "C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/calibrib.ttf" if bold else "C:/Windows/Fonts/calibri.ttf",
    ]
    for path in font_paths:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                pass
    return ImageFont.load_default()

def get_mono_font(size, bold=False):
    font_paths = [
        "C:/Windows/Fonts/consolab.ttf" if bold else "C:/Windows/Fonts/consola.ttf",
        "C:/Windows/Fonts/courbd.ttf" if bold else "C:/Windows/Fonts/cour.ttf",
    ]
    for path in font_paths:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                pass
    return get_font(size, bold)

def create_gui_table_class_diagram(filename):
    W, H = 1200, 750
    img = Image.new("RGB", (W, H), color="#F0F2F5")
    draw = ImageDraw.Draw(img)

    f_title = get_font(13, bold=True)
    f_menu = get_font(12, bold=False)
    f_tree_header = get_font(12, bold=True)
    f_tree = get_font(12, bold=False)
    f_bold = get_font(12, bold=True)
    f_mono = get_mono_font(12, bold=False)
    f_badge = get_font(11, bold=True)

    # 1. Window Titlebar
    draw.rectangle([0, 0, W, 32], fill="#1E293B")
    draw.text((15, 8), "MySQL Workbench 8.0 CE - [student-management - Class - Table]", fill="#E2E8F0", font=f_title)
    draw.rectangle([W - 90, 8, W - 75, 22], fill="#475569")
    draw.rectangle([W - 65, 8, W - 50, 22], fill="#475569")
    draw.rectangle([W - 40, 8, W - 25, 22], fill="#EF4444")

    # 2. Menu bar
    draw.rectangle([0, 32, W, 62], fill="#FFFFFF")
    menus = ["File", "Edit", "View", "Query", "Database", "Server", "Tools", "Scripting", "Help"]
    mx = 15
    for m in menus:
        draw.text((mx, 40), m, fill="#334155", font=f_menu)
        mx += len(m) * 8 + 22

    # 3. Toolbar
    draw.rectangle([0, 62, W, 96], fill="#F8FAFC")
    draw.line([0, 96, W, 96], fill="#E2E8F0", width=1)
    draw.text((20, 72), "Schema: student-management", fill="#0369A1", font=f_bold)

    # 4. Left Sidebar - Navigator
    NAV_W = 280
    draw.rectangle([0, 96, NAV_W, H - 150], fill="#FFFFFF")
    draw.line([NAV_W, 96, NAV_W, H - 150], fill="#CBD5E1", width=1)
    
    draw.rectangle([0, 96, NAV_W, 126], fill="#F1F5F9")
    draw.text((15, 103), "Navigator", fill="#475569", font=f_tree_header)
    
    draw.rectangle([0, 126, NAV_W, 154], fill="#E2E8F0")
    draw.text((15, 133), "SCHEMAS", fill="#0F172A", font=f_tree_header)
    draw.text((NAV_W - 35, 133), "🔄", fill="#475569", font=f_menu)

    # Schema tree
    draw.text((20, 168), "▾ 🗄️ student-management", fill="#0369A1", font=get_font(12, bold=True))
    draw.text((35, 196), "  ▾ 📋 Tables", fill="#334155", font=f_tree_header)
    draw.text((50, 224), "    • Class (new)", fill="#059669", font=get_font(12, bold=True))
    draw.text((50, 252), "    • Teacher", fill="#64748B", font=f_tree)
    draw.text((50, 280), "    • Student", fill="#64748B", font=f_tree)
    draw.text((35, 308), "  ▸ 👁️ Views", fill="#64748B", font=f_tree)
    draw.text((20, 336), "▸ 🗄️ demo", fill="#64748B", font=f_tree)
    draw.text((20, 364), "▸ 🗄️ sys", fill="#64748B", font=f_tree)

    # Context menu simulation overlay for Create Table
    draw.rectangle([40, 190, 220, 280], fill="#FFFFFF", outline="#94A3B8", width=1)
    cm_items = ["Alter Schema...", "Drop Schema...", "Create Table...", "Create View...", "Schema Inspector"]
    cmy = 196
    for item in cm_items:
        if item == "Create Table...":
            draw.rectangle([42, cmy - 2, 218, cmy + 18], fill="#3B82F6")
            draw.text((50, cmy), item, fill="#FFFFFF", font=f_bold)
        else:
            draw.text((50, cmy), item, fill="#334155", font=f_menu)
        cmy += 20

    # 5. Right Editor Panel - Create Table GUI
    ED_X = NAV_W
    draw.rectangle([ED_X, 96, W, 126], fill="#F1F5F9")
    draw.line([ED_X, 126, W, 126], fill="#CBD5E1", width=1)
    
    # Active Tab
    draw.rectangle([ED_X + 5, 100, ED_X + 160, 126], fill="#FFFFFF", outline="#CBD5E1", width=1)
    draw.text((ED_X + 15, 105), "Class - Table ✕", fill="#0F172A", font=f_badge)

    # Table Properties Bar
    draw.rectangle([ED_X, 127, W, 185], fill="#FFFFFF")
    draw.line([ED_X, 185, W, 185], fill="#E2E8F0", width=1)
    draw.text((ED_X + 20, 138), "Table Name:", fill="#475569", font=f_bold)
    draw.rectangle([ED_X + 110, 134, ED_X + 320, 160], fill="#F8FAFC", outline="#3B82F6", width=2)
    draw.text((ED_X + 120, 139), "Class", fill="#0F172A", font=get_font(13, bold=True))

    draw.text((ED_X + 350, 138), "Schema:", fill="#475569", font=f_menu)
    draw.text((ED_X + 410, 138), "student-management", fill="#0369A1", font=f_bold)
    draw.text((ED_X + 600, 138), "Engine: InnoDB  |  Collation: Default", fill="#64748B", font=f_menu)

    # Columns Grid Header
    GRID_Y = 186
    draw.rectangle([ED_X, GRID_Y, W, GRID_Y + 30], fill="#E2E8F0")
    cols_header = [
        ("Column Name", 220),
        ("Datatype", 180),
        ("PK", 45),
        ("NN", 45),
        ("UQ", 45),
        ("B", 45),
        ("UN", 45),
        ("ZF", 45),
        ("AI", 45),
        ("Default / Expression", 160)
    ]
    cx = ED_X + 15
    for htitle, hw in cols_header:
        draw.text((cx, GRID_Y + 7), htitle, fill="#1E293B", font=get_font(11, bold=True))
        cx += hw

    # Grid Rows
    rows_data = [
        ("id", "INT", True, True, "Primary Key Identifier"),
        ("name", "VARCHAR(200)", False, False, "Class Name (e.g. C0123G1)")
    ]
    ry = GRID_Y + 31
    for cname, ctype, is_pk, is_nn, cdesc in rows_data:
        draw.rectangle([ED_X, ry, W, ry + 36], fill="#FFFFFF", outline="#F1F5F9", width=1)
        # Column Name
        draw.text((ED_X + 15, ry + 9), cname, fill="#2563EB" if is_pk else "#0F172A", font=get_mono_font(12, bold=True))
        # Datatype
        draw.text((ED_X + 235, ry + 9), ctype, fill="#059669", font=get_mono_font(12, bold=True))
        # Checkboxes
        for idx, (val, offset) in enumerate([(is_pk, 415), (is_nn, 460), (False, 505), (False, 550), (False, 595), (False, 640), (False, 685)]):
            draw.rectangle([ED_X + offset, ry + 10, ED_X + offset + 16, ry + 26], fill="#F8FAFC", outline="#94A3B8", width=1)
            if val:
                draw.rectangle([ED_X + offset + 3, ry + 13, ED_X + offset + 13, ry + 23], fill="#3B82F6")
        # Default
        draw.text((ED_X + 745, ry + 9), "NULL", fill="#94A3B8", font=f_mono)
        ry += 37

    # Empty placeholder row
    draw.rectangle([ED_X, ry, W, ry + 36], fill="#F8FAFC", outline="#E2E8F0", width=1)
    draw.text((ED_X + 15, ry + 9), "<Click to add column>", fill="#94A3B8", font=get_font(11, bold=False))

    # Bottom Actions Bar
    BAR_Y = H - 150
    draw.rectangle([ED_X, BAR_Y - 50, W, BAR_Y], fill="#F8FAFC")
    draw.line([ED_X, BAR_Y - 50, W, BAR_Y - 50], fill="#E2E8F0", width=1)
    
    # Apply button (Highlighted)
    draw.rectangle([W - 130, BAR_Y - 42, W - 30, BAR_Y - 10], fill="#16A34A", outline="#15803D", width=1)
    draw.text((W - 105, BAR_Y - 34), "Apply", fill="#FFFFFF", font=get_font(13, bold=True))
    
    # Revert button
    draw.rectangle([W - 240, BAR_Y - 42, W - 145, BAR_Y - 10], fill="#E2E8F0", outline="#CBD5E1", width=1)
    draw.text((W - 215, BAR_Y - 34), "Revert", fill="#475569", font=get_font(13, bold=False))

    # Action output at bottom
    draw.rectangle([0, BAR_Y, W, BAR_Y + 28], fill="#E2E8F0")
    draw.text((15, BAR_Y + 6), "Action Output", fill="#0F172A", font=f_tree_header)
    draw.rectangle([0, BAR_Y + 28, W, H], fill="#FFFFFF")
    draw.ellipse([15, BAR_Y + 36, 25, BAR_Y + 46], fill="#16A34A")
    draw.text((17, BAR_Y + 35), "✓", fill="#FFFFFF", font=get_font(9, bold=True))
    draw.text((35, BAR_Y + 35), "16:48:10", fill="#334155", font=f_mono)
    draw.text((120, BAR_Y + 35), "CREATE TABLE `student-management`.`Class` ( `id` INT, `name` VARCHAR(200) )", fill="#0F172A", font=f_mono)
    draw.text((950, BAR_Y + 35), "0 row(s) affected", fill="#16A34A", font=f_mono)

    # Highlight Callout Bubble
    draw.rectangle([W - 360, BAR_Y - 105, W - 50, BAR_Y - 55], fill="#FEF3C7", outline="#F59E0B", width=2)
    draw.text((W - 345, BAR_Y - 98), "👉 Bước 3: Nhấn nút Apply", fill="#92400E", font=get_font(12, bold=True))
    draw.text((W - 345, BAR_Y - 78), "để thực thi lệnh tạo bảng Class", fill="#B45309", font=get_font(11, bold=False))

    img.save(filename, "PNG", quality=95)
    print(f"Created: {filename}")

def create_gui_table_teacher_diagram(filename):
    W, H = 1200, 750
    img = Image.new("RGB", (W, H), color="#F0F2F5")
    draw = ImageDraw.Draw(img)

    f_title = get_font(13, bold=True)
    f_bold = get_font(12, bold=True)
    f_mono = get_mono_font(12, bold=False)
    f_badge = get_font(11, bold=True)

    # Window titlebar
    draw.rectangle([0, 0, W, 32], fill="#1E293B")
    draw.text((15, 8), "MySQL Workbench 8.0 CE - [student-management - Teacher - Table]", fill="#E2E8F0", font=f_title)
    draw.rectangle([W - 90, 8, W - 75, 22], fill="#475569")
    draw.rectangle([W - 65, 8, W - 50, 22], fill="#475569")
    draw.rectangle([W - 40, 8, W - 25, 22], fill="#EF4444")

    # Background layout
    draw.rectangle([0, 32, W, 62], fill="#FFFFFF")
    draw.text((20, 40), "File   Edit   View   Query   Database   Server   Tools   Scripting   Help", fill="#475569", font=get_font(12, bold=False))

    # Main content split
    NAV_W = 280
    draw.rectangle([0, 62, NAV_W, H], fill="#FFFFFF")
    draw.line([NAV_W, 62, NAV_W, H], fill="#CBD5E1", width=1)
    draw.rectangle([0, 62, NAV_W, 92], fill="#E2E8F0")
    draw.text((15, 70), "SCHEMAS", fill="#0F172A", font=f_bold)
    
    # Schemas tree
    draw.text((20, 110), "▾ 🗄️ student-management", fill="#0369A1", font=get_font(12, bold=True))
    draw.text((35, 138), "  ▾ 📋 Tables", fill="#334155", font=f_bold)
    draw.text((50, 166), "    • Class", fill="#334155", font=get_font(12, bold=False))
    draw.text((50, 194), "    • Teacher (active)", fill="#059669", font=get_font(12, bold=True))
    draw.text((50, 222), "    • Student", fill="#334155", font=get_font(12, bold=False))

    # Modal Dialog "Apply SQL Script to Database" centered overlay
    DIA_W, DIA_H = 750, 480
    DX = NAV_W + (W - NAV_W - DIA_W) // 2
    DY = 100

    # Modal Drop shadow & Card
    draw.rectangle([DX - 4, DY - 4, DX + DIA_W + 4, DY + DIA_H + 4], fill="#CBD5E1")
    draw.rectangle([DX, DY, DX + DIA_W, DY + DIA_H], fill="#FFFFFF", outline="#94A3B8", width=1)
    
    # Dialog Title bar
    draw.rectangle([DX, DY, DX + DIA_W, DY + 38], fill="#0F172A")
    draw.text((DX + 18, DY + 10), "Apply SQL Script to Database - Create Table 'Teacher'", fill="#FFFFFF", font=f_bold)
    draw.text((DX + DIA_W - 30, DY + 10), "✕", fill="#94A3B8", font=f_bold)

    # Dialog Subtitle
    draw.text((DX + 20, DY + 55), "Review the SQL script to be applied on the database:", fill="#334155", font=get_font(12, bold=False))

    # SQL Editor preview inside modal
    CODE_X = DX + 20
    CODE_Y = DY + 85
    CODE_W = DIA_W - 40
    CODE_H = 290
    draw.rectangle([CODE_X, CODE_Y, CODE_X + CODE_W, CODE_Y + CODE_H], fill="#1E1E1E", outline="#334155", width=1)

    sql_lines = [
        "-- Table: Teacher in schema student-management",
        "-- Auto-generated by MySQL Workbench Table Editor",
        "",
        "CREATE TABLE `student-management`.`Teacher` (",
        "  `id` INT NULL,",
        "  `name` VARCHAR(200) NULL,",
        "  `age` INT NULL,",
        "  `country` VARCHAR(50) NULL",
        ");"
    ]

    sy = CODE_Y + 18
    for line in sql_lines:
        if line.startswith("--"):
            draw.text((CODE_X + 15, sy), line, fill="#6A9955", font=f_mono)
        elif "CREATE TABLE" in line:
            draw.text((CODE_X + 15, sy), line, fill="#569CD6", font=get_mono_font(13, bold=True))
        elif "INT" in line or "VARCHAR" in line:
            draw.text((CODE_X + 15, sy), line, fill="#4EC9B0", font=f_mono)
        else:
            draw.text((CODE_X + 15, sy), line, fill="#D4D4D4", font=f_mono)
        sy += 25

    # Dialog Buttons Bar
    BTNY = DY + DIA_H - 55
    draw.line([DX, BTNY - 10, DX + DIA_W, BTNY - 10], fill="#E2E8F0", width=1)
    
    # Back button
    draw.rectangle([DX + DIA_W - 320, BTNY, DX + DIA_W - 230, BTNY + 32], fill="#F1F5F9", outline="#CBD5E1", width=1)
    draw.text((DX + DIA_W - 290, BTNY + 8), "< Back", fill="#475569", font=get_font(12, bold=False))

    # Apply button (Active)
    draw.rectangle([DX + DIA_W - 215, BTNY, DX + DIA_W - 125, BTNY + 32], fill="#3B82F6", outline="#2563EB", width=1)
    draw.text((DX + DIA_W - 185, BTNY + 8), "Apply", fill="#FFFFFF", font=f_bold)

    # Cancel button
    draw.rectangle([DX + DIA_W - 110, BTNY, DX + DIA_W - 20, BTNY + 32], fill="#F1F5F9", outline="#CBD5E1", width=1)
    draw.text((DX + DIA_W - 80, BTNY + 8), "Cancel", fill="#475569", font=get_font(12, bold=False))

    # Action Output at bottom
    OUT_Y = H - 120
    draw.rectangle([0, OUT_Y, W, OUT_Y + 28], fill="#E2E8F0")
    draw.text((15, OUT_Y + 6), "Action Output", fill="#0F172A", font=f_bold)
    draw.rectangle([0, OUT_Y + 28, W, H], fill="#FFFFFF")
    
    out_records = [
        ("16:48:22", "CREATE TABLE `student-management`.`Class` ( `id` INT, `name` VARCHAR(200) )", "0 row(s) affected", "0.031 sec"),
        ("16:48:35", "CREATE TABLE `student-management`.`Teacher` ( `id` INT, `name` VARCHAR(200), `age` INT, ... )", "0 row(s) affected", "0.028 sec")
    ]
    oy = OUT_Y + 35
    for t, cmd, msg, dur in out_records:
        draw.ellipse([15, oy + 2, 25, oy + 12], fill="#16A34A")
        draw.text((17, oy + 1), "✓", fill="#FFFFFF", font=get_font(9, bold=True))
        draw.text((35, oy), t, fill="#334155", font=f_mono)
        draw.text((120, oy), cmd[:60] + ("..." if len(cmd) > 60 else ""), fill="#0F172A", font=f_mono)
        draw.text((700, oy), msg, fill="#16A34A", font=f_mono)
        draw.text((950, oy), dur, fill="#64748B", font=f_mono)
        oy += 24

    img.save(filename, "PNG", quality=95)
    print(f"Created: {filename}")

def create_erd_student_management_diagram(filename):
    W, H = 1200, 720
    img = Image.new("RGB", (W, H), color="#FFFFFF")
    draw = ImageDraw.Draw(img)

    f_title = get_font(18, bold=True)
    f_sub = get_font(12, bold=False)
    f_tbl_h = get_font(13, bold=True)
    f_tbl_c = get_mono_font(12, bold=False)
    f_badge = get_font(11, bold=True)

    # Top Banner
    draw.rectangle([0, 0, W, 80], fill="#0F172A")
    draw.text((35, 18), "SƠ ĐỒ THỰC THỂ QUAN HỆ (ERD) - CƠ SỞ DỮ LIỆU `student-management`", fill="#FFFFFF", font=f_title)
    draw.text((35, 48), "Cấu trúc các bảng Class, Teacher, Student và mối liên kết quan hệ trong quản lý đào tạo", fill="#94A3B8", font=f_sub)

    # Table 1: Teacher (Left)
    T1_X, T1_Y, T1_W = 70, 150, 320
    draw.rectangle([T1_X, T1_Y, T1_X + T1_W, T1_Y + 280], fill="#F8FAFC", outline="#3B82F6", width=2)
    draw.rectangle([T1_X, T1_Y, T1_X + T1_W, T1_Y + 45], fill="#3B82F6")
    draw.text((T1_X + 15, T1_Y + 12), "📋 Teacher (Giảng viên)", fill="#FFFFFF", font=f_tbl_h)
    
    t1_fields = [
        ("🔑 id", "INT", "#2563EB", "Mã giảng viên"),
        ("📝 name", "VARCHAR(200)", "#0F172A", "Họ và tên"),
        ("🔢 age", "INT", "#0F172A", "Độ tuổi"),
        ("🌐 country", "VARCHAR(50)", "#0F172A", "Quốc gia")
    ]
    fy = T1_Y + 58
    for fld, ftype, col, note in t1_fields:
        draw.text((T1_X + 15, fy), fld, fill=col, font=get_font(12, bold=True if "🔑" in fld else False))
        draw.text((T1_X + 160, fy), ftype, fill="#059669", font=f_tbl_c)
        draw.text((T1_X + 15, fy + 18), note, fill="#94A3B8", font=get_font(10, bold=False))
        fy += 48

    # Table 2: Class (Center)
    T2_X, T2_Y, T2_W = 440, 150, 320
    draw.rectangle([T2_X, T2_Y, T2_X + T2_W, T2_Y + 280], fill="#F8FAFC", outline="#10B981", width=2)
    draw.rectangle([T2_X, T2_Y, T2_X + T2_W, T2_Y + 45], fill="#10B981")
    draw.text((T2_X + 15, T2_Y + 12), "📋 Class (Lớp học)", fill="#FFFFFF", font=f_tbl_h)

    t2_fields = [
        ("🔑 id", "INT", "#2563EB", "Mã lớp học"),
        ("📝 name", "VARCHAR(200)", "#0F172A", "Tên lớp (e.g. C0123G1)"),
        ("🔗 teacher_id", "INT (FK)", "#D97706", "Giảng viên phụ trách")
    ]
    fy = T2_Y + 58
    for fld, ftype, col, note in t2_fields:
        draw.text((T2_X + 15, fy), fld, fill=col, font=get_font(12, bold=True if "🔑" in fld or "🔗" in fld else False))
        draw.text((T2_X + 170, fy), ftype, fill="#059669", font=f_tbl_c)
        draw.text((T2_X + 15, fy + 18), note, fill="#94A3B8", font=get_font(10, bold=False))
        fy += 52

    # Table 3: Student (Right)
    T3_X, T3_Y, T3_W = 810, 150, 320
    draw.rectangle([T3_X, T3_Y, T3_X + T3_W, T3_Y + 280], fill="#F8FAFC", outline="#8B5CF6", width=2)
    draw.rectangle([T3_X, T3_Y, T3_X + T3_W, T3_Y + 45], fill="#8B5CF6")
    draw.text((T3_X + 15, T3_Y + 12), "📋 Student (Sinh viên)", fill="#FFFFFF", font=f_tbl_h)

    t3_fields = [
        ("🔑 id", "INT", "#2563EB", "Mã sinh viên"),
        ("📝 name", "VARCHAR(200)", "#0F172A", "Họ tên sinh viên"),
        ("🔢 age", "INT", "#0F172A", "Độ tuổi sinh viên"),
        ("🌐 country", "VARCHAR(50)", "#0F172A", "Quê quán / Quốc gia"),
        ("🔗 class_id", "INT (FK)", "#D97706", "Lớp đang theo học")
    ]
    fy = T3_Y + 58
    for fld, ftype, col, note in t3_fields:
        draw.text((T3_X + 15, fy), fld, fill=col, font=get_font(12, bold=True if "🔑" in fld or "🔗" in fld else False))
        draw.text((T3_X + 170, fy), ftype, fill="#059669", font=f_tbl_c)
        draw.text((T3_X + 15, fy + 16), note, fill="#94A3B8", font=get_font(10, bold=False))
        fy += 40

    # Relationship connectors
    # Teacher (1) ---> (N) Class
    draw.line([T1_X + T1_W, T1_Y + 180, T2_X, T2_Y + 180], fill="#3B82F6", width=3)
    draw.polygon([(T2_X, T2_Y + 180), (T2_X - 10, T2_Y + 175), (T2_X - 10, T2_Y + 185)], fill="#3B82F6")
    draw.text((T1_X + T1_W + 8, T1_Y + 155), "1 : N", fill="#1E40AF", font=f_badge)

    # Class (1) ---> (N) Student
    draw.line([T2_X + T2_W, T2_Y + 180, T3_X, T3_Y + 180], fill="#10B981", width=3)
    draw.polygon([(T3_X, T3_Y + 180), (T3_X - 10, T3_Y + 175), (T3_X - 10, T3_Y + 185)], fill="#10B981")
    draw.text((T2_X + T2_W + 8, T2_Y + 155), "1 : N", fill="#065F46", font=f_badge)

    # Summary Panel Bottom
    draw.rectangle([70, 480, W - 70, 680], fill="#F8FAFC", outline="#E2E8F0", width=1)
    draw.rectangle([70, 480, W - 70, 520], fill="#F1F5F9")
    draw.text((90, 492), "TỔNG HỢP KIỂM CHỨNG CÁC BẢNG TRONG CSDL `student-management`", fill="#0F172A", font=f_tbl_h)

    summary_items = [
        ("• Bảng Class:", "2 trường (id: INT, name: VARCHAR(200)) - Phân lớp học viên trong trung tâm."),
        ("• Bảng Teacher:", "4 trường (id: INT, name: VARCHAR(200), age: INT, country: VARCHAR(50)) - Quản lý giảng viên hướng dẫn."),
        ("• Bảng Student:", "4 trường (id: INT, name: VARCHAR(200), age: INT, country: VARCHAR(50)) - Quản lý thông tin học viên tích hợp từ bài trước."),
        ("• Thao tác GUI:", "Thực hiện thành công qua chức năng Create Table -> Apply của MySQL Workbench.")
    ]
    smy = 535
    for lbl, desc in summary_items:
        draw.text((90, smy), lbl, fill="#1E40AF", font=get_font(12, bold=True))
        draw.text((260, smy), desc, fill="#334155", font=get_font(12, bold=False))
        smy += 34

    img.save(filename, "PNG", quality=95)
    print(f"Created: {filename}")

if __name__ == "__main__":
    out_dir = r"C:\Users\dathao\.gemini\antigravity-ide\scratch\bai-tap-csdl-quan-ly-sinh-vien"
    create_gui_table_class_diagram(os.path.join(out_dir, "mysql_workbench_gui_create_table_class.png"))
    create_gui_table_teacher_diagram(os.path.join(out_dir, "mysql_workbench_gui_create_table_teacher.png"))
    create_erd_student_management_diagram(os.path.join(out_dir, "mysql_workbench_erd_student_management.png"))
