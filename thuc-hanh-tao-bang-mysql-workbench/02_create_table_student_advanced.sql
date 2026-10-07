-- =============================================================================
-- BÀI THỰC HÀNH: TẠO BẢNG TRÊN MYSQL WORKBENCH - CHUẨN DOANH NGHIỆP
-- Tiêu chuẩn Database Architect:
-- 1. IF NOT EXISTS chống xung đột lỗi runtime.
-- 2. Bộ mã utf8mb4 hỗ trợ đa ngôn ngữ và tiếng Việt có dấu.
-- 3. Khóa chính (PRIMARY KEY) kết hợp AUTO_INCREMENT.
-- 4. Ràng buộc toàn vẹn dữ liệu (NOT NULL, CHECK, DEFAULT).
-- 5. Metadata kiểm toán bản ghi (created_at, updated_at).
-- =============================================================================

-- 1. Tạo database an toàn với bảng mã chuẩn
CREATE DATABASE IF NOT EXISTS demo
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE demo;

-- 2. Tạo bảng Student chuẩn hóa cao cấp
CREATE TABLE IF NOT EXISTS Student_Advanced (
    id INT AUTO_INCREMENT PRIMARY KEY COMMENT 'Mã định danh duy nhất của sinh viên',
    name VARCHAR(200) NOT NULL COMMENT 'Họ và tên sinh viên',
    age INT NOT NULL CHECK (age >= 16 AND age <= 100) COMMENT 'Tuổi sinh viên hợp lệ (16-100)',
    country VARCHAR(50) NOT NULL DEFAULT 'Vietnam' COMMENT 'Quốc gia / Quê quán',
    email VARCHAR(100) UNIQUE COMMENT 'Địa chỉ email duy nhất',
    status ENUM('Active', 'Suspended', 'Graduated') DEFAULT 'Active' COMMENT 'Trạng thái học tập',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT 'Thời điểm tạo bản ghi',
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Thời điểm cập nhật bản ghi'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Hiển thị mô tả bảng
DESCRIBE Student_Advanced;
