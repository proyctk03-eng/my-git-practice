-- =============================================================================
-- BÀI TẬP THỰC HÀNH: XOÁ CSDL TRÊN MYSQL WORKBENCH
-- Phần 4: Bảo Vệ An Toàn Cơ Sở Dữ Liệu Trong Môi Trường Doanh Nghiệp (Production)
-- Tác giả: Nguyễn Tuấn Đạt (proyctk03-eng)
-- =============================================================================

-- 1. Xem danh sách các quyền hạn hiện có của user
SHOW GRANTS FOR CURRENT_USER();

-- 2. Nguyên tắc đặc quyền tối thiểu (Principle of Least Privilege):
-- Chỉ tài khoản DBA / Root cấp cao mới được cấp quyền DROP DATABASE.
-- Người dùng ứng dụng (App User) tuyệt đối không được cấp quyền DROP.
-- Ví dụ: Thu hồi quyền DROP trên toàn cục từ user ứng dụng:
-- REVOKE DROP ON *.* FROM 'app_user'@'localhost';
-- FLUSH PRIVILEGES;

-- 3. Tạo người dùng chỉ có quyền đọc & ghi dữ liệu thông thường (DML):
-- CREATE USER IF NOT EXISTS 'developer_user'@'%' IDENTIFIED BY 'StrongPassword123!';
-- GRANT SELECT, INSERT, UPDATE, DELETE ON `my_database`.* TO 'developer_user'@'%';
-- FLUSH PRIVILEGES;

-- 4. Bật chế độ Safe Updates trong MySQL Workbench:
-- Preferences -> SQL Editor -> Tích chọn "Safe Updates (rejects UPDATEs and DELETEs with no key)"
SET SQL_SAFE_UPDATES = 1;
