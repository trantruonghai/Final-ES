class BookManager:
    def __init__(self, db_connection):
        """
        Khởi tạo với kết nối DB. 
        Admin sẽ dùng đối tượng này để quản lý kho sách.
        """
        self.db = db_connection
        self.cursor = db_connection.cursor(dictionary=True)
    def add_book(self, title, author, category, quantity):
        """Use Case: Add Book"""
        query = "INSERT INTO Books (Title, Author, Category, Quantity) VALUES (%s, %s, %s, %s)"
        values = (title, author, category, quantity)
        try:
            self.cursor.execute(query, values)
            self.db.commit()
            print(f"Thêm thành công sách: {title}")
        except Exception as e:
            print(f"Lỗi thêm sách: {e}")
    def edit_book(self, book_id, update_fields):
        """
        Use Case: Edit Book
        update_fields: một dictionary chứa các trường cần sửa (ví dụ: {'Quantity': 20})
        """
        placeholders = ", ".join([f"{key} = %s" for key in update_fields.keys()])
        values = list(update_fields.values())
        values.append(book_id)        
        query = f"UPDATE Books SET {placeholders} WHERE Book_id = %s"
        try:
            self.cursor.execute(query, tuple(values))
            self.db.commit()
            print(f"Đã cập nhật thông tin cho sách ID: {book_id}")
        except Exception as e:
            print(f"Lỗi cập nhật: {e}")
    def remove_book(self, book_id):
        """
        Use Case: Delete Book
        Ràng buộc quan trọng: Không được xóa nếu sách đang có người mượn 
        (Dựa trên kiểm thử ràng buộc dữ liệu trong yêu cầu)
        """
        check_query = "SELECT COUNT(*) as count FROM Borrow WHERE Book_id = %s AND Status = 'Borrowing'"
        self.cursor.execute(check_query, (book_id,))
        result = self.cursor.fetchone()
        if result['count'] > 0:
            print("❌ LỖI KIỂM THỬ: Không thể xóa sách này vì đang có người mượn!")
            return False        
        delete_query = "DELETE FROM Books WHERE Book_id = %s"
        try:
            self.cursor.execute(delete_query, (book_id,))
            self.db.commit()
            print(f"✅ Đã xóa sách ID {book_id} khỏi hệ thống.")
            return True
        except Exception as e:
            print(f"Lỗi khi xóa: {e}")
            return False
