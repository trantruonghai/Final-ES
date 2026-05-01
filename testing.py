class TestAdminConstraints(unittest.TestCase):
    def setUp(self):
        self.db = MockDB() 
        self.book_mgr = BookManager(self.db)
        self.mem_mgr = MemberManager(self.db)
        self.borrow_mgr = BorrowingManager(self.db)
    def test_delete_book_constraint(self):
        print("\nTest: Kiểm tra ràng buộc xóa sách...")
        book_id = 5
        result = self.book_mgr.remove_book(book_id)        
        self.assertFalse(result, "Lỗi: Hệ thống vẫn cho phép xóa sách đang được mượn!")
        print("=> Đạt: Hệ thống đã chặn xóa sách thành công.")
    def test_delete_member_constraint(self):
        print("\nTest: Kiểm tra ràng buộc xóa thành viên...")
        member_id = "M001"
        result = self.mem_mgr.delete_member(member_id)        
        self.assertFalse(result, "Lỗi: Hệ thống vẫn cho phép xóa thành viên đang mượn sách!")
        print("=> Đạt: Hệ thống đã chặn xóa thành viên thành công.")
    def test_manual_penalty_input(self):
        print("\nTest: Kiểm tra tính năng Admin tự nhập tiền phạt...")
        borrow_id = 101
        actual_return_date = "2026-05-10"     
        try:
            self.borrow_mgr.manage_return_and_penalty(borrow_id, actual_return_date)
            print("=> Đạt: Hệ thống chấp nhận số tiền phạt do Admin nhập thủ công.")
        except Exception as e:
            self.fail(f"Lỗi khi thực hiện nhập phạt thủ công: {e}")
class MockDB:
    def cursor(self, dictionary=True): return self
    def execute(self, query, params=None): return True
    def fetchone(self): 
        return {'count': 1, 'Book_id': 5, 'Due_date': datetime(2026, 5, 1).date()}
    def commit(self): pass
if __name__ == '__main__':
    unittest.main()
