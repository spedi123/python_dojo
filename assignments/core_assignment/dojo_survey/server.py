from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "peteranishere"
# this is going to move in the future


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def survey_info():
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
