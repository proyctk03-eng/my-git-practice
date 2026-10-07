-- =============================================================================
-- BÀI TẬP THỰC HÀNH: XOÁ CSDL TRÊN MYSQL WORKBENCH
-- Cách 2: Xoá CSDL Bằng Câu Lệnh SQL Trực Tiếp Trên Query Editor
-- Tác giả: Nguyễn Tuấn Đạt (proyctk03-eng)
-- =============================================================================

-- Bước 1: Trong cửa sổ MySQL Workbench, mở New Query Tab (phím tắt Ctrl + T).
-- Bước 2: Nhập câu lệnh xóa CSDL theo đúng yêu cầu đề bài:

DROP DATABASE `my_database`;

-- =============================================================================
-- MỞ RỘNG KỸ THUẬT: CÂU LỆNH XÓA AN TOÀN TRÁNH CRASH TRONG HỆ THỐNG
-- =============================================================================

-- 1. Nếu chạy `DROP DATABASE my_database;` khi CSDL không tồn tại, MySQL sẽ báo lỗi:
--    Error Code: 1008. Can't drop database 'my_database'; database doesn't exist
--    Để script chạy mượt mà không bị dừng đột ngột (đặc biệt trong migration CI/CD),
--    ta dùng từ khóa IF EXISTS:

DROP DATABASE IF EXISTS `my_database`;

-- 2. Kiểm tra lại danh sách các CSDL còn lại trên máy chủ MySQL:
SHOW DATABASES;

-- 3. Kiểm tra xem CSDL `my_database` còn tồn tại trong metadata hay không:
SELECT 
    SCHEMA_NAME AS `Tên CSDL`,
    DEFAULT_CHARACTER_SET_NAME AS `Bảng Mã`
FROM INFORMATION_SCHEMA.SCHEMATA
WHERE SCHEMA_NAME = 'my_database';
-- Kết quả trả về 0 row(s), xác nhận CSDL đã được xóa hoàn toàn và giải phóng vùng nhớ.
