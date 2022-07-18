from flask_app import app
from flask_app.model.model_ninjas import Ninjas
from flask_app.model.model_dojos import Dojos
from flask import render_template, request, redirect


@app.route("/ninjas")
def add_new_ninja():
    dojos = Dojos.get_all()
    return render_template("add_ninja.html", dojos=dojos)


@app.route("/ninjas/add_ninja", methods=['POST'])
def add_ninja():
    dojo_id = Ninjas.save(request.form)
    return redirect(f"/dojos/{dojo_id}")
