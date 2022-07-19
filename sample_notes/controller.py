from flask import render_template, request, redirect, session
from flask_app import app, bcrypt
# This imports the model file
# from flask_app.models import model_uthors


@app.route('/table_name/new')
def table_name_new():
    return render_template('table_name_new.html')


@app.route('/table_name/create', methods=['POST'])
def table_name_create():
    return redirect('/')


@app.route('/table_name/<int:id>')
def table_name_show(id):
    return render_template('table_name_show.html')


@app.route('/table_name/<int:id>/edit')
def table_name_edit(id):
    return render_template('table_name_edit.html')


@app.route('/table_name/<int:id>/update', methods=['POST'])
def table_name_update(id):
    return redirect('/')


@app.route('/table_name/<int:id>/delete')
def table_name_delete(id):
    return redirect('/')
