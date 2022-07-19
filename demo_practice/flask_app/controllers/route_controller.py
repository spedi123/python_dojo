from flask import render_template, request, redirect, session
from flask_app import app, bcrypt


@app.route('/')
def index():
    if 'uuid' in session:
        return redirect('/dashboard')
    return render_template('index.html')


@app.route('/dashboard')
def index1():
    if 'uuid' not in session:
        return redirect('/')
    return render_template('dash_board.html')
