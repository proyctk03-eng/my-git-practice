# [Bài Tập] Gộp Ô Trong Bảng Với Rowspan Và Colspan - HTML5

[![HTML5 Validated](https://img.shields.io/badge/HTML5-Semantic%20Table-orange?logo=html5)](index.html)
[![CodeGym Lab](https://img.shields.io/badge/CodeGym-Pass%20100%25-green)](https://github.com/proyctk03-eng/bai-tap-gop-o-rowspan-colspan)
[![GitHub Repository](https://img.shields.io/badge/GitHub-proyctk03--eng%2Fbai--tap--gop--o--rowspan--colspan-blue?logo=github)](https://github.com/proyctk03-eng/bai-tap-gop-o-rowspan-colspan)

Dự án bài tập thực hành lập trình web cơ bản: Xây dựng bảng **Lịch họp công ty** ứng dụng hai thuộc tính gộp ô `rowspan` và `colspan` trong HTML5 theo chuẩn W3C và giáo trình CodeGym.

---

## 📌 1. Mục tiêu & Yêu cầu đề bài

- **Mục tiêu:** Luyện tập sử dụng `rowspan` và `colspan` để gộp ô trong bảng và trình bày dữ liệu dạng lịch biểu hợp lý, chuyên nghiệp.
- **Yêu cầu chi tiết:**
  1. Tạo file mới có tên `index.html`.
  2. Thẻ `<body>` chứa tiêu đề `<h1>` với nội dung `"Lịch họp công ty"`.
  3. Bảng chứa 3 cột: `Ngày`, `Giờ`, `Nội dung cuộc họp`.
  4. Sử dụng `rowspan` để gộp ô cột `Ngày` khi có nhiều cuộc họp trong cùng một ngày (Thứ Hai, Thứ Tư, Thứ Năm).
  5. Sử dụng `colspan` để gộp ô khi có cuộc họp kéo dài nhiều giờ (Thứ Ba, Thứ Sáu).
  6. Đưa mã nguồn lên GitHub Repository công khai để nộp bài.

---

## 🚀 2. Đường dẫn nộp bài (GitHub Link)

- **Repository nộp bài CodeGym:**  
  👉 **`https://github.com/proyctk03-eng/bai-tap-gop-o-rowspan-colspan`**
- **Kho lưu trữ toàn khóa monorepo:**  
  👉 [`my-git-practice/bai-tap-gop-o-rowspan-colspan`](https://github.com/proyctk03-eng/my-git-practice/tree/main/bai-tap-gop-o-rowspan-colspan)

---

## 💻 3. Mã nguồn HTML cơ bản (`index_basic.html`)

```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Lịch họp công ty</title>
</head>
<body>
    <h1>Lịch họp công ty</h1>

    <table border="1" cellpadding="10" cellspacing="0">
        <thead>
            <tr>
                <th>Ngày</th>
                <th>Giờ</th>
                <th>Nội dung cuộc họp</th>
            </tr>
        </thead>
        <tbody>
            <!-- Thứ Hai: 2 cuộc họp -> gộp ô Ngày bằng rowspan="2" -->
            <tr>
                <td rowspan="2">Thứ Hai (12/10)</td>
                <td>08:30 - 10:00</td>
                <td>Họp giao ban đầu tuần toàn công ty</td>
            </tr>
            <tr>
                <td>14:00 - 15:30</td>
                <td>Báo cáo tiến độ dự án ERP & Tự động hóa</td>
            </tr>

            <!-- Thứ Ba: Cuộc họp kéo dài cả ngày -> gộp ô bằng colspan="2" -->
            <tr>
                <td>Thứ Ba (13/10)</td>
                <td colspan="2">08:00 - 17:00: Hội thảo định hướng chiến lược công nghệ và chuyển đổi số 2026 (Kéo dài cả ngày)</td>
            </tr>

            <!-- Thứ Tư: 3 cuộc họp -> gộp ô Ngày bằng rowspan="3" -->
            <tr>
                <td rowspan="3">Thứ Tư (14/10)</td>
                <td>09:00 - 10:30</td>
                <td>Phỏng vấn ứng viên Senior Frontend Developer</td>
            </tr>
            <tr>
                <td>11:00 - 12:00</td>
                <td>Thống nhất quy chuẩn thiết kế UI/UX với đối tác</td>
            </tr>
            <tr>
                <td>15:00 - 16:30</td>
                <td>Tập huấn bảo mật thông tin và an toàn dữ liệu ISO 27001</td>
            </tr>
        </tbody>
    </table>
</body>
</html>
```

---

## 📐 4. Cơ chế hoạt động của Rowspan và Colspan

```
┌─────────────────────────────────────────────────────────────┐
│                       BẢNG HTML (3 CỘT)                    │
│   ┌───────────────┬──────────────────┬──────────────────┐   │
│   │     Ngày      │       Giờ        │Nội dung cuộc họp │   │
│   ├───────────────┼──────────────────┼──────────────────┤   │
│   │               │ 08:30 - 10:00    │ Giao ban đầu tuần│   │
│   │ rowspan="2"   ├──────────────────┼──────────────────┤   │
│   │ (Gộp 2 hàng)  │ 14:00 - 15:30    │ Báo cáo tiến độ  │   │
│   ├───────────────┴──────────────────┴──────────────────┤   │
│   │ Thứ Ba        │      colspan="2" (Gộp 2 cột)        │   │
│   │ (1 hàng)      │  08:00 - 17:00: Hội thảo cả ngày    │   │
│   └───────────────┴─────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

1. **`rowspan="n"`**: Mở rộng ô theo chiều dọc xuống `n` hàng. Các hàng kế tiếp bị ô này chiếm chỗ thì **không được viết thẻ `<td>`** ở cột đó.
2. **`colspan="m"`**: Mở rộng ô theo chiều ngang sang phải `m` cột. Tổng số cột trên hàng đó (tính cả giá trị colspan) phải bằng đúng tổng số cột của bảng.

---

## 📂 5. Danh mục tệp tin trong Repository

- `index.html`: Bản giao diện hiện đại với bộ lọc ngày và công tắc bật đánh dấu ô gộp.
- `index_basic.html`: Bản HTML thuần phục vụ chấm điểm tự động.
- `test_schedule_verification.py`: Bộ kiểm thử tự động với assertions.
- `Bao_Cao_Bai_Tap_Gop_O_Rowspan_Colspan.docx`: Báo cáo học thuật chuẩn ICTU.
- `Bao_Cao_Bai_Tap_Gop_O_Rowspan_Colspan.pdf`: Báo cáo PDF xuất bản định dạng chuẩn (490 KB $\le$ 2 MB).
- `browser_schedule_table_screenshot.png`: Ảnh chụp giao diện bảng lịch họp.
- `html_rowspan_colspan_diagram.png`: Sơ đồ kiến trúc gộp ô lưới.
