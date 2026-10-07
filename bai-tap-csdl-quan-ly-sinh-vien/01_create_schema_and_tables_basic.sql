-- =============================================================================
-- [BÀI TẬP] XÂY DỰNG CƠ SỞ DỮ LIỆU QUẢN LÝ SINH VIÊN
-- Mục tiêu: Tạo CSDL 'student-management', tạo bảng Class và bảng Teacher trên MySQL Workbench
-- Tác giả: proyctk03-eng
-- =============================================================================

-- Bước 1: Khởi tạo Cơ sở dữ liệu 'student-management'
-- Lưu ý: Do tên CSDL có dấu gạch ngang '-', cần đặt trong dấu backticks ``
CREATE DATABASE IF NOT EXISTS `student-management`;

-- Bước 2: Chọn CSDL 'student-management' làm ngữ cảnh hiện hành
USE `student-management`;

-- =============================================================================
-- Bước 3: Tạo bảng Class (Lớp học)
-- Các trường: id, name
-- =============================================================================
CREATE TABLE IF NOT EXISTS Class (
    id INT,
    name VARCHAR(200)
);

-- =============================================================================
-- Bước 4: Tạo bảng Teacher (Giảng viên)
-- Các trường: id, name, age, country
-- =============================================================================
CREATE TABLE IF NOT EXISTS Teacher (
    id INT,
    name VARCHAR(200),
    age INT,
    country VARCHAR(50)
);

-- =============================================================================
-- Bổ sung: Bảng Student từ bài thực hành trước để hoàn thiện CSDL Quản lý sinh viên
-- =============================================================================
CREATE TABLE IF NOT EXISTS Student (
    id INT,
    name VARCHAR(200),
    age INT,
    country VARCHAR(50)
);

-- =============================================================================
-- Bước 5: Kiểm tra danh sách bảng và cấu trúc các bảng vừa tạo
-- =============================================================================
SHOW TABLES;

-- Thanh tra cấu trúc bảng Class
DESCRIBE Class;

-- Thanh tra cấu trúc bảng Teacher
DESCRIBE Teacher;
