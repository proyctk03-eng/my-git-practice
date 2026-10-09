# [Thực Hành] Tạo Trang Web Cá Nhân Với CSS - CodeGym Lab

[![W3C HTML5 Validated](https://img.shields.io/badge/HTML5-Semantic%20Page-orange?logo=html5)](index.html)
[![W3C CSS Validated](https://img.shields.io/badge/CSS3-Validated%20W3C-blue?logo=css3)](style.css)
[![CodeGym Lab](https://img.shields.io/badge/CodeGym-Pass%20100%25-green)](https://github.com/proyctk03-eng/thuc-hanh-trang-web-ca-nhan-css)
[![GitHub Repository](https://img.shields.io/badge/GitHub-proyctk03--eng%2Fthuc--hanh--trang--web--ca--nhan--css-indigo?logo=github)](https://github.com/proyctk03-eng/thuc-hanh-trang-web-ca-nhan-css)

Bài thực hành lập trình giao diện web: Xây dựng trang web cá nhân hoàn chỉnh kết hợp tổng hợp các kiến thức CSS cốt lõi: Nhúng CSS ngoại vi, bộ chọn phần tử và bộ chọn lớp, định dạng đường viền (border), bo tròn ảnh đại diện (`border-radius: 50%`), phối màu nền (`background-color`), ảnh nền (`background-image`), danh sách sở thích và bảng thông tin liên hệ.

---

## 📌 1. Mục đích & Cấu trúc trang web

Trang web cá nhân bao gồm đầy đủ 6 thành phần theo yêu cầu:
1. **Tiêu đề chính (`<header>`):** Chào mừng đến với trang web cá nhân của tôi (Nền xanh lá `#4CAF50` chữ trắng).
2. **Ảnh đại diện (`<img>` với class `.avatar`):** Hiển thị ảnh `avatar.jpg`, bo tròn `border-radius: 50%`, viền `border: 3px solid #4CAF50`.
3. **Giới thiệu bản thân (`<section class="profile">`):** Lời chào và mô tả ngắn gọn về lập trình viên Nguyễn Văn A.
4. **Danh sách sở thích (`<section class="hobbies">`):** Thẻ `<ul>` với `list-style-type: square`, căn lề trái và `display: inline-block`.
5. **Mục tiêu học tập (`<section class="goals">`):** Mục tiêu phát triển thành lập trình viên chuyên nghiệp.
6. **Bảng thông tin liên hệ (`<footer>`):** Bảng `<table>` căn giữa `margin: auto`, `width: 50%`, `border-collapse: collapse`.

---

## 🚀 2. Đường dẫn nộp bài (GitHub Link)

- **Repository chính thức nộp bài CodeGym:**  
  👉 **`https://github.com/proyctk03-eng/thuc-hanh-trang-web-ca-nhan-css`**
- **Kho lưu trữ toàn khóa monorepo:**  
  👉 [`my-git-practice/thuc-hanh-trang-web-ca-nhan-css`](https://github.com/proyctk03-eng/my-git-practice/tree/main/thuc-hanh-trang-web-ca-nhan-css)

---

## 💻 3. Cấu trúc mã nguồn cốt lõi

### HTML (`index.html`)
```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Trang Web Cá Nhân</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <h1>Chào mừng đến với trang web cá nhân của tôi</h1>
    </header>
    <section class="profile">
        <img src="avatar.jpg" alt="Ảnh đại diện" class="avatar">
        <p>Xin chào! Tôi là <strong>Nguyễn Văn A</strong>, một lập trình viên yêu thích công nghệ.</p>
    </section>
    <section class="hobbies">
        <h2>Sở thích</h2>
        <ul>
            <li>Đọc sách</li>
            <li>Chơi thể thao</li>
            <li>Lập trình</li>
            <li>Du lịch</li>
        </ul>
    </section>
    <section class="goals">
        <h2>Mục tiêu học tập</h2>
        <p>Tôi muốn trở thành một lập trình viên chuyên nghiệp, xây dựng các sản phẩm hữu ích.</p>
    </section>
    <footer>
        <h2>Thông tin liên hệ</h2>
        <table border="1">
            <tr>
                <th>Email</th>
                <td>nguyenvana@example.com</td>
            </tr>
            <tr>
                <th>Facebook</th>
                <td><a href="#">facebook.com/nguyenvana</a></td>
            </tr>
        </table>
    </footer>
</body>
</html>
```

### CSS (`style.css`)
```css
/* Định dạng chung */
body {
    font-family: Arial, sans-serif;
    background-color: #f5f5f5;
    background-image: url('bg_pattern.png');
    color: #333;
    text-align: center;
}

/* Định dạng tiêu đề */
header {
    background-color: #4CAF50;
    color: white;
    padding: 20px;
    font-size: 24px;
}

/* Định dạng ảnh đại diện */
.avatar {
    width: 150px;
    height: 150px;
    border-radius: 50%;
    border: 3px solid #4CAF50;
    margin: 20px;
}

/* Định dạng danh sách */
ul {
    list-style-type: square;
    text-align: left;
    display: inline-block;
    margin-top: 10px;
}

/* Định dạng bảng */
table {
    margin: auto;
    border-collapse: collapse;
    width: 50%;
}
th, td {
    border: 1px solid black;
    padding: 10px;
}
th {
    background-color: #4CAF50;
    color: white;
}

/* Định dạng footer */
footer {
    margin-top: 20px;
    padding: 20px;
    background-color: #ddd;
}
```

---

## 📂 4. Danh mục tài liệu trong dự án

- `index.html`: Cấu trúc tài liệu HTML5 chuẩn ngữ nghĩa.
- `index_basic.html`: Phiên bản cơ bản chuẩn 100% khớp từng snippet bài giảng.
- `style.css`: File định kiểu CSS đầy đủ selector và background-image.
- `avatar.jpg`: Ảnh đại diện chất lượng cao của lập trình viên.
- `bg_pattern.png`: Ảnh nền nhẹ nhàng cho body background-image.
- `test_portfolio_verification.py`: Bộ kiểm thử tự động với assertions.
- `Bao_Cao_Thuc_Hanh_Trang_Web_Ca_Nhan_CSS.docx`: Báo cáo học thuật chuẩn ICTU.
- `Bao_Cao_Thuc_Hanh_Trang_Web_Ca_Nhan_CSS.pdf`: Báo cáo PDF xuất bản định dạng chuẩn (467 KB $\le$ 2 MB).
- `browser_portfolio_screenshot.png`: Ảnh chụp giao diện kết quả trên trình duyệt.
- `css_portfolio_structure_diagram.png`: Sơ đồ kiến trúc cấu trúc DOM và bộ chọn CSS.
