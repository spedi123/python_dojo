from flask import render_template, request, redirect, session
from flask_app import app, bcrypt
# This imports the model file
from flask_app.models import model_instrument


@app.route('/instrument/new')
def instrument_new():
    return render_template('instrument_new.html')


@app.route('/instrument/create', methods=['POST'])
def instrument_create():
    # validations
    if not model_instrument.Instrument.validator(request.form):
        return redirect('/instrument/new')

    # create instument
    data = {
        **request.form,
        'user_id': session['uuid']
    }
    model_instrument.Instrument.create(data)
    return redirect('/')


@app.route('/instrument/<int:id>')
def instrument_show(id):
    return render_template('instrument_show.html')


@app.route('/instrument/<int:id>/edit')
def instrument_edit(id):
    return render_template('instrument_edit.html')


@app.route('/instrument/<int:id>/update', methods=['POST'])
def instrument_update(id):
    return redirect('/')


@app.route('/instrument/<int:id>/delete')
def instrument_delete(id):
    model_instrument.Instrument.delete_one({'id': id})
    return redirect('/')
