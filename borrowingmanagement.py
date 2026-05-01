class BorrowingManager:
    def __init__(self, db_connection):
        self.db = db_connection
        self.cursor = db_connection.cursor(dictionary=True)
    def manage_return_and_penalty(self, borrow_id, actual_return_date_str):
        """
        Use Case: Manage Borrowing Activities
        Admin chỉ định mức phạt trực tiếp dựa trên tình hình thực tế.
        """
        query = "SELECT * FROM Borrow WHERE Borrow_id = %s"
        self.cursor.execute(query, (borrow_id,))
        record = self.cursor.fetchone()
        if not record:
            print("❌ Không tìm thấy mã phiếu mượn!")
            return
        fmt = "%Y-%m-%d"
        due_date = record['Due_date']
        return_date = datetime.strptime(actual_return_date_str, fmt).date()       
        print(f"\n--- XỬ LÝ TRẢ SÁCH ---")
        print(f"Sách: {record['Book_id']} | Hạn trả: {due_date} | Ngày trả thực: {return_date}")        
        if return_date > due_date:
            overdue_days = (return_date - due_date).days
            print(f"⚠️ CẢNH BÁO: Quá hạn {overdue_days} ngày!")
        else:
            print(f"✅ Trả đúng hạn.")
        try:
            final_penalty = float(input("Admin nhập số tiền phạt (Nhập 0 nếu không phạt): "))
        except ValueError:
            print("Giá trị nhập không hợp lệ, mặc định là 0 VNĐ.")
            final_penalty = 0
        update_borrow_query = """
            UPDATE Borrow 
            SET Return_date = %s, Penalty = %s, Status = 'Returned' 
            WHERE Borrow_id = %s
        """
        self.cursor.execute(update_borrow_query, (return_date, final_penalty, borrow_id))        
        update_book_query = "UPDATE Books SET Quantity = Quantity + 1 WHERE Book_id = %s"
        self.cursor.execute(update_book_query, (record['Book_id'],))
        
        self.db.commit()
        print(f"✅ Hoàn tất! Tiền phạt đã lưu: {final_penalty:,} VNĐ")
