from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.model_users import Users


@app.route("/")
def home():
    friendships = Users.get_user_friendships()
    users = Users.get_all()
    return render_template("index.html", friendships=friendships, users=users)


@app.route("/add_user", methods=['POST'])
def add_user():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name']
    }
    Users.save(data)
    return redirect('/')


@app.route("/add_friendship", methods=['POST'])
def add_friendship():
    if request.form['user'] == request.form['friend']:
        return redirect('/')
    data = {
        'user_id': request.form['user'],
        'friend_id': request.form['friend']
    }
    Users.add_friendship(data)
    return redirect('/')
