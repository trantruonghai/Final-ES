class MemberManager:
    def __init__(self, db_connection):
        """
        Khởi tạo với kết nối database để Admin thực hiện các truy vấn.
        """
        self.db = db_connection
        self.cursor = db_connection.cursor(dictionary=True)
    def view_all_members(self):
        """Use Case: View Member Account (Dành cho Admin)"""
        query = "SELECT Member_id, Full_name, Email, Role FROM Members"
        self.cursor.execute(query)
        members = self.cursor.fetchall()
        return members
    def update_member_info(self, member_id, new_data):
        """Use Case: Update Member (Admin sửa thông tin thành viên)"""
        query = "UPDATE Members SET Full_name=%s, Email=%s WHERE Member_id=%s"
        values = (new_data['name'], new_data['email'], member_id)
        try:
            self.cursor.execute(query, values)
            self.db.commit()
            print(f"Thành công: Đã cập nhật thành viên {member_id}")
        except Exception as e:
            print(f"Lỗi khi cập nhật: {e}")
    def delete_member(self, member_id):
        """
        Use Case: Delete Member
        Kiểm tra ràng buộc: Không xóa nếu đang mượn sách hoặc nợ phạt.
        """
        check_query = "SELECT COUNT(*) as count FROM Borrow WHERE Member_id=%s AND Status IN ('Borrowing', 'Overdue')"
        self.cursor.execute(check_query, (member_id,))
        result = self.cursor.fetchone()
        if result['count'] > 0:
            print(f"LỖI: Thành viên {member_id} không thể xóa vì vẫn còn sách chưa trả hoặc đang nợ phạt!")
            return False
        else:
            delete_query = "DELETE FROM Members WHERE Member_id=%s"
            self.cursor.execute(delete_query, (member_id,))
            self.db.commit()
            print(f"Xác nhận: Đã xóa tài khoản thành viên {member_id} khỏi hệ thống.")
            return True
