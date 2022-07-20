from flask import render_template, request, redirect, session
from flask_app import app, bcrypt
# This imports the model file
from flask_app.models import model_user


@app.route('/user/login', methods=['POST'])
def user_new():
    # validate
    model_user.User.validator_login(request.form)
    return redirect('/')


@app.route('/user/create', methods=['POST'])
def user_create():
    if not model_user.User.validator(request.form):
        return redirect('/')
    hash_pw = bcrypt.generate_password_hash(request.form['pw'])
    data = {
        **request.form,
        'pw': hash_pw
    }
    id = model_user.User.create(data)
    session['uuid'] = id
    return redirect('/dashboard')


@app.route('/logout')
def user_logout():
    session.clear()
    return redirect('/')
