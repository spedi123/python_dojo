from flask_app import app
from flask import Flask, render_template, redirect, request, session
from flask_app.model.model_dojos import Dojos


@app.route("/")
def index():
    users = Dojos.get_all()
    return render_template("index.html", users=users)


@app.route("/savedojo", methods=['POST'])
def save_dojo():
    data = {
        'name': request.form['name']
    }
    print(data)
    Dojos.save(data)
    return redirect('/')


@app.route("/dojos/<int:dojo_id>")
def dojo_detail(dojo_id):
    data = {'dojo_id': dojo_id}
    dojo_data = Dojos.get_dojo_ninjas(data)
    print(dojo_data)
    return render_template('dojo_detail.html', dojo_data=dojo_data)

# @app.route("/users/new")
# def newuser():
#     return render_template('add_user.html')


# @app.route("/users/new", methods=['POST'])
# def add_user():
#     data = {
#         "first_name": request.form["first_name"],
#         "last_name": request.form["last_name"],
#         "email": request.form["email"]
#     }
#     Users.save(data)
#     return redirect('/users')


# @app.route("/users/detail/<int:id>")
# def user_detail(id):
#     data = {"id": id}
#     return render_template("user_detail.html", user=Users.get_one(data))


# @app.route("/users/edit/<int:id>")
# def user_edit(id):
#     data = {"id": id}
#     return render_template("edit_user.html", user=Users.get_one(data))


# @app.route("/users/update", methods=['POST'])
# def user_update():
#     print(request.form)
#     Users.update(request.form)
#     return redirect('/users')


# @app.route("/users/delete/<int:id>")
# def user_delete(id):
#     data = {"id": id}
#     Users.delete(data)
#     return redirect('/users')
