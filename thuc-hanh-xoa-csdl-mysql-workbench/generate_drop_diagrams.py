import os
from PIL import Image, ImageDraw, ImageFont

def get_font(size, bold=False):
    font_paths = [
        r"C:\Windows\Fonts\segoeui.ttf" if not bold else r"C:\Windows\Fonts\segouib.ttf",
        r"C:\Windows\Fonts\calibri.ttf" if not bold else r"C:\Windows\Fonts\calibrib.ttf",
        r"C:\Windows\Fonts\arial.ttf" if not bold else r"C:\Windows\Fonts\arialbd.ttf"
    ]
    for p in font_paths:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                pass
    return ImageFont.load_default()

def render_gui_drop():
    w, h = 1400, 850
    img = Image.new("RGB", (w, h), "#0F172A")
    draw = ImageDraw.Draw(img)

    f_title = get_font(24, bold=True)
    f_body = get_font(15, bold=False)
    f_body_b = get_font(15, bold=True)
    f_code = get_font(17, bold=True)
    f_small = get_font(13, bold=False)

    # Top App Bar
    draw.rectangle([0, 0, w, 40], fill="#020617")
    draw.text((20, 10), "MySQL Workbench - [Local instance 3306] - Cach 1: Xoa CSDL bang GUI (Drop Schema & Drop Now)", fill="#F8FAFC", font=f_body_b)
    draw.rectangle([w - 45, 0, w, 40], fill="#EF4444")
    draw.text((w - 28, 10), "X", fill="#FFFFFF", font=f_body_b)

    # Menu bar
    draw.rectangle([0, 40, w, 75], fill="#1E293B")
    menus = ["File", "Edit", "View", "Query", "Database", "Server", "Tools", "Scripting", "Help"]
    mx = 20
    for m in menus:
        draw.text((mx, 48), m, fill="#94A3B8", font=f_small)
        mx += 65

    # Toolbar
    draw.rectangle([0, 75, w, 115], fill="#334155")
    draw.rounded_rectangle([25, 80, 260, 110], radius=5, fill="#475569")
    draw.text((35, 86), "[+] Create a new schema", fill="#CBD5E1", font=f_small)

    # Left Sidebar: Navigator & SCHEMAS
    draw.rectangle([0, 115, 320, h - 35], fill="#020617")
    draw.rectangle([0, 115, 320, 150], fill="#0F172A")
    draw.text((20, 122), "Navigator: SCHEMAS", fill="#F8FAFC", font=f_body_b)
    draw.text((280, 122), "[R]", fill="#60A5FA", font=f_body_b)

    # Schemas list with context menu
    schemas = [
        ("[-] sys", False),
        ("[-] sakila", False),
        ("[*] my_database (Chon de xoa)", True),
        ("[-] world", False)
    ]
    sy = 165
    for s_name, is_target in schemas:
        if is_target:
            draw.rectangle([5, sy - 4, 315, sy + 30], fill="#7F1D1D", outline="#EF4444", width=1)
            draw.text((15, sy + 2), s_name, fill="#FCA5A5", font=f_body_b)
            # Context menu popup mockup
            menu_y = sy + 32
            draw.rectangle([60, menu_y, 280, menu_y + 160], fill="#1E293B", outline="#475569", width=1)
            ctx_items = [
                "Set as Default Schema",
                "Schema Inspector",
                "Create Schema...",
                "Drop Schema...  <-- CLICK CHON",
                "Refresh All"
            ]
            cy = menu_y + 6
            for idx, c_item in enumerate(ctx_items):
                if "Drop Schema" in c_item:
                    draw.rectangle([62, cy - 2, 278, cy + 24], fill="#DC2626")
                    draw.text((70, cy), c_item, fill="#FFFFFF", font=f_body_b)
                else:
                    draw.text((70, cy), c_item, fill="#94A3B8", font=f_small)
                cy += 30
            sy += 165
        else:
            draw.text((15, sy), s_name, fill="#94A3B8", font=f_body)
            sy += 38

    # Right Content Area (Blurred editor background)
    draw.rectangle([320, 115, w, h - 35], fill="#090D16")

    # Center Modal Dialog: Confirm Drop Schema
    modal_box = [420, 220, 1280, 600]
    draw.rounded_rectangle(modal_box, radius=10, fill="#0F172A", outline="#DC2626", width=2)
    
    # Modal Header
    draw.rectangle([420, 220, 1280, 275], fill="#7F1D1D")
    draw.text((450, 235), "CANH BAO NGUY HIEM: Xac Nhan Xoa Co So Du Lieu (Confirm Schema Drop)", fill="#FEE2E2", font=f_title)

    # Modal Body
    draw.text((460, 310), "Ban dang thao tac yeu cau xoa hoan toan CSDL:", fill="#F8FAFC", font=f_body)
    draw.text((460, 345), "SCHEMA:  `my_database`", fill="#F87171", font=f_code)
    
    warning_box = [460, 395, 1240, 485]
    draw.rounded_rectangle(warning_box, radius=6, fill="#450A0A", outline="#B91C1C", width=1)
    draw.text((480, 410), "! CANH BAO DU LIEU TU DE BAI:", fill="#FCA5A5", font=f_body_b)
    draw.text((480, 440), "Tat ca cac bang, view, stored procedure va toan bo du lieu ben trong se bi XOA VINH VIEN", fill="#FEF2F2", font=f_body)
    draw.text((480, 462), "neu chua duoc sao luu (backup) truoc do. Thao tac nay khong the hoan tac (Cannot be undone)!", fill="#FCA5A5", font=f_small)

    # Modal Action Buttons
    # Button 1: Review SQL
    draw.rounded_rectangle([750, 520, 890, 565], radius=5, fill="#334155", outline="#64748B", width=1)
    draw.text((770, 532), "Review SQL", fill="#E2E8F0", font=f_body)

    # Button 2: Cancel
    draw.rounded_rectangle([910, 520, 1030, 565], radius=5, fill="#334155", outline="#64748B", width=1)
    draw.text((945, 532), "Cancel", fill="#CBD5E1", font=f_body)

    # Button 3: Drop Now (Highlighted TARGET)
    draw.rounded_rectangle([1050, 520, 1240, 565], radius=5, fill="#DC2626", outline="#EF4444", width=2)
    draw.text((1085, 532), "Drop Now  [V]", fill="#FFFFFF", font=f_body_b)
    draw.text((1060, 572), "<-- NHAN NUT NAY THEO DE BAI", fill="#FBBF24", font=f_small)

    # Action Output at Bottom
    draw.rectangle([320, 680, w, h - 35], fill="#020617")
    draw.rectangle([320, 680, w, 715], fill="#1E293B")
    draw.text((340, 688), "Action Output - Ket qua thuc thi", fill="#F8FAFC", font=f_body_b)

    draw.rectangle([320, 715, w, 755], fill="#064E3B")
    draw.text((340, 725), "[OK]", fill="#4ADE80", font=f_body_b)
    draw.text((410, 725), "16:25:20", fill="#E2E8F0", font=f_small)
    draw.text((500, 725), "DROP SCHEMA `my_database`", fill="#FFFFFF", font=f_body_b)
    draw.text((820, 725), "0 row(s) affected", fill="#4ADE80", font=f_body_b)
    draw.text((1150, 725), "0.018 sec", fill="#CBD5E1", font=f_small)

    # Bottom Status Bar
    draw.rectangle([0, h - 35, w, h], fill="#020617")
    draw.text((20, h - 26), "Ready. Connected to MySQL 8.0 on port 3306. | Cach 1: Xoa bang GUI (Drop Schema -> Drop Now) thanh cong | Tac gia: Nguyen Tuan Dat", fill="#22C55E", font=f_small)

    out_file = r"C:\Users\dathao\.gemini\antigravity-ide\scratch\thuc-hanh-xoa-csdl-mysql-workbench\mysql_workbench_gui_drop_schema.png"
    img.save(out_file)
    print("Saved clean GUI Drop diagram:", out_file)

def render_sql_drop():
    w, h = 1400, 850
    img = Image.new("RGB", (w, h), "#0F172A")
    draw = ImageDraw.Draw(img)

    f_title = get_font(24, bold=True)
    f_body = get_font(15, bold=False)
    f_body_b = get_font(15, bold=True)
    f_code = get_font(18, bold=True)
    f_small = get_font(13, bold=False)

    # Top App Bar
    draw.rectangle([0, 0, w, 40], fill="#020617")
    draw.text((20, 10), "MySQL Workbench - [Local instance 3306] - Cach 2: Xoa CSDL bang cau lenh SQL (DROP DATABASE)", fill="#F8FAFC", font=f_body_b)
    draw.rectangle([w - 45, 0, w, 40], fill="#EF4444")
    draw.text((w - 28, 10), "X", fill="#FFFFFF", font=f_body_b)

    # Menu bar
    draw.rectangle([0, 40, w, 75], fill="#1E293B")
    menus = ["File", "Edit", "View", "Query", "Database", "Server", "Tools", "Scripting", "Help"]
    mx = 20
    for m in menus:
        draw.text((mx, 48), m, fill="#94A3B8", font=f_small)
        mx += 65

    # Toolbar
    draw.rectangle([0, 75, w, 115], fill="#334155")
    draw.rounded_rectangle([25, 80, 240, 110], radius=5, fill="#1D4ED8", outline="#60A5FA", width=1)
    draw.text((35, 86), "[+] New Query Tab (Ctrl+T)", fill="#FFFFFF", font=f_body_b)

    draw.rounded_rectangle([250, 80, 420, 110], radius=5, fill="#16A34A", outline="#4ADE80", width=1)
    draw.text((260, 86), "> Execute (Ctrl+Enter)", fill="#FFFFFF", font=f_body_b)

    # Left Sidebar: Navigator & SCHEMAS
    draw.rectangle([0, 115, 300, h - 35], fill="#020617")
    draw.rectangle([0, 115, 300, 150], fill="#0F172A")
    draw.text((20, 122), "Navigator: SCHEMAS", fill="#F8FAFC", font=f_body_b)
    draw.text((260, 122), "[R]", fill="#60A5FA", font=f_body_b)

    schemas = [
        ("[-] sys", False),
        ("[-] sakila", False),
        ("[-] world", False),
        ("[x] my_database (Da bien mat sau khi xoa)", True)
    ]
    sy = 165
    for s_name, is_target in schemas:
        if is_target:
            draw.rectangle([5, sy - 4, 295, sy + 28], fill="#334155")
            draw.text((15, sy), s_name, fill="#94A3B8", font=f_small)
        else:
            draw.text((15, sy), s_name, fill="#CBD5E1", font=f_body)
        sy += 38

    # Right Content Area: Query Editor Tab
    draw.rectangle([300, 115, w, 520], fill="#0F172A")
    
    # Query Tab Header
    draw.rectangle([300, 115, 480, 150], fill="#1E293B")
    draw.text((315, 122), "Query 1  [X]", fill="#38BDF8", font=f_body_b)

    draw.rectangle([300, 150, 350, 520], fill="#020617")
    for l_num in range(1, 10):
        draw.text((320, 160 + (l_num - 1) * 36), str(l_num), fill="#475569", font=f_small)

    editor_x = 370
    draw.text((editor_x, 160), "-- ===========================================================", fill="#64748B", font=f_code)
    draw.text((editor_x, 196), "-- BAI TAP: XOA CSDL BANG CAU LENH SQL TREN MYSQL WORKBENCH", fill="#64748B", font=f_code)
    draw.text((editor_x, 232), "-- ===========================================================", fill="#64748B", font=f_code)
    
    # Target Query Highlighted
    draw.rectangle([editor_x - 10, 268, w - 30, 312], fill="#450A0A", outline="#DC2626", width=2)
    draw.text((editor_x, 276), "DROP DATABASE `my_database`;", fill="#FCA5A5", font=f_code)
    draw.text((editor_x + 360, 276), "<-- CAU LENH YEU CAU DE BAI", fill="#FBBF24", font=f_body_b)

    draw.text((editor_x, 340), "-- Lenh mo rong an toan phong ngua loi:", fill="#94A3B8", font=f_code)
    draw.text((editor_x, 376), "DROP DATABASE IF EXISTS `my_database`;", fill="#38BDF8", font=f_code)
    draw.text((editor_x, 412), "SHOW DATABASES;", fill="#F43F5E", font=f_code)

    # Action Output Panel at Bottom
    draw.rectangle([300, 520, w, h - 35], fill="#020617")
    draw.rectangle([300, 520, w, 555], fill="#1E293B")
    draw.text((315, 526), "Action Output", fill="#F8FAFC", font=f_body_b)

    draw.rectangle([300, 555, w, 585], fill="#0F172A")
    draw.text((320, 560), "Status", fill="#94A3B8", font=f_small)
    draw.text((400, 560), "Time", fill="#94A3B8", font=f_small)
    draw.text((490, 560), "Action", fill="#94A3B8", font=f_small)
    draw.text((820, 560), "Message", fill="#94A3B8", font=f_small)
    draw.text((1150, 560), "Duration / Fetch", fill="#94A3B8", font=f_small)

    # Output Row: DROP DATABASE
    draw.rectangle([300, 585, w, 625], fill="#064E3B")
    draw.text((320, 595), "[OK]", fill="#4ADE80", font=f_body_b)
    draw.text((400, 595), "16:25:30", fill="#E2E8F0", font=f_small)
    draw.text((490, 595), "DROP DATABASE `my_database`", fill="#FFFFFF", font=f_body_b)
    draw.text((820, 595), "0 row(s) affected", fill="#4ADE80", font=f_body_b)
    draw.text((1150, 595), "0.012 sec", fill="#CBD5E1", font=f_small)

    # Output Row: SHOW DATABASES
    draw.rectangle([300, 625, w, 665], fill="#020617")
    draw.text((320, 635), "[OK]", fill="#4ADE80", font=f_body_b)
    draw.text((400, 635), "16:25:32", fill="#E2E8F0", font=f_small)
    draw.text((490, 635), "SHOW DATABASES", fill="#E2E8F0", font=f_body)
    draw.text((820, 635), "3 row(s) returned (my_database khong con)", fill="#94A3B8", font=f_small)
    draw.text((1150, 635), "0.000 sec", fill="#CBD5E1", font=f_small)

    # Bottom Status Bar
    draw.rectangle([0, h - 35, w, h], fill="#020617")
    draw.text((20, h - 26), "Query completed successfully. Database `my_database` has been dropped. | Tac gia: Nguyen Tuan Dat (proyctk03-eng)", fill="#22C55E", font=f_small)

    out_file = r"C:\Users\dathao\.gemini\antigravity-ide\scratch\thuc-hanh-xoa-csdl-mysql-workbench\mysql_workbench_sql_query_drop_database.png"
    img.save(out_file)
    print("Saved clean SQL Drop diagram:", out_file)

def render_safety_lifecycle():
    w, h = 1400, 750
    img = Image.new("RGB", (w, h), "#0F172A")
    draw = ImageDraw.Draw(img)

    f_title = get_font(26, bold=True)
    f_step_title = get_font(18, bold=True)
    f_body = get_font(15, bold=False)
    f_code = get_font(15, bold=True)
    f_small = get_font(13, bold=False)

    # Title Banner
    draw.rectangle([0, 0, w, 110], fill="#020617")
    draw.text((50, 25), "QUY TRINH 4 BUOC AN TOAN KHI XOA CO SO DU LIEU (DATA SAFETY LIFECYCLE)", fill="#F8FAFC", font=f_title)
    draw.text((50, 70), "Chuan hoa theo khuyen nghi RDBMS / MySQL: Phong ngua mat mat du lieu vinh vien va dam bao tinh lien tuc", fill="#94A3B8", font=f_body)

    # 4 Steps Cards
    steps = [
        ("BUOC 1: XAC MINH", "Xac minh moi truong & CSDL can xoa", [
            "Kiem tra dung moi truong Dev/Test/Staging",
            "Tuyet doi khong Drop truc tiep tren Production",
            "Kiem tra danh sach user & app dang ket noi"
        ], "#1E3A8A", "#3B82F6"),
        ("BUOC 2: SAO LUU (BACKUP)", "Backup truoc khi thuc hien Drop", [
            "Workbench: Server -> Data Export",
            "CLI: mysqldump -u root -p db > db.sql",
            "Kiem tra file dump co dung luong > 0 byte"
        ], "#065F46", "#10B981"),
        ("BUOC 3: THUC THI AN TOAN", "Cau lenh DROP co co che IF EXISTS", [
            "Dung lenh: DROP DATABASE IF EXISTS `db`;",
            "Tranh phat sinh Error 1008 lam stop script",
            "Xem xet thu hoi quyen DROP cua App User"
        ], "#7F1D1D", "#EF4444"),
        ("BUOC 4: KIEM CHUNG", "Verify & Giai phong tai nguyen", [
            "Chay: SHOW DATABASES; de xac nhan",
            "Kiem tra Schema Navigator da bien mat",
            "Ghi log audit thoi diem & nguoi thuc hien"
        ], "#0F766E", "#14B8A6")
    ]

    cx = 50
    card_w = 300
    for idx, (s_tag, s_name, points, bg_c, b_c) in enumerate(steps):
        box = [cx, 150, cx + card_w, 660]
        draw.rounded_rectangle(box, radius=8, fill="#1E293B", outline=b_c, width=2)
        
        # Header banner
        draw.rounded_rectangle([cx, 150, cx + card_w, 220], radius=8, fill=bg_c)
        draw.text((cx + 15, 160), s_tag, fill="#F8FAFC", font=f_step_title)
        draw.text((cx + 15, 192), s_name, fill="#E2E8F0", font=f_small)

        # Content bullets
        py = 245
        for p in points:
            draw.text((cx + 15, py), "[*]", fill=b_c, font=f_code)
            # Wrap text manually if needed
            words = p.split()
            line1 = " ".join(words[:4])
            line2 = " ".join(words[4:])
            draw.text((cx + 38, py), line1, fill="#F8FAFC", font=f_body)
            if line2:
                py += 22
                draw.text((cx + 38, py), line2, fill="#CBD5E1", font=f_small)
            py += 36

        # Flow arrow between cards
        if idx < 3:
            draw.text((cx + card_w + 5, 380), "==>", fill="#60A5FA", font=f_code)

        cx += card_w + 33

    # Bottom status bar
    draw.rectangle([0, h - 40, w, h], fill="#020617")
    draw.text((50, h - 28), "Tac gia: Nguyen Tuan Dat (proyctk03-eng) | RDBMS Safe Drop Practice Architecture", fill="#60A5FA", font=f_small)

    out_file = r"C:\Users\dathao\.gemini\antigravity-ide\scratch\thuc-hanh-xoa-csdl-mysql-workbench\mysql_workbench_data_safety_lifecycle.png"
    img.save(out_file)
    print("Saved clean Safety Lifecycle diagram:", out_file)

if __name__ == "__main__":
    render_gui_drop()
    render_sql_drop()
    render_safety_lifecycle()
