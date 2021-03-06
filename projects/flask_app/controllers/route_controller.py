from flask_app import app
from flask import render_template, request, redirect, session


# from flask_app.models import model_instrument


@app.route('/')
def index():
    if 'uuid' in session:
        return redirect('/dashboard')
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    if 'uuid' not in session:
        return redirect('/')

    return render_template('cocktail_list.html')
