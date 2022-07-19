from flask import render_template, request, redirect, session
from flask_app import app, bcrypt
# This imports the model file
from flask_app.models import model_user


@app.route('/user/login')
def user_new():
    return render_template('user_new.html')


@app.route('/user/create', methods=['POST'])
def user_create():
    # validations
    if not model_user.User.validator(request.form):
        return redirect('/')

    # hasing

    # create my user

    # store user_id in session
    return redirect('/')


@app.route('/user/<int:id>')
def user_show():
    return render_template('user_show.html')


@app.route('/user/<int:id>/edit')
def user_edit():
    return render_template('user_edit.html')


@app.route('/user/<int:id>/update', methods=['POST'])
def user_update():
    return redirect('/')


@app.route('/user/<int:id>/delete')
def user_delete():
    return redirect('/')
