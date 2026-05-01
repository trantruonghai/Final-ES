class BookManager:
    def __init__(self, db_connection):
        self.db = db_connection
    def add_book(self, title, author, category, quantity):
        query = "INSERT INTO Books (Title, Author, Category, Quantity) VALUES (%s, %s, %s, %s)"
        self.db.execute(query, (title, author, category, quantity))
        print("Thêm sách mới thành công!")
    def edit_book(self, book_id, new_data):
        query = "UPDATE Books SET Title=%s, Quantity=%s WHERE Book_id=%s"
        self.db.execute(query, (new_data['title'], new_data['quantity'], book_id))
        print(f"Cập nhật thông tin sách {book_id} thành công!")
    def remove_book(self, book_id):
        check_query = "SELECT COUNT(*) FROM Borrow WHERE Book_id=%s AND Status='Borrowing'"
        count = self.db.fetch_one(check_query, (book_id,))        
        if count > 0:
            print("LỖI: Không thể xóa sách này vì đang có thành viên mượn!") [cite: 1141]
        else:
            delete_query = "DELETE FROM Books WHERE Book_id=%s"
            self.db.execute(delete_query, (book_id,))
            print("Đã xóa sách khỏi hệ thống.")
