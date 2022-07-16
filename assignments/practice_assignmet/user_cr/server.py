from flask import Flask, render_template, redirect, request, session
from model.model_user import Users
app = Flask(__name__)
app.secret_key = "peteranishere"


@app.route("/users")
def index():
    users = Users.get_all()
    return render_template("index.html", users=users)


@app.route("/users/new")
def newuser():
    return render_template('add_user.html')


@app.route("/users/new", methods=['POST'])
def add_user():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    Users.save(data)
    return redirect('/users')


@app.route("/users/detail/<int:id>")
def user_detail(id):
    data = {"id": id}
    return render_template("user_detail.html", user=Users.get_one(data))


@app.route("/users/edit/<int:id>")
def user_edit(id):
    data = {"id": id}
    return render_template("edit_user.html", user=Users.get_one(data))


@app.route("/users/update", methods=['POST'])
def user_update():
    print(request.form)
    Users.update(request.form)
    return redirect('/users')


@app.route("/users/delete/<int:id>")
def user_delete(id):
    data = {"id": id}
    Users.delete(data)
    return redirect('/users')


if __name__ == "__main__":
    app.run(debug=True)
