-- =============================================================================
-- [BÀI TẬP] DỮ LIỆU MẪU & TRUY VẤN KIỂM THỬ (TESTING & VERIFICATION)
-- =============================================================================

USE `student-management`;

-- 1. Thêm dữ liệu vào bảng Class
INSERT INTO Class (id, name) VALUES
(1, 'C0123G1 - Java Fullstack'),
(2, 'C0223G1 - React & Node.js'),
(3, 'C0323G1 - Python Data Science'),
(4, 'C0423G1 - Cloud & DevOps');

-- 2. Thêm dữ liệu vào bảng Teacher
INSERT INTO Teacher (id, name, age, country) VALUES
(101, 'Nguyen Van Tuan', 38, 'Vietnam'),
(102, 'Tran Thi Mai', 34, 'Vietnam'),
(103, 'David Wilson', 42, 'United Kingdom'),
(104, 'Yamamoto Ken', 36, 'Japan');

-- 3. Thêm dữ liệu vào bảng Student
INSERT INTO Student (id, name, age, country) VALUES
(1001, 'Le Van Hoang', 20, 'Vietnam'),
(1002, 'Pham Thi Ha', 21, 'Vietnam'),
(1003, 'Alex Johnson', 22, 'Australia'),
(1004, 'Dang Quang Huy', 19, 'Vietnam');

-- 4. Truy vấn hiển thị toàn bộ dữ liệu bảng Class
SELECT * FROM Class;

-- 5. Truy vấn hiển thị toàn bộ dữ liệu bảng Teacher
SELECT * FROM Teacher;

-- 6. Truy vấn hiển thị toàn bộ dữ liệu bảng Student
SELECT * FROM Student;
