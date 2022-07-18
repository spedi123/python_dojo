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
