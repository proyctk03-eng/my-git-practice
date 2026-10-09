# [Thực Hành] Bảng Trong CSS - CodeGym Lab

[![W3C CSS Validated](https://img.shields.io/badge/CSS3-Tables%20Model-blue?logo=css3)](style.css)
[![CodeGym Lab](https://img.shields.io/badge/CodeGym-Pass%20100%25-green)](https://github.com/proyctk03-eng/thuc-hanh-bang-trong-css)
[![GitHub Repository](https://img.shields.io/badge/GitHub-proyctk03--eng%2Fthuc--hanh--bang--trong--css-indigo?logo=github)](https://github.com/proyctk03-eng/thuc-hanh-bang-trong-css)

Bài thực hành lập trình giao diện web: Luyện tập sử dụng các thuộc tính CSS để định kiểu cho bảng trong HTML (`<table>`, `<tr>`, `<th>`, `<td>`), làm chủ đường viền, gộp viền đơn (`border-collapse: collapse`), kích thước chiều rộng/chiều cao, căn chỉnh ngang (`text-align`), căn chỉnh dọc (`vertical-align`), đệm ô (`padding`) và phối màu sắc hiện đại.

---

## 📌 1. Mục tiêu bài thực hành

- Định kiểu đường viền cơ bản với `border: 1px solid black` cho `table, th, td`.
- Loại bỏ đường viền kép của bảng với `border-collapse: collapse`.
- Tùy chỉnh chiều rộng `width: 100%` và chiều cao tiêu đề `height: 50px`.
- Căn chỉnh văn bản theo chiều ngang `text-align: left`.
- Căn chỉnh văn bản theo chiều dọc `vertical-align: bottom` và `height: 80px`.
- Tạo khoảng cách đệm trong ô với `padding: 15px`.
- Thiết lập màu sắc: Tiêu đề nền tối `#333` chữ trắng, dòng dữ liệu nền sáng `#f2f2f2` chữ xám đậm.
- Bài tập tổng hợp: Xây dựng bảng quản lý học viên chuẩn UI/UX hiện đại (Zebra striping, hover effect, badges).

---

## 🚀 2. Đường dẫn nộp bài (GitHub Link)

- **Repository chính thức nộp bài CodeGym:**  
  👉 **`https://github.com/proyctk03-eng/thuc-hanh-bang-trong-css`**
- **Kho lưu trữ toàn khóa monorepo:**  
  👉 [`my-git-practice/thuc-hanh-bang-trong-css`](https://github.com/proyctk03-eng/my-git-practice/tree/main/thuc-hanh-bang-trong-css)

---

## 💻 3. Cấu trúc mã nguồn cốt lõi

### HTML (`index.html`)
```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>[Thực hành] Bảng trong CSS</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <table>
        <thead>
            <tr>
                <th>Họ tên</th>
                <th>Tuổi</th>
                <th>Lớp</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Nguyễn Văn A</td>
                <td>20</td>
                <td>Web</td>
            </tr>
            <tr>
                <td>Trần Thị B</td>
                <td>21</td>
                <td>Web</td>
            </tr>
        </tbody>
    </table>
</body>
</html>
```

### CSS (`style.css`)
```css
/* 1. Đường viền và gộp viền đơn */
table {
    width: 100%;
    border-collapse: collapse;
}

table, th, td {
    border: 1px solid black;
}

/* 2. Chiều cao & căn chỉnh ngang cho tiêu đề */
th {
    height: 50px;
    text-align: left;
    background-color: #333;
    color: white;
    padding: 15px;
}

/* 3. Chiều cao & căn chỉnh dọc cho dữ liệu */
td {
    height: 80px;
    vertical-align: bottom;
    background-color: #f2f2f2;
    color: #333;
    padding: 15px;
}
```

---

## 📂 4. Danh mục tài liệu trong dự án

- `index.html`: Giao diện trực quan đầy đủ 8 phần thực hành.
- `index_basic.html`: Phiên bản cơ bản chuẩn 100% theo từng snippet bài giảng.
- `style.css`: File định kiểu CSS độc lập chuẩn W3C.
- `test_table_css_verification.py`: Bộ kiểm thử tự động với assertions.
- `Bao_Cao_Thuc_Hanh_Bang_Trong_CSS.docx`: Báo cáo học thuật chuẩn ICTU.
- `Bao_Cao_Thuc_Hanh_Bang_Trong_CSS.pdf`: Báo cáo PDF xuất bản định dạng chuẩn (520 KB $\le$ 2 MB).
- `browser_table_css_screenshot.png`: Ảnh chụp giao diện kết quả trên trình duyệt.
- `css_table_properties_diagram.png`: Sơ đồ kiến trúc mô hình bảng CSS.
