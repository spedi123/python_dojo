from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "peteran is here"
# this is going to move in the future


@app.route('/')
def hello_world():
    if 'num' not in session:
        session['num'] = random.randint(1, 100)
    return render_template('index.html')


@app.route('/guess', methods=['POST'])
def guessnumber():
    session['guess'] = int(request.form['guess'])
    return redirect('/')
# end of moving area


@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


# this must be on the bottom of this file
if __name__ == "__main__":
    app.run(debug=True)
