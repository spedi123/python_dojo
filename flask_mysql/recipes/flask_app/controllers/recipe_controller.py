from flask import render_template, request, redirect, session
from flask_app import app, bcrypt
# This imports the model file
from flask_app.models import model_recipe
from flask_app.models import model_user


@app.route('/recipe/new')
def recipe_new():
    if 'uuid' not in session:
        return redirect('/')
    return render_template('recipe_new.html')


@app.route('/recipe/create', methods=['POST'])
def recipe_create():
    if 'uuid' not in session:
        return redirect('/')

    if not model_recipe.Recipe.validator(request.form):
        return redirect('/recipe/new')

    data = {
        **request.form,
        'user_id': session['uuid']
    }
    model_recipe.Recipe.create(data)
    return redirect('/')


@app.route('/recipe/<int:id>')
def recipe_show(id):
    if 'uuid' not in session:
        return redirect('/')

    recipe = model_recipe.Recipe.get_one({'id': id})
    data = {
        'id': session['uuid']
    }
    user = model_user.User.get_one(data)
    return render_template('recipe_detail.html', recipe=recipe, user=user)


@app.route('/recipe/<int:id>/edit')
def recipe_edit(id):
    if 'uuid' not in session:
        return redirect('/')

    recipe = model_recipe.Recipe.get_one({'id': id})
    return render_template('recipe_edit.html', recipe=recipe)


@app.route('/recipe/<int:id>/update', methods=['POST'])
def recipe_update(id):
    if 'uuid' not in session:
        return redirect('/')

    if not model_recipe.Recipe.validator(request.form):
        return redirect('/recipe/{id}/update')

    data = {
        **request.form,
        'id': id
    }
    model_recipe.Recipe.update_one(data)
    return redirect('/')


@app.route('/recipe/<int:id>/delete')
def recipe_delete(id):
    if 'uuid' not in session:
        return redirect('/')

    model_recipe.Recipe.delete_one({'id': id})
    return redirect('/')
