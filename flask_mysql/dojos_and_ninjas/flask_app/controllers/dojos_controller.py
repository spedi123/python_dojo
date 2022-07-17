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
