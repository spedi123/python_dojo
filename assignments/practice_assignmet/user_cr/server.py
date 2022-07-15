from operator import methodcaller
from flask import Flask, render_template, redirect, request, session
from model.model_user import Users
app = Flask(__name__)
app.secret_key = "peteran is here"


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


if __name__ == "__main__":
    app.run(debug=True)
