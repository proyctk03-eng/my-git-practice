# [Thực Hành] Danh Sách Trong CSS - CodeGym Lab

[![W3C CSS Validated](https://img.shields.io/badge/CSS3-Validated%20W3C-blue?logo=css3)](style.css)
[![CodeGym Lab](https://img.shields.io/badge/CodeGym-Pass%20100%25-green)](https://github.com/proyctk03-eng/thuc-hanh-danh-sach-css)
[![GitHub Repository](https://img.shields.io/badge/GitHub-proyctk03--eng%2Fthuc--hanh--danh--sach--css-indigo?logo=github)](https://github.com/proyctk03-eng/thuc-hanh-danh-sach-css)

Bài thực hành lập trình giao diện web: Luyện tập sử dụng các thuộc tính CSS để định kiểu cho danh sách HTML (`<ul>`, `<ol>`, `<li>`), làm chủ các thuộc tính marker, vị trí, ảnh nền và xây dựng lộ trình học web hiện đại.

---

## 📌 1. Mục tiêu bài thực hành

- Sử dụng `list-style-type` để thay đổi kiểu đánh dấu danh sách (hình vuông `square`, số La Mã `upper-roman`).
- Sử dụng `list-style-image` để tạo dấu đánh dấu bằng hình ảnh biểu tượng tùy chỉnh (`bullet.png`).
- Sử dụng `list-style-position` để phân biệt vị trí marker (`outside` vs `inside`).
- Sử dụng thuộc tính rút gọn `list-style`.
- Tùy biến màu sắc và khoảng cách của danh sách bằng `background-color`, `color`, `padding`, `margin`.
- Bài tập tổng hợp: Thiết kế danh sách "Lộ trình học lập trình Web" 5 chặng chuẩn UI/UX.

---

## 🚀 2. Đường dẫn nộp bài (GitHub Link)

- **Repository chính thức nộp bài CodeGym:**  
  👉 **`https://github.com/proyctk03-eng/thuc-hanh-danh-sach-css`**
- **Kho lưu trữ toàn khóa monorepo:**  
  👉 [`my-git-practice/thuc-hanh-danh-sach-css`](https://github.com/proyctk03-eng/my-git-practice/tree/main/thuc-hanh-danh-sach-css)

---

## 💻 3. Cấu trúc mã nguồn cốt lõi

### HTML (`index.html`)
```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>[Thực hành] Danh sách trong CSS</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <!-- 2. list-style-type: square -->
    <ul class="list-subjects">
        <li>HTML</li>
        <li>CSS</li>
        <li>JavaScript</li>
        <li>Git</li>
    </ul>

    <!-- 3. list-style-type: upper-roman -->
    <ol class="list-steps">
        <li>Học HTML</li>
        <li>Học CSS</li>
        <li>Học JavaScript</li>
        <li>Học Git</li>
    </ol>

    <!-- 4. list-style-image -->
    <ul class="list-tools">
        <li>Visual Studio Code</li>
        <li>Google Chrome</li>
        <li>GitHub</li>
        <li>Git</li>
    </ul>

    <!-- 5. list-style-position: outside & inside -->
    <ul class="list-outside">...</ul>
    <ul class="list-inside">...</ul>

    <!-- 6. list-style shorthand -->
    <ul class="list-shorthand">...</ul>

    <!-- 7. Colors & Spacing -->
    <ul class="list-languages">
        <li>HTML</li>
        <li>CSS</li>
        <li>JavaScript</li>
        <li>Python</li>
    </ul>

    <!-- 8. Lộ trình học Web tổng hợp -->
    <ul class="list-roadmap">...</ul>
</body>
</html>
```

### CSS (`style.css`)
```css
/* Mục 2: list-style-type: square */
.list-subjects {
    list-style-type: square;
    padding-left: 28px;
}

/* Mục 3: list-style-type: upper-roman */
.list-steps {
    list-style-type: upper-roman;
    padding-left: 32px;
}

/* Mục 4: list-style-image */
.list-tools {
    list-style-image: url('bullet.png');
    padding-left: 32px;
}

/* Mục 5: list-style-position */
.list-outside {
    list-style-position: outside;
}

.list-inside {
    list-style-position: inside;
}

/* Mục 6: list-style shorthand */
.list-shorthand {
    list-style: square inside url('bullet.png');
}

/* Mục 7: Colors & Spacing */
.list-languages {
    background-color: #0f172a;
    padding: 20px 28px;
    border-radius: 12px;
}

.list-languages li {
    color: #38bdf8;
    margin-bottom: 10px;
    padding: 8px 14px;
    background-color: #1e293b;
    border-radius: 6px;
}
```

---

## 📂 4. Danh mục tài liệu trong dự án

- `index.html`: Cấu trúc tài liệu HTML5 chuẩn ngữ nghĩa.
- `style.css`: File định kiểu CSS3 tách bạch hoàn toàn.
- `bullet.png`: Icon đánh dấu chất lượng cao cho `list-style-image`.
- `test_css_list_verification.py`: Bộ kiểm thử tự động với assertions.
- `Bao_Cao_Thuc_Hanh_Danh_Sach_Trong_CSS.docx`: Báo cáo học thuật chuẩn ICTU.
- `Bao_Cao_Thuc_Hanh_Danh_Sach_Trong_CSS.pdf`: Báo cáo PDF (487 KB $\le$ 2 MB).
- `browser_css_list_screenshot.png`: Ảnh chụp giao diện kết quả bài thực hành.
- `css_list_properties_diagram.png`: Sơ đồ kiến trúc CSS List properties.
