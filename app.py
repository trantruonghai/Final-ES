from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    books = [
        {"id": 1, "title": "Python", "author": "Guido"},
        {"id": 2, "title": "Flask", "author": "Armin"},
    ]
    return render_template("index.html", books=books)

if __name__ == "__main__":
    app.run(debug=True)
