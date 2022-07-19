from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.model_dojo import Dojo


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def survey_info():
    is_valid = Dojo.validate(request.form)
    if not is_valid:
        return redirect('/')
    for key in request.form:
        session[key] = request.form[key]
    return redirect('/result')


@app.route('/result')
def result():
    return render_template('result.html')

# end of moving area


# this must be on the bottom of this file
if __name__ == "__main__":
    app.run(debug=True)
