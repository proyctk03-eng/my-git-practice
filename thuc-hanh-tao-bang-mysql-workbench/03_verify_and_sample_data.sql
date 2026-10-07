-- =============================================================================
-- KIỂM THỬ VÀ DỮ LIỆU MẪU (TESTING & VERIFICATION)
-- =============================================================================

USE demo;

-- 1. Thêm dữ liệu mẫu vào bảng Student
INSERT INTO Student (id, name, age, country) VALUES
(1, 'Nguyen Van An', 20, 'Vietnam'),
(2, 'Tran Thi Bich', 21, 'Vietnam'),
(3, 'John Smith', 22, 'United States'),
(4, 'Tanaka Kenji', 19, 'Japan'),
(5, 'Le Hoang Nam', 23, 'Vietnam');

-- 2. Truy vấn toàn bộ dữ liệu bảng Student
SELECT * FROM Student;

-- 3. Truy vấn có điều kiện lọc và sắp xếp
SELECT id, name, age, country 
FROM Student 
WHERE age >= 20 
ORDER BY name ASC;

-- 4. Thống kê số lượng sinh viên theo quốc gia
SELECT country, COUNT(*) AS total_students, AVG(age) AS avg_age
FROM Student
GROUP BY country;
