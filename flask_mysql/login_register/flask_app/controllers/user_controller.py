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
    return redirect('/')


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
    # store user_id in session
    session['uuid'] = id
    return redirect('/loginpage')


@app.route('/loginpage')
def loginpage():
    return render_template('login_page.html')

# @app.route('/users/create', methods=['POST'])
# def table_name_create():
#     return redirect('/')


# @app.route('/users/<int:id>')
# def table_name_show(id):
#     return render_template('table_name_show.html')


# @app.route('/users/<int:id>/edit')
# def table_name_edit(id):
#     return render_template('table_name_edit.html')


# @app.route('/users/<int:id>/update', methods=['POST'])
# def table_name_update(id):
#     return redirect('/')


# @app.route('/users/<int:id>/delete')
# def table_name_delete(id):
#     return redirect('/')
