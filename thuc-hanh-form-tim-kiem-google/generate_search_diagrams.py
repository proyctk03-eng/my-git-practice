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

def create_ui_demo_diagram(filename):
    W, H = 1200, 720
    img = Image.new("RGB", (W, H), color="#F8FAFC")
    draw = ImageDraw.Draw(img)

    f_title = get_font(13, bold=True)
    f_url = get_mono_font(12, bold=False)
    f_body = get_font(13, bold=False)
    f_bold = get_font(13, bold=True)
    f_btn = get_font(12, bold=True)
    f_badge = get_font(11, bold=True)
    f_google_logo = get_font(36, bold=True)

    # 1. Browser Window Frame (Top)
    draw.rectangle([0, 0, W, 40], fill="#1E293B")
    draw.text((20, 11), "Google Search Form - Thực Hành Gửi Dữ Liệu Lên Server", fill="#E2E8F0", font=f_title)
    # Window controls
    draw.rectangle([W - 90, 12, W - 75, 26], fill="#475569")
    draw.rectangle([W - 65, 12, W - 50, 26], fill="#475569")
    draw.rectangle([W - 40, 12, W - 25, 26], fill="#EF4444")

    # 2. Browser Navigation Bar
    draw.rectangle([0, 40, W, 82], fill="#FFFFFF")
    draw.line([0, 82, W, 82], fill="#E2E8F0", width=1)
    
    # Nav buttons
    draw.text((20, 52), "←   →   ⟳", fill="#64748B", font=f_bold)
    
    # URL bar
    draw.rectangle([110, 48, W - 40, 74], fill="#F1F5F9", outline="#CBD5E1", width=1)
    draw.text((125, 53), "🔒 https://proyctk03-eng.github.io/thuc-hanh-form-tim-kiem-google/index.html", fill="#0F172A", font=f_url)

    # 3. Two-Column Layout: Left = Local Form, Right = Google Search Result
    COL_W = 560
    
    # --- LEFT PANEL: CLIENT LOCAL FORM ---
    L_X, L_Y = 30, 105
    draw.rectangle([L_X, L_Y, L_X + COL_W, H - 30], fill="#FFFFFF", outline="#CBD5E1", width=1)
    
    # Card Header
    draw.rectangle([L_X, L_Y, L_X + COL_W, L_Y + 45], fill="#F8FAFC")
    draw.line([L_X, L_Y + 45, L_X + COL_W, L_Y + 45], fill="#E2E8F0", width=1)
    draw.text((L_X + 20, L_Y + 12), "1. Giao Diện Form HTML Thực Hành (Client)", fill="#0F172A", font=f_bold)
    draw.rectangle([L_X + COL_W - 140, L_Y + 10, L_X + COL_W - 15, L_Y + 35], fill="#EFF6FF", outline="#93C5FD", width=1)
    draw.text((L_X + COL_W - 130, L_Y + 14), "METHOD: GET", fill="#1E40AF", font=f_badge)

    # Logo
    draw.text((L_X + 210, L_Y + 80), "G", fill="#4285F4", font=f_google_logo)
    draw.text((L_X + 235, L_Y + 80), "o", fill="#EA4335", font=f_google_logo)
    draw.text((L_X + 255, L_Y + 80), "o", fill="#FBBC05", font=f_google_logo)
    draw.text((L_X + 275, L_Y + 80), "g", fill="#4285F4", font=f_google_logo)
    draw.text((L_X + 298, L_Y + 80), "l", fill="#34A853", font=f_google_logo)
    draw.text((L_X + 310, L_Y + 80), "e", fill="#EA4335", font=f_google_logo)

    # Form Code Callout
    draw.rectangle([L_X + 30, L_Y + 150, L_X + COL_W - 30, L_Y + 230], fill="#0F172A", outline="#1E293B", width=1)
    draw.text((L_X + 45, L_Y + 160), '<form action="https://www.google.com.vn/search" method="GET">', fill="#569CD6", font=get_mono_font(11, bold=True))
    draw.text((L_X + 60, L_Y + 182), '<input type="text" name="q" placeholder="Nhập từ khóa"/>', fill="#9CDCFE", font=get_mono_font(11, bold=False))
    draw.text((L_X + 60, L_Y + 204), '<input type="submit" value="Tìm kiếm"/>', fill="#CE9178", font=get_mono_font(11, bold=False))

    # Form Input UI rendering
    draw.text((L_X + 35, L_Y + 250), "Trường nhập liệu (name='q'):", fill="#334155", font=get_font(11, bold=True))
    draw.rectangle([L_X + 30, L_Y + 275, L_X + COL_W - 30, L_Y + 325], fill="#FFFFFF", outline="#3B82F6", width=2)
    draw.text((L_X + 45, L_Y + 288), "🔍  Lập trình web HTML", fill="#0F172A", font=f_body)

    # Submit Button UI
    draw.rectangle([L_X + 180, L_Y + 350, L_X + 360, L_Y + 395], fill="#3B82F6", outline="#2563EB", width=1)
    draw.text((L_X + 225, L_Y + 363), "Tìm kiếm 🚀", fill="#FFFFFF", font=f_btn)

    # Action note
    draw.rectangle([L_X + 30, L_Y + 430, L_X + COL_W - 30, L_Y + 540], fill="#F0FDF4", outline="#86EFAC", width=1)
    draw.text((L_X + 45, L_Y + 445), "QUY TRÌNH KHI NGƯỜI DÙNG BẤM 'TÌM KIẾM':", fill="#166534", font=get_font(11, bold=True))
    draw.text((L_X + 45, L_Y + 472), "1. Trình duyệt thu thập giá trị ô input: 'Lập trình web HTML'", fill="#15803D", font=get_font(11, bold=False))
    draw.text((L_X + 45, L_Y + 494), "2. Nối tham số vào URL mục tiêu: action + '?' + name + '=' + value", fill="#15803D", font=get_font(11, bold=False))
    draw.text((L_X + 45, L_Y + 516), "3. Trình duyệt gửi HTTP GET Request tới Google Search Server.", fill="#15803D", font=get_font(11, bold=False))

    # --- RIGHT PANEL: GOOGLE SEARCH RESULT ---
    R_X = 610
    draw.rectangle([R_X, L_Y, R_X + COL_W, H - 30], fill="#FFFFFF", outline="#CBD5E1", width=1)
    
    # Header
    draw.rectangle([R_X, L_Y, R_X + COL_W, L_Y + 45], fill="#F8FAFC")
    draw.line([R_X, L_Y + 45, R_X + COL_W, L_Y + 45], fill="#E2E8F0", width=1)
    draw.text((R_X + 20, L_Y + 12), "2. Kết Quả Nhận Được Trên Google Search (Server)", fill="#0F172A", font=f_bold)

    # Address bar on Google
    draw.rectangle([R_X + 20, L_Y + 60, R_X + COL_W - 20, L_Y + 95], fill="#EFF6FF", outline="#93C5FD", width=1)
    draw.text((R_X + 30, L_Y + 68), "URL đích:", fill="#1E40AF", font=get_font(11, bold=True))
    draw.text((R_X + 90, L_Y + 68), "https://www.google.com.vn/search?q=Lập+trình+web+HTML", fill="#0369A1", font=get_mono_font(11, bold=False))

    # Search result item 1
    draw.text((R_X + 30, L_Y + 120), "https://codegym.vn › hoc-lap-trinh-web", fill="#475569", font=get_font(11, bold=False))
    draw.text((R_X + 30, L_Y + 140), "Khóa học Lập trình Web từ cơ bản đến nâng cao - CodeGym", fill="#1A0DAB", font=get_font(13, bold=True))
    draw.text((R_X + 30, L_Y + 165), "Học lập trình web với HTML5, CSS3, JavaScript và cơ sở dữ liệu...", fill="#4B5563", font=get_font(11, bold=False))
    draw.text((R_X + 30, L_Y + 185), "Thực hành xây dựng các ứng dụng web thực tế theo chuẩn doanh nghiệp.", fill="#4B5563", font=get_font(11, bold=False))

    # Search result item 2
    draw.text((R_X + 30, L_Y + 230), "https://developer.mozilla.org › Web › HTML › Element › form", fill="#475569", font=get_font(11, bold=False))
    draw.text((R_X + 30, L_Y + 250), "<form>: The HTML Form element - MDN Web Docs", fill="#1A0DAB", font=get_font(13, bold=True))
    draw.text((R_X + 30, L_Y + 275), "The <form> HTML element represents a document section containing", fill="#4B5563", font=get_font(11, bold=False))
    draw.text((R_X + 30, L_Y + 295), "interactive controls for submitting information to a web server (action & method).", fill="#4B5563", font=get_font(11, bold=False))

    # Search result item 3
    draw.text((R_X + 30, L_Y + 340), "https://w3schools.com › html › html_forms", fill="#475569", font=get_font(11, bold=False))
    draw.text((R_X + 30, L_Y + 360), "HTML Forms - W3Schools", fill="#1A0DAB", font=get_font(13, bold=True))
    draw.text((R_X + 30, L_Y + 385), "An HTML form is used to collect user input. The user input is most often", fill="#4B5563", font=get_font(11, bold=False))
    draw.text((R_X + 30, L_Y + 405), "sent to a server for processing using GET or POST HTTP methods.", fill="#4B5563", font=get_font(11, bold=False))

    # Summary verification box
    draw.rectangle([R_X + 20, L_Y + 450, R_X + COL_W - 20, L_Y + 540], fill="#FEF3C7", outline="#FCD34D", width=1)
    draw.text((R_X + 35, L_Y + 465), "ĐÁNH GIÁ KẾT QUẢ THỰC NGHIỆM:", fill="#92400E", font=get_font(11, bold=True))
    draw.text((R_X + 35, L_Y + 490), "✓ Dữ liệu từ form đã truyền tới máy chủ Google thành công 100%.", fill="#B45309", font=get_font(11, bold=False))
    draw.text((R_X + 35, L_Y + 512), "✓ Máy chủ phân tích đúng tham số `q` và trả về đúng nội dung tìm kiếm.", fill="#B45309", font=get_font(11, bold=False))

    img.save(filename, "PNG", quality=95)
    print(f"Created: {filename}")

def create_get_vs_post_diagram(filename):
    W, H = 1200, 720
    img = Image.new("RGB", (W, H), color="#FFFFFF")
    draw = ImageDraw.Draw(img)

    f_title = get_font(18, bold=True)
    f_sub = get_font(12, bold=False)
    f_box_h = get_font(13, bold=True)
    f_box_c = get_font(11, bold=False)
    f_mono = get_mono_font(11, bold=False)
    f_badge = get_font(11, bold=True)

    # Title Banner
    draw.rectangle([0, 0, W, 80], fill="#0F172A")
    draw.text((35, 18), "SƠ ĐỒ PHÂN TÍCH KIẾN TRÚC GIAO THỨC HTTP: GET VS POST", fill="#FFFFFF", font=f_title)
    draw.text((35, 48), "Cơ chế truyền tải dữ liệu từ Biểu mẫu HTML (Client) lên Máy chủ (Web Server)", fill="#94A3B8", font=f_sub)

    # --- ROW 1: METHOD GET ---
    Y1 = 110
    draw.rectangle([40, Y1, W - 40, Y1 + 250], fill="#F0F9FF", outline="#0284C7", width=2)
    # Header bar
    draw.rectangle([40, Y1, W - 40, Y1 + 40], fill="#0284C7")
    draw.text((55, Y1 + 10), "1. PHƯƠNG THỨC HTTP GET (Mặc định cho tìm kiếm / Truy vấn dữ liệu)", fill="#FFFFFF", font=f_box_h)
    draw.text((W - 250, Y1 + 12), "action + ?q=keyword", fill="#E0F2FE", font=f_mono)

    # Client Box
    draw.rectangle([70, Y1 + 60, 320, Y1 + 225], fill="#FFFFFF", outline="#BAE6FD", width=1)
    draw.text((85, Y1 + 75), "💻 Trình Duyệt (Client)", fill="#0369A1", font=get_font(12, bold=True))
    draw.text((85, Y1 + 100), "• Form: <form method='GET'>", fill="#334155", font=f_box_c)
    draw.text((85, Y1 + 125), "• Input: name='q', value='CodeGym'", fill="#334155", font=f_box_c)
    draw.text((85, Y1 + 150), "• Dữ liệu gắn liền sau URL", fill="#334155", font=f_box_c)
    draw.text((85, Y1 + 175), "• Thanh địa chỉ hiện rõ từ khóa", fill="#16A34A", font=get_font(11, bold=True))

    # Arrow 1
    draw.line([330, Y1 + 140, 580, Y1 + 140], fill="#0284C7", width=3)
    draw.polygon([(580, Y1 + 140), (570, Y1 + 133), (570, Y1 + 147)], fill="#0284C7")
    draw.text((345, Y1 + 115), "HTTP Request Line: GET /search?q=CodeGym HTTP/1.1", fill="#0369A1", font=f_mono)

    # Server Box
    draw.rectangle([590, Y1 + 60, 840, Y1 + 225], fill="#FFFFFF", outline="#BAE6FD", width=1)
    draw.text((605, Y1 + 75), "🖥️ Máy Chủ (Google Server)", fill="#0369A1", font=get_font(12, bold=True))
    draw.text((605, Y1 + 100), "• Bóc tách Query String (?q=...)", fill="#334155", font=f_box_c)
    draw.text((605, Y1 + 125), "• Truy vấn Index Database", fill="#334155", font=f_box_c)
    draw.text((605, Y1 + 150), "• Trả về HTML kết quả tìm kiếm", fill="#334155", font=f_box_c)
    draw.text((605, Y1 + 175), "• HTTP Response: 200 OK", fill="#16A34A", font=get_font(11, bold=True))

    # Characteristics Box
    draw.rectangle([860, Y1 + 60, W - 60, Y1 + 225], fill="#F8FAFC", outline="#CBD5E1", width=1)
    draw.text((875, Y1 + 75), "Đặc Điểm Kỹ Thuật:", fill="#0F172A", font=get_font(12, bold=True))
    draw.text((875, Y1 + 100), "✔ Bookmark / Share URL được", fill="#16A34A", font=f_box_c)
    draw.text((875, Y1 + 125), "✔ Lưu trong Browser History", fill="#16A34A", font=f_box_c)
    draw.text((875, Y1 + 150), "✔ Tính chất Idempotent (An toàn)", fill="#16A34A", font=f_box_c)
    draw.text((875, Y1 + 175), "✖ Giới hạn độ dài (~2048 ký tự)", fill="#DC2626", font=f_box_c)
    draw.text((875, Y1 + 200), "✖ Không bảo mật (Lộ tham số)", fill="#DC2626", font=f_box_c)

    # --- ROW 2: METHOD POST ---
    Y2 = 390
    draw.rectangle([40, Y2, W - 40, Y2 + 250], fill="#FFF1F2", outline="#E11D48", width=2)
    # Header bar
    draw.rectangle([40, Y2, W - 40, Y2 + 40], fill="#E11D48")
    draw.text((55, Y2 + 10), "2. PHƯƠNG THỨC HTTP POST (Dùng cho gửi dữ liệu nhạy cảm / Đăng nhập / Thanh toán)", fill="#FFFFFF", font=f_box_h)
    draw.text((W - 270, Y2 + 12), "action + Body Payload", fill="#FFE4E6", font=f_mono)

    # Client Box
    draw.rectangle([70, Y2 + 60, 320, Y2 + 225], fill="#FFFFFF", outline="#FECDD3", width=1)
    draw.text((85, Y2 + 75), "💻 Trình Duyệt (Client)", fill="#BE123C", font=get_font(12, bold=True))
    draw.text((85, Y2 + 100), "• Form: <form method='POST'>", fill="#334155", font=f_box_c)
    draw.text((85, Y2 + 125), "• URL trên thanh địa chỉ giữ nguyên", fill="#334155", font=f_box_c)
    draw.text((85, Y2 + 150), "• Dữ liệu ẩn trong Request Body", fill="#16A34A", font=get_font(11, bold=True))
    draw.text((85, Y2 + 175), "• Payload: q=CodeGym", fill="#BE123C", font=f_mono)

    # Arrow 2
    draw.line([330, Y2 + 140, 580, Y2 + 140], fill="#E11D48", width=3)
    draw.polygon([(580, Y2 + 140), (570, Y2 + 133), (570, Y2 + 147)], fill="#E11D48")
    draw.text((345, Y2 + 115), "POST /search HTTP/1.1 (Payload in Body)", fill="#BE123C", font=f_mono)

    # Server Box
    draw.rectangle([590, Y2 + 60, 840, Y2 + 225], fill="#FFFFFF", outline="#FECDD3", width=1)
    draw.text((605, Y2 + 75), "🖥️ Máy Chủ (Web Server)", fill="#BE123C", font=get_font(12, bold=True))
    draw.text((605, Y2 + 100), "• Đọc dữ liệu từ luồng Request Body", fill="#334155", font=f_box_c)
    draw.text((605, Y2 + 125), "• Xử lý thêm mới/cập nhật dữ liệu", fill="#334155", font=f_box_c)
    draw.text((605, Y2 + 150), "• Google Search từ chối POST:", fill="#DC2626", font=get_font(11, bold=True))
    draw.text((605, Y2 + 175), "  -> 405 Method Not Allowed / 302", fill="#DC2626", font=f_mono)

    # Characteristics Box
    draw.rectangle([860, Y2 + 60, W - 60, Y2 + 225], fill="#F8FAFC", outline="#CBD5E1", width=1)
    draw.text((875, Y2 + 75), "Đặc Điểm Kỹ Thuật:", fill="#0F172A", font=get_font(12, bold=True))
    draw.text((875, Y2 + 100), "✔ Bảo mật hơn (Không hiện URL)", fill="#16A34A", font=f_box_c)
    draw.text((875, Y2 + 125), "✔ Không giới hạn kích thước gửi", fill="#16A34A", font=f_box_c)
    draw.text((875, Y2 + 150), "✔ Hỗ trợ gửi file, ảnh, tài liệu", fill="#16A34A", font=f_box_c)
    draw.text((875, Y2 + 175), "✖ Không thể Bookmark kết quả", fill="#DC2626", font=f_box_c)
    draw.text((875, Y2 + 200), "✖ Cảnh báo khi bấm F5 reload trang", fill="#DC2626", font=f_box_c)

    # Bottom Footer note
    draw.rectangle([40, H - 45, W - 40, H - 15], fill="#F1F5F9")
    draw.text((55, H - 37), "💡 KẾT LUẬN THỰC HÀNH: Tìm kiếm thông tin bắt buộc phải dùng GET để người dùng có thể chia sẻ và lưu trữ liên kết kết quả.", fill="#334155", font=get_font(10, bold=True))

    img.save(filename, "PNG", quality=95)
    print(f"Created: {filename}")

def create_multi_engine_mapping_diagram(filename):
    W, H = 1200, 680
    img = Image.new("RGB", (W, H), color="#FFFFFF")
    draw = ImageDraw.Draw(img)

    f_title = get_font(18, bold=True)
    f_sub = get_font(12, bold=False)
    f_tbl_h = get_font(12, bold=True)
    f_tbl_c = get_mono_font(11, bold=False)
    f_bold = get_font(12, bold=True)

    # Title Banner
    draw.rectangle([0, 0, W, 80], fill="#0F172A")
    draw.text((35, 18), "BẢNG ÁNH XẠ THUỘC TÍNH ACTION VÀ THAM SỐ TRUY VẤN CỦA CÁC CÔNG CỤ TÌM KIẾM", fill="#FFFFFF", font=f_title)
    draw.text((35, 48), "Giải đáp câu hỏi mở rộng: 'Nếu muốn sử dụng trang tìm kiếm của Bing thì làm thế nào?'", fill="#94A3B8", font=f_sub)

    # 4 Search Engines Cards
    cards = [
        ("GOOGLE SEARCH", "#4285F4", "#EFF6FF", 
         "action=\"https://www.google.com.vn/search\"", "name=\"q\"", "https://www.google.com.vn/search?q=tu_khoa",
         "Công cụ tìm kiếm phổ biến nhất thế giới. Nhận từ khóa qua tham số 'q'."),
        ("MICROSOFT BING (ĐỀ BÀI)", "#008272", "#ECFDF5",
         "action=\"https://www.bing.com/search\"", "name=\"q\"", "https://www.bing.com/search?q=tu_khoa",
         "Dùng chung quy chuẩn tham số 'q'. Chỉ cần đổi duy nhất thuộc tính action!"),
        ("DUCKDUCKGO (BẢO MẬT)", "#DE5833", "#FFF7ED",
         "action=\"https://duckduckgo.com/\"", "name=\"q\"", "https://duckduckgo.com/?q=tu_khoa",
         "Công cụ bảo mật quyền riêng tư. Cũng sử dụng cùng tham số 'q'."),
        ("YAHOO SEARCH", "#720E9E", "#FAF5FF",
         "action=\"https://search.yahoo.com/search\"", "name=\"p\"", "https://search.yahoo.com/search?p=tu_khoa",
         "Lưu ý khác biệt: Yahoo sử dụng tham số 'p' (parameters) thay vì 'q'.")
    ]

    card_y = 110
    card_h = 320
    card_w = 260
    cx = 40

    for title, border_col, bg_col, action_val, name_val, url_eg, desc in cards:
        # Card body
        draw.rectangle([cx, card_y, cx + card_w, card_y + card_h], fill=bg_col, outline=border_col, width=2)
        # Header bar
        draw.rectangle([cx, card_y, cx + card_w, card_y + 40], fill=border_col)
        draw.text((cx + 15, card_y + 11), title, fill="#FFFFFF", font=get_font(11, bold=True))

        # Action box
        draw.text((cx + 15, card_y + 55), "Thuộc tính action:", fill="#475569", font=get_font(10, bold=True))
        draw.rectangle([cx + 10, card_y + 75, cx + card_w - 10, card_y + 115], fill="#FFFFFF", outline="#CBD5E1", width=1)
        draw.text((cx + 15, card_y + 82), action_val[:32], fill="#0F172A", font=get_mono_font(9.5, bold=False))
        if len(action_val) > 32:
            draw.text((cx + 15, card_y + 97), action_val[32:], fill="#0F172A", font=get_mono_font(9.5, bold=False))

        # Name param box
        draw.text((cx + 15, card_y + 128), "Thuộc tính name:", fill="#475569", font=get_font(10, bold=True))
        draw.rectangle([cx + 10, card_y + 148, cx + card_w - 10, card_y + 180], fill="#FFFFFF", outline="#CBD5E1", width=1)
        draw.text((cx + 15, card_y + 156), name_val, fill="#B45309" if "name=\"p\"" in name_val else "#15803D", font=get_mono_font(11, bold=True))

        # Target URL example
        draw.text((cx + 15, card_y + 195), "Cấu trúc URL sinh ra:", fill="#475569", font=get_font(10, bold=True))
        draw.text((cx + 15, card_y + 215), url_eg[:30], fill="#0369A1", font=get_mono_font(9, bold=False))
        if len(url_eg) > 30:
            draw.text((cx + 15, card_y + 230), url_eg[30:], fill="#0369A1", font=get_mono_font(9, bold=False))

        # Description
        draw.text((cx + 15, card_y + 260), desc[:36], fill="#334155", font=get_font(9.5, bold=False))
        draw.text((cx + 15, card_y + 280), desc[36:75], fill="#334155", font=get_font(9.5, bold=False))

        cx += 285

    # Bottom Detailed Answer Section for Bing
    draw.rectangle([40, 460, W - 40, 650], fill="#F0FDF4", outline="#16A34A", width=2)
    draw.rectangle([40, 460, W - 40, 500], fill="#16A34A")
    draw.text((55, 470), "💡 CÂU TRẢ LỜI CHÍNH THỨC: NẾU MUỐN SỬ DỤNG TRANG TÌM KIẾM CỦA BING THÌ LÀM THẾ NÀO?", fill="#FFFFFF", font=get_font(12, bold=True))

    ans_lines = [
        "1. Xác định URL xử lý tìm kiếm của Microsoft Bing: https://www.bing.com/search",
        "2. Kiểm tra tên trường tham số từ khóa: Bing cũng sử dụng tham số q (viết tắt của 'query'), hoàn toàn trùng khớp với Google Search.",
        "3. Cách thay đổi trong mã nguồn HTML:",
        "   Thay vì action=\"https://www.google.com.vn/search\", ta chỉ cần đổi thuộc tính action thành: action=\"https://www.bing.com/search\"",
        "   Mã hoàn chỉnh: <form action=\"https://www.bing.com/search\" method=\"GET\"><input type=\"text\" name=\"q\" placeholder=\"Nhập từ khóa\"/><input type=\"submit\" value=\"Tìm kiếm\"/></form>"
    ]
    ay = 515
    for l in ans_lines:
        draw.text((55, ay), l, fill="#166534" if "Mã hoàn chỉnh" in l else "#0F172A", font=get_font(11, bold=True if "3. Cách thay đổi" in l or "Mã hoàn chỉnh" in l else False))
        ay += 26

    img.save(filename, "PNG", quality=95)
    print(f"Created: {filename}")

if __name__ == "__main__":
    out_dir = r"C:\Users\dathao\.gemini\antigravity-ide\scratch\thuc-hanh-form-tim-kiem-google"
    create_ui_demo_diagram(os.path.join(out_dir, "google_search_form_ui_demo.png"))
    create_get_vs_post_diagram(os.path.join(out_dir, "http_get_vs_post_architecture.png"))
    create_multi_engine_mapping_diagram(os.path.join(out_dir, "multi_search_engine_action_mapping.png"))
