-- =============================================================================
-- BÀI THỰC HÀNH: TẠO BẢNG TRÊN MYSQL WORKBENCH
-- Mục tiêu: Tạo CSDL 'demo' và tạo bảng 'Student' với các trường: id, name, age, country
-- Người thực hiện: proyctk03-eng
-- =============================================================================

-- Bước 1: Tạo cơ sở dữ liệu mới có tên là 'demo'
CREATE DATABASE demo;

-- Bước 2: Chọn CSDL 'demo' làm cơ sở dữ liệu hiện hành để thao tác
USE demo;

-- Bước 3: Tạo bảng 'Student' với các trường (thuộc tính) theo yêu cầu bài học
-- - id: Kiểu dữ liệu INT (Số nguyên)
-- - name: Kiểu dữ liệu VARCHAR(200) (Chuỗi ký tự độ dài tối đa 200)
-- - age: Kiểu dữ liệu INT (Số nguyên)
-- - country: Kiểu dữ liệu VARCHAR(50) (Chuỗi ký tự độ dài tối đa 50)
CREATE TABLE Student (
    id INT,
    name VARCHAR(200),
    age INT,
    country VARCHAR(50)
);

-- =============================================================================
-- Bước 4: Kiểm tra trạng thái và cấu trúc bảng sau khi tạo
-- =============================================================================

-- Hiển thị danh sách các bảng trong database hiện hành
SHOW TABLES;

-- Xem chi tiết cấu trúc (metadata) của bảng Student vừa tạo
DESCRIBE Student;
