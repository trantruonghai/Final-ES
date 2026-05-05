# DỰ ÁN QUẢN LÝ THƯ VIỆN - NHÓM 11 (LỚP SE)

## 1. Công việc của Nhóm trưởng (Trần Trường Hải)
- Thiết kế mô hình dữ liệu (ERD) và sơ đồ lớp (Class Diagram).
- Xây dựng nền tảng Database bằng SQLite.
- Lập trình Logic nghiệp vụ cốt lõi: Mượn sách, Trả sách, Tính tiền phạt.

## 2. Hướng dẫn chạy chương trình
- Bước 1: Cài đặt Python.
- Bước 2: Chạy file `database_init.py` để khởi tạo dữ liệu.
- Bước 3: Chạy `main.py` để bắt đầu quản lý.

## 3. Công việc của Linh (Frontend & Account Management)

- Thiết kế giao diện:
  - Trang Đăng nhập
  - Trang Đăng ký
  - Trang Hồ sơ cá nhân
- Xây dựng chức năng:
  - Register Account
  - Login
  - Update Profile
  - Reset Password
  - Delete Account
- Viết Test Case cho toàn bộ chức năng quản lý tài khoản.

## 4. Công việc của Tài (Book & Search Module)

- Thiết kế giao diện:
  - Trang chủ (Home Page)
  - Trang chi tiết sách (Book Detail)
- Xây dựng chức năng:
  - Hiển thị danh sách sách từ database (View Book)
  - Tìm kiếm sách theo từ khóa (Search Book)
  - Xem chi tiết thông tin sách
- Xử lý:
  - Trường hợp không có kết quả tìm kiếm
  - Đảm bảo hiển thị dữ liệu nhanh và chính xác
 
    ## 5. Công việc của Phong (Borrowing & Penalty Logic)
•	Lập trình: Xử lý logic nghiệp vụ phức tạp nhất tại lớp BorrowManagement. 
•	Chức năng: Viết code cho Use Case: Borrow Book (check tồn kho), Return Book (cập nhật số lượng), Calculate Penalty (tự động tính tiền phạt dựa trên số ngày quá hạn) . 
•	Kiểm thử: Chạy thử các kịch bản quá hạn để kiểm tra tính chính xác của tiền phạt. 

## 6. Công việc của Đức (History & Admin Dashboard)
•	Lập trình: Thiết kế giao diện Trang Lịch sử mượn trả và Trang Quản trị (Admin Page) . 
•	Chức năng: Triển khai Use Case: View Borrowing History, Manage Book (Add/Edit/Remove), Manage Member và Manage Borrowing Activities . 
•	Kiểm thử: Kiểm tra các ràng buộc dữ liệu (ví dụ: không được xóa sách khi đang có người mượn). 


