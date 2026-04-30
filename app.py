from flask import Flask, render_template, request
from modelbook import Book

app = Flask(__name__)

#Trang chủ
@app.route('/')
def home():
    books = Book.get_all_books()
    return render_template('home.html', books=books)

#Tìm kiếm
@app.route('/search')
def search():
    keyword = request.args.get('keyword')
    books = Book.search_books(keyword)
    return render_template('home.html', books=books)

#Thông tin sách 
@app.route('/book/<int:book_id>')
def book_detail(book_id):
    book = Book.get_book_by_id(book_id)
    return render_template('book_detail.html', book=book)

if __name__ == '__main__':
    app.run(debug=True)
