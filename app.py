from flask import Flask, render_template, request, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

#SQLCONNECT
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "your_password",
    "database": "library_db"
}

def get_db():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except Error as e:
        print(f"Lỗi kết nối DB: {e}")
        return None


#VIEWBOOK
@app.route("/")
def index():
    conn = get_db()
    books = []
    categories = []
    if conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM books ORDER BY title")
        books = cursor.fetchall()
        cursor.execute("SELECT DISTINCT category FROM books ORDER BY category")
        categories = [row["category"] for row in cursor.fetchall()]
        cursor.close()
        conn.close()
    return render_template("index.html", books=books, categories=categories)


#BOOK DETAIL
@app.route("/book/<int:book_id>")
def book_detail(book_id):
    conn = get_db()
    book = None
    if conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM books WHERE id = %s", (book_id,))
        book = cursor.fetchone()
        cursor.close()
        conn.close()
    if not book:
        return render_template("404.html"), 404
    return render_template("book_detail.html", book=book)


#API GET BOOK
@app.route("/api/search")
def search_books():
    keyword = request.args.get("q", "").strip()
    category = request.args.get("category", "").strip()
    available = request.args.get("available", "").strip()

    conn = get_db()
    if not conn:
        return jsonify({"error": "Không kết nối được database"}), 500

    query = "SELECT * FROM books WHERE 1=1"
    params = []

    if keyword:
        query += " AND (title LIKE %s OR author LIKE %s OR isbn LIKE %s)"
        kw = f"%{keyword}%"
        params += [kw, kw, kw]

    if category:
        query += " AND category = %s"
        params.append(category)

    if available == "1":
        query += " AND available_qty > 0"

    query += " ORDER BY title"

    cursor = conn.cursor(dictionary=True)
    cursor.execute(query, params)
    books = cursor.fetchall()
    cursor.close()
    conn.close()

    return jsonify({"results": books, "count": len(books)})


#API GET BOOK
@app.route("/api/books")
def get_books():
    conn = get_db()
    if not conn:
        return jsonify({"error": "Không kết nối được database"}), 500
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM books ORDER BY title")
    books = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify({"results": books, "count": len(books)})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
