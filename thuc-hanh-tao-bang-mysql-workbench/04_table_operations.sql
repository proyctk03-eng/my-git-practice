-- =============================================================================
-- CÁC THAO TÁC QUẢN TRỊ BẢNG (TABLE MANAGEMENT DDL OPERATIONS)
-- =============================================================================

USE demo;

-- 1. Thêm cột mới vào bảng
ALTER TABLE Student ADD COLUMN email VARCHAR(100);

-- 2. Sửa kiểu dữ liệu / độ dài của cột
ALTER TABLE Student MODIFY COLUMN country VARCHAR(100);

-- 3. Đổi tên cột
ALTER TABLE Student RENAME COLUMN country TO nationality;

-- 4. Xóa một cột khỏi bảng
ALTER TABLE Student DROP COLUMN email;

-- 5. Xem lại cấu trúc bảng sau các thao tác ALTER
DESCRIBE Student;

-- 6. Xóa trắng dữ liệu trong bảng nhưng giữ lại cấu trúc
-- TRUNCATE TABLE Student;

-- 7. Xóa bảng hoàn toàn khỏi CSDL
-- DROP TABLE IF EXISTS Student;
