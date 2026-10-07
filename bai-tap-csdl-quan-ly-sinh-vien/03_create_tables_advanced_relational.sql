-- =============================================================================
-- [BÀI TẬP] MÔ HÌNH QUẢN LÝ SINH VIÊN CHUẨN DOANH NGHIỆP (RELATIONAL ARCHITECTURE)
-- Áp dụng tiêu chuẩn Database Architect:
-- 1. Khóa chính (PRIMARY KEY) & AUTO_INCREMENT.
-- 2. Khóa ngoại (FOREIGN KEY) đảm bảo toàn vẹn tham chiếu (Referential Integrity).
-- 3. Ràng buộc CHECK cho độ tuổi (age >= 18).
-- 4. Bảng mã utf8mb4 cho toàn bộ văn bản tiếng Việt.
-- =============================================================================

CREATE DATABASE IF NOT EXISTS `student-management`
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE `student-management`;

-- 1. Bảng Teacher (Giảng viên)
CREATE TABLE IF NOT EXISTS Teacher_Advanced (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(200) NOT NULL COMMENT 'Họ và tên giảng viên',
    age INT NOT NULL CHECK (age >= 21 AND age <= 70) COMMENT 'Tuổi giảng viên hợp lệ (21-70)',
    country VARCHAR(50) NOT NULL DEFAULT 'Vietnam' COMMENT 'Quốc gia / Quê quán',
    email VARCHAR(100) UNIQUE COMMENT 'Email liên hệ',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 2. Bảng Class (Lớp học) có liên kết với giảng viên chủ nhiệm
CREATE TABLE IF NOT EXISTS Class_Advanced (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(200) NOT NULL UNIQUE COMMENT 'Tên mã lớp học (ví dụ: C0123G1)',
    teacher_id INT COMMENT 'Mã giảng viên chủ nhiệm',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_class_teacher FOREIGN KEY (teacher_id) 
        REFERENCES Teacher_Advanced(id) 
        ON DELETE SET NULL 
        ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 3. Bảng Student (Sinh viên) có liên kết với lớp học
CREATE TABLE IF NOT EXISTS Student_Advanced (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(200) NOT NULL COMMENT 'Họ và tên sinh viên',
    age INT NOT NULL CHECK (age >= 16 AND age <= 100),
    country VARCHAR(50) NOT NULL DEFAULT 'Vietnam',
    class_id INT COMMENT 'Mã lớp sinh viên đang theo học',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_student_class FOREIGN KEY (class_id) 
        REFERENCES Class_Advanced(id) 
        ON DELETE RESTRICT 
        ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
