from flask import render_template, request, redirect
from flask_app import app
from flask_app.model.model_authors import Authors
from flask_app.model.model_books import Books


@app.route("/books")
def list_books():
    books = Books.get_all()
    return render_template("new_books.html", books=books)


@app.route("/books/save", methods=['POST'])
def save_book():
    data = {
        'title': request.form['title'],
        'num_of_pages': request.form['num_of_pages']
    }
    Books.save(data)
    return redirect("/books")


@app.route("/books/<int:id>")
def book_detail(id):
    data = {'id': id}
    book = Books.get_book_authors(data)
    authors = Authors.get_all()
    return render_template('book_detail.html', book=book, authors=authors)


@app.route("/books/favorite/<int:book_id>", methods=['POST'])
def add_favorite_authors(book_id):
    data = {
        'author_id': request.form['author'],
        'book_id': book_id
    }
    Authors.save_favorites(data)
    return redirect(f"/books/{book_id}")
