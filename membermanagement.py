def manage_members(admin_action, member_id=None):
    if admin_action == "VIEW_ALL":
        return db.query("SELECT Member_id, Full_name, Email, Role FROM Members")    
    elif admin_action == "DELETE":
        debt_check = db.query("SELECT * FROM Borrow WHERE Member_id=%s AND Status IN ('Borrowing', 'Overdue')", (member_id,))
        if debt_check:
            print("Cảnh báo: Thành viên vẫn còn sách chưa trả hoặc tiền phạt!") [cite: 1185]
        else:
            db.execute("DELETE FROM Members WHERE Member_id=%s", (member_id,))
            print("Đã xóa tài khoản thành viên.")
