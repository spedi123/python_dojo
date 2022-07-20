from flask_app import app
from flask import render_template, request, redirect, session


from flask_app.models import model_recipe
from flask_app.models import model_user


@app.route('/')
def index():
    if 'uuid' in session:
        return redirect('/dashboard')
    return render_template('index.html')


@app.route('/dashboard')
def dashboard():
    if 'uuid' not in session:
        return redirect('/')

    # context = {
    #     'all_recipes': model_recipe.Recipe.get_all()
    # }
    all_recipes = model_recipe.Recipe.get_all()
    data = {'id': session['uuid']}
    user = model_user.User.get_one(data)
    return render_template('recipe_list.html', all_recipes=all_recipes, user=user)
