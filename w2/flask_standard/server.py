from flask import Flask, render_template, redirect, request, session
# import the class from friend.py
from friend import Friend
app = Flask(__name__)
app.secret_key = "peteran is here"


@app.route("/")
def index():
    # call the get all classmethod to get all friends
    friends = Friend.get_all()
    return render_template("index.html", friends=friends)


@app.route("/friend/add", methods=['POST'])
def create_friend():
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "occ": request.form["occ"]
    }
    Friend.save(data)

    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
