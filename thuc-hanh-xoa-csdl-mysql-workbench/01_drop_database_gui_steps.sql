-- =============================================================================
-- BÀI TẬP THỰC HÀNH: XOÁ CSDL TRÊN MYSQL WORKBENCH
-- Cách 1: Thao Tác Xóa CSDL Bằng Giao Diện Đồ Họa (GUI - Drop Schema)
-- Tác giả: Nguyễn Tuấn Đạt (proyctk03-eng)
-- =============================================================================

-- HƯỚNG DẪN THAO TÁC TRÊN GIAO DIỆN MYSQL WORKBENCH:
-- Bước 1: Khởi động MySQL Workbench, đăng nhập vào kết nối MySQL Server (Local instance 3306).
-- Bước 2: Tại panel "Navigator: SCHEMAS" bên trái, tìm CSDL cần xóa (ví dụ: `my_database` hoặc `my_database1`).
-- Bước 3: Click chuột phải (Right-Click) vào tên CSDL đó, chọn "Drop Schema...".
-- Bước 4: Hộp thoại xác nhận xuất hiện với cảnh báo nguy hiểm:
--         "You have selected to drop the schema 'my_database'. All tables and data will be permanently deleted."
--         Hộp thoại cung cấp 3 nút tùy chọn:
--         - [Review SQL]: Xem trước câu lệnh SQL trước khi quyết định thực thi.
--         - [Cancel]: Hủy bỏ thao tác nếu bấm nhầm.
--         - [Drop Now]: Xóa ngay lập tức CSDL và toàn bộ bảng bên trong.
-- Bước 5: Nhấn chọn nút [Drop Now] theo yêu cầu đề bài.
-- Bước 6: Quan sát panel Action Output: Lệnh thực thi thành công và tên CSDL biến mất khỏi danh sách SCHEMAS.

-- Đoạn mã SQL do Workbench tự động sinh và gửi ngầm lên Server khi chọn Drop Now:
DROP SCHEMA `my_database`;
