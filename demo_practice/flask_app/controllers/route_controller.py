from flask import render_template, request, redirect, session
from flask_app import app, bcrypt


@app.route('/')
def index():
    return render_template('index.html')
