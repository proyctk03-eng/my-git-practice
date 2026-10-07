-- =============================================================================
-- BÀI TẬP THỰC HÀNH: XOÁ CSDL TRÊN MYSQL WORKBENCH
-- Phần 3: Quy Trình Chuẩn An Toàn Dữ Liệu (Backup -> Drop -> Verify)
-- Tác giả: Nguyễn Tuấn Đạt (proyctk03-eng)
-- =============================================================================

-- =============================================================================
-- GIAI ĐOẠN 1: KHỞI TẠO MÔI TRƯỜNG THỰC NGHIỆM
-- =============================================================================
CREATE DATABASE IF NOT EXISTS `temp_demo_db`
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE `temp_demo_db`;

CREATE TABLE IF NOT EXISTS `demo_items` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `item_name` VARCHAR(100) NOT NULL,
    `quantity` INT DEFAULT 1,
    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO `demo_items` (`item_name`, `quantity`) VALUES
('Sản phẩm kiểm thử A', 10),
('Sản phẩm kiểm thử B', 25);

-- Xác nhận dữ liệu tồn tại
SELECT * FROM `demo_items`;

-- =============================================================================
-- GIAI ĐOẠN 2: LƯU Ý AN TOÀN - CƠ CHẾ SAO LƯU (BACKUP)
-- Lưu ý từ đề bài: "Chúng ta phải rất cẩn thận với thao tác xoá CSDL
-- bởi vì tất cả các dữ liệu trong CSDL này sẽ bị mất nếu không được sao lưu trước đó."
-- =============================================================================
-- Trong MySQL Workbench:
-- Vào menu: Server -> Data Export -> Chọn CSDL `temp_demo_db`
-- Tích chọn "Dump Structure and Data" -> Nhấn "Start Export" để tạo file backup .sql.
-- Hoặc qua terminal dòng lệnh (mysqldump):
-- mysqldump -u root -p temp_demo_db > backup_temp_demo_db.sql

-- =============================================================================
-- GIAI ĐOẠN 3: THỰC THI XÓA CSDL AN TOÀN
-- =============================================================================
DROP DATABASE IF EXISTS `temp_demo_db`;

-- =============================================================================
-- GIAI ĐOẠN 4: KIỂM TRA XÁC NHẬN (VERIFICATION)
-- =============================================================================
SHOW DATABASES;
