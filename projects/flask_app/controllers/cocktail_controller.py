from flask import render_template, request, redirect, session, jsonify
from flask_app import app, bcrypt
# This imports the model file
from flask_app.models import model_cocktail, model_user


@app.route('/cocktail/mylist')
def cocktail_mylist():
    data = {'id': session['uuid']}
    user = model_user.User.get_one(data)
    user_cocktails = model_cocktail.Cocktail.get_user_all(data)
    return render_template('cocktail_mylist.html', user_cocktails=user_cocktails, user=user)


@app.route('/cocktail/new')
def cocktail_new():
    return render_template('cocktail_new.html')


@app.route('/cocktail/create', methods=['POST'])
def cocktail_create():
    # validations
    if not model_cocktail.Cocktail.validator(request.form):
        return redirect('/cocktail/new')

    data = {
        **request.form,
        'user_id': session['uuid']
    }
    model_cocktail.Cocktail.create(data)
    return redirect('/cocktail/mylist')


@app.route('/api/cocktail/create', methods=['POST'])
def api_cocktail_create():
    # validations
    # if not model_cocktail.Cocktail.validator(request.form):
    #     return redirect('/cocktail/new')

    data = {
        **request.form,
        'user_id': session['uuid']
    }
    model_cocktail.Cocktail.create(data)

    res = {
        'msg': 'success!!!!'
    }
    return redirect('/cocktail/mylist')


@app.route('/cocktail/mylist/<int:id>')
def cocktail_show(id):
    if 'uuid' not in session:
        return redirect('/')

    cocktail = model_cocktail.Cocktail.get_one({'id': id})
    data = {
        'id': session['uuid']
    }
    user = model_user.User.get_one(data)
    return render_template('cocktail_detail.html', cocktail=cocktail, user=user)


@app.route('/cocktail/mylist/<int:id>/edit')
def cocktail_edit(id):
    cocktail = model_cocktail.Cocktail.get_one({'id': id})
    return render_template('cocktail_edit.html', cocktail=cocktail)


@app.route('/cocktail/mylist/<int:id>/update', methods=['POST'])
def cocktail_update(id):
    if 'uuid' not in session:
        return redirect('/')

    if not model_cocktail.Cocktail.validator(request.form):
        return redirect(f'/cocktail/mylist/{id}/edit')

    data = {
        **request.form,
        'id': id
    }
    model_cocktail.Cocktail.update_one(data)
    return redirect('/cocktail/mylist')


@app.route('/cocktail/mylist/<int:id>/delete')
def cocktail_delete(id):
    model_cocktail.Cocktail.delete_one({'id': id})
    return redirect('/cocktail/mylist')
