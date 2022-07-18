from flask import render_template, request, redirect
from flask_app import app
from flask_app.model.model_authors import Authors
from flask_app.model.model_books import Books


@app.route("/authors")
def list_authors():
    authors = Authors.get_all()
    print(authors)
    return render_template("index.html", authors=authors)


@app.route("/authors/save", methods=['POST'])
def save_author():
    data = {
        'name': request.form['name']
    }
    Authors.save(data)
    return redirect("/authors")


@app.route("/authors/<int:id>")
def author_detail(id):
    data = {'id': id}
    author = Authors.get_author_books(data)
    books = Books.get_all()
    print(author)
    print(books)
    return render_template('author_detail.html', author=author, books=books)
