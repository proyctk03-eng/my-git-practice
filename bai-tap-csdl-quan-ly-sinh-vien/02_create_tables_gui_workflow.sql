-- =============================================================================
-- [BÀI TẬP] QUY TRÌNH TẠO BẢNG BẰNG GIAO DIỆN (GUI) MYSQL WORKBENCH
-- Tài liệu phân tích DDL tự động sinh bởi MySQL Workbench Table Editor
-- =============================================================================

/*
CÁC BƯỚC THỰC HIỆN TRÊN GIAO DIỆN MYSQL WORKBENCH:

1. BẢNG CLASS:
   - Bước 1: Trong ngăn Navigator (Schemas), click chuột phải vào schema `student-management`.
   - Bước 2: Chọn 'Create Table...'.
   - Bước 3: Đặt 'Table Name' là: Class.
   - Bước 4: Trong bảng danh sách Columns bên dưới:
       + Dòng 1: Column Name = id, Datatype = INT
       + Dòng 2: Column Name = name, Datatype = VARCHAR(200)
   - Bước 5: Click nút 'Apply' ở góc dưới bên phải.
   - Bước 6: Cửa sổ 'Apply SQL Script to Database' xuất hiện, kiểm tra lệnh và nhấn 'Apply' -> 'Finish'.

2. BẢNG TEACHER:
   - Bước 1: Tương tự, click chuột phải vào schema `student-management` -> 'Create Table...'.
   - Bước 2: Đặt 'Table Name' là: Teacher.
   - Bước 3: Điền các trường:
       + Dòng 1: Column Name = id, Datatype = INT
       + Dòng 2: Column Name = name, Datatype = VARCHAR(200)
       + Dòng 3: Column Name = age, Datatype = INT
       + Dòng 4: Column Name = country, Datatype = VARCHAR(50)
   - Bước 4: Click nút 'Apply' -> 'Apply' -> 'Finish'.
*/

-- Đoạn mã DDL chính xác mà MySQL Workbench GUI tự sinh ra khi nhấn Apply cho bảng Class:
CREATE TABLE `student-management`.`Class` (
  `id` INT NULL,
  `name` VARCHAR(200) NULL
);

-- Đoạn mã DDL chính xác mà MySQL Workbench GUI tự sinh ra khi nhấn Apply cho bảng Teacher:
CREATE TABLE `student-management`.`Teacher` (
  `id` INT NULL,
  `name` VARCHAR(200) NULL,
  `age` INT NULL,
  `country` VARCHAR(50) NULL
);
