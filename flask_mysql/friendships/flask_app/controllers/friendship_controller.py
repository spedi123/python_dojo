from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.model_users import Users


@app.route("/")
def home():
    friendships = Users.get_user_friendships()
    users = Users.get_all()
    return render_template("index.html", friendships=friendships, users=users)


# @app.route("/authors/save", methods=['POST'])
# def save_author():
#     data = {
#         'name': request.form['name']
#     }
#     Friends.save(data)
#     return redirect("/authors")


# @app.route("/authors/<int:id>")
# def author_detail(id):
#     data = {'id': id}
#     author = Friends.get_author_books(data)
#     books = Books.get_all()
#     print(author)
#     print(books)
#     return render_template('author_detail.html', author=author, books=books)


# @app.route("/authors/favorite/<int:author_id>", methods=['POST'])
# def add_favorite_books(author_id):
#     data = {
#         'author_id': author_id,
#         'book_id': request.form['book']
#     }
#     Friends.save_favorites(data)
#     return redirect(f"/authors/{author_id}")
