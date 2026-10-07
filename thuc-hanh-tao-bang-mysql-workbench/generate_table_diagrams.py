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

def create_workbench_create_table_diagram(filename):
    W, H = 1200, 750
    img = Image.new("RGB", (W, H), color="#F0F2F5")
    draw = ImageDraw.Draw(img)

    f_title = get_font(13, bold=True)
    f_menu = get_font(12, bold=False)
    f_tree_header = get_font(12, bold=True)
    f_tree = get_font(12, bold=False)
    f_code = get_mono_font(13, bold=False)
    f_code_kw = get_mono_font(13, bold=True)
    f_output = get_mono_font(11, bold=False)
    f_badge = get_font(11, bold=True)

    # 1. Window Titlebar
    draw.rectangle([0, 0, W, 32], fill="#1E293B")
    draw.text((15, 8), "MySQL Workbench 8.0 CE - [demo - Query 1 : Local instance MySQL80]", fill="#E2E8F0", font=f_title)
    
    # Window controls
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
    
    # Toolbar icons / buttons
    draw.rectangle([15, 68, 125, 90], fill="#E2E8F0", outline="#CBD5E1", width=1)
    draw.text((22, 72), "+ SQL Query", fill="#1E293B", font=f_menu)

    # Lightning Execute Button
    draw.rectangle([135, 68, 220, 90], fill="#FEF08A", outline="#EAB308", width=1)
    draw.polygon([(145, 78), (150, 72), (150, 76), (155, 71), (148, 86), (149, 80)], fill="#CA8A04")
    draw.text((160, 72), "Execute", fill="#854D0E", font=f_badge)

    draw.text((235, 73), "Schema: demo", fill="#0369A1", font=get_font(12, bold=True))

    # 4. Left Sidebar - Navigator (Schemas)
    NAV_W = 280
    draw.rectangle([0, 96, NAV_W, H - 180], fill="#FFFFFF")
    draw.line([NAV_W, 96, NAV_W, H - 180], fill="#CBD5E1", width=1)
    
    # Navigator Header
    draw.rectangle([0, 96, NAV_W, 126], fill="#F1F5F9")
    draw.text((15, 103), "Navigator", fill="#475569", font=f_tree_header)
    
    draw.rectangle([0, 126, NAV_W, 154], fill="#E2E8F0")
    draw.text((15, 133), "SCHEMAS", fill="#0F172A", font=f_tree_header)
    draw.text((NAV_W - 35, 133), "🔄", fill="#475569", font=f_menu)

    # Schema tree
    tree_items = [
        ("▾ 🗄️ demo (default)", "#0369A1", True, 20),
        ("  ▾ 📋 Tables", "#334155", True, 35),
        ("    ▾ 📄 Student", "#0F172A", True, 50),
        ("      ▪ 🔑 id : int", "#2563EB", False, 65),
        ("      ▪ 📝 name : varchar(200)", "#059669", False, 65),
        ("      ▪ 🔢 age : int", "#2563EB", False, 65),
        ("      ▪ 🌐 country : varchar(50)", "#D97706", False, 65),
        ("  ▸ 👁️ Views", "#64748B", False, 35),
        ("  ▸ ⚙️ Stored Procedures", "#64748B", False, 35),
        ("▸ 🗄️ sakila", "#64748B", False, 20),
        ("▸ 🗄️ sys", "#64748B", False, 20),
        ("▸ 🗄️ world", "#64748B", False, 20)
    ]
    ty = 165
    for text, color, bold, indent in tree_items:
        draw.text((indent, ty), text, fill=color, font=get_font(12, bold=bold))
        ty += 24

    # 5. Central Editor - Query 1 Tab
    draw.rectangle([NAV_W, 96, W, 126], fill="#F1F5F9")
    draw.line([NAV_W, 126, W, 126], fill="#CBD5E1", width=1)
    
    # Active Tab
    draw.rectangle([NAV_W + 5, 100, NAV_W + 160, 126], fill="#FFFFFF", outline="#CBD5E1", width=1)
    draw.text((NAV_W + 15, 105), "demo - Query 1 ✕", fill="#0F172A", font=f_badge)

    # Code Editor Canvas
    CODE_X = NAV_W
    CODE_Y = 127
    CODE_H = 430
    draw.rectangle([CODE_X, CODE_Y, W, CODE_Y + CODE_H], fill="#1E1E1E")

    # Line Numbers gutter
    draw.rectangle([CODE_X, CODE_Y, CODE_X + 45, CODE_Y + CODE_H], fill="#252526")
    draw.line([CODE_X + 45, CODE_Y, CODE_X + 45, CODE_Y + CODE_H], fill="#333333", width=1)

    code_lines = [
        "1   | -- Bước 1: Tạo cơ sở dữ liệu mới có tên 'demo'",
        "2   | CREATE DATABASE demo;",
        "3   | ",
        "4   | -- Bước 2: Chọn CSDL 'demo' để thao tác",
        "5   | USE demo;",
        "6   | ",
        "7   | -- Bước 3: Tạo bảng 'Student' theo đúng yêu cầu đề bài",
        "8   | CREATE TABLE Student (",
        "9   |     id INT,",
        "10  |     name VARCHAR(200),",
        "11  |     age INT,",
        "12  |     country VARCHAR(50)",
        "13  | );",
        "14  | ",
        "15  | -- Bước 4: Kiểm tra cấu trúc bảng vừa tạo",
        "16  | DESCRIBE Student;"
    ]

    cy = CODE_Y + 12
    for line in code_lines:
        num, content = line.split("|")
        draw.text((CODE_X + 8, cy), num.strip(), fill="#858585", font=f_code)
        
        # Simple syntax highlight simulation
        c_text = content
        if c_text.strip().startswith("--"):
            draw.text((CODE_X + 55, cy), c_text, fill="#6A9955", font=f_code)
        elif "CREATE DATABASE" in c_text or "CREATE TABLE" in c_text or "USE" in c_text or "DESCRIBE" in c_text:
            draw.text((CODE_X + 55, cy), c_text, fill="#569CD6", font=f_code_kw)
        elif "INT" in c_text or "VARCHAR" in c_text:
            draw.text((CODE_X + 55, cy), c_text, fill="#4EC9B0", font=f_code)
        else:
            draw.text((CODE_X + 55, cy), c_text, fill="#D4D4D4", font=f_code)
        cy += 24

    # 6. Bottom Panel - Action Output
    OUT_Y = H - 180
    draw.rectangle([0, OUT_Y, W, OUT_Y + 28], fill="#E2E8F0")
    draw.text((15, OUT_Y + 6), "Action Output", fill="#0F172A", font=f_tree_header)
    
    draw.rectangle([0, OUT_Y + 28, W, H], fill="#FFFFFF")
    draw.line([0, OUT_Y + 28, W, OUT_Y + 28], fill="#CBD5E1", width=1)

    # Output table headers
    draw.rectangle([0, OUT_Y + 28, W, OUT_Y + 52], fill="#F8FAFC")
    draw.line([0, OUT_Y + 52, W, OUT_Y + 52], fill="#E2E8F0", width=1)
    draw.text((35, OUT_Y + 33), "Time", fill="#64748B", font=f_badge)
    draw.text((120, OUT_Y + 33), "Action", fill="#64748B", font=f_badge)
    draw.text((500, OUT_Y + 33), "Message", fill="#64748B", font=f_badge)
    draw.text((950, OUT_Y + 33), "Duration", fill="#64748B", font=f_badge)

    actions = [
        ("16:35:10", "CREATE DATABASE demo", "1 row(s) affected", "0.015 sec", "#16A34A"),
        ("16:35:11", "USE demo", "0 row(s) affected", "0.000 sec", "#16A34A"),
        ("16:35:12", "CREATE TABLE Student ( id INT, name VARCHAR(200), age INT, country ... )", "0 row(s) affected", "0.031 sec", "#16A34A"),
        ("16:35:13", "DESCRIBE Student", "4 row(s) returned", "0.002 sec", "#16A34A")
    ]

    oy = OUT_Y + 58
    for t, act, msg, dur, col in actions:
        # Green success circle
        draw.ellipse([15, oy + 2, 25, oy + 12], fill=col)
        draw.text((17, oy + 1), "✓", fill="#FFFFFF", font=get_font(9, bold=True))
        draw.text((35, oy), t, fill="#334155", font=f_output)
        draw.text((120, oy), act[:55] + ("..." if len(act) > 55 else ""), fill="#0F172A", font=f_output)
        draw.text((500, oy), msg, fill="#16A34A", font=f_output)
        draw.text((950, oy), dur, fill="#64748B", font=f_output)
        oy += 22

    img.save(filename, "PNG", quality=95)
    print(f"Created: {filename}")

def create_table_structure_and_data_diagram(filename):
    W, H = 1200, 720
    img = Image.new("RGB", (W, H), color="#F8FAFC")
    draw = ImageDraw.Draw(img)

    f_title = get_font(16, bold=True)
    f_sec = get_font(13, bold=True)
    f_tbl_h = get_font(12, bold=True)
    f_tbl_c = get_mono_font(12, bold=False)
    f_badge = get_font(11, bold=True)

    # 1. Header Banner
    draw.rectangle([0, 0, W, 60], fill="#0F172A")
    draw.text((25, 18), "MySQL Result Inspector - Cấu trúc Bảng & Dữ liệu Mẫu (Bảng 'Student')", fill="#FFFFFF", font=f_title)
    draw.rectangle([W - 190, 15, W - 25, 45], fill="#0369A1", outline="#38BDF8", width=1)
    draw.text((W - 178, 22), "CSDL: demo | MySQL 8.0", fill="#FFFFFF", font=f_badge)

    # 2. Section 1: DESCRIBE Student
    draw.rectangle([25, 80, W - 25, 340], fill="#FFFFFF", outline="#E2E8F0", width=1)
    draw.rectangle([25, 80, W - 25, 120], fill="#F1F5F9")
    draw.text((40, 92), "1. Cấu trúc trường dữ liệu (Schema Metadata) - Kết quả: DESCRIBE Student;", fill="#1E293B", font=f_sec)
    
    # Table headers for DESCRIBE
    cols_desc = [
        ("Field", 180),
        ("Type", 200),
        ("Null", 120),
        ("Key", 120),
        ("Default", 160),
        ("Extra", 200)
    ]
    
    dy = 130
    draw.rectangle([40, dy, W - 40, dy + 28], fill="#E2E8F0")
    cx = 50
    for hname, hw in cols_desc:
        draw.text((cx, dy + 6), hname, fill="#334155", font=f_tbl_h)
        cx += hw

    desc_rows = [
        ("id", "int", "YES", "", "NULL", ""),
        ("name", "varchar(200)", "YES", "", "NULL", ""),
        ("age", "int", "YES", "", "NULL", ""),
        ("country", "varchar(50)", "YES", "", "NULL", "")
    ]

    dy = 162
    for r in desc_rows:
        draw.rectangle([40, dy, W - 40, dy + 32], fill="#FFFFFF" if (dy//32)%2==0 else "#F8FAFC", outline="#F1F5F9", width=1)
        cx = 50
        for i, val in enumerate(r):
            col_color = "#2563EB" if i == 0 else ("#059669" if i == 1 else "#0F172A")
            draw.text((cx, dy + 8), val, fill=col_color, font=f_tbl_c)
            cx += cols_desc[i][1]
        dy += 34

    draw.rectangle([40, 305, W - 40, 330], fill="#F0FDF4", outline="#BBF7D0", width=1)
    draw.text((50, 310), "✓ Đã khởi tạo thành công 4 thuộc tính (id, name, age, country) đúng chuẩn đề bài yêu cầu.", fill="#166534", font=f_badge)

    # 3. Section 2: SELECT * FROM Student
    draw.rectangle([25, 360, W - 25, 680], fill="#FFFFFF", outline="#E2E8F0", width=1)
    draw.rectangle([25, 360, W - 25, 400], fill="#F1F5F9")
    draw.text((40, 372), "2. Dữ liệu thực nghiệm (Sample Data Grid) - Kết quả: SELECT * FROM Student;", fill="#1E293B", font=f_sec)

    cols_data = [
        ("id (INT)", 150),
        ("name (VARCHAR 200)", 350),
        ("age (INT)", 180),
        ("country (VARCHAR 50)", 300)
    ]

    sy = 410
    draw.rectangle([40, sy, W - 40, sy + 28], fill="#E2E8F0")
    cx = 50
    for hname, hw in cols_data:
        draw.text((cx, sy + 6), hname, fill="#334155", font=f_tbl_h)
        cx += hw

    data_rows = [
        ("1", "Nguyen Van An", "20", "Vietnam"),
        ("2", "Tran Thi Bich", "21", "Vietnam"),
        ("3", "John Smith", "22", "United States"),
        ("4", "Tanaka Kenji", "19", "Japan"),
        ("5", "Le Hoang Nam", "23", "Vietnam")
    ]

    sy = 442
    for r in data_rows:
        draw.rectangle([40, sy, W - 40, sy + 32], fill="#FFFFFF" if (sy//32)%2==0 else "#F8FAFC", outline="#F1F5F9", width=1)
        cx = 50
        for i, val in enumerate(r):
            draw.text((cx, sy + 8), val, fill="#0F172A", font=f_tbl_c)
            cx += cols_data[i][1]
        sy += 34

    draw.rectangle([40, 640, W - 40, 665], fill="#EFF6FF", outline="#BFDBFE", width=1)
    draw.text((50, 645), "ℹ 5 rows in set (0.001 sec) - Toàn bộ dữ liệu hiển thị chính xác theo mô hình quan hệ RDBMS.", fill="#1E40AF", font=f_badge)

    img.save(filename, "PNG", quality=95)
    print(f"Created: {filename}")

def create_architecture_overview_diagram(filename):
    W, H = 1200, 650
    img = Image.new("RGB", (W, H), color="#FFFFFF")
    draw = ImageDraw.Draw(img)

    f_title = get_font(18, bold=True)
    f_sub = get_font(12, bold=False)
    f_box_h = get_font(13, bold=True)
    f_box_c = get_font(11, bold=False)
    f_badge = get_font(11, bold=True)

    # Title Banner
    draw.rectangle([0, 0, W, 80], fill="#0F172A")
    draw.text((35, 18), "KIẾN TRÚC MÔ HÌNH DỮ LIỆU BẢNG (TABLE DATA MODEL ARCHITECTURE)", fill="#FFFFFF", font=f_title)
    draw.text((35, 48), "Mối liên kết phân tầng từ MySQL Server Instance đến Cơ sở dữ liệu, Bảng và Trường thuộc tính", fill="#94A3B8", font=f_sub)

    # 4 Architecture Layers
    cards = [
        ("TẦNG 1: RDBMS SERVER", "MySQL Server Instance (localhost:3306)", 
         ["• Phiên bản: MySQL 8.0 CE", "• Bộ máy lưu trữ: InnoDB Engine", "• Quản lý kết nối Client-Server", "• Thực thi bộ phân tích cú pháp SQL"],
         "#3B82F6", "#EFF6FF", 40),
        ("TẦNG 2: CƠ SỞ DỮ LIỆU", "Database / Schema: `demo`",
         ["• Lệnh tạo: CREATE DATABASE demo", "• Bảng mã mặc định: utf8mb4", "• Quản lý không gian tên (Namespace)", "• Chứa các đối tượng Tables, Views, SP"],
         "#059669", "#ECFDF5", 325),
        ("TẦNG 3: BẢNG DỮ LIỆU", "Table: `Student`",
         ["• Lệnh tạo: CREATE TABLE Student(...)", "• Cấu trúc dòng (Row) & cột (Column)", "• Định nghĩa tập hợp thực thể sinh viên", "• Lưu trữ dữ liệu thực tế trên đĩa"],
         "#D97706", "#FFFBEB", 610),
        ("TẦNG 4: THUỘC TÍNH (FIELDS)", "Columns & Data Types",
         ["• id: INT (Mã định danh)", "• name: VARCHAR(200) (Họ tên)", "• age: INT (Tuổi sinh viên)", "• country: VARCHAR(50) (Quốc gia)"],
         "#8B5CF6", "#F5F3FF", 895)
    ]

    card_w = 265
    card_h = 360
    card_y = 120

    for title, subtitle, items, border_c, bg_c, x in cards:
        # Card body
        draw.rectangle([x, card_y, x + card_w, card_y + card_h], fill=bg_c, outline=border_c, width=2)
        # Header bar
        draw.rectangle([x, card_y, x + card_w, card_y + 45], fill=border_c)
        draw.text((x + 12, card_y + 8), title, fill="#FFFFFF", font=get_font(11, bold=True))
        draw.text((x + 12, card_y + 24), subtitle[:28] + ("..." if len(subtitle) > 28 else ""), fill="#FFFFFF", font=get_font(10, bold=False))

        # Items
        iy = card_y + 60
        for item in items:
            draw.text((x + 15, iy), item, fill="#1E293B", font=f_box_c)
            iy += 35

    # Arrows between cards
    for ax in [307, 592, 877]:
        draw.line([ax, card_y + card_h // 2, ax + 16, card_y + card_h // 2], fill="#475569", width=3)
        draw.polygon([(ax + 16, card_y + card_h // 2 - 5), (ax + 24, card_y + card_h // 2), (ax + 16, card_y + card_h // 2 + 5)], fill="#475569")

    # Bottom Summary Box
    draw.rectangle([40, 510, W - 40, 610], fill="#F8FAFC", outline="#CBD5E1", width=1)
    draw.text((60, 525), "QUY TRÌNH THỰC THI CHUẨN TRÊN MYSQL WORKBENCH:", fill="#0F172A", font=get_font(12, bold=True))
    draw.text((60, 552), "1. Mở New Query Tab (Ctrl+T) ➔ 2. Soạn thảo SQL Script ➔ 3. Nhấn biểu tượng Execute (Tia sét) ➔ 4. Xác nhận trạng thái tại Action Output", fill="#334155", font=f_box_c)
    draw.text((60, 578), "5. Nhấn nút Refresh tại Schemas Navigator để thấy bảng `Student` cùng 4 trường thuộc tính xuất hiện trên giao diện.", fill="#059669", font=get_font(11, bold=True))

    img.save(filename, "PNG", quality=95)
    print(f"Created: {filename}")

if __name__ == "__main__":
    out_dir = r"C:\Users\dathao\.gemini\antigravity-ide\scratch\thuc-hanh-tao-bang-mysql-workbench"
    create_workbench_create_table_diagram(os.path.join(out_dir, "mysql_workbench_sql_create_table.png"))
    create_table_structure_and_data_diagram(os.path.join(out_dir, "mysql_workbench_table_structure_and_data.png"))
    create_architecture_overview_diagram(os.path.join(out_dir, "mysql_workbench_architecture_overview.png"))
