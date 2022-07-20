from flask import render_template, request, redirect, session
from flask_app import app, bcrypt
# This imports the model file
from flask_app.models import model_user


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/login', methods=['POST'])
def user_new():
    # validate
    model_user.User.validator_login(request.form)
    return redirect('/loginpage')


@app.route('/user/logout')
def logout_user():
    del session['uuid']
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
    return redirect('/loginpage')


@app.route('/loginpage')
def loginpage():
    user = model_user.User.get_one({'id': session['uuid']})
    return render_template('login_page.html', user=user)
