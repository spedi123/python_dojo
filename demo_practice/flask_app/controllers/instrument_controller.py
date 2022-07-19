from flask import render_template, request, redirect, session
from flask_app import app, bcrypt
# This imports the model file
# from flask_app.model.model_authors import Authors


@app.route('/instrument/new')
def instrument_new():
    return render_template('instrument_new.html')


@app.route('/instrument/create', methods=['POST'])
def instrument_create():
    return redirect('/')


@app.route('/instrument/<int:id>')
def instrument_show():
    return render_template('instrument_show.html')


@app.route('/instrument/<int:id>/edit')
def instrument_edit():
    return render_template('instrument_edit.html')


@app.route('/instrument/<int:id>/update', methods=['POST'])
def instrument_update():
    return redirect('/')


@app.route('/instrument/<int:id>/delete')
def instrument_delete():
    return redirect('/')
