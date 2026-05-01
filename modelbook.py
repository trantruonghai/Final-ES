from database import get_db

class Book:

    @staticmethod
    def view_all_book():
        conn = get_db()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()
        conn.close()
        return books

    @staticmethod
    def search_book(keyword):
        conn = get_db()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM books WHERE title LIKE %s"
        cursor.execute(query, ('%' + keyword + '%',))
        books = cursor.fetchall()
        conn.close()
        return books

    @staticmethod
    def search_book_by_id(book_id):
        conn = get_db()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM books WHERE id = %s"
        cursor.execute(query, (book_id,))
        book = cursor.fetchone()
        conn.close()
        return book